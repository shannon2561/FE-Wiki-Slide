# 財務工程與金融創新（一）講義 06：使用 BS 之 PDE 推導 BS 定價公式

**類型**：course  
**作者**：授課教師（講義未署名）  
**年份**：2026（115-1 四上財工）  
**原始檔**：衍生性金融商品/四上財工/上課簡報/06 使用BS之PDE推導BS定價公式.pdf  
**檔名**：06 使用BS之PDE推導BS定價公式.pdf（22 頁）

---

## 核心問題
不用機率（期望值）的方法，直接解 Black-Scholes PDE，能不能得到同一個 BS 公式？

## 方法
1. 介紹物理學的熱傳導方程式 $U_t=c^2U_{xx}$。
2. 用傅立葉轉換把 PDE 變成常微分方程（ODE），解完再用傅立葉逆轉換換回來，得到熱傳導方程式的解。
3. 用變數轉換把 BS PDE 變成熱傳導方程式。
4. 代入熱傳導方程式的解，經過積分變數轉換得到 BS 公式。

## 主要發現
- **熱傳導方程式的解**：$U(x,t)=\int_{-\infty}^{\infty}\frac{1}{\sqrt{4\pi c^2t}}e^{-\frac{(x-y)^2}{4c^2t}}g(y)\,dy$，也就是把起始溫度 $g$ 用常態分配的鐘形曲線「抹開」。見 [[heat-equation-method]]。
- **關鍵變數轉換**：令 $\tau=T-t$（距到期時間）、$x=\ln\frac SK+(r-\frac12\sigma^2)\tau$、$C=e^{-r\tau}V(x,\tau)$，BS PDE 就變成 $V_\tau=\frac12\sigma^2V_{xx}$，到期條件變成 $V(x,0)=K(e^x-1)^+$。也就是說，選擇權價格隨時間的變化，數學上跟熱在金屬棒裡擴散是同一件事。
- **解出 BS 公式**：代入熱傳導方程式的解並做兩次積分變數轉換，得到 $V=Se^{r\tau}N(d_1)-KN(d_2)$，乘回 $e^{-r\tau}$ 就是 $C=SN(d_1)-Ke^{-r\tau}N(d_2)$，和 [[fe-03-black-scholes-formula]] 用 Feynman-Kac 得到的結果完全一樣。見 [[black-scholes-pde]]。
- **ingest 時的驗證**：以 $K=100$、$r=5\%$、$\sigma=20\%$ 數值檢查，轉換後的函數確實滿足 $V_\tau=\frac12\sigma^2V_{xx}$（6.18426 vs 6.18425）；用熱核積分算出的 $V$ 與 BS 公式一致（13.49246 vs 13.49248）。

## 關聯概念
[[black-scholes-pde]]、[[heat-equation-method]]、[[black-scholes-model]]

## 關聯文獻
[[fe-03-black-scholes-formula]]（同一個公式的 Feynman-Kac 推導）；[[fe-07-martingale-pricing]]（Martingale 推導）
