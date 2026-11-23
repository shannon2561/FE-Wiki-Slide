# 財務工程與金融創新（一）講義 07：Martingale 定價理論

**類型**：course  
**作者**：授課教師（講義未署名）  
**年份**：2026（115-1 四上財工；投影片頁尾日期為 2024/9/27）  
**原始檔**：衍生性金融商品/四上財工/上課簡報/07 Martingale定價理論.pdf  
**檔名**：07 Martingale定價理論.pdf（25 頁）

---

## 核心問題
為什麼「在風險中立世界取期望值再折現」就是正確的價格？從真實世界換到風險中立世界，數學上是怎麼換的？

## 方法
1. 無套利理論：Harrison & Pliska (1981) 與資產定價第一基本定理。
2. 定義 martingale，寫出或有求償權（任何到期 payoff 為 $H(T)$ 的商品）的定價公式。
3. 用 Girsanov 定理做測度轉換：真實測度 $P$ → 風險中立測度 $Q$ → 以股票為計價單位的測度 $R$。
4. 用 martingale 定價公式加上測度轉換推出 BS 公式。

## 主要發現
- **無套利 ⇔ 存在風險中立測度**：Harrison & Pliska (1981) 指出，在無套利條件下存在一個與真實測度 $P$ 對等的機率測度 $Q$，在 $Q$ 下資產的「相對價格」（除以貨幣帳戶 $\beta(t)=e^{\int_0^t r(u)du}$）是 martingale。資產定價第一基本定理：只要有風險中立測度，市場就沒有套利機會。見 [[risk-neutral-valuation]]。
- **Martingale**：$X(t)=E^Q[X(T)\mid\mathcal F_t]$，意思是「對未來的最佳預測就是現在的值」，像一場公平的賭局。若現值小於期望則是 sub-martingale，大於則是 super-martingale。見 [[martingale]]。
- **定價公式**：$\frac{H(t)}{\beta(t)}=E^Q\left[\frac{H(T)}{\beta(T)}\Big|\mathcal F_t\right]$，歐式買權即 $H(t)=E^Q[e^{-\int_t^T r\,du}\max(S_T-K,0)\mid\mathcal F_t]$。
- **測度轉換**：由 Girsanov 定理，$dw^P=dw^Q-\frac{\mu-r}{\sigma}dt$，股價從 $\frac{dS}{S}=\mu\,dt+\sigma dw^P$ 變成 $\frac{dS}{S}=r\,dt+\sigma dw^Q$。$\mu-r$ 是風險溢酬；在 $Q$ 下看不到風險溢酬，但講義強調這「不代表風險溢酬應被忽略」，而是它已經反映在測度的轉換裡。再令 $dw^Q=dw^R+\sigma dt$，得到 $R$ 測度下 $\frac{dS}{S}=(r+\sigma^2)dt+\sigma dw^R$。見 [[measure-change-girsanov]]。
- **BS 公式的機率解讀**：$C=S\cdot\Pr^R(S_T>K)-Ke^{-r(T-t)}\Pr^Q(S_T>K)=SN(d_1)-Ke^{-r(T-t)}N(d_2)$。也就是 $N(d_2)$ 是風險中立世界裡買權到期會被執行的機率，$N(d_1)$ 是換成以股票計價的測度 $R$ 後同一件事的機率。見 [[black-scholes-model]]。
- **ingest 時的驗證**：40 萬次蒙地卡羅模擬（$S=K=100$、$r=5\%$、$\sigma=20\%$、$T=1$）：$Q$ 下執行機率 0.5600 vs $N(d_2)=0.5596$；$R$ 下 0.6368 vs $N(d_1)=0.6368$；模擬買權價格 10.450 vs 公式 10.4506。

## 關聯概念
[[martingale]]、[[measure-change-girsanov]]、[[risk-neutral-valuation]]、[[black-scholes-model]]、[[brownian-motion]]

## 關聯文獻
[[fe-03-black-scholes-formula]]（Feynman-Kac 推導）、[[fe-06-bs-pde-derivation]]（PDE 推導）；Harrison & Pliska (1981)、Shreve (2004)（講義引用，未 ingest）
