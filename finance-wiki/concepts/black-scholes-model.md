# Black-Scholes Model（Black-Scholes 模型與風險中立定價）

## 定義

歐式選擇權的封閉解定價模型。假設股價服從幾何布朗運動 (GBM)，透過無套利的避險組合推導出 Black-Scholes PDE，解得 $C = S N(d_1) - Ke^{-rT}N(d_2)$。延伸模型包括 Merton（連續股息 q）、Garman-Kohlhagen（外匯，q 為外幣無風險利率）與 Black 1976（期貨選擇權，q = r），三者皆可視為把持有收益率 q 代入同一個公式。

模型背後的原理為風險中立定價 (Risk-Neutral Pricing)：在風險中立測度下計算 payoff 的期望值，再以無風險利率折現。離散版本即二項樹的風險中立機率 $q = \frac{e^{rT}-d}{u-d}$（與 [[binomial-option-pricing]] 統一符號，$p$ 保留給真實機率）；連續版本則由 Feynman-Kac 定理連接 PDE 的解與期望值。理解兩者的對應，即可說明 PDE 中的真實報酬率 $\mu$ 為何會消失。

---

## 在知識庫中的出現

- **[[fe-01-options-binomial-tree]]**：講義 01 以二元樹建立風險中立定價的離散版本（見 [[binomial-option-pricing]]、[[risk-neutral-valuation]]），習題 4 指出期數 N→∞ 時會收斂至 BS 公式。
- **[[fe-02-stock-dynamics-ito]]**：講義 02 提供推導 BS 所需的工具，包括布朗運動、幾何布朗運動股價模型與 Itô 定理。
- **[[fe-03-black-scholes-formula]]**：講義 03 列出六個假設，以 Itô 定理與無風險組合推出 [[black-scholes-pde]]，再以 Feynman-Kac 定理解出買權、賣權公式與五個 [[option-greeks]]。
- **[[fe-06-bs-pde-derivation]]**：講義 06 將 BS PDE 轉換為熱傳導方程式後直接求解（[[heat-equation-method]]），得到相同公式。
- **[[fe-07-martingale-pricing]]**：講義 07 以 [[martingale]] 定價與 [[measure-change-girsanov]] 推導，並給出機率解讀：$N(d_2)=\Pr^Q(S_T>K)$、$N(d_1)=\Pr^R(S_T>K)$。
- **[[derivatives-course-113-1]]**：三上課程第九章 BSM 模型與第六章二項式樹定價。

---

## 關聯概念

[[derivatives]]（BS 模型為衍生性商品定價中最常用的封閉解方法）、[[no-arbitrage]]、[[normal-distribution]]、[[discounting-continuous-compounding]]
