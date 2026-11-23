# Option Greeks（選擇權避險參數）

## 定義

衡量選擇權價格對各項因素敏感程度的指標，皆為 BS 公式的偏微分。以歐式買權為例：

- Delta $=\partial C/\partial S=N(d_1)$：股價變動 1 元時選擇權價格的變動量，亦為避險時應持有的股數。
- Gamma $=\partial^2C/\partial S^2=\frac{n(d_1)}{S\sigma\sqrt{T-t}}$：Delta 隨股價變動的速度。
- Vega $=\partial C/\partial\sigma=S\sqrt{T-t}\,n(d_1)$：波動度變動的影響。
- Rho $=\partial C/\partial r=K(T-t)e^{-r(T-t)}N(d_2)$：利率變動的影響。
- Theta $=\partial C/\partial t=-\frac{S\sigma n(d_1)}{2\sqrt{T-t}}-rKe^{-r(T-t)}N(d_2)$：時間經過造成的價值減少，買權為負。

其中 $N(\cdot)$ 為標準常態累積分配函數，$n(\cdot)$ 為標準常態機率密度函數。

## 在知識庫中的出現

- [[fe-03-black-scholes-formula]]：第 3 節逐一證明五個 Greeks；ingest 時以數值微分驗證皆一致，並發現第 4 頁總表中 Theta 第二項的正負號有誤。
- [[delta-hedging-replication]]：二元樹的 Delta $\frac{f_u-f_d}{S_u-S_d}$ 為連續版 Delta 的離散對應。
- [[derivatives-course-113-1]]：三上課程第十章，Greeks 與避險。

## 關聯概念

[[black-scholes-model]]、[[delta-hedging-replication]]、[[calculus-basics]]（Greeks 皆為偏微分）、[[normal-distribution]]
