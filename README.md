# FE-Wiki-Slide：用 LLM Wiki 做一份選擇權定價教學簡報

生成式 AI 課第 10 週作業。先維護一份 LLM Wiki，再讓 AI 只用 Wiki 當知識來源，產生給外行人看的教學 HTML 簡報。

## 內容

| 資料夾 | 是什麼 |
|---|---|
| [`finance-wiki/`](finance-wiki/) | LLM Wiki 本體。規則在 [`CLAUDE.md`](finance-wiki/CLAUDE.md)，總索引在 [`index.md`](finance-wiki/index.md)，每次 ingest 的紀錄在 [`log.md`](finance-wiki/log.md) |
| [`option-slides/`](option-slides/) | 教學簡報、需求確認紀錄、執行與檢查紀錄（[`run-log.md`](option-slides/run-log.md)） |

## 本週 ingest 的 5 份資料

財務工程課程講義（四上），每份建一頁 source：

| 講義 | 頁數 | Wiki 來源頁 |
|---|---|---|
| 01 選擇權介紹與二項樹模型 | 53 | [`fe-01-options-binomial-tree`](finance-wiki/sources/fe-01-options-binomial-tree.md) |
| 02 股價動態過程及 Itô 定理 | 39 | [`fe-02-stock-dynamics-ito`](finance-wiki/sources/fe-02-stock-dynamics-ito.md) |
| 03 BS 模型和 BS 選擇權定價公式 | 29 | [`fe-03-black-scholes-formula`](finance-wiki/sources/fe-03-black-scholes-formula.md) |
| 06 使用 BS 之 PDE 推導 BS 定價公式 | 22 | [`fe-06-bs-pde-derivation`](finance-wiki/sources/fe-06-bs-pde-derivation.md) |
| 07 Martingale 定價理論 | 25 | [`fe-07-martingale-pricing`](finance-wiki/sources/fe-07-martingale-pricing.md) |

原始講義 PDF 有著作權，不放進 repo（`finance-wiki/raw/` 已排除）。

## 與上週作業的關係

這份 Wiki 是上週 [Finance-Wiki](https://github.com/shannon2561/Finance-Wiki) 網站背後的私人 wiki，篩掉無關內容和個資後的公開版本，再加上本週 ingest 的選擇權主題。

## 進度

- [x] 先討論、後生成：需求確認
- [x] Ingest 5 份講義（含數字重算與 lint）
- [ ] 從 Wiki 排教學大綱（人工審核）
- [ ] 逐頁產生與檢查
- [ ] 組成 HTML 簡報、GitHub Pages
- [ ] loop / graph 說明與反思
