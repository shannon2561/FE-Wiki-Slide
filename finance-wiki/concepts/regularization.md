# Regularization（正則化：Ridge／Lasso／Elastic Net）

## 定義

在最小平方目標函數中加入懲罰項（L1/L2）以控制模型複雜度、避免過擬合的方法。代表方法：**Ridge**（L2 懲罰，係數平滑收縮，不做變數選擇）、**Lasso**（L1 懲罰，可將係數收縮至 0，具變數選擇效果）、**Elastic Net**（L1+L2 混合）。在財務資料訊噪比低、特徵間常高度共線性的情境下，Ridge 的係數收縮通常比 Lasso 的離散變數選擇更穩定。

---

## 在知識庫中的出現

- **[[ml-financial-econometrics-course]]**：講義第 6 章、HW2（用 5-fold CV 選 λ 估計 Lasso／Ridge 分類模型，並與理論 λ 版本比較混淆矩陣、precision/recall/F1）、Mock Exam 考題（Ridge 高 λ 的 bias-variance 判斷、手算 Lasso/Ridge 收縮後係數）
- **[[ridge-xgboost-stock-return-prediction]]**：Ridge 為主要線性模型，與 XGBoost 對照；模型選擇過程曾比較 Lasso、Elastic Net、Ridge 三者的多空投組表現，Ridge 最佳；發現正則化強度（Ridge 的 `alpha`）會隨市場波動自適應調整（危機期偏強、平穩期偏弱）

---

## 關聯概念

[[machine-learning-asset-pricing]]（正則化線性模型是 ML 資產定價方法分類中的一支；本概念獨立成頁，因正則化本身是更基礎、跨領域的統計方法）
