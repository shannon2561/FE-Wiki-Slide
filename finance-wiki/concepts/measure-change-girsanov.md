# Measure Change & Girsanov Theorem（測度轉換與 Girsanov 定理）

## 定義
同一支股票，可以用不同的「機率眼鏡」來看。**真實測度 $P$** 下，股票期望報酬率是 $\mu$（包含風險溢酬 $\mu-r$）；**風險中立測度 $Q$** 下，期望報酬率是無風險利率 $r$。Girsanov 定理說明怎麼在兩者之間轉換：只要把布朗運動加上一個漂移，$dw^P=dw^Q-\frac{\mu-r}{\sigma}dt$，股價方程式就從 $\frac{dS}{S}=\mu\,dt+\sigma dw^P$ 變成 $\frac{dS}{S}=r\,dt+\sigma dw^Q$。換測度不會改變哪些事情「可能發生」，只改變它們的機率權重。另外還能再換到以股票計價的測度 $R$（$dw^Q=dw^R+\sigma dt$），用來算 BS 公式中的 $N(d_1)$。

## 在知識庫中的出現
- [[fe-07-martingale-pricing]]：第 2–3 節示範 $P\to Q\to R$ 的轉換與 Radon-Nikodym 導數，並用 $R$ 測度算出 $N(d_1)$。
- [[fe-03-black-scholes-formula]]：對照真實世界 $P$ 與風險中立世界 $Q$ 下 $S_T$ 的分配與期望值。

## 關聯概念
[[risk-neutral-valuation]]、[[martingale]]、[[brownian-motion]]、[[black-scholes-model]]
