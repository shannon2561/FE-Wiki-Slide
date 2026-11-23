# Discounting & Continuous Compounding（折現與連續複利）

## 定義

- **折現**：將未來的一筆錢換算成今天的價值。今天的 1 元存入銀行會生利息，故未來的 1 元價值低於今天的 1 元；利率越高、時間越長，未來的錢折算回今天就越少。
- **連續複利**：利息計算的頻率無限加快的極限情形。年利率 $r$、期間 $T$ 年時，1 元到期成長為 $e^{rT}$；反過來，未來的 1 元現值為 $e^{-rT}$。$e\approx2.718$ 為自然常數。
- 選擇權定價中的 $e^{-rT}$、$Ke^{-r(T-t)}$ 皆為折現：將到期的金額換算為現在的價值。

## 例子

[[fe-01-options-binomial-tree]] 的一期例題中，無風險組合 3 個月後值 4.5 元，年利率 12%，現值為 $4.5\times e^{-0.12\times0.25}=4.367$ 元。若改為每季計息一次，3 個月後的成長倍數為 1.03；連續複利則為 $e^{0.03}=1.0305$，兩者相差不大。

## 在知識庫中的出現

- [[fe-01-options-binomial-tree]]、[[binomial-option-pricing]]：$f=e^{-rT}[q f_u+(1-q)f_d]$，期望值乘以 $e^{-rT}$ 折現。
- [[black-scholes-model]]：$Ke^{-rT}N(d_2)$ 為履約價的現值乘以機率。
- [[martingale]]、[[fe-07-martingale-pricing]]：貨幣帳戶 $\beta(t)=e^{\int_0^t r(u)du}$，資產價格除以 $\beta(t)$ 即為折現後的價格。

## 關聯概念

[[probability-expected-value]]、[[no-arbitrage]]、[[risk-neutral-valuation]]

## 來源說明

定義為財務基礎知識的整理；例子的數字依 [[fe-01-options-binomial-tree]] 的例題重新計算。
