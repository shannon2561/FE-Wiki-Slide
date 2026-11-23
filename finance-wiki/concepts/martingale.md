# Martingale（鞅）

## 定義
一個隨時間變動的隨機量，如果「根據目前所有資訊，對它未來值的最佳預測就是它現在的值」，就叫 martingale：$X(t)=E^Q[X(T)\mid\mathcal F_t]$。可以想成一場公平的賭局：平均來說不會賺也不會賠。在定價理論裡，無套利的市場存在一個風險中立測度 $Q$，使所有資產價格除以貨幣帳戶 $\beta(t)$ 之後都是 martingale，因此任何商品的價格 $=\beta(t)\,E^Q[H(T)/\beta(T)]$，也就是「風險中立期望值再折現」。

## 在知識庫中的出現
- [[fe-07-martingale-pricing]]：定義 martingale／sub-／super-martingale，寫出或有求償權的定價公式，並以此推出 BS 公式。

## 關聯概念
[[risk-neutral-valuation]]、[[measure-change-girsanov]]、[[black-scholes-model]]
