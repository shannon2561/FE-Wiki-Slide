# Retrieval-Augmented Generation（RAG，檢索增強生成）

## 定義

LLM 生成答案前，先從外部語料檢索相關段落作為上下文，以減少幻覺，並補足訓練資料未涵蓋的知識。主要元件包括文件切分（chunking，須權衡 chunk size 與重疊步長 stride）、檢索器（BM25 詞頻式、向量嵌入語意式或兩者混合）、排序融合（如 Reciprocal Rank Fusion, RRF）與生成端的 prompt 組裝；進階系統另涉及向量資料庫、RAG 評估（如 ragas）與服務化部署（如 LangServe）。

---

## 在知識庫中的出現

- **[[rag-hongloumeng-retrieval]]**：自行實作 BM25（`rank_bm25` 搭配 `jieba` 中文斷詞）與向量檢索（`multilingual-e5-large`）兩路，以 RRF 融合排序，依序挑戰 Simple、Medium、Strong、Boss 四級 baseline。
- **[[nvidia-rag-agents-course]]**：NVIDIA DLI 課程教材，以 LangChain 整合文件處理、embedding、向量資料庫、RAG 評估 (ragas)、Guardrails 與服務化部署 (LangServe)，與 `rag-hongloumeng-retrieval` 的自行實作方式形成對照。

---

## 關聯概念

[[prompt-injection]]、[[multi-agent-review]]（同屬 LLM 系統工程的相關主題）
