# FE-Wiki-Slide

選擇權定價的 LLM Wiki，以及從它產生的入門教學簡報。

我把財務工程課的講義 ingest 進一份由 LLM 維護的 Wiki，再只用 Wiki 當知識來源，做一份給沒學過財金、微積分和機率的人看的簡報：選擇權為什麼能被定價、Black-Scholes 公式在算什麼。

## 內容

| 資料夾 | 是什麼 |
|---|---|
| [`finance-wiki/`](finance-wiki/) | Wiki 本體。維護規則在 [`CLAUDE.md`](finance-wiki/CLAUDE.md)，總索引在 [`index.md`](finance-wiki/index.md)，每次 ingest 的紀錄在 [`log.md`](finance-wiki/log.md) |
| [`option-slides/`](option-slides/) | 簡報與製作紀錄：需求確認、每個步驟的檢查結果（[`run-log.md`](option-slides/run-log.md)） |

## 收錄的講義

| 講義 | 頁數 | Wiki 來源頁 |
|---|---|---|
| 01 選擇權介紹與二項樹模型 | 53 | [`fe-01-options-binomial-tree`](finance-wiki/sources/fe-01-options-binomial-tree.md) |
| 02 股價動態過程及 Itô 定理 | 39 | [`fe-02-stock-dynamics-ito`](finance-wiki/sources/fe-02-stock-dynamics-ito.md) |
| 03 BS 模型和 BS 選擇權定價公式 | 29 | [`fe-03-black-scholes-formula`](finance-wiki/sources/fe-03-black-scholes-formula.md) |
| 06 使用 BS 之 PDE 推導 BS 定價公式 | 22 | [`fe-06-bs-pde-derivation`](finance-wiki/sources/fe-06-bs-pde-derivation.md) |
| 07 Martingale 定價理論 | 25 | [`fe-07-martingale-pricing`](finance-wiki/sources/fe-07-martingale-pricing.md) |

講義裡的公式和數值例都用 Python 重算過，發現的筆誤記在各來源頁。原始講義 PDF 有著作權，不放進 repo。

## 相關專案

[Finance-Wiki](https://github.com/shannon2561/Finance-Wiki)：同一份 Wiki 的概念網站版本。
