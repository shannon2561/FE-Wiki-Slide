# Black-Scholes PDE（Black-Scholes 偏微分方程）

## 定義

以同一支股票為標的之衍生性商品，價格 $f(S,t)$ 皆須滿足：
$$rf=\frac{\partial f}{\partial t}+rS\frac{\partial f}{\partial S}+\frac12\sigma^2S^2\frac{\partial^2 f}{\partial S^2}$$
推導方式為先以 Itô 定理寫出 $df$，再建構「賣出 1 單位衍生性商品、買入 $\partial f/\partial S$ 股股票」的組合，兩者的隨機項互相抵銷，組合無風險，故只能賺取無風險利率 $r$，整理後即得此方程式。股票的真實期望報酬率 $\mu$ 在過程中消去，代表價格與投資人對報酬的預期無關。不同商品的差別僅在到期條件，例如歐式買權為 $f(S_T,T)=\max(S_T-K,0)$；求解方式分為封閉解與數值解。

## 在知識庫中的出現

- [[fe-03-black-scholes-formula]]：第 2.1–2.3 節以 Itô 定理與無風險組合推出 PDE，再以 Feynman-Kac 定理求解，得到 BS 公式。
- [[fe-06-bs-pde-derivation]]：直接求解 PDE 推導 BS 公式。

## 關聯概念

[[black-scholes-model]]、[[itos-lemma]]、[[delta-hedging-replication]]、[[risk-neutral-valuation]]
