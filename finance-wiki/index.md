# Wiki 總索引

**主題**：財務金融學習筆記 — 衍生性商品與選擇權定價、資產定價、投資組合、機器學習與量化實務
**最後更新**：2026-11-23

---

## Sources（來源摘要）

| 頁面 | 類型 | 作者 | 年份 | 一句話說明 |
|------|------|------|------|-----------|
| [[empirical-asset-pricing-ml]] | journal | [[gu-shihao]]、[[kelly-bryan]]、[[xiu-dacheng]] | 2020 | 系統比較 ML 方法在資產定價的表現，神經網路與樹模型勝出 |
| [[capturing-risk-premia-taiwan]] | journal | [[vincent-kendro]] et al. | 2025 | RP-PCA 在台灣股市不靠特徵即可有效捕捉風險溢酬 |
| [[derivatives-course-113-1]] | course | — | 113-1（2025 秋，學期標註待確認） | 政大衍生性金融商品課程講義與簡報索引 |
| [[fe-01-options-binomial-tree]] | course | 授課教師 | 2026（115-1） | 四上財工講義 01：選擇權損益、二元樹定價、風險中立機率、複製與動態 Delta 避險 |
| [[fe-02-stock-dynamics-ito]] | course | 授課教師 | 2026（115-1） | 四上財工講義 02：Markov、布朗運動、幾何布朗運動、Itô 定理 |
| [[fe-03-black-scholes-formula]] | course | 授課教師 | 2026（115-1） | 四上財工講義 03：BS 假設、PDE、Feynman-Kac 求解、買賣權公式、Greeks |
| [[fe-06-bs-pde-derivation]] | course | 授課教師 | 2026（115-1） | 四上財工講義 06：BS PDE 轉熱傳導方程式，用傅立葉轉換求解 |
| [[fe-07-martingale-pricing]] | course | 授課教師 | 2026（115-1） | 四上財工講義 07：無套利與 martingale、Girsanov 測度轉換、BS 公式的機率解讀 |
| [[quantitative-methods-finance-course]] | course | [[chiang-mi-hsiu]] | 114-1（2025 秋） | 金融系線性代數課程，聚焦向量空間與線性變換證明 |
| [[investments-course]] | course | — | 113-2（推估） | Fama-French 三因子 IVOL 分析作業 |
| [[ml-financial-econometrics-course]] | course | — | 114-2（推估） | risk minimization 框架貫穿正則化、降維、樹模型到神經網路 |
| [[dia-course-114-1]] | course | [[chung-douglas]] | 114-1（2025 秋） | Data-driven Investment Analysis：MPT/CAPM/APT 與台灣 50 指數複製 |
| [[nvidia-rag-agents-course]] | course | NVIDIA DLI | 未確認 | 「Building RAG Agents with LLMs」課程教材結構索引 |
| [[tmba-trading-dept-quant-intro-preread]] | course | 社團講者 | 2025~2026 | TMBA 程交部量化交易入門預習教材（三單元：觀念課／Python／回測框架） |

> `campus-seminars-2025`、`etp-negotiation-mock-interview` 的「類型」欄位超出 CLAUDE.md 現行 schema（`journal\|thesis\|course`），暫以最接近值標註；2026-09-02 批次再新增 `tutorial-video`／`meeting`／`showcase` 三個暫用類型，是否正式擴充 schema 留待使用者裁決（見 `Logs/ingest-2026-07-07-batch-e.md` 第 5 節、`Logs/ingest-2026-09-02-batch-g.md`）。

---

## Projects（專案）

| 頁面 | 情境 | 期間 | 一句話說明 |
|------|------|------|-----------|
| [[ivol-fama-french-analysis]] | course-project | 2025-02 ~ 03（113-2） | Fama-French 三因子殘差估計個股 IVOL |
| [[ridge-xgboost-stock-return-prediction]] | course-project | 未確認（114-2 推估） | Ridge vs XGBoost 預測 40 檔美股次月報酬 |
| [[rag-hongloumeng-retrieval]] | course-project | 2025-11（114-1） | 紅樓夢 RAG 系統，BM25＋向量檢索＋RRF 融合，四級 baseline |
| [[harness-wiki-llm]] | self-study | 2026-05 ~ | LLM 維護個人知識庫模板，含跨模型對抗式驗證工作流（multi-agent-dev） |
| [[macd-adx-fibonacci-futures-strategy]] | self-study | 2026 | TMBA 程交部台指期策略：MACD+ADX+費波那契，v3 純多單版 OOS 轉正但屬 hindsight bias 非獨立驗證 |
| [[rsi-overbought-oversold-futures-strategy]] | self-study | 2026 | TMBA 程交部 RSI 超買超賣台指期策略，OOS 跑輸 Buy&Hold 且找不到穩健參數高原 |
| [[adx-regime-switching-donchian-bollinger-strategy]] | self-study | 2026 | TMBA 程交部 ADX 狀態切換（唐奇安突破×布林均值回歸），IS/OOS 皆虧損，優化未過穩健性 gate |
| [[volatility-squeeze-breakout]] | self-study | 2026 | TMBA 程交部波動率壓縮突破策略，v1→v2→v3 迭代，v3 提高交易頻率但正常成本下 Sharpe 趨零 |
| [[factor-investing-project]] | self-study | 2026（規劃階段） | TMBA 程交部因子投資專案，僅完成方向規劃，尚未動工 |
| [[bollinger-trend-vs-reversion]] | self-study | 2026 | 布林通道順勢 vs 逆勢策略對照，逆勢引擎方向性錯誤、順勢引擎訊號正確但被成本吃光 |

---

## Concepts（概念）

| 頁面 | 一句話說明 |
|------|-----------|
| [[machine-learning-asset-pricing]] | 機器學習方法（樹、神經網路、正則化線性）在股票報酬預測的應用 |
| [[risk-premium-pca]] | RP-PCA：在 PCA 目標函數加入橫截面定價誤差，提升因子的風險溢酬捕捉能力 |
| [[option-basics]] | 選擇權基本概念：買權／賣權、歐式／美式、到期損益 max(S_T−K,0) |
| [[binomial-option-pricing]] | 二項樹定價：無風險組合＋無套利 → f=e^{-rT}[qf_u+(1−q)f_d] |
| [[risk-neutral-valuation]] | 風險中立評價：用讓股票期望報酬等於無風險利率的機率 q 定價 |
| [[delta-hedging-replication]] | 用 Δ 股股票＋借貸複製選擇權；Delta 隨股價變動需動態、自我融資調整 |
| [[brownian-motion]] | 布朗運動：獨立、常態、變異數等於時間的隨機變動；二次變異為 t |
| [[geometric-brownian-motion]] | 股價模型 dS=μS dt+σS dz：報酬率＝固定成長＋隨機衝擊 |
| [[itos-lemma]] | Itô 定理：隨機世界的連鎖律，多出 ½b²f_XX 項 |
| [[black-scholes-pde]] | BS 偏微分方程：無風險組合推出，μ 被消掉 |
| [[option-greeks]] | Delta、Gamma、Vega、Rho、Theta 的定義與公式 |
| [[heat-equation-method]] | BS PDE 經變數轉換變成熱傳導方程式並求解 |
| [[martingale]] | 公平賭局：最佳預測等於現值；折現價格在 Q 下為 martingale |
| [[measure-change-girsanov]] | Girsanov 定理：P→Q→R 測度轉換，μ 換成 r |
| [[factor-models]] | 資產定價因子模型：從 CAPM 到 Fama-French 再到統計因子 |
| [[momentum]] | 動能效應：過去績效優異的資產在短期內繼續優異 |
| [[neural-networks]] | 神經網路在財務預測中的應用與架構 |
| [[principal-component-analysis]] | PCA 及其變體（RP-PCA、PCR）在因子萃取的應用 |
| [[sharpe-ratio]] | 風險調整後報酬的核心績效指標 |
| [[derivatives]] | 衍生性金融商品：選擇權、期貨、遠期契約的定價與應用 |
| [[portfolio-optimization]] | 投資組合最佳化：從 Markowitz 到因子組合 |
| [[black-scholes-model]] | BS 模型推導、Greeks 與風險中立定價（離散二元樹 ↔ 連續 Feynman-Kac） |
| [[structured-notes]] | 結構型商品／連動債：Autocallable、Memory Coupon Equity-Linked Notes |
| [[idiosyncratic-volatility]] | 因子模型迴歸殘差標準差，衡量個股特有風險 |
| [[linear-algebra-vector-space]] | 向量空間、基底、秩、線性變換的財金數學基礎 |
| [[technical-indicators]] | MA／MACD／KD／ATR／ADX 等價格技術指標 |
| [[regularization]] | Ridge／Lasso／Elastic Net 正則化方法 |
| [[retrieval-augmented-generation]] | RAG 檢索增強生成：切分、檢索、融合、生成 |
| [[prompt-injection]] | 提示注入攻擊與防禦手法 |
| [[multi-agent-review]] | 多模型分工規劃與驗證，避免同源誤差（self-review bias） |
| [[llm-knowledge-base-architecture]] | raw／wiki／規則三層分離＋Ingest／Query／Lint 的 LLM 知識庫架構 |
| [[backtest-overfitting-and-validation]] | 回測過擬合防範與驗證方法論：七大偏誤清單＋參數高原判定／one-standard-error rule／無未來函數驗證法等工程技術 |
| [[quant-factor-mining-methodology]] | 業界量化因子挖掘實務流程（挖掘→IC篩選→監控衰退） |

---

## People（作者／教師）

| 頁面 | 機構 | 主要貢獻 |
|------|------|---------|
| [[gu-shihao]] | Chicago Booth | [[empirical-asset-pricing-ml]] |
| [[kelly-bryan]] | Yale / AQR | [[empirical-asset-pricing-ml]] |
| [[xiu-dacheng]] | Chicago Booth | [[empirical-asset-pricing-ml]] |
| [[lettau-martin]] | UC Berkeley | RP-PCA 原創者，被 [[capturing-risk-premia-taiwan]] 引用 |
| [[pelger-markus]] | Stanford | RP-PCA 原創者，被 [[capturing-risk-premia-taiwan]] 引用 |
| [[vincent-kendro]] | 政大金融系 | [[capturing-risk-premia-taiwan]] |
| [[chiang-mi-hsiu]] | 政大金融系 | [[quantitative-methods-finance-course]] 授課教師（拼音未確認） |
| [[chung-douglas]] | 政大國際經營與貿易學系 | [[dia-course-114-1]] 授課教師 |

---
