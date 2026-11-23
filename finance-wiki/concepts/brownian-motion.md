# Brownian Motion（布朗運動／Wiener 過程）

## 定義

描述連續且無法預測之隨機變動的數學模型。標準布朗運動 $B(t)$ 由 0 開始，任一段時間的變動量與過去的變動獨立（獨立增量），且服從平均數為 0、變異數等於時間長度的常態分配，即 $B(t+\Delta t)-B(t)\sim N(0,\Delta t)$。布朗運動具有 Markov 性質，未來只與現在有關，與過去的路徑無關。其路徑連續但處處不可微分，在 $[0,t]$ 上的二次變異恰為 $t$，此即 Itô 定理中 $(dz)^2=dt$ 的來源。

## 在知識庫中的出現

- [[fe-02-stock-dynamics-ito]]：第 1–3 節由 Markov 過程與隨機漫步的實證證據，講至 Wiener 過程的定義與路徑性質，再加入漂移項成為廣義 Wiener 過程 $dX=a\,dt+b\,dz$。

## 關聯概念

[[geometric-brownian-motion]]、[[itos-lemma]]、[[black-scholes-model]]
