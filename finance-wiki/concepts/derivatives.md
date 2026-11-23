# Derivatives（衍生性金融商品）

## 定義

價值由一個或多個標的資產（股票、指數、匯率、利率等）決定的金融合約，主要類型為遠期契約、期貨、選擇權與互換。

---

## 主要類型

| 類型 | 特色 |
|------|------|
| 遠期契約 | 場外交易 (OTC)，雙方約定未來以特定價格交割 |
| 期貨 | 標準化的遠期契約，於交易所交易並每日結算 |
| 選擇權 | 持有人有權利、無義務在特定條件下買入或賣出標的 |
| 互換 | 雙方交換現金流，例如利率互換、匯率互換 |

---

## 選擇權定價框架

1. **無套利界限與平價關係**：Put-Call Parity，$C - P = S - Ke^{-rT}$。
2. **二項樹** (Binomial Tree)：風險中立機率 $q = \frac{e^{rT} - d}{u - d}$，多期時由到期日往回逐期折現。
3. **Black-Scholes-Merton 模型**：假設幾何布朗運動、連續交易、無套利，$C = S N(d_1) - Ke^{-rT}N(d_2)$；延伸為 Merton 模型（含股息）與 Black 模型（期貨選擇權）。
4. **Greeks（避險參數）**：Delta 衡量對標的價格的敏感度，為 Delta 避險的依據；另有 Gamma、Theta、Vega、Rho。

---

## 在知識庫中的出現

- **[[fe-01-options-binomial-tree]]**：四上財工講義 01，從選擇權定義與損益講到一期、二期二元樹定價。
- **[[fe-02-stock-dynamics-ito]]**、**[[fe-03-black-scholes-formula]]**、**[[fe-06-bs-pde-derivation]]**、**[[fe-07-martingale-pricing]]**：四上財工講義 02–07，依序為股價隨機過程、BS 公式、PDE 解法與 Martingale 定價。
- **[[derivatives-course-113-1]]**：三上衍生性金融商品課程，涵蓋基礎概念至 BSM 模型。

---

## 關聯概念

[[portfolio-optimization]]、[[derivatives-course-113-1|衍生性商品課程]]、[[black-scholes-model]]、[[structured-notes]]
