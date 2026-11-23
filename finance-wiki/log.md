# Ingest 紀錄

> 2026-11-23 以前的紀錄保留於主 wiki（`學校\wiki\log.md`），此 wiki 自 2026-11-23 起獨立維護。

---

## 2026-11-23：範圍整理，由主 wiki 篩出公開版本

**原因**：此副本整個複製自主 wiki，混有無關內容與個人資料。  
**基準**：上週 Finance Wiki 網站的 14 個概念，加上本週的選擇權主題。  
**移至 `生成式AI\_finance-wiki-archive\`（未刪除）**：

- 無關內容：concepts 14 頁、sources 13 頁、projects 10 頁、people 8 頁（社團講者），以及舊的 Logs、implementation-notes 與 raw 的除錯檔。
- 敏感內容：nccu-thesis-abstracts（碩論作者姓名）、tmba-trading-dept-meetings-2026 與 tmba-quant-trading-department-sessions（社團內部紀錄）、graduate-school-application-2026 與 black-scholes-option-pricing（升學規劃）、taiwan-index-option-simulation（組員姓名與學號）。

**保留頁面的修改**：指向已移除頁面的 wikilink 改為純文字（40 處）；僅描述已移除來源的列表項目整行刪除；刪除碩論作者姓名；學號改為「本人」；社團成員姓名改為泛稱；index.md 已過期的跨來源地圖整段刪除。  
**規則修改**：CLAUDE.md 新增「收錄範圍與公開規則」，ingest 前即依此過濾。

---

## 2026-11-23：Ingest 四上財工講義 01

**原始檔**：`衍生性金融商品/四上財工/上課簡報/01 financial engineering.pdf`（53 頁）  
**新增**：sources/[[fe-01-options-binomial-tree]]；concepts/[[option-basics]]、[[binomial-option-pricing]]、[[risk-neutral-valuation]]、[[delta-hedging-replication]]  
**更新**：concepts/[[derivatives]]、[[black-scholes-model]]；index.md  
**檢查**：以 Python 重算講義數字，發現 2.6 節借款 13.7055 應為 13.9749，2.5 節 p² 應為 q²，已記於來源頁。

---

## 2026-11-23：Ingest 四上財工講義 02、03、06、07

| 講義 | 新增 source | 新增 concepts | 驗證 |
|---|---|---|---|
| 02 股價動態過程及 Itô 定理（39 頁） | [[fe-02-stock-dynamics-ito]] | [[brownian-motion]]、[[geometric-brownian-motion]]、[[itos-lemma]] | 推導性內容，無數值例 |
| 03 BS 模型和 BS 選擇權定價公式（29 頁） | [[fe-03-black-scholes-formula]] | [[black-scholes-pde]]、[[option-greeks]] | 買權 10.4506、賣權 5.5735，平價誤差 0；五個 Greeks 與數值微分一致；第 4 頁 Theta 第二項正負號有誤，以第 28 頁證明為準 |
| 06 使用 BS 之 PDE 推導 BS 定價公式（22 頁） | [[fe-06-bs-pde-derivation]] | [[heat-equation-method]] | 變數轉換後滿足 $V_\tau=\frac12\sigma^2V_{xx}$，熱核積分與 BS 公式一致 |
| 07 Martingale 定價理論（25 頁） | [[fe-07-martingale-pricing]] | [[martingale]]、[[measure-change-girsanov]] | 40 萬次蒙地卡羅：$\Pr^Q(S_T>K)$ 0.5600 對 $N(d_2)$ 0.5596，$\Pr^R$ 0.6368 對 $N(d_1)$ 0.6368 |

**更新既有概念頁**：[[black-scholes-model]]、[[risk-neutral-valuation]]、[[delta-hedging-replication]]、[[derivatives]]  
**Lint 發現的矛盾**：[[black-scholes-model]] 舊內容將二項樹的風險中立機率寫為 $p$，與 [[binomial-option-pricing]] 的 $q$ 衝突，已統一為 $q$；[[derivatives]] 亦同。

---

## 2026-11-23：全部頁面依寫作規則改寫

**範圍**：concepts 33 頁、sources 14 頁、projects 10 頁、people 8 頁，以及 index.md 與 CLAUDE.md。  
**做法**：逐頁重寫文字，公式、數字、檔名、路徑與 wikilink 保持不變；移除第一人稱、破折號與誇大用語，社團名稱改為泛稱，刪除指向私人設定檔的說明。  
**規則修改**：CLAUDE.md 新增「頁面寫作規則」。  
**連帶修正**：prompt-injection、quant-factor-mining-methodology 兩頁的來源已於範圍整理時移除，「在知識庫中的出現」補上說明，不再留空。

---

## 2026-11-23：新增基礎知識概念頁

**原因**：排簡報大綱時發現，「期望值」「折現」「無套利」等詞在多頁使用，卻沒有任何一頁以白話定義；簡報讀者沒有財金、微積分與機率基礎，故補上基礎知識頁。  
**新增**：concepts/[[no-arbitrage]]、[[probability-expected-value]]、[[normal-distribution]]、[[discounting-continuous-compounding]]、[[calculus-basics]]  
**例子**：皆取自已 ingest 的講義並以 Python 重算，例如一期例題中買權定價為 0.70 時可套利 0.069 元、為 0.60 時可套利 0.034 元；$4.5e^{-0.03}=4.367$；$N(1)=0.8413$。  
**規則修改**：CLAUDE.md 新增「基礎知識頁」一節，要求頁尾註明來源說明。
