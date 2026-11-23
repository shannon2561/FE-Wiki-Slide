# Delta Hedging & Replication（Delta 避險與複製）

## 定義

複製 (replication) 為以 $\Delta$ 股股票加上借貸金額 $B$ 組成投資組合，使其在每種情境下的現金流皆與選擇權相同。兩者到期現金流相同，現在的價格亦須相同，否則存在套利。Delta 為股價變動 1 單位時選擇權價格的變動量，二元樹中 $\Delta=\frac{f_u-f_d}{S_u-S_d}$，買權為正、賣權為負。多期時 Delta 隨股價改變，持股須動態調整，且調整所需資金僅來自組合本身，稱為自我融資 (self-financing)。

## 在知識庫中的出現

- [[fe-01-options-binomial-tree]]：2.4 節以一期複製解出 $\Delta=0.25$、$B=-4.367$，買權價格 0.633；2.6 節二期例題 Delta(A)=0.5064、Delta(B)=0.7273、Delta(C)=0，並逐步追蹤發行商的避險組合，於每個到期節點恰好支付投資人應得金額。
- [[fe-03-black-scholes-formula]]：連續時間版本。持有 $\partial f/\partial S$ 股股票可抵銷選擇權的隨機項，此無風險組合即為推導 BS PDE 的起點；連續版 Delta 為 $N(d_1)$（見 [[option-greeks]]）。
- [[derivatives-course-113-1]]：三上課程第十章，Greeks 與避險。

## 關聯概念

[[binomial-option-pricing]]、[[risk-neutral-valuation]]、[[black-scholes-model]]
