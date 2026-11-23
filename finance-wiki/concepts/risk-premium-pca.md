# Risk-Premium PCA（RP-PCA）

## 定義

由 [[lettau-martin]] 與 [[pelger-markus]]（2020）提出的統計因子萃取方法。在傳統 [[principal-component-analysis|PCA]] 的目標函數中加入**橫截面定價誤差項**，使萃取出的因子同時兼顧時序共變結構與橫截面風險溢酬捕捉能力。

**目標函數：**
$$L(\hat{F}_{RP}, \hat{\Lambda}_{RP}) = \frac{1}{NT}\sum (X_{nt} - F_t\Lambda_n^\top)^2 + \gamma \sum (\bar{X}_n - \bar{F}\Lambda_n^\top)^2$$

- 第一項：傳統 PCA 的時序配適誤差
- 第二項：橫截面定價誤差（加權 γ）

等價於對 $\Sigma_{RP} = \frac{1}{T}X^\top X + \gamma\bar{X}\bar{X}^\top$ 做 [[principal-component-analysis|PCA]]。

---

## 超參數 γ 的意義

| γ | 行為 |
|---|------|
| -1 | 等同於傳統 PCA（只看時序共變） |
| > 0 | 強調橫截面定價，γ 越大越強調 |
| 最佳（台灣市場） | γ = 10（進一步增至 20 改善有限） |

---

## 在知識庫中的出現

- **[[capturing-risk-premia-taiwan]]**：RP-PCA 在台灣前 100 大成交量股票上的應用；γ=10、T=13（季窗口）+ 130/30 策略下，第一因子年化 Sharpe Ratio 達 0.84，超越等權重基準（0.54）顯著

---

## 與傳統 PCA 的差異

| | 傳統 PCA | RP-PCA |
|--|---------|--------|
| 目標 | 最大化報酬共變數解釋比例 | 同時最大化時序配適 + 橫截面定價能力 |
| 萃取的因子 | 常反映統計雜訊 | 具明確風險溢酬意義 |
| 適用情境 | 降維 | 因子投資組合構建 |

---

## 關聯概念

[[principal-component-analysis]]、[[factor-models]]、[[machine-learning-asset-pricing]]、[[momentum]]、[[portfolio-optimization]]

## 關鍵文獻

Lettau & Pelger (2020) → 原創論文（在 [[capturing-risk-premia-taiwan]] 中為核心引用）
