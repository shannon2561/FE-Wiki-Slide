# 紅樓夢 RAG 檢索系統（GenAI/ML 課程 HW2）

**類型**：project  
**期間**：2025-11（114-1 學期，Introduction to GenAI and ML 2025 Fall）  
**情境**：course-project  
**原始檔**：GenAI-ML/GenAIML_HW2_Build_a_Basic_RAG_System.ipynb（原始 notebook）、GenAI-ML/genaiml_hw2_build_a_basic_rag_system.py（匯出版本）、GenAI-ML/*.json（各 baseline 的預測結果）、GenAI-ML/submission*.csv（繳交檔）  
**技術棧**：Python、`rank_bm25` (BM25Okapi)、`sentence-transformers` (`intfloat/multilingual-e5-large`)、`jieba`（中文斷詞）

---

## 目標

於《紅樓夢》全文資料集上實作並比較不同層級的 RAG 系統，透過改善檢索模型、資料前處理與 prompt 設計，逐步提升問答表現。

## 方法與架構

全文依 `chunk_size`（預設 600 字）切段，建立兩種檢索器：

1. BM25 檢索：以 `jieba` 對各 chunk 斷詞，建立 `BM25Okapi` 模型 (`bm25_retrieve`)。
2. 向量檢索：以多語言 embedding 模型 `intfloat/multilingual-e5-large` 編碼所有 chunk，依查詢向量與 chunk 向量的相似度排序 (`embedding_retrieve`)。

四級 baseline 依序為：

- Simple：不檢索，直接由模型回答。
- Medium：僅以 BM25 取前 10 段作為上下文。
- Strong：BM25 與向量檢索兩路結果以 RRF (Reciprocal Rank Fusion) 融合排序，取前 10 段。
- Boss：同樣以 RRF 融合，改取前 20 段，並開放調整 `chunk_size` 與 `stride`（重疊步長）。程式中標註 `TODO: For boss baseline, adjust 'chunk_size' and 'stride'` 與 `TODO: find a proper number of chunks fed into LLM`，可見這兩項為作業要求自行調整的部分。

## 結果

資料夾內有多個版本的預測結果 JSON，每筆格式為 `{"id": ..., "pred": ...}`，另有 `submission.csv`、`submission (1).csv` 繳交檔。JSON 僅含預測的類別編號，不含正確率，故此頁不列準確率，實際分數須對照 NTU COOL 或 Kaggle 平台（未確認）。由檔名可見曾比較 `epochs=20` 與 `epochs=40`、`dropout=0.3` 等設定，boss baseline 階段至少做過一輪超參數比較。

## 學到什麼

- BM25（詞頻式）與向量嵌入（語意式）互補：BM25 對關鍵字精確命中較敏感，embedding 對語意相近但用詞不同的查詢較穩健；RRF 不需額外訓練即可結合兩者的排序。
- 中文檢索須先以 `jieba` 斷詞，BM25 才能有效運作，英文語料通常不需要這一步。
- chunk 的大小、重疊步長，以及送入生成模型的段落數量，對 RAG 表現影響很大，boss baseline 將其列為可調項目即為此故。

## 關聯概念

[[retrieval-augmented-generation]]

## 關聯頁面

[[nvidia-rag-agents-course]]（同為 RAG 主題的外部課程教材，可對照做法）
