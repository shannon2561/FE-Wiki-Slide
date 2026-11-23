# Empirical Asset Pricing via Machine Learning

**類型**：journal  
**作者**：[[gu-shihao]]、[[kelly-bryan]]、[[xiu-dacheng]]  
**年份**：2020  
**期刊**：The Review of Financial Studies, Vol. 33, pp. 2223–2273  
**原始檔**：raw/journals/Empirical_Asset_Pricing_via_Machine_Learning.md

---

## 核心問題

傳統資產定價用線性回歸預測股票超額報酬，面臨兩個困境：
1. 預測變數超過 900 個，線性模型嚴重過擬合
2. 無法捕捉預測變數之間的**非線性交互效果**

這篇在問：各種 [[machine-learning-asset-pricing|機器學習方法]] 哪個最能預測股票報酬？能帶來多少經濟價值？

---

## 方法

在 CRSP 月報酬（1957–2016，約 30,000 檔股票）、920 個預測因子上，比較：

| 類別 | 模型 |
|------|------|
| 線性 | OLS、Elastic Net |
| 降維 | [[principal-component-analysis\|PCR]]、PLS |
| 非線性 | GLM + 樣條、Random Forest、GBRT |
| 非線性 | [[neural-networks\|Neural Network]] NN1–NN5 |

訓練 1957–1974 / 驗證 1975–1986 / 測試 1987–2016，以樣本外 $R^2_{oos}$ 評估。

---

## 主要發現

- **樹模型與神經網路**勝出，月度股票層 $R^2_{oos}$ 介於 0.33%–0.40%
- 成功關鍵在於允許**預測變數之間的非線性交互**；僅加樣條但不允許交互的 GLM 無法穩定勝過線性模型
- [[neural-networks|神經網路]] 峰值在三層隱藏層，再深反而下降（「淺學習」優於「深學習」）
- S&P 500 擇時：神經網路 Sharpe Ratio 0.77 vs. 買持 0.51
- 個股多空十分位策略：SR 1.35，超過線性基準兩倍以上
- 所有模型一致認同的最強訊號：[[momentum|動能]]、流動性、波動率

---

## 關聯概念

[[machine-learning-asset-pricing]]、[[neural-networks]]、[[factor-models]]、[[momentum]]、[[principal-component-analysis]]、[[sharpe-ratio]]、[[portfolio-optimization]]

## 關聯文獻

[[capturing-risk-premia-taiwan]] — 同樣比較統計方法與特徵基礎方法，聚焦台灣市場
