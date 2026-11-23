# Risk-Neutral Valuation（風險中立評價）

## 定義
替衍生性商品定價時，不用股價真實的漲跌機率 $p$，而是改用一組「讓股票期望報酬率剛好等於無風險利率」的機率 $q$（風險中立機率），算出到期 payoff 的期望值，再用無風險利率折現。可以這樣做，是因為選擇權的價格由無套利（能不能被複製）決定，跟投資人喜不喜歡風險無關。在風險中立機率下，$E^Q[S_T]=S_0e^{rT}$，任何證券的平均報酬率都是無風險利率。

## 在知識庫中的出現
- [[fe-03-black-scholes-formula]]：對照 $P$ 測度 $E^P[S_T]=S_te^{\mu(T-t)}$ 與 $Q$ 測度 $E^Q[S_T]=S_te^{r(T-t)}$；Feynman-Kac 定理把 BS PDE 的解寫成 $e^{-r(T-t)}E^Q[C_T]$
- [[fe-07-martingale-pricing]]：給出理論根據：無套利 ⇔ 存在風險中立測度（Harrison & Pliska 1981、資產定價第一基本定理），並用 Girsanov 定理說明 $P\to Q$ 怎麼換（見 [[measure-change-girsanov]]、[[martingale]]）
- [[fe-01-options-binomial-tree]]：2.3 節以二元樹說明真實測度 $P$ 與風險中立測度 $Q$ 的差別，指出評價時必須把 $p$ 換成 $q$。
- [[black-scholes-model]]：概念頁已整理離散（二元樹的 $q$）與連續（Feynman-Kac）版本的對應。

## 關聯概念
[[binomial-option-pricing]]、[[delta-hedging-replication]]、[[black-scholes-model]]
