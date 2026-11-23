# 紅樓夢 RAG 檢索系統（GenAI/ML 課程 HW2）

**類型**：project
**期間**：2025-11（114-1 學期，Introduction to GenAI and ML 2025 Fall）
**情境**：course-project
**原始檔**：GenAI-ML/GenAIML_HW2_Build_a_Basic_RAG_System.ipynb（原始 notebook）、GenAI-ML/genaiml_hw2_build_a_basic_rag_system.py（匯出的 .py 版本）、GenAI-ML/*.json（各版本 baseline 的預測結果）、GenAI-ML/submission*.csv（繳交檔）
**技術棧**：Python、`rank_bm25`（BM25Okapi）、`sentence-transformers`（`intfloat/multilingual-e5-large`）、`jieba`（中文斷詞）

---

## 目標

課程作業要求在《紅樓夢》全文資料集上實作並比較不同層級的 RAG（Retrieval-Augmented Generation）系統，透過改進檢索模型、資料前處理與 prompt 設計，逐步提升問答表現。

## 方法與架構

程式將全文依 `chunk_size`（作業預設 600 字）切段，建立兩種獨立的檢索器：

1. **BM25 檢索**：用 `jieba` 對每個 chunk 斷詞，建立 `BM25Okapi` 模型（`bm25_retrieve`）
2. **向量檢索**：用 `sentence-transformers` 的多語言 embedding 模型 `intfloat/multilingual-e5-large` 對所有 chunk 編碼，以查詢向量與 chunk 向量的相似度排序（`embedding_retrieve`）

四級 baseline（逐級加碼）：
- **Simple baseline**：不做任何檢索，直接讓模型回答問題
- **Medium baseline**：只用 BM25 取前 10 個相關段落作為上下文
- **Strong baseline**：BM25 + 向量檢索兩路結果，透過 **RRF（Reciprocal Rank Fusion）** 融合排序，取前 10 段
- **Boss baseline**：同樣走 RRF 融合，但擴大取前 20 段，並開放調整 `chunk_size` 與 `stride`（重疊步長）作為額外優化空間（程式中明確標註 `TODO: For boss baseline, adjust 'chunk_size' and 'stride'`、`TODO: find a proper number of chunks fed into LLM`，顯示這兩個參數是作業要求學生自行調整的部分）

## 結果

專案資料夾中留有多個版本的預測結果 JSON，每筆為 `{"id": ..., "pred": ...}` 格式的多選題預測結果，以及對應的 `submission.csv`／`submission (1).csv` 繳交檔。

這些 JSON 只包含預測的類別編號，**檔案中未包含對應的正確率/分數等評分數字**，因此本頁不生成任何準確率數字——命中率須由使用者自行對照 NTU COOL / Kaggle 平台上的實際評分結果確認（**未確認**）。從檔名可看出曾嘗試 `epochs=20` vs `epochs=40`、`dropout=0.3` 等超參數調整，顯示 boss baseline 階段有做過至少一輪超參數比較實驗。

## 學到什麼

- BM25（詞頻式）與向量嵌入（語意式）是兩種互補的檢索取向：BM25 對關鍵字精確命中敏感、embedding 對語意相似但用詞不同的查詢較穩健，RRF 融合是不需要額外訓練就能結合兩者排序的簡單有效做法
- 中文檢索的前處理（`jieba` 斷詞）是 BM25 能否有效運作的前提，這點在英文語料中通常不需要特別處理
- chunk 切分策略（大小、重疊步長）與餵給生成模型的段落數量，是 RAG 系統中經常被低估、但影響表現很大的超參數——這與 boss baseline 階段特別把它們列為可調項目的設計意圖一致

## 關聯概念
[[retrieval-augmented-generation]]

## 關聯頁面
prompt-injection-defense-judgebot（同一門 GenAI/ML 課程的另一份作業）、[[nvidia-rag-agents-course]]（同樣主題為 RAG 的外部課程教材，可對照方法論）
