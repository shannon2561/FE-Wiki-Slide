# NVIDIA DLI 課程：Building RAG Agents with LLMs

**類型**：course  
**作者**：NVIDIA Deep Learning Institute（課程提供機構，未建立 people 頁）  
**年份**：未確認（檔案內無修習日期紀錄）  
**原始檔**：GenAI-ML/Nvidia Online Courses/Building RAG Agents with LLMs/（12 份主教材 notebook、`solutions/` 解答、`llm_client/` 與 `frontend/` 輔助程式碼、`imgs/` 與 `slides/` 圖片投影片）

---

## 核心問題

如何以 LangChain 等工具，從頭組裝一套 RAG (Retrieval-Augmented Generation) Agent 系統，範圍包括微服務化的 LLM 服務、文件處理、embedding、向量資料庫、評估，以及以 LangServe 部署。

## 方法

課程依序由 12 份 notebook 組成：`00_jupyterlab`、`01_microservices`（微服務架構）、`02_llms`（LLM 基礎）、`03_langchain_intro`（LangChain 入門）、`04_running_state`（對話狀態管理）、`05_documents`（文件處理）、`06_embeddings`（向量嵌入）、`07_vectorstores`（向量資料庫）、`08_evaluation`（RAG 評估，如 ragas）、`09_langserve`（服務化部署）、`64_guardrails`（護欄機制）、`99_table_of_contents`（總目錄）。

每份主教材皆有對應的 `solutions/` 解答；另附 `llm_client/`（含 Dockerfile，以容器執行 LLM client-server）與 `frontend/`（Gradio 前端，`frontend_server.py`、`frontend_block.py`），可見課程包含可實際執行的前後端整合範例。

## 主要發現

此頁僅記錄教材結構與涵蓋範圍，未逐份讀取 notebook 內容；是否已完整修習、是否有個人練習成果，亦未確認。

## 關聯概念

[[retrieval-augmented-generation]]

## 關聯文獻

[[rag-hongloumeng-retrieval]]：同為 RAG 主題的課程作業。此課程以 LangChain 整合各元件，該作業則自行實作 BM25 與 embedding 檢索並融合排序。
