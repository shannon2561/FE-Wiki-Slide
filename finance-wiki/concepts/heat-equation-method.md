# Heat Equation Method（以熱傳導方程式求解 BS PDE）

## 定義

熱傳導方程式 $U_t=c^2U_{xx}$ 描述熱在金屬棒中隨時間擴散的情形，其解為以常態分配的鐘形曲線對起始溫度分布 $g(x)$ 加權平均：$U(x,t)=\int\frac{1}{\sqrt{4\pi c^2t}}e^{-\frac{(x-y)^2}{4c^2t}}g(y)\,dy$。Black-Scholes PDE 經變數轉換（$\tau=T-t$、$x=\ln\frac SK+(r-\frac12\sigma^2)\tau$、$C=e^{-r\tau}V$）後，即成為 $c^2=\frac12\sigma^2$ 的熱傳導方程式，故可直接套用此解得到 BS 公式。到期 payoff 相當於起始溫度，距到期時間越長，不確定性如熱一般擴散得越開。

## 在知識庫中的出現

- [[fe-06-bs-pde-derivation]]：示範以傅立葉轉換求解熱傳導方程式、BS PDE 的變數轉換，以及積分得到 BS 公式的完整過程；ingest 時已以數值驗證轉換與解的正確性。

## 關聯概念

[[black-scholes-pde]]、[[black-scholes-model]]
