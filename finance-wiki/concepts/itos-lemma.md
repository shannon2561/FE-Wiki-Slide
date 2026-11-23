# Itô's Lemma（Itô 定理）

## 定義
隨機世界裡的「連鎖律」：已知某個資產 $X$ 怎麼隨機變動（$dX=a\,dt+b\,dz$），就能算出依附在它上面的函數 $f(X,t)$（例如選擇權價格）怎麼變動：
$$df=\left(\frac{\partial f}{\partial t}+a\frac{\partial f}{\partial X}+\frac12 b^2\frac{\partial^2 f}{\partial X^2}\right)dt+b\frac{\partial f}{\partial X}dz$$
跟一般微積分最大的差別是多了 $\frac12 b^2\frac{\partial^2 f}{\partial X^2}$。原因是布朗運動的 $(dz)^2$ 不是可以忽略的小量，而是等於 $dt$，所以泰勒展開的二階項會留下來。

## 在知識庫中的出現
- [[fe-02-stock-dynamics-ito]]：第 5 節以泰勒展開證明單一資產與兩資產（含相關係數 $\rho$ 的交叉項）版本，並說明這是推導 BS 方程式的工具。
- [[black-scholes-model]]：BS PDE 的推導鏈中使用 Itô 定理。

## 關聯概念
[[brownian-motion]]、[[geometric-brownian-motion]]、[[black-scholes-model]]
