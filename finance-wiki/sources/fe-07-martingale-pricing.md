# 財務工程與金融創新（一）講義 07：Martingale 定價理論

**類型**：course  
**作者**：授課教師（講義未署名）  
**年份**：2026（115-1 四上財工；投影片頁尾日期為 2024/9/27）  
**原始檔**：衍生性金融商品/四上財工/上課簡報/07 Martingale定價理論.pdf  
**檔名**：07 Martingale定價理論.pdf（25 頁）

---

## 核心問題

為何在風險中立世界取期望值再折現即為正確價格；由真實世界轉換至風險中立世界，數學上如何進行。

## 方法

1. 無套利理論：Harrison & Pliska (1981) 與資產定價第一基本定理。
2. 定義 martingale，寫出或有求償權（任何到期 payoff 為 $H(T)$ 的商品）的定價公式。
3. 以 Girsanov 定理轉換測度：真實測度 $P$、風險中立測度 $Q$、以股票為計價單位的測度 $R$。
4. 以 martingale 定價公式搭配測度轉換推導 BS 公式。

## 主要發現

- 無套利與風險中立測度：Harrison & Pliska (1981) 指出，無套利條件下存在一個與真實測度 $P$ 對等的機率測度 $Q$，在 $Q$ 下資產的相對價格（除以貨幣帳戶 $\beta(t)=e^{\int_0^t r(u)du}$）為 martingale。資產定價第一基本定理：只要存在風險中立測度，市場即無套利機會。見 [[risk-neutral-valuation]]。
- Martingale：$X(t)=E^Q[X(T)\mid\mathcal F_t]$，即對未來的最佳預測等於現在的值；現值小於期望為 sub-martingale，大於期望則為 super-martingale。見 [[martingale]]。
- 定價公式：$\frac{H(t)}{\beta(t)}=E^Q\left[\frac{H(T)}{\beta(T)}\Big|\mathcal F_t\right]$，歐式買權即 $H(t)=E^Q[e^{-\int_t^T r\,du}\max(S_T-K,0)\mid\mathcal F_t]$。
- 測度轉換：由 Girsanov 定理，$dw^P=dw^Q-\frac{\mu-r}{\sigma}dt$，股價由 $\frac{dS}{S}=\mu\,dt+\sigma dw^P$ 轉為 $\frac{dS}{S}=r\,dt+\sigma dw^Q$。$\mu-r$ 為風險溢酬，$Q$ 測度下雖看不到風險溢酬，講義強調這不代表風險溢酬可被忽略，而是已反映於測度轉換之中。再令 $dw^Q=dw^R+\sigma dt$，得 $R$ 測度下 $\frac{dS}{S}=(r+\sigma^2)dt+\sigma dw^R$。見 [[measure-change-girsanov]]。
- BS 公式的機率解讀：$C=S\cdot\Pr^R(S_T>K)-Ke^{-r(T-t)}\Pr^Q(S_T>K)=SN(d_1)-Ke^{-r(T-t)}N(d_2)$。$N(d_2)$ 為風險中立世界中買權到期被執行的機率，$N(d_1)$ 則為以股票計價的測度 $R$ 下同一事件的機率。見 [[black-scholes-model]]。
- ingest 時的驗證：以 40 萬次蒙地卡羅模擬（$S=K=100$、$r=5\%$、$\sigma=20\%$、$T=1$），$Q$ 測度下的執行機率為 0.5600，$N(d_2)=0.5596$；$R$ 測度下為 0.6368，$N(d_1)=0.6368$；模擬的買權價格為 10.450，公式為 10.4506。

## 關聯概念

[[martingale]]、[[measure-change-girsanov]]、[[risk-neutral-valuation]]、[[black-scholes-model]]、[[brownian-motion]]

## 關聯文獻

[[fe-03-black-scholes-formula]]（Feynman-Kac 推導）、[[fe-06-bs-pde-derivation]]（PDE 推導）；Harrison & Pliska (1981)、Shreve (2004)（講義引用，未 ingest）
