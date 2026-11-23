# Machine Learning in Asset Pricing

## 定義

將機器學習方法（正則化線性、降維、樹模型、神經網路）應用於預測股票超額報酬的研究領域。核心挑戰是在高維預測因子空間中控制過擬合，同時捕捉非線性與交互效果。

---

## 主要方法分類

| 類別 | 代表方法 | 優勢 |
|------|---------|------|
| 正則化線性 | Lasso、Ridge、Elastic Net | 高維特徵選擇 |
| 降維 | [[principal-component-analysis\|PCR]]、PLS | 處理多重共線性 |
| 樹模型 | Random Forest、GBRT | 非線性交互 |
| [[neural-networks\|神經網路]] | NN1–NN5 | 複雜非線性 |

---

## 在知識庫中的出現

- **[[empirical-asset-pricing-ml]]**（2020）：最系統性的大規模比較；920 個因子、60 年美股資料；樹模型與神經網路勝出，關鍵在允許預測變數交互
- **[[capturing-risk-premia-taiwan]]**（2025）：聚焦統計因子（RP-PCA、Convex-NMF），不依賴預設特徵，台灣市場應用
- **[[ml-financial-econometrics-course]]**：課程核心框架，以「risk minimization」統一貫穿迴歸/分類任務，涵蓋正則化（見 [[regularization]]）、降維、樹模型、神經網路
- **[[ridge-xgboost-stock-return-prediction]]**：期末專案，Ridge vs XGBoost 預測 40 檔美股次月報酬，直接呼應 Gu-Kelly-Xiu (2020) 的研究問題

---

## 關聯概念

[[neural-networks]]、[[principal-component-analysis]]、[[factor-models]]、[[momentum]]、[[sharpe-ratio]]、[[risk-premium-pca]]

## 關鍵文獻

Gu, Kelly, Xiu (2020) → [[empirical-asset-pricing-ml]]
