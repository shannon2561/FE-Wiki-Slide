# Geometric Brownian Motion（幾何布朗運動）

## 定義

Black-Scholes 模型對股價的假設：$dS=\mu S\,dt+\sigma S\,dz$。股價每一小段時間的報酬率 $dS/S$ 由兩部分組成，一為固定的期望成長 $\mu\,dt$，二為與波動度 $\sigma$ 成正比的隨機衝擊 $\sigma\,dz$，其中 $dz$ 為布朗運動的增量。由於隨機變動的是報酬率，股價不會變成負數；若沒有隨機項，股價即為連續複利成長 $S_t=S_0e^{\mu t}$。

## 在知識庫中的出現

- [[fe-02-stock-dynamics-ito]]：第 4 節將股價寫成 Itô 過程的特例，$\frac{dS}{S}\sim N(\mu\,dt,\sigma^2dt)$，並說明考慮隨機項後須以 Itô 定理推導 BS 方程式；習題 4 要求推導 $\ln S$ 的變動過程。
- [[black-scholes-model]]：BS 模型以 GBM 作為股價假設。

## 關聯概念

[[brownian-motion]]、[[itos-lemma]]、[[black-scholes-model]]
