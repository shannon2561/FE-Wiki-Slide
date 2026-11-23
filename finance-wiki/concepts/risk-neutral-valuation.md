# Risk-Neutral Valuation（風險中立評價）

## 定義

衍生性商品定價時，不使用股價真實的漲跌機率 $p$，改用使股票期望報酬率等於無風險利率的機率 $q$（風險中立機率），計算到期 payoff 的期望值後，再以無風險利率折現。可以如此處理，是因為選擇權價格由無套利條件決定（能否以股票與借貸複製），與投資人的風險偏好無關。在風險中立機率下，$E^Q[S_T]=S_0e^{rT}$，任何證券的期望報酬率皆為無風險利率。

## 在知識庫中的出現

- [[fe-01-options-binomial-tree]]：2.3 節以二元樹說明真實測度 $P$ 與風險中立測度 $Q$ 的差異，評價時須將 $p$ 換成 $q$。
- [[fe-03-black-scholes-formula]]：比較 $P$ 測度下 $E^P[S_T]=S_te^{\mu(T-t)}$ 與 $Q$ 測度下 $E^Q[S_T]=S_te^{r(T-t)}$；Feynman-Kac 定理將 BS PDE 的解寫成 $e^{-r(T-t)}E^Q[C_T]$。
- [[fe-07-martingale-pricing]]：提供理論依據，即無套利與風險中立測度的存在互為等價（Harrison & Pliska 1981、資產定價第一基本定理），並以 Girsanov 定理說明 $P$ 如何轉換為 $Q$（見 [[measure-change-girsanov]]、[[martingale]]）。
- [[black-scholes-model]]：整理離散版本（二元樹的 $q$）與連續版本（Feynman-Kac）的對應。

## 關聯概念

[[binomial-option-pricing]]、[[delta-hedging-replication]]、[[black-scholes-model]]
