# Wiki 總索引

**主題**：財務金融學習筆記，涵蓋衍生性商品與選擇權定價、資產定價、投資組合、機器學習與量化實務  
**最後更新**：2026-11-23

---

## Sources（來源摘要）

| 頁面 | 類型 | 作者 | 年份 | 一句話說明 |
|------|------|------|------|-----------|
| [[fe-01-options-binomial-tree]] | course | 授課教師 | 2026（115-1） | 四上財工講義 01：選擇權損益、二元樹定價、風險中立機率、複製與動態 Delta 避險 |
| [[fe-02-stock-dynamics-ito]] | course | 授課教師 | 2026（115-1） | 四上財工講義 02：Markov 過程、布朗運動、幾何布朗運動、Itô 定理 |
| [[fe-03-black-scholes-formula]] | course | 授課教師 | 2026（115-1） | 四上財工講義 03：BS 假設、PDE、Feynman-Kac 求解、買賣權公式、Greeks |
| [[fe-06-bs-pde-derivation]] | course | 授課教師 | 2026（115-1） | 四上財工講義 06：BS PDE 轉換為熱傳導方程式，以傅立葉轉換求解 |
| [[fe-07-martingale-pricing]] | course | 授課教師 | 2026（115-1） | 四上財工講義 07：無套利與 martingale、Girsanov 測度轉換、BS 公式的機率解讀 |
| [[derivatives-course-113-1]] | course | — | 113-1（學期標註待確認） | 三上衍生性金融商品課程的講義與簡報索引 |
| [[empirical-asset-pricing-ml]] | journal | [[gu-shihao]]、[[kelly-bryan]]、[[xiu-dacheng]] | 2020 | 比較 ML 方法於資產定價的表現，神經網路與樹模型最佳 |
| [[capturing-risk-premia-taiwan]] | journal | [[vincent-kendro]] et al. | 2025 | 不依賴公司特徵，以 RP-PCA 於台灣股市捕捉風險溢酬 |
| [[quantitative-methods-finance-course]] | course | [[chiang-mi-hsiu]] | 114-1（2025 秋） | 金融系線性代數課程，以向量空間與線性變換的證明為主 |
| [[investments-course]] | course | — | 113-2（推估） | 以 Fama-French 三因子估計 IVOL 的作業 |
| [[ml-financial-econometrics-course]] | course | — | 114-2（推估） | 以 risk minimization 貫穿正則化、降維、樹模型至神經網路 |
| [[dia-course-114-1]] | course | [[chung-douglas]] | 114-1（2025 秋） | Data-driven Investment Analysis：MPT、CAPM、APT 與台灣 50 指數複製 |
| [[nvidia-rag-agents-course]] | course | NVIDIA DLI | 未確認 | Building RAG Agents with LLMs 課程教材的結構索引 |
| [[tmba-trading-dept-quant-intro-preread]] | course | 社團講者 | 2025–2026 | 量化交易社團入門預習教材，分觀念課、Python、回測框架三個單元 |

---

## Projects（專案）

| 頁面 | 情境 | 期間 | 一句話說明 |
|------|------|------|-----------|
| [[ivol-fama-french-analysis]] | course-project | 2025-02 ~ 03（113-2） | 以 Fama-French 三因子殘差估計個股 IVOL |
| [[ridge-xgboost-stock-return-prediction]] | course-project | 未確認（推估 114-2） | 以 Ridge 與 XGBoost 預測 40 檔美股的次月報酬 |
| [[rag-hongloumeng-retrieval]] | course-project | 2025-11（114-1） | 紅樓夢 RAG 系統，BM25 與向量檢索以 RRF 融合，共四級 baseline |
| [[harness-wiki-llm]] | self-study | 2026-05 起 | LLM 維護知識庫的模板，含跨模型驗證工作流 (multi-agent-dev) |
| [[macd-adx-fibonacci-futures-strategy]] | self-study | 2026 | MACD、ADX 與費波那契回撤台指期策略；v3 純多單版樣本外轉正，但屬 hindsight bias，非獨立驗證 |
| [[rsi-overbought-oversold-futures-strategy]] | self-study | 2026 | RSI 超買超賣台指期策略，樣本外落後 Buy&Hold，找不到穩健參數高原 |
| [[adx-regime-switching-donchian-bollinger-strategy]] | self-study | 2026 | ADX 狀態切換（唐奇安突破與布林均值回歸），樣本內外皆虧損，優化未通過穩健性門檻 |
| [[volatility-squeeze-breakout]] | self-study | 2026 | 波動率壓縮突破策略，迭代至 v3；提高交易頻率後，正常成本下 Sharpe 趨近 0 |
| [[factor-investing-project]] | self-study | 2026（規劃中） | 跨股票因子選股專案，僅完成方向規劃，尚未實作 |
| [[bollinger-trend-vs-reversion]] | self-study | 2026 | 布林通道順勢與逆勢對照；逆勢方向錯誤，順勢訊號正確但毛利被成本抵銷 |

---

## Concepts（概念）

### 基礎知識

| 頁面 | 一句話說明 |
|------|-----------|
| [[probability-expected-value]] | 機率、期望值、變異數、標準差與測度，波動度即為報酬率的標準差 |
| [[return-rate]] | 報酬率、對數報酬率、年化與期望報酬率 |
| [[logarithm-exponential]] | 指數 e^x 與自然對數 ln，兩者互為反運算 |
| [[normal-distribution]] | 常態分配、累積機率 N(·) 與機率密度 n(·) |
| [[discounting-continuous-compounding]] | 折現與連續複利，e^{-rT} 將未來金額換算為現值 |
| [[calculus-basics]] | 微分、偏微分、積分與偏微分方程的白話說明 |
| [[no-arbitrage]] | 無套利：不存在零成本、無風險又穩賺的機會，為選擇權定價的出發點 |

### 選擇權定價

| 頁面 | 一句話說明 |
|------|-----------|
| [[derivatives]] | 衍生性金融商品：選擇權、期貨、遠期契約與互換 |
| [[option-basics]] | 買權與賣權、歐式與美式、到期損益 max(S_T−K,0) |
| [[binomial-option-pricing]] | 二項樹定價：無風險組合加上無套利條件，f=e^{-rT}[qf_u+(1−q)f_d] |
| [[risk-neutral-valuation]] | 以使股票期望報酬等於無風險利率的機率 q 定價 |
| [[delta-hedging-replication]] | 以 Δ 股股票與借貸複製選擇權，Delta 隨股價改變須動態、自我融資調整 |
| [[brownian-motion]] | 布朗運動：獨立、常態、變異數等於時間長度的隨機變動，二次變異為 t |
| [[geometric-brownian-motion]] | 股價模型 dS=μS dt+σS dz：報酬率由固定成長與隨機衝擊組成 |
| [[itos-lemma]] | Itô 定理：隨機過程的連鎖律，多出 ½b²f_XX 一項 |
| [[black-scholes-pde]] | BS 偏微分方程：由無風險組合推出，μ 在過程中消去 |
| [[black-scholes-model]] | BS 模型、Greeks 與風險中立定價（離散二元樹與連續 Feynman-Kac 的對應） |
| [[option-greeks]] | Delta、Gamma、Vega、Rho、Theta 的定義與公式 |
| [[heat-equation-method]] | BS PDE 經變數轉換成為熱傳導方程式並求解 |
| [[martingale]] | 最佳預測等於現值；折現後價格在 Q 測度下為 martingale |
| [[measure-change-girsanov]] | Girsanov 定理：P、Q、R 測度轉換，μ 換成 r |
| [[structured-notes]] | 結構型商品：Autocallable、Memory Coupon Equity-Linked Note |

### 資產定價與投資組合

| 頁面 | 一句話說明 |
|------|-----------|
| [[factor-models]] | 因子模型：由 CAPM、Fama-French 至統計因子 |
| [[risk-premium-pca]] | RP-PCA：於 PCA 目標函數加入橫截面定價誤差，提升風險溢酬的捕捉 |
| [[principal-component-analysis]] | PCA 及其變體（RP-PCA、PCR）於因子萃取的應用 |
| [[momentum]] | 動能效應：過去表現較好的資產短期內傾向繼續較好 |
| [[idiosyncratic-volatility]] | 因子模型迴歸殘差的標準差，衡量個股特有風險 |
| [[sharpe-ratio]] | 最常用的風險調整後報酬指標 |
| [[portfolio-optimization]] | 投資組合最佳化：由 Markowitz 至因子組合 |
| [[linear-algebra-vector-space]] | 向量空間、基底、秩與線性變換，為財金矩陣運算的數學基礎 |

### 機器學習與量化實務

| 頁面 | 一句話說明 |
|------|-----------|
| [[machine-learning-asset-pricing]] | 樹模型、神經網路與正則化線性模型於股票報酬預測的應用 |
| [[neural-networks]] | 神經網路於財務預測的應用與層數選擇 |
| [[regularization]] | Ridge、Lasso 與 Elastic Net |
| [[technical-indicators]] | MA、MACD、KD、ATR、ADX 等價格技術指標 |
| [[backtest-overfitting-and-validation]] | 回測偏誤清單，以及參數高原、one-standard-error rule、未來函數檢查等驗證技術 |
| [[quant-factor-mining-methodology]] | 業界因子挖掘流程：挖掘、IC 篩選、監控衰退 |

### LLM 應用

| 頁面 | 一句話說明 |
|------|-----------|
| [[retrieval-augmented-generation]] | RAG：切分、檢索、融合排序與生成 |
| [[prompt-injection]] | 提示注入攻擊與防禦方式 |
| [[multi-agent-review]] | 由不同模型分別規劃與驗證，避免同源誤差 (self-review bias) |
| [[llm-knowledge-base-architecture]] | raw、wiki、規則三層分離，加上 Ingest、Query、Lint 三種操作 |

---

## People（作者與教師）

| 頁面 | 機構 | 主要貢獻 |
|------|------|---------|
| [[gu-shihao]] | Chicago Booth | [[empirical-asset-pricing-ml]] |
| [[kelly-bryan]] | Yale／AQR | [[empirical-asset-pricing-ml]] |
| [[xiu-dacheng]] | Chicago Booth | [[empirical-asset-pricing-ml]] |
| [[lettau-martin]] | UC Berkeley | RP-PCA 原始作者，[[capturing-risk-premia-taiwan]] 引用 |
| [[pelger-markus]] | Stanford | RP-PCA 原始作者，[[capturing-risk-premia-taiwan]] 引用 |
| [[vincent-kendro]] | 政大金融系 | [[capturing-risk-premia-taiwan]] |
| [[chiang-mi-hsiu]] | 政大金融系 | [[quantitative-methods-finance-course]] 授課教師（拼音未確認） |
| [[chung-douglas]] | 政大國際經營與貿易學系 | [[dia-course-114-1]] 授課教師 |
