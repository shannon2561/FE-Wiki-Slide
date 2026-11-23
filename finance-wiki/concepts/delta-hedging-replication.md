# Delta Hedging & Replication（Delta 避險與複製）

## 定義
**複製**：用 $\Delta$ 股股票加上借貸金額 $B$ 組成一個投資組合，讓它在每一種情境下的現金流都跟選擇權一樣。兩者到期現金流相同，現在的價格就必須相同，否則有套利。**Delta** 是股價變動 1 單位時選擇權價格的變動量，二元樹裡 $\Delta=\frac{f_u-f_d}{S_u-S_d}$，買權為正、賣權為負。多期時 Delta 會隨股價改變，所以要**動態**調整持股；調整的錢只從組合本身來、不另外加錢，稱為**自我融資**。

## 在知識庫中的出現
- [[fe-03-black-scholes-formula]]：連續時間版本：持有 $\partial f/\partial S$ 股股票剛好抵消選擇權的隨機項，這個無風險組合就是推導 BS PDE 的起點；連續版 Delta $=N(d_1)$（見 [[option-greeks]]）
- [[fe-01-options-binomial-tree]]：2.4 節一期複製解出 $\Delta=0.25$、$B=-4.367$，買權 0.633；2.6 節二期例子 Delta(A)=0.5064、Delta(B)=0.7273、Delta(C)=0，並逐步追蹤發行商的避險組合，在每個到期節點剛好付清給投資人。
- [[derivatives-course-113-1]]：三上課程第十章 Greeks 與避險。

## 關聯概念
[[binomial-option-pricing]]、[[risk-neutral-valuation]]、[[black-scholes-model]]
