# Harness-Wiki-LLM：LLM 維護個人知識庫模板

**類型**：project
**期間**：2026-05 ~ 2026-05（114-2 學期，仍在迭代）
**情境**：self-study
**原始檔**：AIC/1142/Harness/Harness-Wiki-LLM（模板/開發版本）、AIC/1142/社團事務/Harness-Wiki-LLM（套用於社團事務資料的實例）
**技術棧**：Markdown、Bash、Git hooks（pre-commit）、GitHub Actions、Claude Code skills（`.claude/skills/ingest`、`lint`、`query`）、Codex（作為跨模型驗證代理）

---

## 目標

打造一個「LLM 維護的個人知識庫」通用模板，融合兩套設計哲學：Andrej Karpathy 的 LLM Wiki 架構（raw / wiki / 規則三層分離 + Ingest / Query / Lint 三大操作）與 Harness Engineering（repo 即真實來源、地圖而非手冊、機械化檢查、漸進式披露）。目的是讓「丟原始資料進去、AI 整理成可交叉引用的知識庫頁面」這件事可重複套用到不同主題（個人知識管理、社團事務、產業研究等），而不必每次重新設計架構。

專案內還內建了一套獨立的 **multi-agent-dev 工作流**：用 Claude 規劃、Codex 作對抗式驗證（plan-advisor / impl-validator 兩階段），透過 ADR（Architecture Decision Record）機制正式記錄每個工作流設計決策的取捨過程。

## 方法與架構

**三層職責分工**（核心心智模型）：
- `raw/`：使用者擁有、只進不出、LLM 唯讀的原始資料層
- `wiki/`（`summaries/`、`entities/`、`concepts/`、`syntheses/`、`index.md`、`log.md`）：LLM 整理、持久化累積的知識層
- `.agent/workflows/`（`ingest.md`、`query.md`、`lint.md`）+ `.agent/docs/`：規則層，定義三大操作的標準流程與各子目錄寫作規範

**機械化守門**（`scripts/check-consistency.sh`，W1–W4）：
- W1 `index.md` 與實際頁面一致（無孤兒頁、無幽靈索引）
- W2 `log.md` 條目格式可被 `grep "^## \["` 解析
- W3 wiki 內部相對連結無斷link
- W4 每份 `raw/` 來源至少有一篇對應 `summaries/`

透過 `.githooks/pre-commit`（本地）與 `.github/workflows/consistency.yml`（CI）雙重把關，避免 LLM 整理過程產生的結構性漂移。

**兩個實例**：
1. `Harness/Harness-Wiki-LLM`：模板本體的開發版本，用真實的 Instagram 個人資料匯出檔（`raw/instagram-2026-05-17-.../`）作為 ingest 流程的示範資料（僅作結構示範，內容涉及個人隱私，本頁不展開）。
2. `社團事務/Harness-Wiki-LLM`：把同一套模板套用在社團事務（`社團/補助&社費.md`）的實際案例，驗證模板在真實場景下的可用性；此份額外擴充了 `multi-agent-dev/` 子系統。

**multi-agent-dev 子系統**（透過 ADR 記錄的關鍵設計決策）：
- ADR-0001：採用 ADR 機制記錄架構決策
- ADR-0002：驗證代理選用 Codex 而非同一模型家族——核心理由是避免「同源誤差（self-review bias）」：同一模型規劃又驗證，規劃時的盲點驗證時仍看不到；只有跨公司、跨訓練資料、跨對齊取向的模型才能提供真正獨立的第二意見
- ADR-0003：驗證代理拆成 **Plan-Advisor**（諮詢協商模式，可反駁、多輪共識）與 **Impl-Validator**（PASS/FAIL 對抗式守門模式），因為兩階段的互動節奏與終局規則本質不同，共用同一 session/prompt 會造成角色錯亂與 session 污染
- ADR-0004：三條經驗寫作原則
- ADR-0005：`run-log.md` 採時間軸格式
- ADR-0006：兩個驗證階段 max retry 統一設為 3 輪，權衡「太少提早放棄」與「太多拖慢節奏、使用者疲於裁決」
- ADR-0007：v0.2 修訂——引入 Karpathy 基線錨定審查標準（避免審查者自由心證、標準不一致）、協商上限依建議性質分級為 2/3 輪（結構性 vs 風格性）、精簡 prompt 注入

## 結果

- 模板已可運行的部分：`raw/` → `wiki/` 的三大操作（ingest/query/lint）、機械化一致性檢查腳本、本地與 CI 雙重 git hook
- 已有兩個實例分別驗證：一般知識庫（Instagram 示範資料）與社團事務資料
- multi-agent-dev 子系統已走到 ADR-0007（第二輪修訂），顯示這是一個持續迭代、有真實使用回饋（來自另一個先前專案「OpenStock」的痛點）在驅動設計調整的工作流，而非一次性草稿
- 未在檔案中找到量化的「使用效果」數字（例如整理速度提升幾成），此為**未確認**事項

## 學到什麼

- **同源誤差（self-review bias）是 AI 輔助工作流的核心風險**：規劃者與驗證者若共享同一模型/訓練分佈，驗證形同橡皮圖章；ADR-0002 明確把「跨模型」當成解法而非可有可無的優化
- **同一個「驗證」角色在不同階段可能需要完全不同的互動模式**（協商 vs 守門），硬塞進同一套 prompt 會造成邏輯打架——這與本 wiki 系統遵循的「主對話不下場、驗證不自驗、且驗證者用 fresh-context」的調度守則（`model-dispatch.md`）是同一個設計原則的不同實作
- **機械化檢查 + 語意檢查雙軌並行**：能用腳本驗的（孤兒頁、斷連結）不靠人腦，需要判斷的（矛盾、過期主張）才留給語意層——這正是本 wiki 系統 Lint 操作設計的直接參考來源
- **ADR 機制本身就是「隨做隨記」的正式化版本**：每個決策附脈絡、決策、後果三段式紀錄，與本 wiki 系統的 `implementation-notes.md` 精神一致，但更適合團隊協作場景

## 關聯概念
[[llm-knowledge-base-architecture]]、[[multi-agent-review]]

## 關聯頁面
（無）
