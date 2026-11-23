# Binomial Option Pricing（二項樹選擇權定價）

## 定義

假設每期股價只會上漲至 $S_0u$ 或下跌至 $S_0d$。建構「賣出 1 單位選擇權、買入 $\Delta$ 單位股票」的組合，選擇 $\Delta$ 使組合在漲跌兩種情況下價值相同，此時組合無風險，依無套利條件只能賺取無風險利率，即可解出選擇權價格：
$$f=e^{-rT}[q f_u+(1-q)f_d],\qquad q=\frac{e^{rT}-d}{u-d}$$
多期時由到期日開始，每個節點以同一公式往回折現。$0<q<1$ 時才沒有套利機會；期數切得越細，結果越接近 Black-Scholes 公式。

## 在知識庫中的出現

- [[fe-01-options-binomial-tree]]：2.1–2.5 節。一期例題 $S_0=20$、$u=1.1$、$d=0.9$、$K=21$、$r=12\%$、$T=0.25$，得 $q=0.6523$，買權價格 0.633；二期例題的起點價值為 1.2823。另附賣權與美式賣權練習題 ($K=52$)。
- [[derivatives-course-113-1]]：三上課程第六章，二項式樹定價。

## 關聯概念

[[risk-neutral-valuation]]、[[delta-hedging-replication]]、[[option-basics]]、[[black-scholes-model]]

## 關聯文獻

Cox, Ross & Rubinstein (1979), "Option Pricing: A Simplified Approach"（講義引用，未 ingest）
