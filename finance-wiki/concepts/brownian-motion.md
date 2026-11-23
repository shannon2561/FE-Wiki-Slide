# Brownian Motion（布朗運動／Wiener 過程）

## 定義
描述「完全隨機、無法預測的連續變動」的數學模型。標準布朗運動 $B(t)$ 從 0 出發；任何一段時間的變動量都跟過去的變動無關（獨立增量），而且服從平均 0、變異數等於時間長度的常態分配：$B(t+\Delta t)-B(t)\sim N(0,\Delta t)$。它具有 Markov 性質（未來只跟現在有關，跟過去的路徑無關）。路徑是連續的，但到處都不平滑（不可微分），而且在 $[0,t]$ 上的二次變異恰好等於 $t$，這是 Itô 定理裡 $(dz)^2=dt$ 的來源。

## 在知識庫中的出現
- [[fe-02-stock-dynamics-ito]]：第 1–3 節，從 Markov 過程、隨機漫步的實證證據講到 Wiener 過程的定義與路徑性質，再加上漂移成為廣義 Wiener 過程 $dX=a\,dt+b\,dz$。

## 關聯概念
[[geometric-brownian-motion]]、[[itos-lemma]]、[[black-scholes-model]]
