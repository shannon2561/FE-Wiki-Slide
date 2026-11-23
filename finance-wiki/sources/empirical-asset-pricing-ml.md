# Empirical Asset Pricing via Machine Learning

**類型**：journal  
**作者**：[[gu-shihao]]、[[kelly-bryan]]、[[xiu-dacheng]]  
**年份**：2020  
**期刊**：The Review of Financial Studies, Vol. 33, pp. 2223–2273  
**原始檔**：raw/journals/Empirical_Asset_Pricing_via_Machine_Learning.md

---

## 核心問題

傳統資產定價以線性迴歸預測股票超額報酬，面臨兩個問題：一是預測變數超過 900 個，線性模型容易過擬合；二是無法捕捉預測變數之間的非線性交互效果。此文比較各種[[machine-learning-asset-pricing|機器學習方法]]預測股票報酬的能力，以及能帶來多少經濟價值。

---

## 方法

使用 CRSP 月報酬（1957–2016，約 30,000 檔股票）與 920 個預測變數，比較以下模型：

| 類別 | 模型 |
|------|------|
| 線性 | OLS、Elastic Net |
| 降維 | [[principal-component-analysis\|PCR]]、PLS |
| 非線性 | GLM 搭配樣條、Random Forest、GBRT |
| 非線性 | [[neural-networks\|Neural Network]] NN1–NN5 |

樣本切分為訓練期 1957–1974、驗證期 1975–1986、測試期 1987–2016，以樣本外 $R^2_{oos}$ 評估。

---

## 主要發現

- 樹模型與神經網路表現最佳，個股月度 $R^2_{oos}$ 為 0.33%–0.40%。
- 原因在於允許預測變數之間的非線性交互；僅加入樣條、不允許交互的 GLM，無法穩定優於線性模型。
- [[neural-networks|神經網路]]在三層隱藏層時表現最佳，層數再增加反而下降。
- S&P 500 擇時：神經網路的 Sharpe Ratio 為 0.77，買進持有為 0.51。
- 個股多空十分位策略的 SR 為 1.35，為線性基準的兩倍以上。
- 各模型共同認定的最強訊號為[[momentum|動能]]、流動性與波動率。

---

## 關聯概念

[[machine-learning-asset-pricing]]、[[neural-networks]]、[[factor-models]]、[[momentum]]、[[principal-component-analysis]]、[[sharpe-ratio]]、[[portfolio-optimization]]

## 關聯文獻

[[capturing-risk-premia-taiwan]]：同樣比較統計方法與特徵方法，以台灣市場為對象。
