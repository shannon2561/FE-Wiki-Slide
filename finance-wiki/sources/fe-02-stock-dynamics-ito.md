# 財務工程與金融創新（一）講義 02：股價動態過程及 Itô 定理

**類型**：course  
**作者**：授課教師（講義未署名）  
**年份**：2026（115-1 四上財工）  
**原始檔**：衍生性金融商品/四上財工/上課簡報/02 股價動態過程及Itô定理.pdf  
**檔名**：02 股價動態過程及Itô定理.pdf（39 頁）

---

## 核心問題
股價在連續時間裡怎麼隨機變動？如果股價是隨機的，依附在股價上的衍生性商品價格又會怎麼變動？

## 方法
依序建立五個工具：Markov 過程 → Wiener 過程（布朗運動）→ 廣義 Wiener 過程（加漂移）→ Itô 過程（股價模型）→ Itô 定理（用泰勒展開推導），並推廣到兩個資產的 Itô 定理。

## 主要發現
- **Markov 性質**：明天股價的機率分配只跟今天的股價有關，跟更早的歷史無關。講義以實證文獻說明股價、利率、匯率的短期變動近似隨機漫步、無法預測，並以 2013 年諾貝爾經濟學獎（Fama、Hansen、Shiller）說明「短期無法預測、長期有一定可預測性」。見 [[brownian-motion]]。
- **Wiener 過程（布朗運動）**：$B(0)=0$；增量獨立且平穩；一小段時間 $\Delta t$ 的增量 $\Delta z=\varepsilon\sqrt{\Delta t}$、$\varepsilon\sim N(0,1)$，所以平均 0、變異數 $\Delta t$。路徑連續但處處不可微，在 $[0,t]$ 的二次變異等於 $t$。見 [[brownian-motion]]。
- **廣義 Wiener 過程**：$dX=a\,dt+b\,dz$，期望變動 $a\,dt$、變異數 $b^2dt$；積分得 $X_t=X_0+at+bz_t$。
- **股價模型（Itô 過程的特例）**：$dS=\mu S\,dt+\sigma S\,dz$，等價於報酬率 $\frac{dS}{S}\sim N(\mu\,dt,\sigma^2dt)$；$\mu$ 是年化期望報酬率，$\sigma$ 是年化波動度。忽略隨機項時 $S_t=S_0e^{\mu t}$。見 [[geometric-brownian-motion]]。
- **Itô 定理**：若 $dX=a\,dt+b\,dz$、$f=f(X,t)$，則 $df=\left(\frac{\partial f}{\partial t}+a\frac{\partial f}{\partial X}+\frac12b^2\frac{\partial^2f}{\partial X^2}\right)dt+b\frac{\partial f}{\partial X}dz$。和一般微積分的差別是多出 $\frac12b^2\frac{\partial^2 f}{\partial X^2}$ 這一項，原因是 $(dz)^2=dt$ 不能忽略。見 [[itos-lemma]]。
- **兩資產版本**：兩個布朗運動相關係數 $\rho$ 時，多出交叉項 $b_1b_2\rho\frac{\partial^2f}{\partial X_1\partial X_2}dt$（習題 6：以新台幣計價的 IBM 股價 $S_tX_t$）。
- 結論：股價的隨機變動要靠 Itô 定理才能推到衍生性商品價格的變動，這是推導 [[black-scholes-model|Black-Scholes]] 方程式的前置工具。

## 關聯概念
[[brownian-motion]]、[[geometric-brownian-motion]]、[[itos-lemma]]、[[black-scholes-model]]、[[factor-models]]

## 關聯文獻
[[fe-01-options-binomial-tree]]（前一份講義）；Ross (2000) *Introduction to Probability Models*、Shreve (2004) *Stochastic Calculus for Finance II*（講義引用，未 ingest）
