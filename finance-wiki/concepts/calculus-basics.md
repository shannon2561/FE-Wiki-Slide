# Calculus Basics（微積分基礎：微分、偏微分、積分）

## 定義

- **微分**：瞬間的變化率，即一個量改變一點點時，另一個量跟著改變多少。記為 $\frac{df}{dx}$。例如位置對時間微分即為速度。
- **偏微分**：函數有多個變數時，只讓其中一個變動、其他固定，所得到的變化率，記為 $\frac{\partial f}{\partial x}$。選擇權價格同時受股價、時間、波動度、利率影響，對股價偏微分即為 Delta。
- **二階微分**：變化率本身的變化率。對股價二階偏微分即為 Gamma，衡量 Delta 隨股價變化的速度。
- **$dt$、$dS$、$dz$**：極小的時間間隔，以及這段時間內股價或隨機項的變動量。$dS=\mu S\,dt+\sigma S\,dz$ 即描述極短時間內股價如何變動。
- **積分**：把很多極小的量加總起來，在圖上即為曲線下的面積。累積機率 $N(d)$ 即為標準常態曲線在 $d$ 左側的面積。
- **偏微分方程 (PDE)**：含有偏微分的方程式，描述一個量如何隨多個變數一起變化。Black-Scholes PDE 與熱傳導方程式皆屬此類。

## 例子

以 $S=K=100$、$r=5\%$、$\sigma=20\%$、$T=1$ 計算，買權價格為 10.4506，Delta $=\partial C/\partial S=0.6368$，代表股價由 100 元漲至 101 元時，買權價格約上漲 0.64 元（見 [[fe-03-black-scholes-formula]]、[[option-greeks]]）。

## 在知識庫中的出現

- [[option-greeks]]：五個 Greeks 皆為 BS 公式的偏微分。
- [[itos-lemma]]：隨機過程的連鎖律，以泰勒展開推導。
- [[black-scholes-pde]]、[[heat-equation-method]]：偏微分方程與其解法。
- [[brownian-motion]]、[[geometric-brownian-motion]]：以 $dt$、$dz$ 描述極短時間的變動。
- [[normal-distribution]]：累積機率為曲線下的面積。

## 關聯概念

[[normal-distribution]]、[[itos-lemma]]、[[black-scholes-pde]]、[[option-greeks]]

## 來源說明

定義為微積分基礎知識的整理；Delta 數值取自 [[fe-03-black-scholes-formula]] 的驗證結果。
