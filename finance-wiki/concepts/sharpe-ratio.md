# Sharpe Ratio（夏普比率）

## 定義

$$SR = \frac{E[R_p] - R_f}{\sigma_p}$$

每承擔一單位總風險所得到的超額報酬，為最常用的風險調整後績效指標。月度 SR 乘以 √12 即為年化 SR。

---

## 知識庫中的數字

| 策略 | [[sharpe-ratio|SR]] | 來源 |
|------|-----|------|
| 台灣等權重基準 (EW top-100) | 0.54 | [[capturing-risk-premia-taiwan]] |
| RP-PCA (γ = 10, T = 13) 第一因子 | 0.82 | [[capturing-risk-premia-taiwan]] |
| RP-PCA (γ = 10, T = 13) 搭配 130/30，第一因子 | 0.84 | [[capturing-risk-premia-taiwan]] |
| Convex-NMF 第一因子 | 0.49 | [[capturing-risk-premia-taiwan]] |
| S&P 500 神經網路擇時 | 0.77，買進持有為 0.51 | [[empirical-asset-pricing-ml]] |
| 個股多空十分位組合（神經網路） | 1.35 | [[empirical-asset-pricing-ml]] |

---

## 在知識庫中的出現

- **[[empirical-asset-pricing-ml]]**：以 SR 衡量 ML 預測的經濟價值，神經網路使 SR 約提高一倍。
- **[[capturing-risk-premia-taiwan]]**：RP-PCA 高於等權重基準 (0.54)，最高為 0.84；Convex-NMF 則低於基準。
- **[[dia-course-114-1]]**：MPT 範例 notebook 輸出各投組的日頻 Sharpe（未年化），顯示最小變異數與最大 Sharpe 等不同目標函數，在樣本外的表現未必符合預期。
- **[[macd-adx-fibonacci-futures-strategy]]**、**[[rsi-overbought-oversold-futures-strategy]]**、**[[adx-regime-switching-donchian-bollinger-strategy]]**、**[[volatility-squeeze-breakout]]**：社團量化交易策略專案，皆以年化 Sharpe 為主要績效指標。多數專案的樣本外 Sharpe 低於預期或落後 Buy & Hold，例如 RSI 策略樣本外 Sharpe 為 0.45，Buy & Hold 為 1.00，可作為「回測 Sharpe 須打折」的實例。

---

## 相關指標

| 指標 | 計算 | 特色 |
|------|------|------|
| Sharpe Ratio | 超額報酬 ÷ 總波動 | 最常用 |
| Calmar Ratio | 年化報酬 ÷ 最大回撤 | 較重視尾部風險 |
| Information Ratio | 主動報酬 ÷ 追蹤誤差 | 相對於基準 |

---

## 關聯概念

[[portfolio-optimization]]、[[factor-models]]、[[risk-premium-pca]]、[[machine-learning-asset-pricing]]
