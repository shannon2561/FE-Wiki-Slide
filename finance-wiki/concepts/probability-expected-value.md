# Probability & Expected Value（機率、期望值、變異數、標準差與測度）

## 定義

- **機率**：某件事發生的可能性，介於 0 到 1。例如股價只會上漲或下跌，上漲機率 0.6，下跌機率即為 0.4，所有可能情況的機率加總為 1。
- **隨機變數**：結果事先無法確定、但每種結果都有對應機率的量，例如 3 個月後的股價。
- **期望值**：以機率為權重，對所有可能結果加權平均，代表重複很多次時的平均結果，記為 $E[X]$。例如買權到期值為 1（機率 q）或 0（機率 1 − q），期望值為 $q\times1+(1-q)\times0=q$。
- **變異數**：各結果與期望值差距的平方，再以機率加權平均，衡量結果分散的程度，記為 $\mathrm{Var}(X)$。
- **測度**：一套「指定給所有可能結果的機率」。同樣是股價漲跌，可以用真實的機率衡量（真實測度 $P$），也可以用定價用的風險中立機率衡量（風險中立測度 $Q$）；轉換測度不改變哪些結果可能發生，只改變各結果的機率（見 [[measure-change-girsanov]]）。
- **標準差**：變異數開根號，單位與原本的量相同，記為 $\sigma$。金融上所說的波動度 (volatility) 即為報酬率的標準差，例如年化波動度 20%，代表一年報酬率的標準差為 20%。

## 例子

[[fe-01-options-binomial-tree]] 的一期例題中，風險中立機率 $q=0.6523$，買權到期值的期望值為 $0.6523\times1+0.3477\times0=0.6523$，再折現 $0.6523\times e^{-0.03}=0.633$，即為買權價格。

## 在知識庫中的出現

- [[risk-neutral-valuation]]、[[binomial-option-pricing]]：以風險中立機率計算到期 payoff 的期望值，再折現。
- [[brownian-motion]]：布朗運動增量的平均數為 0、變異數等於時間長度。
- [[geometric-brownian-motion]]：$\sigma$ 為年化波動度，即報酬率的標準差。
- [[martingale]]：以條件期望值 $E^Q[\cdot\mid\mathcal F_t]$ 定義。
- [[idiosyncratic-volatility]]：IVOL 為迴歸殘差的標準差。

## 關聯概念

[[normal-distribution]]、[[discounting-continuous-compounding]]、[[risk-neutral-valuation]]、[[return-rate]]、[[measure-change-girsanov]]

## 來源說明

定義為機率與統計的基礎知識整理；例子的數字依 [[fe-01-options-binomial-tree]] 的例題重新計算。
