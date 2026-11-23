# Ingest 紀錄

> 2026-11-23 以前的紀錄留在主 wiki（`學校\wiki\log.md`）。這份 wiki 從 2026-11-23 起獨立維護。

---

## 2026-11-23 — 範圍整理：從主 wiki 篩出公開版本

**觸發**：作業要繳交 Wiki 成果，但這份副本整個複製自主 wiki，混有無關內容和個資。
**基準**：上週 Finance Wiki 網站的 14 個概念，加上本週選擇權主題。
**移到 `生成式AI\_finance-wiki-archive\`（不刪除）**：
- 無關：concepts 14 頁、sources 13 頁、projects 10 頁、people 8 頁（TMBA 講者）、舊 Logs 與 implementation-notes、raw 的除錯檔
- 敏感：nccu-thesis-abstracts（碩論作者姓名）、tmba-trading-dept-meetings-2026、tmba-quant-trading-department-sessions（社團內部）、graduate-school-application-2026、black-scholes-option-pricing（推甄）、taiwan-index-option-simulation（組員姓名與學號）
**留下頁面的修改**：指向被移走頁面的 wikilink 改成純文字（40 處）；只在講被移走來源的列表項目整行刪除；刪除碩論作者姓名；學號改成「本人」；社團成員姓名改成泛稱；index.md 的跨來源地圖已過期，整段刪除
**規則修改**：CLAUDE.md 新增「收錄範圍與公開規則」，之後 ingest 前先檢查

---

## 2026-11-23 — Ingest 四上財工講義 01

**原始檔**：`衍生性金融商品/四上財工/上課簡報/01 financial engineering.pdf`（53 頁）
**新增**：sources/[[fe-01-options-binomial-tree]]；concepts/[[option-basics]]、[[binomial-option-pricing]]、[[risk-neutral-valuation]]、[[delta-hedging-replication]]
**更新**：concepts/[[derivatives]]、[[black-scholes-model]]；index.md
**檢查**：講義數字以 Python 重算，發現 2.6 節借款 13.7055 應為 13.9749、2.5 節 p² 應為 q²，已記在 source 頁

---

## 2026-11-23 — Ingest 四上財工講義 02、03、06、07

| 講義 | 新增 source | 新增 concepts | 驗證 |
|---|---|---|---|
| 02 股價動態過程及 Itô 定理（39 頁） | [[fe-02-stock-dynamics-ito]] | [[brownian-motion]]、[[geometric-brownian-motion]]、[[itos-lemma]] | 推導性內容，無數值例 |
| 03 BS 模型和 BS 選擇權定價公式（29 頁） | [[fe-03-black-scholes-formula]] | [[black-scholes-pde]]、[[option-greeks]] | 公式算出買權 10.4506、賣權 5.5735，平價誤差 0；五個 Greeks 與數值微分一致；**發現第 4 頁 Theta 第二項正負號錯誤**（以第 28 頁證明為準） |
| 06 使用 BS 之 PDE 推導 BS 定價公式（22 頁） | [[fe-06-bs-pde-derivation]] | [[heat-equation-method]] | 數值驗證變數轉換後 $V_\tau=\frac12\sigma^2V_{xx}$，熱核積分結果與 BS 公式一致 |
| 07 Martingale 定價理論（25 頁） | [[fe-07-martingale-pricing]] | [[martingale]]、[[measure-change-girsanov]] | 40 萬次蒙地卡羅：$\Pr^Q(S_T>K)$ 0.5600 vs $N(d_2)$ 0.5596、$\Pr^R$ 0.6368 vs $N(d_1)$ 0.6368 |

**更新既有概念頁**：[[black-scholes-model]]、[[risk-neutral-valuation]]、[[delta-hedging-replication]]、[[derivatives]]
**Lint 發現的矛盾並修正**：[[black-scholes-model]] 舊內容把二項樹風險中立機率寫成 $p$，與 [[binomial-option-pricing]] 的 $q$ 衝突，統一為 $q$
