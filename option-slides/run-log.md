# 執行與檢查紀錄（run-log）

每個節點的輸入、輸出、檢查結果、是否重做，都記在這裡。

## 節點 0｜先討論（2026-11-23）
- 輸出：`docs/01-requirements.md`
- 人工檢查：使用者逐項確認範圍、讀者、長度、公式處理方式
- 討論中的修正：原本假設「上台報告」，用一頁 1 分鐘估長度；使用者指出沒有要上台，改成「讀者自己閱讀」，並新增檢查條件 3（不靠口頭說明也要看得懂）

## 節點 1｜Ingest

### 1-1 講義 01 financial engineering（53 頁）
- 輸出：sources/fe-01-options-binomial-tree；新增 4 個概念頁（option-basics、binomial-option-pricing、risk-neutral-valuation、delta-hedging-replication）；更新 derivatives、black-scholes-model、index、log
- 檢查 A（數字）：用 Python 重算講義所有數值例。q=0.6523、一期買權 0.633、二期 2.0257／1.2823、Delta 0.5064／0.7273 都吻合。**發現講義筆誤**：2.6 節借款 13.7055 應為 13.9749；2.5 節 p² 應為 q²。已記在 source 頁，Wiki 採用正確值
- 檢查 B（lint）：死連結 0、缺少必要區塊 0、新頁面都有其他頁面連進來
- 待人工確認：授課教師姓名（講義未署名）

### 1-0 範圍整理（在 ingest 02 之前插入的步驟）
- 觸發：使用者用 Obsidian 打開作業 wiki，發現混了很多跟主題無關的頁面
- 做法：以上週網站 14 個概念＋本週選擇權主題為基準，掃描所有頁面分成「核心／被引用／無關」；另外用關鍵字（推甄、碩論、學號、組員、人名）掃描敏感內容
- 結果：無關與敏感頁面共 51 頁移到 `_finance-wiki-archive`（不刪除）；留下的頁面改了 40 個連結、刪了 88 行含個資或指向已移除來源的內容
- 檢查：完整 lint 結果為死連結 0、孤立頁面 0、未進索引 0；敏感詞重掃 0
- **流程調整**：在 CLAUDE.md 加入「收錄範圍與公開規則」，讓範圍和個資檢查在 ingest 時就做，不用等到最後要公開才發現

### 1-2 ～ 1-5 講義 02、03、06、07
| 講義 | 輸出 | 檢查方法 | 結果 |
|---|---|---|---|
| 02 Itô 定理（39 頁） | 1 source＋3 concepts | 對照講義定義 | 通過（純推導，沒有數值例可重算） |
| 03 BS 公式（29 頁） | 1 source＋2 concepts | 公式數值計算、買賣權平價、五個 Greeks 與數值微分比對；抽字看不清楚的頁面改看原圖 | **發現講義第 4 頁 Theta 正負號錯誤**（和第 28 頁的證明矛盾），Wiki 採用證明頁版本 |
| 06 PDE 推導（22 頁） | 1 source＋1 concept | 數值檢查變數轉換後的方程式、熱核積分 vs 公式 | 通過 |
| 07 Martingale（25 頁） | 1 source＋2 concepts | 40 萬次蒙地卡羅檢查 $N(d_1)$、$N(d_2)$ 的機率解讀 | 通過 |

- Lint（全 wiki）：發現 1 個矛盾——舊的 black-scholes-model 頁把二項樹風險中立機率寫成 $p$，新頁用 $q$。已統一為 $q$。修正後死連結 0、孤立頁 0、缺區塊 0、未進索引 0
- 小結：5 份講義中有 2 份發現講義本身的錯誤（01 兩處、03 一處），都是靠「重算數字」抓到，只靠閱讀抓不到
- Ingest 後的 Wiki：concepts 33、sources 14（其中本週新增 5）、本週新增概念 12 頁

### 1-6 全部頁面依寫作規則改寫
- 原因：使用者要求所有產出依個人寫作風格（不用第一人稱、不用「本研究」、書面且精簡）與去 AI 味規則撰寫
- 範圍：concepts 33 頁、sources 14 頁、projects 10 頁、people 8 頁、index.md、log.md、CLAUDE.md
- 檢查：lint 結果為死連結 0、孤立頁 0、缺區塊 0、未進索引 0；禁用詞掃描僅剩誤判（「自我融資」「個人版」、表格空格、CLAUDE.md 中列出的禁用詞）
- 順帶發現：prompt-injection、quant-factor-mining-methodology 兩頁的「在知識庫中的出現」在範圍整理後變成空白，lint 規則沒有檢查空區塊，改寫時才發現並補上說明；derivatives 頁仍寫著 $p$，與 binomial-option-pricing 的 $q$ 不一致，一併修正
- 流程調整：CLAUDE.md 新增「頁面寫作規則」，之後 ingest 時即依規則撰寫，不必事後整批改寫

## 節點 2｜排大綱（查詢 Wiki）

### 2-1 大綱 v1
- 輸出：`docs/02-outline.md`，主線 15 頁加附錄 A–D，每頁標註對應的 Wiki 頁面與首次出現的術語
- 檢查 A（出處）：**未通過**。第 5 頁需要的「期望值」「折現」「無套利」三個詞，Wiki 中多頁使用（binomial-option-pricing、risk-neutral-valuation、black-scholes-model 等），卻沒有任何一頁以白話定義。讀者沒有機率基礎，若在簡報中直接補，該頁將無法對應至 Wiki
- 檢查 B（術語順序）：補上第 5 頁的前提下通過
- 檢查 C（五份講義皆有對應）：通過
- 處理：退回節點 1 補概念頁

### 2-2 人工審核：退回 Wiki 補基礎知識頁
- 使用者決定：讀者沒有基礎，無套利以外，微積分與機率分配等基礎也一併補進 Wiki，讓簡報每頁皆有頁面可對應
- 新增 5 個概念頁：no-arbitrage（無套利）、probability-expected-value（機率、期望值、變異數與標準差）、normal-distribution（常態分配與累積機率 N(·)）、discounting-continuous-compounding（折現與連續複利）、calculus-basics（微分、偏微分、積分）
- 每頁的例子皆取自已 ingest 的講義並以 Python 重算，例如買權定價偏高為 0.70 時可套利 0.069 元、偏低為 0.60 時可套利 0.034 元、$N(1)=0.8413$；定義屬基礎知識整理者，於頁尾「來源說明」註明

### 2-3 大綱 v2 重新檢查
- 第 5、11、12 頁改對應新增的基礎知識頁，附錄 B 加入 calculus-basics
- 檢查 A（出處）、B（術語順序）、C（五份講義皆有對應）、D（頁數）皆通過
- Wiki lint 發現新頁 calculus-basics 為孤立頁，於 option-greeks、itos-lemma、black-scholes-pde 補上連結後通過
- **流程調整**：lint 存為 `tools/lint_wiki.py`，並新增「空區塊」檢查。範圍整理後兩頁的「在知識庫中的出現」曾變成空白，原本的 lint 只檢查標題是否存在，未能發現
