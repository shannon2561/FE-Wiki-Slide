# FE-Wiki-Slide

我把財務工程課的五份講義 ingest 進一份由 LLM 維護的 Wiki，再只拿 Wiki 的內容做簡報。簡報寫給沒學過財金、微積分和機率的人看，講選擇權怎麼定價、Black-Scholes 公式到底在算什麼。

## 資料夾

[`finance-wiki/`](finance-wiki/) 是 Wiki 本體。維護規則寫在 [`CLAUDE.md`](finance-wiki/CLAUDE.md)，[`index.md`](finance-wiki/index.md) 是總索引，[`log.md`](finance-wiki/log.md) 記每次 ingest 加了哪些頁面。

[`option-slides/`](option-slides/) 放簡報和製作紀錄。每一步怎麼檢查、抓到什麼問題，都寫在 [`run-log.md`](option-slides/run-log.md)。

## 收錄的講義

| 講義 | 頁數 | Wiki 來源頁 |
|---|---|---|
| 01 選擇權介紹與二項樹模型 | 53 | [`fe-01-options-binomial-tree`](finance-wiki/sources/fe-01-options-binomial-tree.md) |
| 02 股價動態過程及 Itô 定理 | 39 | [`fe-02-stock-dynamics-ito`](finance-wiki/sources/fe-02-stock-dynamics-ito.md) |
| 03 BS 模型和 BS 選擇權定價公式 | 29 | [`fe-03-black-scholes-formula`](finance-wiki/sources/fe-03-black-scholes-formula.md) |
| 06 使用 BS 之 PDE 推導 BS 定價公式 | 22 | [`fe-06-bs-pde-derivation`](finance-wiki/sources/fe-06-bs-pde-derivation.md) |
| 07 Martingale 定價理論 | 25 | [`fe-07-martingale-pricing`](finance-wiki/sources/fe-07-martingale-pricing.md) |

講義裡的公式和數值例，我都用 Python 重算了一遍，找到 3 處筆誤。像講義 03 第 4 頁的 Theta 公式，第二項的正負號寫反了，跟同一份講義第 28 頁的證明對不起來。每一處都記在對應的來源頁。

原始講義 PDF 有著作權，所以沒有放進 repo。

## 相關專案

[Finance-Wiki](https://github.com/shannon2561/Finance-Wiki)：用同一份 Wiki 做的金融概念網站，一頁講一個概念。
