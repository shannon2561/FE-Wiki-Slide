# Derivatives（衍生性金融商品）

## 定義

衍生性金融商品是其價值衍生自一個或多個標的資產（股票、指數、匯率、利率等）的金融合約。主要類型包括遠期契約、期貨、選擇權、互換。

---

## 主要類型

| 類型 | 特色 |
|------|------|
| **遠期契約** | 場外交易（OTC），雙方同意未來以特定價格交割 |
| **期貨** | 標準化遠期，在交易所交易，每日結算 |
| **選擇權** | 賦予持有人**權利**（非義務）在特定條件下買/賣標的 |
| **互換** | 交換現金流（利率互換、匯率互換等） |

---

## 選擇權定價框架（[[derivatives-course-113-1]] 核心）

### 1. 無套利界限與平價關係
- Put-Call Parity：$C - P = S - Ke^{-rT}$

### 2. Binomial Tree
- 風險中立機率：$p = \frac{e^{rT} - d}{u - d}$
- 多期倒推定價

### 3. Black-Scholes-Merton（BSM）模型
- 假設：幾何布朗運動、連續交易、無套利
- $C = S N(d_1) - Ke^{-rT}N(d_2)$
- 延伸：Merton 模型（含股息）、Black 模型（期貨選擇權）

### 4. Greeks（避險參數）
- Delta（Δ）：對標的價格的敏感度 → Delta 避險
- Gamma（Γ）、Theta（Θ）、Vega（ν）、Rho（ρ）

---

## 在知識庫中的出現

- **[[fe-02-stock-dynamics-ito]]**、**[[fe-03-black-scholes-formula]]**、**[[fe-06-bs-pde-derivation]]**、**[[fe-07-martingale-pricing]]**：四上財工講義 02–07，從股價隨機過程、BS 公式、PDE 解法到 Martingale 定價，完整串起選擇權定價理論
- **[[derivatives-course-113-1]]**：政大 113-1 課程，涵蓋從基礎到 BSM 的完整框架
- **[[fe-01-options-binomial-tree]]**：四上財工講義 01，從選擇權定義與損益講到一期、二期二元樹定價，是本主題的入門鋪墊

---

## 關聯概念

[[portfolio-optimization]]、[[derivatives-course-113-1|衍生性商品課程]]、[[black-scholes-model]]、[[structured-notes]]
