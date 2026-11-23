# FE-Wiki-Slide

以財務工程課程講義建立 LLM Wiki，並以 Wiki 為唯一知識來源，製作選擇權定價的入門教學簡報。簡報讀者設定為未修習財金、微積分與機率的初學者，說明選擇權如何定價，以及 Black-Scholes 公式的意義。

## 資料夾

- [`finance-wiki/`](finance-wiki/)：Wiki 本體。[`CLAUDE.md`](finance-wiki/CLAUDE.md) 為維護規則，[`index.md`](finance-wiki/index.md) 為總索引，[`log.md`](finance-wiki/log.md) 記錄每次 ingest 新增與修改的頁面。
- [`option-slides/`](option-slides/)：教學簡報與製作紀錄，各步驟的檢查方式與結果記錄於 [`run-log.md`](option-slides/run-log.md)。

## 收錄講義

| 講義 | 頁數 | Wiki 來源頁 |
|---|---|---|
| 01 選擇權介紹與二項樹模型 | 53 | [`fe-01-options-binomial-tree`](finance-wiki/sources/fe-01-options-binomial-tree.md) |
| 02 股價動態過程及 Itô 定理 | 39 | [`fe-02-stock-dynamics-ito`](finance-wiki/sources/fe-02-stock-dynamics-ito.md) |
| 03 BS 模型和 BS 選擇權定價公式 | 29 | [`fe-03-black-scholes-formula`](finance-wiki/sources/fe-03-black-scholes-formula.md) |
| 06 使用 BS 之 PDE 推導 BS 定價公式 | 22 | [`fe-06-bs-pde-derivation`](finance-wiki/sources/fe-06-bs-pde-derivation.md) |
| 07 Martingale 定價理論 | 25 | [`fe-07-martingale-pricing`](finance-wiki/sources/fe-07-martingale-pricing.md) |

講義中的公式與數值例皆以 Python 重新計算，共發現 3 處筆誤。例如講義 03 第 4 頁 Theta 公式第二項的正負號有誤，與同份講義第 28 頁的證明結果不符。各筆誤皆記錄於對應的來源頁。

原始講義 PDF 涉及著作權，故未放入 repo。

## 相關專案

[Finance-Wiki](https://github.com/shannon2561/Finance-Wiki)：以同一份 Wiki 製作的金融概念網站，每頁說明一個概念。
