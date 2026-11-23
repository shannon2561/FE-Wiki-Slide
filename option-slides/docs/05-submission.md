# 繳交內容

**標題**：政大 112302043 金融四 吳佩馨 選擇權定價 LLM Wiki 教學簡報

## 1. LLM Wiki 主題與簡介

主題為財務金融學習筆記，此次新增選擇權定價。ingest 四上財務工程課程的 5 份講義（選擇權與二元樹、股價動態與 Itô 定理、Black-Scholes 公式、PDE 推導、Martingale 定價），建立 5 頁來源頁與 12 頁概念頁；另為初學者補上無套利、機率與期望值、常態分配、折現、微積分、報酬率、指數與自然對數 7 頁基礎知識頁。講義中的公式與數值例皆以 Python 重算，發現講義本身 3 處筆誤。

## 2. LLM Wiki 連結

https://github.com/shannon2561/FE-Wiki-Slide/tree/main/finance-wiki

## 3. 教學 HTML 簡報連結

https://shannon2561.github.io/FE-Wiki-Slide/option-slides/

主線 15 頁，附錄 A–D 為推導；每頁底部附對應的 Wiki 頁面連結。

## 4. Loop／Graph 設計

https://github.com/shannon2561/FE-Wiki-Slide/blob/main/option-slides/docs/03-workflow.md

流程為「Ingest 講義至 Wiki → 整理重點 → 排大綱 → 產生簡報 → 依 7 項標準檢查 → 未通過則修改並重新檢查 → 定稿」。重複執行的有兩個 loop：每份講義的 ingest 與檢查；簡報的檢查與修改，直到 7 項皆通過，實際共 4 輪。排大綱或檢查時發現 Wiki 缺少知識，退回 Ingest 補頁後再往下重跑。7 項標準為出處、術語順序、單頁可讀、符號說明、數字、寫作風格、基礎名詞，皆寫成腳本，每次修改後可完整重跑。

## 5. 實際執行與檢查紀錄

https://github.com/shannon2561/FE-Wiki-Slide/blob/main/option-slides/run-log.md

- Ingest：5 份講義重算數字，發現講義 01 兩處、講義 03 一處筆誤。
- 排大綱：發現「無套利」「期望值」「折現」在 Wiki 中沒有定義頁，退回 Wiki 補 5 頁基礎知識後重新檢查通過。
- 簡報檢查：第一輪 19 頁中 16 頁未通過，扣除腳本誤判後有內容問題的為 14 頁，修正後第二輪全部通過；簡報完成後發現未標註的基礎名詞不受檢查，新增規則 G 後第三輪抓到 6 頁內容問題，修正後第四輪全部通過。原始輸出存於 `option-slides/logs/`。
- 版面檢查：5 輪截圖，處理超出版面與 3 張圖的標註問題。

## 6. 反思

https://github.com/shannon2561/FE-Wiki-Slide/blob/main/option-slides/docs/04-reflection.md

最常出錯的節點是產生簡報，錯誤集中在符號未說明、數字在 Wiki 找不到與術語先用後定義。檢查往前移至幾處：排大綱時即標註每頁出處與術語，於產生內容前發現 Wiki 缺頁；隱私與寫作規則寫入 CLAUDE.md，ingest 時即遵守；基礎名詞改以 Wiki 基礎知識頁為準自動檢查；lint 新增空區塊檢查。workflow 因此新增退回 Ingest 的路徑；檢查原本規劃 4 項，寫腳本時加入數字與寫作風格，簡報完成後再加入基礎名詞，共 7 項，皆以腳本執行，修改後可完整重跑。
