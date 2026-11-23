# Itô's Lemma（Itô 定理）

## 定義

隨機過程的連鎖律：已知資產 $X$ 的變動 $dX=a\,dt+b\,dz$，可求出依附於 $X$ 的函數 $f(X,t)$（例如選擇權價格）如何變動：
$$df=\left(\frac{\partial f}{\partial t}+a\frac{\partial f}{\partial X}+\frac12 b^2\frac{\partial^2 f}{\partial X^2}\right)dt+b\frac{\partial f}{\partial X}dz$$
與一般微積分相比多出 $\frac12 b^2\frac{\partial^2 f}{\partial X^2}$ 一項，原因在於布朗運動的 $(dz)^2$ 等於 $dt$，並非可忽略的高階項，故泰勒展開的二階項須保留。

## 在知識庫中的出現

- [[fe-02-stock-dynamics-ito]]：第 5 節以泰勒展開證明單一資產與兩資產版本，兩資產版本含相關係數 $\rho$ 的交叉項，並說明此定理為推導 BS 方程式的工具。
- [[black-scholes-model]]：BS PDE 的推導過程使用 Itô 定理。

## 關聯概念

[[brownian-motion]]、[[geometric-brownian-motion]]、[[black-scholes-model]]、[[calculus-basics]]
