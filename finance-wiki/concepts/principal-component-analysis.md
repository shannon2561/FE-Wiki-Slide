# Principal Component Analysis（主成分分析）

## 定義

PCA 是一種無監督降維方法，透過對協方差矩陣做特徵值分解，找出解釋資料最大變異的正交主成分。在金融因子模型中，用來從資產報酬矩陣萃取潛在共同因子。

**標準 PCA 目標函數：**
$$L(\hat{F}_{PCA}, \hat{\Lambda}_{PCA}) = \frac{1}{NT}\sum_{n,t}(X_{nt} - F_t\Lambda_n^\top)^2$$

---

## 變體

| 方法 | 目標 | 差異 |
|------|------|------|
| 標準 PCA | 最大化時序共變解釋 | 不考慮定價能力 |
| **[[risk-premium-pca\|RP-PCA]]** | 時序 + 橫截面定價 | 加入 γ 加權定價誤差項 |
| **PCR**（主成分迴歸） | 降維後做線性迴歸 | [[empirical-asset-pricing-ml]] 使用 |

---

## 在知識庫中的出現

- **[[empirical-asset-pricing-ml]]**：PCR 作為降維基準方法（比 OLS 稍好，但遠不如神經網路）
- **[[capturing-risk-premia-taiwan]]**：RP-PCA 是核心方法；γ=-1 時等同傳統 PCA，γ=10 時顯著改善；傳統 PCA 第二因子 SR ≈ 0，RP-PCA 則為 0.32
- **[[ml-financial-econometrics-course]]**：HW1 對訓練集做 PCA，以 2-fold CV、AIC、Onatski criterion 三種方法決定主成分數，並比較 PCR 與 PLS
- **[[quantitative-methods-finance-course]]**：向量空間與基底變換（[[linear-algebra-vector-space]]）是 PCA 的數學前置知識，課程本身未直接教授 PCA，屬弱關聯

---

## 關鍵限制（傳統 PCA）

傳統 PCA 在因子投資中的核心問題：萃取出的主成分最大化時序共變，但**不保證**這些因子具有定價能力或能預測期望報酬。常常抓到統計雜訊。[[risk-premium-pca]] 是針對這個問題的直接回應。

---

## 關聯概念

[[risk-premium-pca]]、[[factor-models]]、[[machine-learning-asset-pricing]]、[[portfolio-optimization]]
