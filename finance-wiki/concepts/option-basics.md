# Option Basics（選擇權基本概念）

## 定義
選擇權是一種契約：買方先付一筆錢（權利金），換到「在約定日期、用約定價格（履約價 $K$）買或賣某個東西」的**權利，但沒有義務**。可以買的叫買權（call），可以賣的叫賣權（put）。歐式選擇權只能在到期日執行，美式選擇權在到期前任何一天都能執行。到期時，買進買權的損益是 $\max(S_T-K,0)$，買進賣權是 $\max(K-S_T,0)$，$S_T$ 是到期日的股價；賣方的損益正好相反。

## 在知識庫中的出現
- [[fe-01-options-binomial-tree]]：1.1–1.2 節用 Hull 的例子說明。買 100 股歐式買權，$K=100$、權利金每股 5 元：到期股價低於 100 就不執行，損失 500 元；到期股價 115 則執行，每股賺 15 元，扣掉權利金淨賺 1,000 元。
- [[derivatives-course-113-1]]：三上課程第三、四章的選擇權基本性質與交易策略。

## 關聯概念
[[derivatives]]、[[binomial-option-pricing]]、[[black-scholes-model]]

## 關聯文獻
Hull, *Options, Futures, and Other Derivatives*（講義例題出處，未 ingest）
