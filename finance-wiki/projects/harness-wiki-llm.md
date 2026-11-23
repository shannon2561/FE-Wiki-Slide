# Harness-Wiki-LLM：LLM 維護知識庫模板

**類型**：project  
**期間**：2026-05（114-2 學期，仍在迭代）  
**情境**：self-study  
**原始檔**：AIC/1142/Harness/Harness-Wiki-LLM（模板開發版本）、AIC/1142/社團事務/Harness-Wiki-LLM（套用於社團事務資料的實例）  
**技術棧**：Markdown、Bash、Git hooks (pre-commit)、GitHub Actions、Claude Code skills（`.claude/skills/ingest`、`lint`、`query`）、Codex（跨模型驗證代理）

---

## 目標

建立 LLM 維護知識庫的通用模板，結合兩套設計：Andrej Karpathy 的 LLM Wiki 架構（raw、wiki、規則三層分離，以及 Ingest、Query、Lint 三種操作），以及 Harness Engineering（repo 即真實來源、提供地圖而非手冊、機械化檢查、漸進式揭露）。目的是讓「放入原始資料，由 AI 整理成可交叉引用的頁面」可重複套用於不同主題，例如知識管理、社團事務、產業研究，不必每次重新設計架構。

專案另含一套 multi-agent-dev 工作流：由 Claude 規劃、Codex 驗證，分為 plan-advisor 與 impl-validator 兩階段，並以 ADR (Architecture Decision Record) 記錄每項設計決策的取捨。

## 方法與架構

**三層分工**

- `raw/`：原始資料層，只進不出，LLM 僅能讀取。
- `wiki/`（`summaries/`、`entities/`、`concepts/`、`syntheses/`、`index.md`、`log.md`）：LLM 整理並持續累積的知識層。
- `.agent/workflows/`（`ingest.md`、`query.md`、`lint.md`）與 `.agent/docs/`：規則層，定義三種操作的流程與各子目錄的寫作規範。

**機械化檢查**（`scripts/check-consistency.sh`）

- W1：`index.md` 與實際頁面一致，沒有孤立頁或不存在的索引項目。
- W2：`log.md` 的條目格式可被 `grep "^## \["` 解析。
- W3：wiki 內部相對連結沒有斷連結。
- W4：每份 `raw/` 來源至少有一篇對應的 `summaries/`。

檢查同時掛在 `.githooks/pre-commit`（本地）與 `.github/workflows/consistency.yml`（CI），避免 LLM 整理時逐漸偏離原本的結構。

**兩個實例**

1. `Harness/Harness-Wiki-LLM`：模板本體的開發版本，以個人資料匯出檔示範 ingest 流程；該資料涉及隱私，此處不展開。
2. `社團事務/Harness-Wiki-LLM`：將同一套模板套用於社團事務資料，驗證實際場景的可用性，並擴充 `multi-agent-dev/` 子系統。

**multi-agent-dev 的設計決策（ADR）**

- ADR-0001：採用 ADR 記錄架構決策。
- ADR-0002：驗證代理選用 Codex，而非同一模型家族。同一模型規劃又驗證時，規劃階段的盲點在驗證時往往仍看不出來 (self-review bias)；由不同公司、不同訓練資料的模型驗證，才能得到較獨立的第二意見。
- ADR-0003：驗證拆為 Plan-Advisor（諮詢模式，可反駁並多輪取得共識）與 Impl-Validator（守門模式，只判定 PASS 或 FAIL）。兩階段的互動節奏與結束條件不同，共用同一 session 或 prompt 會造成角色混淆。
- ADR-0004：三條寫作原則。
- ADR-0005：`run-log.md` 採時間軸格式。
- ADR-0006：兩個驗證階段的重試上限皆設為 3 輪，權衡過早放棄與拖慢進度。
- ADR-0007：v0.2 修訂，審查標準加入 Karpathy 基線錨定，避免審查標準不一致；協商上限依建議性質分級，結構性為 3 輪、風格性為 2 輪；並精簡 prompt。

## 結果

- 已可運作：`raw/` 至 `wiki/` 的三種操作、一致性檢查腳本、本地與 CI 兩層 git hook。
- 已有兩個實例分別驗證一般知識庫與社團事務資料。
- multi-agent-dev 已修訂至 ADR-0007，設計調整來自先前專案 OpenStock 的實際問題，並非一次性草稿。
- 檔案中沒有量化的使用效果數字，例如整理速度提升幾成，未確認。

## 學到什麼

- 同源誤差是 AI 輔助工作流的主要風險：規劃者與驗證者若為同一模型，驗證容易流於形式，故 ADR-0002 將跨模型驗證列為必要設計。
- 同一個驗證角色在不同階段可能需要不同的互動方式（協商或守門），放在同一套 prompt 中會互相衝突。
- 腳本與語意檢查並行：孤立頁、斷連結等可用腳本檢查的項目交給腳本，矛盾與過期內容等需要判斷的項目才留給語意層，此 wiki 的 Lint 操作即參考此設計。
- ADR 將每項決策以脈絡、決策、後果三段記錄，較適合團隊協作。

## 關聯概念

[[llm-knowledge-base-architecture]]、[[multi-agent-review]]

## 關聯頁面

無。
