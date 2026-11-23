# Regularization（正則化：Ridge／Lasso／Elastic Net）

## 定義

在最小平方目標函數中加入 L1 或 L2 懲罰項，控制模型複雜度以避免過擬合。Ridge 使用 L2 懲罰，係數平滑收縮但不做變數選擇；Lasso 使用 L1 懲罰，可將係數壓至 0，具變數選擇效果；Elastic Net 則同時使用兩者。財務資料的訊噪比低、特徵常高度共線，此時 Ridge 的係數收縮通常比 Lasso 的變數選擇穩定。

---

## 在知識庫中的出現

- **[[ml-financial-econometrics-course]]**：講義第 6 章；HW2 以 5-fold CV 選擇 λ 估計 Lasso 與 Ridge 分類模型，並與理論 λ 的版本比較混淆矩陣、precision、recall 與 F1；Mock Exam 包括判斷 Ridge 高 λ 時的 bias-variance，以及手算 Lasso、Ridge 收縮後的係數。
- **[[ridge-xgboost-stock-return-prediction]]**：以 Ridge 作為主要線性模型，與 XGBoost 對照。模型選擇時比較 Lasso、Elastic Net 與 Ridge 的多空投組表現，Ridge 最佳；此外，Ridge 的 `alpha` 會隨市場波動調整，危機期間較強、平穩期間較弱。

---

## 關聯概念

[[machine-learning-asset-pricing]]（正則化線性模型為 ML 資產定價方法之一；因正則化屬跨領域的基礎統計方法，故獨立成頁）
