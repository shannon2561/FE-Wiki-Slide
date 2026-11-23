# Machine Learning in Asset Pricing（機器學習資產定價）

## 定義

將機器學習方法（正則化線性模型、降維、樹模型、神經網路）用於預測股票超額報酬的研究領域。主要難處在於，預測變數維度高，須控制過擬合，同時又要捕捉非線性與交互效果。

---

## 方法分類

| 類別 | 代表方法 | 優勢 |
|------|---------|------|
| 正則化線性 | Lasso、Ridge、Elastic Net | 高維特徵選擇 |
| 降維 | [[principal-component-analysis\|PCR]]、PLS | 處理多重共線性 |
| 樹模型 | Random Forest、GBRT | 非線性與交互效果 |
| [[neural-networks\|神經網路]] | NN1–NN5 | 複雜非線性 |

---

## 在知識庫中的出現

- **[[empirical-asset-pricing-ml]]**（2020）：以 920 個預測變數、60 年美股資料進行大規模比較，樹模型與神經網路表現最佳，原因在於允許預測變數之間的交互效果。
- **[[capturing-risk-premia-taiwan]]**（2025）：使用統計因子（RP-PCA、Convex-NMF），不預設特徵，應用於台灣市場。
- **[[ml-financial-econometrics-course]]**：課程以 risk minimization 貫穿迴歸與分類，涵蓋正則化（見 [[regularization]]）、降維、樹模型與神經網路。
- **[[ridge-xgboost-stock-return-prediction]]**：期末專案以 Ridge 與 XGBoost 預測 40 檔美股的次月報酬，研究問題與 Gu, Kelly & Xiu (2020) 相同。

---

## 關聯概念

[[neural-networks]]、[[principal-component-analysis]]、[[factor-models]]、[[momentum]]、[[sharpe-ratio]]、[[risk-premium-pca]]

## 關聯文獻

Gu, Kelly & Xiu (2020) → [[empirical-asset-pricing-ml]]
