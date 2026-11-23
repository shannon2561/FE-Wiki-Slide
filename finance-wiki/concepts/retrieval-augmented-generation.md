# Retrieval-Augmented Generation（RAG／檢索增強生成）

## 定義

讓 LLM 在生成答案前先從外部語料檢索相關段落作為上下文，以緩解幻覺、補足模型訓練資料未涵蓋的知識。核心元件包含文件切分（chunking，含 chunk size 與重疊步長 stride 的權衡）、檢索器（BM25 詞頻式／向量嵌入語意式／混合）、排序融合（如 RRF, Reciprocal Rank Fusion）、生成端 prompt 組裝，進階系統另涉及向量資料庫、RAG 評估方法（如 ragas）與服務化部署（如 LangServe）。

---

## 在知識庫中的出現

- **[[rag-hongloumeng-retrieval]]**：手刻 BM25（`rank_bm25`+`jieba` 中文斷詞）與向量檢索（`multilingual-e5-large`）雙路，以 RRF 融合排序，逐級加碼四級 baseline（Simple → Medium → Strong → Boss）
- **[[nvidia-rag-agents-course]]**：NVIDIA DLI 課程教材，以 LangChain 生態系整合式做法涵蓋文件處理、embedding、向量資料庫、RAG 評估（ragas）、Guardrails 護欄機制到服務化部署（LangServe）的完整流程，與 `rag-hongloumeng-retrieval` 的手刻做法形成方法論對照

---

## 關聯概念

[[prompt-injection]]、[[multi-agent-review]]（同屬 LLM 系統工程脈絡的相關主題）
