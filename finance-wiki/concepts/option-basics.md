# Option Basics（選擇權基本概念）

## 定義

選擇權為一種契約：買方支付權利金，取得於約定日期、以約定價格（履約價 $K$）買入或賣出標的資產的權利，但沒有義務。可買入者為買權 (call)，可賣出者為賣權 (put)。歐式選擇權僅能於到期日執行，美式選擇權則可於到期前任一日執行。以 $S_T$ 表示到期日股價，買進買權的到期損益為 $\max(S_T-K,0)$，買進賣權為 $\max(K-S_T,0)$，賣方的損益則與買方相反。

## 在知識庫中的出現

- [[fe-01-options-binomial-tree]]：1.1–1.2 節以 Hull 的例題說明。買進 100 股歐式買權，$K=100$，權利金每股 5 元：到期股價低於 100 時不執行，損失權利金 500 元；到期股價為 115 時執行，每股獲利 15 元，扣除權利金後淨利 1,000 元。
- [[derivatives-course-113-1]]：三上課程第三、四章，選擇權基本性質與交易策略。

## 關聯概念

[[derivatives]]、[[binomial-option-pricing]]、[[black-scholes-model]]

## 關聯文獻

Hull, *Options, Futures, and Other Derivatives*（講義例題出處，未 ingest）
