# Heat Equation Method（以熱傳導方程式求解 BS PDE）

## 定義
熱傳導方程式 $U_t=c^2U_{xx}$ 描述熱在一根金屬棒裡隨時間擴散的情形，它的解是把起始溫度分布 $g(x)$ 用常態分配的鐘形曲線加權平均：$U(x,t)=\int\frac{1}{\sqrt{4\pi c^2t}}e^{-\frac{(x-y)^2}{4c^2t}}g(y)\,dy$。Black-Scholes PDE 經過變數轉換（$\tau=T-t$、$x=\ln\frac SK+(r-\frac12\sigma^2)\tau$、$C=e^{-r\tau}V$）後，會變成 $c^2=\frac12\sigma^2$ 的熱傳導方程式，所以可以直接套用這個解，得到 BS 公式。直覺上，到期 payoff 就像「起始溫度」，越往現在推，不確定性就像熱一樣擴散開來。

## 在知識庫中的出現
- [[fe-06-bs-pde-derivation]]：完整示範傅立葉轉換解熱傳導方程式、BS PDE 的變數轉換，以及積分得到 BS 公式的每一步；ingest 時已用數值驗證轉換與解的正確性。

## 關聯概念
[[black-scholes-pde]]、[[black-scholes-model]]
