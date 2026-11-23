# Principal Component Analysis（主成分分析）

## 定義

無監督的降維方法，對共變異數矩陣進行特徵值分解，找出解釋資料最多變異的正交主成分。在金融因子模型中，用於從資產報酬矩陣萃取潛在的共同因子。

標準 PCA 的目標函數：
$$L(\hat{F}_{PCA}, \hat{\Lambda}_{PCA}) = \frac{1}{NT}\sum_{n,t}(X_{nt} - F_t\Lambda_n^\top)^2$$

---

## 變體

| 方法 | 目標 | 差異 |
|------|------|------|
| 標準 PCA | 最大化時間序列共變的解釋 | 不考慮定價能力 |
| [[risk-premium-pca\|RP-PCA]] | 時間序列與橫截面定價 | 加入以 γ 加權的定價誤差項 |
| PCR（主成分迴歸） | 降維後進行線性迴歸 | [[empirical-asset-pricing-ml]] 使用 |

---

## 在知識庫中的出現

- **[[empirical-asset-pricing-ml]]**：PCR 作為降維的基準方法，表現略優於 OLS，但遠不及神經網路。
- **[[capturing-risk-premia-taiwan]]**：以 RP-PCA 為主要方法；γ = −1 時等同傳統 PCA，γ = 10 時表現明顯改善。傳統 PCA 第二因子的 SR 約為 0，RP-PCA 則為 0.32。
- **[[ml-financial-econometrics-course]]**：HW1 對訓練集進行 PCA，以 2-fold CV、AIC 與 Onatski criterion 三種方法決定主成分個數，並比較 PCR 與 PLS。
- **[[quantitative-methods-finance-course]]**：向量空間與基底變換（[[linear-algebra-vector-space]]）為 PCA 的前置數學，課程本身未教授 PCA。

---

## 限制

傳統 PCA 萃取的主成分只最大化時間序列的共變，不保證具有定價能力，也不保證能預測期望報酬，常會抓到統計雜訊。[[risk-premium-pca]] 即針對此問題提出。

---

## 關聯概念

[[risk-premium-pca]]、[[factor-models]]、[[machine-learning-asset-pricing]]、[[portfolio-optimization]]
