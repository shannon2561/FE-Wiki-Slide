# Neural Networks in Finance（神經網路）

## 定義

多層感知器 (MLP) 及其變體（如 CNN）透過非線性激活函數與多個隱藏層，學習輸入特徵到輸出的非線性映射，在金融領域主要用於股票報酬預測與型態辨識。

---

## 層數選擇

| 層數 | 在 [[empirical-asset-pricing-ml]] 的表現 |
|------|------|
| NN1（1 層） | 尚可 |
| NN2（2 層） | 良好 |
| NN3（3 層） | 最佳 |
| NN4、NN5 | 下降（過擬合） |

結論：在資產定價中，較淺的網路表現優於較深的網路。

---

## 在知識庫中的出現

- **[[empirical-asset-pricing-ml]]**（Gu, Kelly & Xiu, 2020）：神經網路與樹模型表現並列最佳，月度 $R^2_{oos}$ 為 0.33%–0.40%，個股多空策略的 Sharpe Ratio 為 1.35；原因在於允許非線性，以及預測變數之間的交互效果。
- **[[ml-financial-econometrics-course]]**：第 11 章講義為神經網路，另附 R 範例程式（Perceptron、DeepNN、Multivariate_NN）。

---

## 與其他方法比較

| | 神經網路 | 樹模型 | 線性模型 |
|--|---------|--------|---------|
| 非線性 | 是 | 是 | 否（樣條除外） |
| 交互效果 | 是 | 是 | 否 |
| 可解釋性 | 低 | 中 | 高 |
| 計算成本 | 高 | 中 | 低 |

---

## 關聯概念

[[machine-learning-asset-pricing]]、[[factor-models]]、[[momentum]]、[[principal-component-analysis]]
