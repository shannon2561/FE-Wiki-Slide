# Portfolio Optimization（投資組合最佳化）

## 定義

在給定風險或報酬目標下，決定各資產最佳配置比例的方法。從 Markowitz (1952) 的均值-變異數框架，到因子組合、最大化 [[sharpe-ratio|Sharpe Ratio]] 的現代應用。

---

## 主要方法

| 方法 | 目標 | 限制 |
|------|------|------|
| Mean-Variance（Markowitz） | 最大化效用（E[R] - λVar） | 需要準確預測期望報酬 |
| 最大化 [[sharpe-ratio\|Sharpe Ratio]] | 最高 SR | 對輸入估計敏感 |
| 等權重（1/N） | 分散 | 忽略因子資訊 |
| 風險平價 | 各資產風險貢獻相等 | 不考慮報酬預測 |

---

## 權重調整策略（知識庫重點）

[[capturing-risk-premia-taiwan]] 研究了三種 RP-PCA 因子的權重調整策略：

| 策略 | 公式 | 效果 |
|------|------|------|
| **放空限制（Long-only）** | $\omega_n^+ = \max(\omega_n,0) / \sum \max(\omega_i,0)$ | 第 2–5 因子 SR 顯著提升；隱性正規化 |
| **130/30 策略** | 130% 做多 + 30% 放空 | 第一因子最佳（0.84） |
| **波動率標準化** | $\omega_n^{vd} = \omega_n \times \sigma_{target}/\sigma_{factor}$ | 效果不穩定 |

Jagannathan & Ma (2003)：即使是「不正確」的約束（如放空限制），也能透過縮減極端權重來降低估計誤差的影響，起到隱性正規化的效果。

---

## 在知識庫中的出現

- **[[empirical-asset-pricing-ml]]**：ML 預測報酬後直接用於組合構建；個股多空十分位 SR 1.35
- **[[capturing-risk-premia-taiwan]]**：RP-PCA 因子 + 權重調整策略；最優組合 SR 0.84
- **[[dia-course-114-1]]**：MPT 課堂實作範例，用 `scipy.optimize.minimize` 解出 5 種投資組合（全域最小變異數 G／最大 Sharpe M／不可放空版本 Gn、Mn／等權重 EW），樣本外對 SPY 做基準比較（日頻未年化 Sharpe：G 0.1604、Gn 0.1601、Mn 0.1119、M 0.1002、EW 0.0787、SPY 0.0687）——最小變異數組合樣本外表現反而優於以最大化 Sharpe 為目標訓練出的組合，是「訓練目標與樣本外表現未必一致」的具體教學案例

---

## 關聯概念

[[sharpe-ratio]]、[[factor-models]]、[[risk-premium-pca]]、[[momentum]]、[[machine-learning-asset-pricing]]
