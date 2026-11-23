# Ridge vs XGBoost 股票報酬預測（機器學習與財務計量期末專案）

**類型**：project
**期間**：未確認（推測 114-2，作業截止 2026-06-04）
**情境**：course-project
**原始檔**：機器學習與財務計量\作業\Final Project
**技術棧**：Python（yfinance、pandas、numpy、scikit-learn、xgboost、SimFin/FRED/FMP API）

---

## 目標

比較線性模型（Ridge Regression）與非線性模型（XGBoost）在個股次月報酬預測上的表現，回答課程指定的四個問題：(1) D1–D4 分位數投組報酬是否單調遞減；(2) 非線性模型的多空組合（long-short）表現是否優於線性模型；(3) 最佳超參數如何隨時間變化；(4) 各期最重要的預測變數為何。

## 方法與架構

- **樣本**：40 檔美股（多為 S&P 500 成分股），涵蓋科技、半導體、醫療、消費、金融、工業、能源、通訊 8 種產業；樣本期間 2015-01-01 至 2026-02-01，月頻，共 133 個月。股價經 yfinance 取得（auto-adjusted close）。
- **特徵**（基準版本，8 個）：動量類 `mom_1`/`mom_3`/`mom_6`/`mom_12`（`mom_k = P_t/P_{t-k} - 1`）、波動率類 `vol_1m`/`vol_3m`/`vol_6m`/`vol_12m`（日對數報酬年化標準差，`vol_k = σ_k × √252`）。
- **資料前處理**：每月橫斷面做 1%/99% winsorization，再做 cross-sectional z-score 標準化。
- **建模架構（Expanding Window）**：以樣本前 50% 作為起始訓練期，每次估計時再將可用歷史資料依時間切為 2/3 training、1/3 validation，每月底重新估計模型，用截至當期的全部歷史資料預測下一月報酬。
- **超參數選擇**：以 MSE 為準則，Ridge 的 `alpha` 候選集 {0.1, 1, 10, 100}；XGBoost 的 `max_depth` 候選集 {1,2,3,4,5}（固定 `n_estimators=10`、`learning_rate=0.02`、`subsample=0.7`）。
- **模型選擇過程**：線性模型端曾比較 Lasso、Elastic Net、Ridge 三者的多空投組平均報酬，Ridge 表現最佳（推測理由：財務資料訊噪比低，且動量特徵間高度共線性，Lasso 的變數選擇不穩定；Ridge 的係數收縮較適合此情境）。
- **投組建構**：依預測值排序分四組 D1（最高 25%）至 D4（最低 25%）等權組合，並計算多空組合 `LS = D1 - D4`。
- **延伸實驗**：另嘗試 12 特徵版本（加入 P/B ratio、ROE 兩個價值因子（來源 SimFin/SEC EDGAR）、Amihud illiquidity（由 yfinance 成交量計算）、CPI 月變動率（來源 FRED API）四個新特徵）。

## 結果

（以下數字均取自 `Submission/ML_FinalReport.pdf` 的 Q1 主要結果表，為 8-特徵基準版本）

| 投組 | Ridge 月均報酬 | Ridge Mean-to-Vol | XGBoost 月均報酬 | XGBoost Mean-to-Vol |
|---|---|---|---|---|
| D1 | 1.9264% | 0.2538 | 2.2409% | 0.2613 |
| D2 | 1.4915% | 0.2961 | 1.4602% | 0.2816 |
| D3 | 1.4250% | 0.2951 | 1.4577% | 0.3285 |
| D4 | 1.0164% | 0.2555 | 0.3710% | 0.0824 |
| LS | 0.9100% | 0.1327 | 1.8781% | 0.2986 |

- **Q1（單調性）**：兩模型的 D1→D4 平均報酬皆呈單調遞減（Ridge 1.93%→1.02%、XGBoost 2.24%→0.37%），但 mean-to-volatility ratio 並未單調遞減（因 D1 常為高報酬高波動股票，風險調整後表現不一定最佳）。
- **Q2（線性 vs 非線性）**：本例中 XGBoost 的 long-short 組合在平均報酬與 Mean-to-Vol 兩項都優於 Ridge（XGBoost LS 波動更低、風險調整後表現更佳）。
- **Q3（超參數隨時間變化）**：2022 年升息高峰與 2023–2025 AI 行情帶動的劇烈波動期間，兩模型皆傾向選擇更強的正則化（Ridge 提高 alpha、XGBoost 壓低 max_depth），市場相對平穩時則放鬆正則化——結論為「正則化強度隨股市波動自我調整」。
- **Q4（特徵重要性）**：Ridge 的係數長期高度依賴 `vol_12m`（長期波動度）；XGBoost 的主導特徵則隨時期輪換（`mom_6`、`mom_12`、`vol_6m` 等交替），顯示樹模型能捕捉不同市場環境下的動態訊號。
- **12-特徵延伸實驗**：加入 P/B、ROE、Amihud illiquidity、CPI 後，XGBoost 表現大幅惡化（D1 反而低於 D4，LS 平均報酬轉為 -0.4897%），而 Ridge 相對維持穩健（LS 仍為正 1.2710%）。報告推測原因：價值因子公告有時間落後、CPI 為總體變數對個股缺乏區辨力，XGBoost 對雜訊特徵的抗性不如線性模型。

## 學到什麼

- 非線性模型（樹模型）學習能力更強、能捕捉 regime 變化，但對雜訊特徵較敏感，加入弱訊號特徵反而可能使表現惡化；線性模型（Ridge）雖學習能力較弱，抗雜訊能力與泛化穩定性較佳——兩者各有取捨，report 中稱為「學習能力與抗雜訊能力的權衡」。
- Expanding window + 2/3/1/3 training/validation 切分的超參數選擇流程，可作為避免前瞻偏誤（look-ahead bias）的標準做法範例。
- 正則化強度會隨市場波動自適應調整（危機期偏強、平穩期偏弱），可作為市場 regime 的間接指標。

## 關聯概念

[[machine-learning-asset-pricing]]、[[neural-networks]]（樹模型／非線性方法之對照脈絡）、[[regularization]]（Ridge 為主要線性模型）、[[technical-indicators]]（動量/波動率特徵）

## 關聯頁面

[[ml-financial-econometrics-course]]、[[empirical-asset-pricing-ml]]（本專案設計直接呼應 Gu, Kelly & Xiu 2020 的研究問題：非線性 ML 方法是否能在資產定價中創造超額經濟價值）
