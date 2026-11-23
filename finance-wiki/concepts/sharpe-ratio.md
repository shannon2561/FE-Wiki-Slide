# Sharpe Ratio（夏普比率）

## 定義

$$SR = \frac{E[R_p] - R_f}{\sigma_p}$$

風險調整後報酬的核心績效指標。衡量每單位總風險所獲得的超額報酬。年化 Sharpe Ratio 通常將月度 SR × √12。

---

## 知識庫中的關鍵數字

| 策略 | [[sharpe-ratio|SR]] | 來源 |
|------|-----|------|
| 台灣等權重基準（EW top-100） | 0.54 | [[capturing-risk-premia-taiwan]] |
| RP-PCA (γ=10, T=13) 第一因子 | 0.82 | [[capturing-risk-premia-taiwan]] |
| RP-PCA (γ=10, T=13) + 130/30 第一因子 | **0.84** | [[capturing-risk-premia-taiwan]] |
| Convex-NMF 第一因子 | 0.49 | [[capturing-risk-premia-taiwan]] |
| S&P 500 神經網路擇時 | 0.77 vs. 買持 0.51 | [[empirical-asset-pricing-ml]] |
| 個股多空十分位（神經網路） | **1.35** | [[empirical-asset-pricing-ml]] |

---

## 在知識庫中的出現

- **[[empirical-asset-pricing-ml]]**：SR 是評估 ML 預測方法經濟價值的主要指標；神經網路使 SR 翻倍
- **[[capturing-risk-premia-taiwan]]**：RP-PCA 超越等權重基準（0.54）；最優達 0.84；Convex-NMF 低於基準
- **[[dia-course-114-1]]**：MPT 範例 notebook 實際輸出的日頻 Sharpe（未年化）比較表，可作為「不同最佳化目標函數（最小變異數 vs 最大 Sharpe）在樣本外表現未必符合預期」的教學案例
- **[[macd-adx-fibonacci-futures-strategy]]**、**[[rsi-overbought-oversold-futures-strategy]]**、**[[adx-regime-switching-donchian-bollinger-strategy]]**、**[[volatility-squeeze-breakout]]**：TMBA 程交部量化策略專案群，皆以年化 Sharpe 為核心績效指標；多數專案樣本外 Sharpe 明顯低於教科書預期或落後 Buy & Hold（如 RSI 策略 OOS Sharpe 0.45 vs Buy & Hold 1.00），是「回測 Sharpe 打折」經驗法則的具體案例

---

## 相關指標

| 指標 | 計算 | 特色 |
|------|------|------|
| Sharpe Ratio | 超額報酬 / 總波動 | 最常用 |
| Calmar Ratio | 年化報酬 / 最大回撤 | 更關注尾部風險 |
| Information Ratio | 主動報酬 / 追蹤誤差 | 相對基準 |

---

## 關聯概念

[[portfolio-optimization]]、[[factor-models]]、[[risk-premium-pca]]、[[machine-learning-asset-pricing]]
