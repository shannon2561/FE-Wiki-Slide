# NVIDIA DLI 課程：Building RAG Agents with LLMs

**類型**：course
**作者**：NVIDIA Deep Learning Institute（課程提供機構，非個人作者，未建立 people 頁）
**年份**：未確認（檔案內無明確課程修習日期紀錄）
**原始檔**：GenAI-ML/Nvidia Online Courses/Building RAG Agents with LLMs/（資料夾，內含 12 份主教材 notebook + `solutions/` 對照解答 + `llm_client/`、`frontend/` 輔助程式碼 + `imgs/`、`slides/` 圖片投影片）

---

## 核心問題

如何用 LangChain 等工具鏈，從零組裝一套完整的 RAG（Retrieval-Augmented Generation）Agent 系統：涵蓋微服務化的 LLM 服務、文件處理、embedding、向量資料庫、評估、到最終透過 LangServe 部署。

## 方法

課程以 12 份循序 notebook 展開（依編號順序）：
`00_jupyterlab` → `01_microservices`（微服務架構）→ `02_llms`（LLM 基礎）→ `03_langchain_intro`（LangChain 入門）→ `04_running_state`（對話狀態管理）→ `05_documents`（文件處理）→ `06_embeddings`（向量嵌入）→ `07_vectorstores`（向量資料庫）→ `08_evaluation`（RAG 評估方法，如 ragas）→ `09_langserve`（服務化部署）→ `64_guardrails`（護欄機制）→ `99_table_of_contents`（總目錄）。

每份主教材都有對應的 `solutions/` 解答 notebook，另附 `llm_client/`（含 Dockerfile，示範用容器化方式跑 LLM client-server）與 `frontend/`（Gradio 前端，`frontend_server.py`/`frontend_block.py`）等輔助程式碼，顯示課程設計含實際可跑的前後端整合範例，而不只是理論教學。

## 主要發現

本頁僅記錄課程教材的結構與涵蓋範圍，**未逐份 notebook 讀取內容細節**（依取樣策略，課程練習類資料夾以 README/結構層級理解為主，避免逐檔精讀 33 份 GenAI-ML notebook 中屬於這個子資料夾的 12+12 份文件）。是否已完整修習、是否有個人化的練習成果，**未確認**。

## 關聯概念
[[retrieval-augmented-generation]]

## 關聯文獻
[[rag-hongloumeng-retrieval]]（同樣主題為 RAG 的課程作業，可對照方法論差異：本課程用 LangChain 生態系整合式做法，作業則是手刻 BM25+embedding 融合）
