# 財務工程與金融創新（一）講義 03：Black-Scholes 模型和 Black-Scholes 選擇權定價公式

**類型**：course  
**作者**：授課教師（講義未署名）  
**年份**：2026（115-1 四上財工；投影片頁尾日期為 2014/10/2，應為沿用舊版）  
**原始檔**：衍生性金融商品/四上財工/上課簡報/03 BS模型和BS選擇權定價公式.pdf  
**檔名**：03 BS模型和BS選擇權定價公式.pdf（29 頁）

---

## 核心問題

在股價服從幾何布朗運動的假設下，歐式買權的合理價格為何；價格對股價、波動度、利率與時間的敏感度（避險參數）又為何。

## 方法

1. 列出 BS 模型的六項假設。
2. 以 Itô 定理寫出選擇權價格的變動，建構「賣出 1 單位選擇權、買入 $\partial f/\partial S$ 股股票」的組合，使隨機項互相抵銷；無風險組合只能賺取無風險利率，由此得到 BS PDE。
3. 以 Feynman-Kac 定理將 PDE 的解寫成風險中立期望值 $C_t=e^{-r(T-t)}E^Q[C_T]$，拆成兩項積分求出封閉解。
4. 逐一證明五個避險參數 (Greeks)。

## 主要發現

- 六項假設：股價服從 $dS=\mu S\,dt+\sigma S\,dz$；交易連續且股票可無限分割；沒有交易成本與稅；可無限放空並使用放空所得資金；存在無風險利率；存續期間不發放股息。見 [[geometric-brownian-motion]]。
- BS PDE：$rf=\frac{\partial f}{\partial t}+rS\frac{\partial f}{\partial S}+\frac12\sigma^2S^2\frac{\partial^2 f}{\partial S^2}$。推導過程中真實期望報酬率 $\mu$ 消去，任何衍生性商品皆滿足此方程式，差別僅在到期條件。見 [[black-scholes-pde]]。
- 買權公式：$C=SN(d_1)-Ke^{-r(T-t)}N(d_2)$，其中 $d_1=\frac{\ln(S/K)+(r+\frac12\sigma^2)(T-t)}{\sigma\sqrt{T-t}}$，$d_2=d_1-\sigma\sqrt{T-t}$。賣權公式：$P=Ke^{-r(T-t)}N(-d_2)-SN(-d_1)$。見 [[black-scholes-model]]。
- 真實世界與風險中立世界：$P$ 測度下 $E^P[S_T]=S_te^{\mu(T-t)}$，$Q$ 測度下 $E^Q[S_T]=S_te^{r(T-t)}$，定價時使用 $Q$。見 [[risk-neutral-valuation]]。
- 公式兩項的意義（由證明過程得出）：$Ke^{-r(T-t)}N(d_2)$ 為 $Q$ 測度下到期被執行的機率 $N(d_2)$ 乘以履約價的現值；$SN(d_1)$ 則為到期執行時取得之股票的現值。
- 避險參數：Delta $=N(d_1)$、Gamma $=\frac{n(d_1)}{S\sigma\sqrt{T-t}}$、Vega $=S\sqrt{T-t}\,n(d_1)$、Rho $=K(T-t)e^{-r(T-t)}N(d_2)$、Theta $=-\frac{S\sigma n(d_1)}{2\sqrt{T-t}}-rKe^{-r(T-t)}N(d_2)$。見 [[option-greeks]]。
- 講義第 3 頁列出 BS 公式的四種推導方式：二項式模型 ($\Delta t\to0$)、Feynman-Kac 定理、推導 PDE、Martingale，分別對應 [[fe-01-options-binomial-tree]]、此講義、[[fe-06-bs-pde-derivation]] 與 [[fe-07-martingale-pricing]]。
- ingest 時的驗證：以 $S=K=100$、$r=5\%$、$\sigma=20\%$、$T=1$ 計算，$d_1=0.35$、$d_2=0.15$，買權 10.4506、賣權 5.5735，買賣權平價誤差為 0；五個 Greeks 公式皆與數值微分一致。
- 講義疑似筆誤：第 4 頁總表的 Theta 寫為 $-\frac{S\sigma}{2\sqrt{T-t}}n(d_1)+Kre^{-r(T-t)}N(d_2)$，第二項為正；第 28 頁的證明結果則為 $-\{\frac{S\sigma n(d_1)}{2\sqrt\tau}+Kre^{-r\tau}N(d_2)\}$，數值微分支持第 28 頁，故 Wiki 採用第 28 頁的版本。

## 關聯概念

[[black-scholes-model]]、[[black-scholes-pde]]、[[option-greeks]]、[[risk-neutral-valuation]]、[[itos-lemma]]、[[geometric-brownian-motion]]、[[delta-hedging-replication]]

## 關聯文獻

[[fe-02-stock-dynamics-ito]]（前一份講義，提供 Itô 定理）；[[derivatives-course-113-1]]（三上第九章 BSM、第十章 Greeks）
