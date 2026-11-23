# Risk-Premium PCA（RP-PCA）

## 定義

[[lettau-martin]] 與 [[pelger-markus]] (2020) 提出的統計因子萃取方法，在傳統 [[principal-component-analysis|PCA]] 的目標函數中加入橫截面定價誤差項，使萃取出的因子同時解釋時間序列的共變，並捕捉橫截面的風險溢酬。

目標函數：
$$L(\hat{F}_{RP}, \hat{\Lambda}_{RP}) = \frac{1}{NT}\sum (X_{nt} - F_t\Lambda_n^\top)^2 + \gamma \sum (\bar{X}_n - \bar{F}\Lambda_n^\top)^2$$

第一項為傳統 PCA 的時間序列配適誤差，第二項為以 γ 加權的橫截面定價誤差。此問題等價於對 $\Sigma_{RP} = \frac{1}{T}X^\top X + \gamma\bar{X}\bar{X}^\top$ 進行 [[principal-component-analysis|PCA]]。

---

## 超參數 γ

| γ | 行為 |
|---|------|
| −1 | 等同傳統 PCA，只看時間序列共變 |
| 大於 0 | 加重橫截面定價，γ 越大越偏重 |
| 台灣市場最佳值 | γ = 10，增至 20 改善有限 |

---

## 在知識庫中的出現

- **[[capturing-risk-premia-taiwan]]**：應用於台灣成交量前 100 大股票；在 γ = 10、T = 13（季窗口）並搭配 130/30 策略下，第一因子的年化 Sharpe Ratio 為 0.84，高於等權重基準的 0.54。

---

## 與傳統 PCA 比較

| | 傳統 PCA | RP-PCA |
|--|---------|--------|
| 目標 | 最大化報酬共變的解釋比例 | 同時考慮時間序列配適與橫截面定價 |
| 萃取的因子 | 常反映統計雜訊 | 具風險溢酬意義 |
| 適用情境 | 降維 | 建構因子投資組合 |

---

## 關聯概念

[[principal-component-analysis]]、[[factor-models]]、[[machine-learning-asset-pricing]]、[[momentum]]、[[portfolio-optimization]]

## 關聯文獻

Lettau & Pelger (2020)，為 [[capturing-risk-premia-taiwan]] 的主要引用文獻。
