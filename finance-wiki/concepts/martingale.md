# Martingale（鞅）

## 定義

隨時間變動的隨機量，若依據目前所有資訊，對其未來值的最佳預測即為現在的值，則稱為 martingale：$X(t)=E^Q[X(T)\mid\mathcal F_t]$，相當於一場平均而言不賺不賠的公平賭局。在無套利的市場中存在風險中立測度 $Q$，使所有資產價格除以貨幣帳戶 $\beta(t)$ 後皆為 martingale，故任何商品的價格 $=\beta(t)\,E^Q[H(T)/\beta(T)]$，即風險中立期望值再折現。

## 在知識庫中的出現

- [[fe-07-martingale-pricing]]：定義 martingale、sub-martingale 與 super-martingale，寫出或有求償權的定價公式，並由此推出 BS 公式。

## 關聯概念

[[risk-neutral-valuation]]、[[measure-change-girsanov]]、[[black-scholes-model]]
