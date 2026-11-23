# LLM Wiki：Schema

此 wiki 為財務金融學習筆記的知識庫，涵蓋衍生性商品與選擇權定價、資產定價、投資組合、機器學習與量化實務，為主 wiki（`學校\wiki`）篩選後的公開版本。

## 收錄範圍與公開規則（ingest 前檢查）

- 只收錄與上述主題相關的內容，無關的課程、專案與社團活動不 ingest。
- 不得出現：本人以外的人名（同學、組員、社團成員、碩論作者）、學號、推甄或升學規劃、成績。
- 已公開發表論文的作者與授課教師可保留。
- 原始資料含上述內容時，改寫為「組員」「社團成員」等泛稱，或直接略過。

## 頁面寫作規則（撰寫與修改頁面時遵守）

- 不使用第一人稱（我、我們、個人、筆者），亦不使用「本研究」「本報告」「本文」；以無主詞句或討論對象作為主詞。
- 書面、精簡，先寫結論或數字，再寫理由；數字、公式與原始資料保持一致，不為了「更具體」而補入原始資料沒有的內容。
- 不使用破折號、「不是……而是」「不僅……更……」與誇大用語（深度、關鍵、賦能、全方位等）。
- 中英文之間加半形空格；括號內為英文時用半形括號，為中文時用全形括號。
- 寫「瞭解」而非「了解」。

---

## 架構

```
wiki/
├── CLAUDE.md          ← 你正在讀這份（Layer 3：規則）
├── index.md           ← 所有頁面的總索引
├── log.md             ← 每次 ingest 的紀錄
├── raw/               ← 原始資料（不可修改）
│   ├── journals/      ← 期刊論文全文 .md
│   ├── thesis/        ← 學位論文摘要
│   └── courses/       ← 課程講義與投影片索引
├── sources/           ← 每個來源的摘要頁（LLM 撰寫）
├── projects/          ← 專案頁：做過的程式/研究專案（LLM 撰寫）
├── concepts/          ← 概念頁（LLM 撰寫與維護）
└── people/            ← 作者頁（LLM 撰寫與維護）
```

---

## 原始檔引用規則（不複製大檔）

大型原始檔（PDF、影音、程式碼庫）**不複製**進 raw/，改用路徑引用：

- 頁面的「原始檔」欄位記**相對於 `Desktop\學校\` 的路徑**（如 `衍生性商品/04 BS訂價公式.pdf`），並另記「檔名」欄位。
- 檔名是重連的備援鍵：檔案搬家後路徑失效，lint 會用檔名在 `學校\` 底下全域搜尋並自動修正路徑（見 Lint 第 6 條）。
- 只有輕量文字轉檔（.md/.txt）才放進 raw/。

---

## 頁面格式規範

### sources/ 頁面
```markdown
# 來源標題

**類型**：journal | thesis | course  
**作者**：[[人名]]  
**年份**：YYYY  
**原始檔**：raw/journals/filename.md

---

## 核心問題
（這篇在解決什麼？）

## 方法
（用什麼方法？）

## 主要發現
（結果是什麼？）

## 關聯概念
[[concept-1]]、[[concept-2]]

## 關聯文獻
[[source-slug]]
```

### concepts/ 頁面
```markdown
# 概念名稱

## 定義
（一段話解釋）

## 在知識庫中的出現
- [[source-1]]：（這個概念在此來源中的角色）
- [[source-2]]：…

## 關聯概念
[[related-concept]]

## 關聯文獻
（若有學術定義來源）
```

### projects/ 頁面
```markdown
# 專案名稱

**類型**：project  
**期間**：YYYY-MM ~ YYYY-MM（不確定就寫學期，如 113-2）  
**情境**：course-project | competition | self-study | research  
**原始檔**：（相對於 學校\ 的資料夾路徑）  
**技術棧**：Python / sklearn / ...

---

## 目標
（這個專案要解決什麼問題？）

## 方法與架構
（怎麼做的？主要模組/資料流）

## 結果
（做出什麼？數字結論只能來自專案內實際檔案，不可自行生成）

## 學到什麼
（可遷移的教訓與技能）

## 關聯概念
[[concept-1]]、[[concept-2]]

## 關聯頁面
[[source-or-project-slug]]
```

### people/ 頁面
```markdown
# 姓名

**機構**：  
**領域**：

## 在知識庫中的著作
- [[source-slug]]（年份）：一句話說明

## 關聯人物
[[collaborator-name]]
```

---

## 三種操作

### 1. Ingest（新增來源）
收到指令「Ingest raw/xxx.md」、「新增這篇論文」或「ingest 這個資料夾/專案」時：
1. 閱讀原始檔（raw/ 內的，或 `學校\` 底下以路徑引用的）
2. 在 `sources/` 建立摘要頁；專案類則在 `projects/` 建立專案頁（按格式）
3. 更新或新增相關 `concepts/` 頁面（加入此來源的角色說明與 wikilinks）
4. 更新或新增相關 `people/` 頁面
5. 在 `log.md` 新增一筆 ingest 紀錄
6. 在 `index.md` 更新索引

### 2. Query（查詢）
收到問題時：
1. 讀取已合成的 wiki 頁面（不重讀 raw/）
2. 跨頁面整合 [[wikilinks]] 作答
3. 如果答案有助於未來查詢，可將它存為新的 sources/ 或 concepts/ 頁面

### 3. Lint（健康檢查）
收到「lint wiki」指令時：
1. 找出孤立頁面（沒有任何 [[wikilink]] 指向它）
2. 找出矛盾（不同來源對同一概念的說法衝突）
3. 找出 [[wikilink]] 指向不存在的頁面
4. 找出 sources/ 有頁面但 people/ 缺少對應作者頁的情況
5. 回報清單，等待確認後再修正
6. **路徑重連**：檢查所有頁面「原始檔」欄位的路徑是否存在；失效的用「檔名」欄位在 `Desktop\學校\` 底下搜尋，找到唯一匹配就更新路徑，找到多個或零個則列出待人工確認

---

## 命名規則

| 類型 | 檔名格式 | 範例 |
|------|---------|------|
| sources | kebab-case 英文 | `empirical-asset-pricing-ml.md` |
| projects | kebab-case 英文 | `aic-line-chatbot.md` |
| concepts | kebab-case 英文 | `risk-premium-pca.md` |
| people | 姓-名 英文 | `kelly-bryan.md` |
| raw | 保持原檔名 | `Empirical_Asset_Pricing_via_Machine_Learning.md` |

---

## Wikilinks 規則

- 所有跨頁面連結使用 `[[slug]]` 格式（Obsidian 相容）
- 顯示別名用 `[[slug|顯示文字]]`
- 連結對象：sources、projects、concepts、people 四類頁面
- raw/ 頁面不加 wikilinks（原始資料不修改）
