# Normal Distribution（常態分配與累積機率 N(·)）

## 定義

常態分配是左右對稱的鐘形分配，由平均數決定中心位置、標準差決定寬窄。許多隨機現象近似常態分配，布朗運動的增量即服從常態分配。平均數 0、標準差 1 的常態分配稱為標準常態分配。

- 落在平均數 ±1 個標準差內的機率約 68%，±2 個標準差內約 95%。
- **累積機率 $N(d)$**：標準常態隨機變數小於 $d$ 的機率，即鐘形曲線在 $d$ 左側的面積，數值介於 0 與 1。例如 $N(0)=0.5$、$N(1)=0.8413$、$N(-1)=0.1587$。
- **機率密度 $n(d)$**：鐘形曲線在 $d$ 處的高度，$n(d)=\frac{1}{\sqrt{2\pi}}e^{-d^2/2}$。

## 例子

Black-Scholes 公式中的 $N(d_1)$ 與 $N(d_2)$ 皆為累積機率。以 $S=K=100$、$r=5\%$、$\sigma=20\%$、$T=1$ 計算，$N(d_2)=0.5596$，即風險中立世界中買權到期被執行的機率約 56%（見 [[fe-07-martingale-pricing]]）。

## 在知識庫中的出現

- [[brownian-motion]]：增量 $B(t+\Delta t)-B(t)\sim N(0,\Delta t)$。
- [[black-scholes-model]]、[[fe-03-black-scholes-formula]]：公式中的 $N(d_1)$、$N(d_2)$。
- [[option-greeks]]：Gamma、Vega、Theta 公式中的 $n(d_1)$。
- [[fe-07-martingale-pricing]]：$N(d_2)=\Pr^Q(S_T>K)$、$N(d_1)=\Pr^R(S_T>K)$。
- [[heat-equation-method]]：熱傳導方程式的解以常態分配的鐘形曲線加權平均。

## 關聯概念

[[probability-expected-value]]、[[brownian-motion]]、[[black-scholes-model]]

## 來源說明

定義為統計基礎知識的整理；$N(0)$、$N(1)$、68%／95% 等數字以 Python 計算確認，BS 數值例取自 [[fe-07-martingale-pricing]]。
