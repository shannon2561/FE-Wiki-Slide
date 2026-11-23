# LLM Knowledge Base Architecture（LLM 維護知識庫的三層架構）

## 定義

一種讓 AI 可持續整理與調用個人知識的架構模式：`raw`（唯讀原始資料層）／`wiki`（LLM 整理的知識層，含摘要、實體、概念、綜合頁）／規則層（workflows、docs，定義三大操作的標準流程）三層分離，搭配 **Ingest**（新增來源）／**Query**（查詢）／**Lint**（健康檢查：孤兒頁、斷連結、索引不同步、矛盾主張）三大標準操作，並可用機械化腳本（如一致性檢查、pre-commit hook、CI）搭配語意層判斷雙軌把關，避免 LLM 整理過程產生結構性漂移。

---

## 在知識庫中的出現

- **[[harness-wiki-llm]]**：本頁描述的專案本身就是這個架構的一個實例（三層分工 + W1–W4 機械化一致性檢查 + 本地/CI 雙重 git hook）；此外，本 wiki（`學校\wiki\`）自身的 `raw/`／`sources/concepts/people/projects/`／`CLAUDE.md` 三層設計與 Ingest/Query/Lint 三操作，與此概念高度同源——即讀者現在閱讀的這份知識庫，正是同一架構哲學的另一個應用實例

---

## 關聯概念

[[multi-agent-review]]（同一專案內用於守護此架構品質的驗證機制）
