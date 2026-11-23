# LLM Knowledge Base Architecture（LLM 維護知識庫的三層架構）

## 定義

讓 AI 持續整理與查詢知識的架構，分為三層：`raw` 為唯讀的原始資料，`wiki` 為 LLM 整理後的知識頁面（摘要、實體、概念、綜合頁），規則層則定義各項操作的標準流程。操作分為三種：Ingest（新增來源）、Query（查詢）、Lint（檢查孤立頁、斷連結、索引不同步與矛盾內容）。可再以腳本檢查（一致性檢查、pre-commit hook、CI）搭配語意判斷，避免 LLM 整理時逐漸偏離原本的結構。

---

## 在知識庫中的出現

- **[[harness-wiki-llm]]**：此架構的實作，包括三層分工、W1–W4 一致性檢查，以及本地與 CI 兩層 git hook。此 wiki 的 `raw/`、`sources/` 等頁面資料夾與 `CLAUDE.md` 規則，以及 Ingest、Query、Lint 三種操作，亦屬同一架構的應用。

---

## 關聯概念

[[multi-agent-review]]（同一專案中用於維持此架構品質的驗證機制）
