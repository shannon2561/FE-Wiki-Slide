# Black-Scholes PDE（Black-Scholes 偏微分方程）

## 定義
所有以同一支股票為標的的衍生性商品，價格 $f(S,t)$ 都必須滿足的方程式：
$$rf=\frac{\partial f}{\partial t}+rS\frac{\partial f}{\partial S}+\frac12\sigma^2S^2\frac{\partial^2 f}{\partial S^2}$$
推導想法：用 Itô 定理寫出 $df$，再組一個「賣 1 單位衍生性商品、買 $\partial f/\partial S$ 股股票」的組合，兩者的隨機項剛好互相抵消，組合變成無風險，所以只能賺無風險利率 $r$。整理後就得到這條方程式。股票的真實期望報酬率 $\mu$ 在過程中被消掉，所以價格跟投資人對股票報酬的預期無關。不同商品的差別只在到期條件，例如歐式買權是 $f(S_T,T)=\max(S_T-K,0)$。求解方法有封閉解和數值解。

## 在知識庫中的出現
- [[fe-03-black-scholes-formula]]：第 2.1–2.3 節以 Itô 定理＋無風險組合推出 PDE，再用 Feynman-Kac 定理求解得到 BS 公式。
- [[fe-06-bs-pde-derivation]]：直接用 PDE 求解的路徑推導 BS 公式。

## 關聯概念
[[black-scholes-model]]、[[itos-lemma]]、[[delta-hedging-replication]]、[[risk-neutral-valuation]]
