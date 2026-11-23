# Portfolio Optimization（投資組合最佳化）

## 定義

在給定風險或報酬目標下，決定各資產配置比例的方法，從 Markowitz (1952) 的均值-變異數架構，延伸至因子組合與最大化 [[sharpe-ratio|Sharpe Ratio]] 等應用。

---

## 主要方法

| 方法 | 目標 | 限制 |
|------|------|------|
| Mean-Variance (Markowitz) | 最大化效用 E[R] − λVar | 須準確預測期望報酬 |
| 最大化 [[sharpe-ratio\|Sharpe Ratio]] | 最高 SR | 對輸入的估計值敏感 |
| 等權重 (1/N) | 分散 | 忽略因子資訊 |
| 風險平價 | 各資產的風險貢獻相等 | 不考慮報酬預測 |

---

## 權重調整策略

[[capturing-risk-premia-taiwan]] 比較三種 RP-PCA 因子的權重調整方式：

| 策略 | 公式 | 效果 |
|------|------|------|
| 放空限制 (Long-only) | $\omega_n^+ = \max(\omega_n,0) / \sum \max(\omega_i,0)$ | 第 2–5 因子的 SR 提升，具隱性正則化效果 |
| 130/30 策略 | 130% 做多、30% 放空 | 第一因子最佳 (0.84) |
| 波動率標準化 | $\omega_n^{vd} = \omega_n \times \sigma_{target}/\sigma_{factor}$ | 效果不穩定 |

Jagannathan & Ma (2003) 指出，即使是理論上「不正確」的限制（如放空限制），也會壓縮極端權重，降低估計誤差的影響，相當於隱性的正則化。

---

## 在知識庫中的出現

- **[[empirical-asset-pricing-ml]]**：以 ML 預測報酬後直接建構投組，個股多空十分位組合的 SR 為 1.35。
- **[[capturing-risk-premia-taiwan]]**：RP-PCA 因子搭配權重調整策略，最佳組合 SR 為 0.84。
- **[[dia-course-114-1]]**：MPT 課堂實作，以 `scipy.optimize.minimize` 求出 5 種投組，包括全域最小變異數 (G)、最大 Sharpe (M)、兩者的不可放空版本 (Gn、Mn) 與等權重 (EW)，並以 SPY 為樣本外基準。日頻未年化 Sharpe 依序為 G 0.1604、Gn 0.1601、Mn 0.1119、M 0.1002、EW 0.0787、SPY 0.0687。最小變異數組合的樣本外表現反而優於以最大化 Sharpe 為目標的組合，可見訓練目標與樣本外表現未必一致。

---

## 關聯概念

[[sharpe-ratio]]、[[factor-models]]、[[risk-premium-pca]]、[[momentum]]、[[machine-learning-asset-pricing]]
