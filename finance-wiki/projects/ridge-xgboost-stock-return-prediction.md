# Ridge vs XGBoost 股票報酬預測（機器學習與財務計量期末專案）

**類型**：project  
**期間**：未確認（推測為 114-2，截止 2026-06-04）  
**情境**：course-project  
**原始檔**：機器學習與財務計量\作業\Final Project  
**技術棧**：Python（yfinance、pandas、numpy、scikit-learn、xgboost、SimFin／FRED／FMP API）

---

## 目標

比較線性模型 (Ridge Regression) 與非線性模型 (XGBoost) 預測個股次月報酬的表現，回答四個問題：(1) D1–D4 分位數投組的報酬是否單調遞減；(2) 非線性模型的 long-short 表現是否優於線性模型；(3) 最佳超參數如何隨時間變化；(4) 各期最重要的預測變數為何。

## 方法與架構

- 樣本：40 檔美股，多為 S&P 500 成分股，涵蓋科技、半導體、醫療、消費、金融、工業、能源、通訊 8 種產業；期間 2015-01-01 至 2026-02-01，月頻，共 133 個月；股價以 yfinance 取得 (auto-adjusted close)。
- 特徵（基準版本共 8 個）：動能類 `mom_1`、`mom_3`、`mom_6`、`mom_12`（`mom_k = P_t/P_{t-k} - 1`）；波動率類 `vol_1m`、`vol_3m`、`vol_6m`、`vol_12m`（日對數報酬的年化標準差，`vol_k = σ_k × √252`）。
- 前處理：每月橫斷面做 1%／99% winsorization，再做 cross-sectional z-score 標準化。
- 建模 (Expanding Window)：以樣本前 50% 為起始訓練期，每次估計時將可用歷史資料依時間切為 2/3 training、1/3 validation；每月底重新估計，以截至當期的所有歷史資料預測下一月報酬。
- 超參數：以 MSE 為準則。Ridge 的 `alpha` 候選值為 {0.1, 1, 10, 100}；XGBoost 的 `max_depth` 候選值為 {1, 2, 3, 4, 5}，固定 `n_estimators=10`、`learning_rate=0.02`、`subsample=0.7`。
- 模型選擇：線性模型先比較 Lasso、Elastic Net 與 Ridge 的多空投組平均報酬，Ridge 最佳。推測原因在於財務資料訊噪比低，且動能特徵之間高度共線，Lasso 的變數選擇不穩定，Ridge 的係數收縮較適合。
- 投組：依預測值排序分為 D1（最高 25%）至 D4（最低 25%）四組等權組合，多空組合 `LS = D1 - D4`。
- 延伸實驗：12 個特徵的版本，另加入 P/B ratio 與 ROE 兩個價值因子（取自 SimFin／SEC EDGAR）、Amihud illiquidity（以 yfinance 成交量計算）與 CPI 月變動率（取自 FRED API）。

## 結果

以下數字取自 `Submission/ML_FinalReport.pdf` 的 Q1 主要結果表，為 8 個特徵的基準版本：

| 投組 | Ridge 月均報酬 | Ridge Mean-to-Vol | XGBoost 月均報酬 | XGBoost Mean-to-Vol |
|---|---|---|---|---|
| D1 | 1.9264% | 0.2538 | 2.2409% | 0.2613 |
| D2 | 1.4915% | 0.2961 | 1.4602% | 0.2816 |
| D3 | 1.4250% | 0.2951 | 1.4577% | 0.3285 |
| D4 | 1.0164% | 0.2555 | 0.3710% | 0.0824 |
| LS | 0.9100% | 0.1327 | 1.8781% | 0.2986 |

1. 單調性：兩個模型的平均報酬皆由 D1 至 D4 單調遞減，Ridge 由 1.93% 降至 1.02%，XGBoost 由 2.24% 降至 0.37%；mean-to-volatility ratio 則未單調遞減，原因在於 D1 多為高報酬、高波動的股票，風險調整後表現未必最佳。
2. 線性與非線性：XGBoost 的 long-short 組合在平均報酬與 Mean-to-Vol 兩項皆優於 Ridge，波動亦較低。
3. 超參數：2022 年升息與 2023–2025 年 AI 行情的劇烈波動期間，兩個模型皆傾向選擇較強的正則化（Ridge 提高 alpha，XGBoost 壓低 max_depth），市場平穩時則放鬆，可見正則化強度會隨股市波動調整。
4. 特徵重要性：Ridge 長期高度依賴 `vol_12m`（長期波動度）；XGBoost 的主導特徵則隨時期輪替（`mom_6`、`mom_12`、`vol_6m` 等），顯示樹模型能隨市場環境調整。
5. 12 個特徵的延伸實驗：加入 P/B、ROE、Amihud illiquidity 與 CPI 後，XGBoost 表現明顯變差，D1 反而低於 D4，LS 平均報酬轉為 −0.4897%；Ridge 則相對穩定，LS 仍為 1.2710%。報告推測原因在於價值因子的公布有時間落差，CPI 為總體變數、各股數值相同而缺乏區辨力，而 XGBoost 對雜訊特徵的抵抗力不如線性模型。

## 學到什麼

- 樹模型學習能力較強、能捕捉 regime 變化，但對雜訊特徵敏感，加入弱訊號反而可能變差；Ridge 學習能力較弱，但抗雜訊與泛化較穩定。報告將此稱為學習能力與抗雜訊能力的權衡。
- Expanding window 搭配 2/3、1/3 的 training／validation 切分，可作為避免 look-ahead bias 的超參數選擇流程。
- 正則化強度隨市場波動調整（危機期間較強、平穩期間較弱），可作為市場 regime 的間接指標。

## 關聯概念

[[machine-learning-asset-pricing]]、[[neural-networks]]（非線性方法的對照）、[[regularization]]（Ridge 為主要線性模型）、[[technical-indicators]]（動能與波動率特徵）

## 關聯頁面

[[ml-financial-econometrics-course]]、[[empirical-asset-pricing-ml]]（研究問題與 Gu, Kelly & Xiu 2020 相同：非線性 ML 方法能否在資產定價中創造經濟價值）
