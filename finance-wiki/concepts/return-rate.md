# Return Rate（報酬率與年化）

## 定義

- **報酬率**：投資在一段期間內賺或賠的比例，$\frac{S_T-S_0}{S_0}$，$S_0$ 為期初價格、$S_T$ 為期末價格。以比例而非金額衡量，不同價位的資產才能互相比較。
- **對數報酬率**：$\ln(S_T/S_0)$，變動不大時與一般報酬率接近，且多期可直接相加，連續時間的模型多採用此定義（見 [[logarithm-exponential]]）。
- **年化**：將不同長度期間的報酬率或利率換算為一年的數字，方便比較。例如 3 個月的利率為 $0.12\times0.25=0.03$，年化即為 12%。
- **期望報酬率**：報酬率的期望值，即平均而言每年可得的報酬率，模型中記為 $\mu$。
- **波動度**：報酬率的標準差，衡量報酬率上下跳動的幅度，模型中記為 $\sigma$（見 [[probability-expected-value]]）。

## 例子

一期二元樹中，股價由 20 元漲至 22 元，報酬率為 $\frac{22-20}{20}=10\%$；跌至 18 元則為 $-10\%$，即上漲倍數 $u=1.1$、下跌倍數 $d=0.9$（見 [[fe-01-options-binomial-tree]]）。

## 在知識庫中的出現

- [[geometric-brownian-motion]]、[[fe-02-stock-dynamics-ito]]：股價模型 $\frac{dS}{S}=\mu\,dt+\sigma\,dz$ 描述的是報酬率，$\mu$ 為年化期望報酬率、$\sigma$ 為年化波動度。
- [[risk-neutral-valuation]]：風險中立機率下，股票的期望報酬率等於無風險利率。
- [[sharpe-ratio]]：以超額報酬率除以報酬率的標準差。

## 關聯概念

[[logarithm-exponential]]、[[probability-expected-value]]、[[geometric-brownian-motion]]

## 來源說明

定義為財務基礎知識的整理；例子的數字依 [[fe-01-options-binomial-tree]] 的例題重算。
