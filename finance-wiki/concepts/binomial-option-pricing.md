# Binomial Option Pricing（二項樹選擇權定價）

## 定義
假設每一期股價只會漲到 $S_0u$ 或跌到 $S_0d$。建構「賣 1 單位選擇權、買 $\Delta$ 單位股票」的組合，選一個 $\Delta$ 讓組合不管漲跌價值都一樣（無風險），再用「無風險組合只能賺無風險利率」的無套利條件，解出選擇權價格：
$$f=e^{-rT}[q f_u+(1-q)f_d],\qquad q=\frac{e^{rT}-d}{u-d}$$
多期時從到期日開始往回，每個節點都用同一條公式折現。$0<q<1$ 才沒有套利機會。期數越切越細時，結果會收斂到 Black-Scholes 公式。

## 在知識庫中的出現
- [[fe-01-options-binomial-tree]]：2.1–2.5 節。一期例子 $S_0=20$、$u=1.1$、$d=0.9$、$K=21$、$r=12\%$、$T=0.25$，得 $q=0.6523$、買權 0.633；二期例子起點價值 1.2823。另有賣權與美式賣權練習題（$K=52$）。
- [[derivatives-course-113-1]]：三上課程第六章二項式樹定價。

## 關聯概念
[[risk-neutral-valuation]]、[[delta-hedging-replication]]、[[option-basics]]、[[black-scholes-model]]

## 關聯文獻
Cox, Ross & Rubinstein (1979), "Option Pricing: A Simplified Approach"（講義引用，未 ingest）
