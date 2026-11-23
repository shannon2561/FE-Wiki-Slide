# Measure Change & Girsanov Theorem（測度轉換與 Girsanov 定理）

## 定義

同一支股票可在不同機率測度下描述。真實測度 $P$ 下，股票期望報酬率為 $\mu$，包含風險溢酬 $\mu-r$；風險中立測度 $Q$ 下，期望報酬率為無風險利率 $r$。Girsanov 定理說明兩者的轉換方式：將布朗運動加上漂移項，$dw^P=dw^Q-\frac{\mu-r}{\sigma}dt$，股價方程式即由 $\frac{dS}{S}=\mu\,dt+\sigma dw^P$ 轉為 $\frac{dS}{S}=r\,dt+\sigma dw^Q$。轉換測度不改變哪些事件可能發生，只改變其機率權重。此外可再轉換至以股票計價的測度 $R$（$dw^Q=dw^R+\sigma dt$），用於計算 BS 公式中的 $N(d_1)$。

## 在知識庫中的出現

- [[fe-07-martingale-pricing]]：第 2–3 節示範 $P\to Q\to R$ 的轉換與 Radon-Nikodym 導數，並以 $R$ 測度求出 $N(d_1)$。
- [[fe-03-black-scholes-formula]]：比較真實世界 $P$ 與風險中立世界 $Q$ 下 $S_T$ 的分配與期望值。

## 關聯概念

[[risk-neutral-valuation]]、[[martingale]]、[[brownian-motion]]、[[black-scholes-model]]、[[probability-expected-value]]（測度的白話說明）
