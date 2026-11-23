# Black-Scholes Model（Black-Scholes 模型與風險中立定價）

## 定義

歐式選擇權定價的封閉解模型：由幾何布朗運動（GBM）假設與無套利避險組合推導出 Black-Scholes PDE，解得 $C = S N(d_1) - Ke^{-rT}N(d_2)$。延伸模型含 Merton（連續股息 q）、Garman-Kohlhagen（外匯，q=無風險外幣利率）、Black 1976（期貨選擇權，q=r），三者可用同一個「持有收益率 q」的替換邏輯統一理解。

**風險中立定價（Risk-Neutral Pricing）** 是貫穿此模型的核心原理：在風險中立測度下以無風險利率折現期望 payoff。離散版本為二項樹的風險中立機率 $q = \frac{e^{rT}-d}{u-d}$（與 [[binomial-option-pricing]] 統一符號，$p$ 保留給真實機率）；連續版本由 Feynman-Kac 定理連接 PDE 求解與期望值計算——這個「離散二項樹 ↔ 連續 BS PDE」的對應關係，是理解 BS 模型推導（尤其是 PDE 中 $\mu$ 為何消失）的關鍵鋪墊。

---

## 在知識庫中的出現

- **[[fe-02-stock-dynamics-ito]]**：講義 02 提供推導 BS 所需的工具：布朗運動、幾何布朗運動股價模型、Itô 定理
- **[[fe-03-black-scholes-formula]]**：講義 03 列出六個假設，以 Itô 定理＋無風險組合推出 [[black-scholes-pde]]，再以 Feynman-Kac 解出買權、賣權公式與五個 [[option-greeks]]
- **[[fe-06-bs-pde-derivation]]**：講義 06 把 BS PDE 轉成熱傳導方程式直接求解（[[heat-equation-method]]），得到同一個公式
- **[[fe-07-martingale-pricing]]**：講義 07 用 [[martingale]] 定價與 [[measure-change-girsanov]] 推導，並給出機率解讀：$N(d_2)=\Pr^Q(S_T>K)$、$N(d_1)=\Pr^R(S_T>K)$
- **[[fe-01-options-binomial-tree]]**：四上財工講義 01 用二元樹建立風險中立定價的離散版本（見 [[binomial-option-pricing]]、[[risk-neutral-valuation]]），習題 4 指出期數 N→∞ 時會收斂到 BS 公式
- **[[derivatives-course-113-1]]**：課程第九章 BSM 模型、第六章二項式樹定價，是本概念在正式課堂脈絡下的理論來源

---

## 關聯概念

[[derivatives]]（BS 模型是衍生性商品定價框架中最核心的封閉解方法）
