# 教學大綱 v2（待人工審核）

**主題**：選擇權怎麼定價？從二元樹到 Black-Scholes  
**讀者**：沒有財金、微積分與機率基礎的初學者，自行閱讀  
**知識來源**：`finance-wiki/`，每頁標註對應的 Wiki 頁面

## 主線（15 頁）

| 頁 | 標題 | 這頁要讓讀者懂什麼 | 對應 Wiki 頁面 | 首次出現的術語 |
|---|---|---|---|---|
| 1 | 選擇權怎麼定價？ | 封面與學習目標：看完能解釋 BS 公式的兩項在算什麼 | index | — |
| 2 | 選擇權是一種「權利」 | 付權利金換到「可以買、但不一定要買」的權利；買權與賣權、歐式與美式 | option-basics | 選擇權、權利金、標的、履約價、到期日、買權、賣權、歐式、美式 |
| 3 | 到期時賺多少 | Hull 例題：K=100、權利金 5 元，股價 115 時淨賺 1,000 元，低於 100 時賠 500 元；損益圖 | option-basics、fe-01 | 到期損益 max(S_T−K,0) |
| 4 | 難題：今天該付多少錢 | 直覺是「猜漲跌機率算平均」，但每個人猜的機率不同，答案就不同 | risk-neutral-valuation、probability-expected-value | 機率 |
| 5 | 三個基本工具 | 期望值（機率加權平均）、折現（未來的錢換算成今天，e^{-rT}）、無套利（不存在零成本又穩賺的機會） | probability-expected-value、discounting-continuous-compounding、no-arbitrage | 期望值、折現、無風險利率 r、無套利 |
| 6 | 最簡單的世界：一期二元樹 | 股價 20，3 個月後只會變 22 或 18；K=21 的買權到期值 1 或 0 | binomial-option-pricing、fe-01 | 二元樹 |
| 7 | 關鍵一步：組一個不怕漲跌的組合 | 賣 1 單位買權、買 0.25 股，漲跌到期都值 4.5；折現後 4.367；買權 = 5 − 4.367 = 0.633；價格若為 0.70 或 0.60 即可套利 | binomial-option-pricing、delta-hedging-replication、no-arbitrage | Δ（避險股數）、無風險組合 |
| 8 | 為什麼不用猜機率 | 換算出的 q = 0.6523 不是真實機率，而是「讓股票只賺無風險利率」的機率；用 q 算期望值再折現，答案同為 0.633 | risk-neutral-valuation、fe-01 | 風險中立機率 q、真實機率 p |
| 9 | 換個角度：複製 | 股票加借錢可以做出跟買權一模一樣的現金流，所以兩者價格必須相同 | delta-hedging-replication | 複製 |
| 10 | 從兩期到無限多期 | 二期例題起點價值 1.2823；期數切得越細，結果越接近 Black-Scholes 公式 | binomial-option-pricing、fe-01 | 多期二元樹 |
| 11 | 股價在連續時間怎麼動 | 報酬率＝固定成長 μ＋隨機衝擊 σ；隨機部分為布朗運動，服從常態分配；σ 即報酬率的標準差 | geometric-brownian-motion、brownian-motion、normal-distribution、probability-expected-value | 波動度 σ（標準差）、期望報酬率 μ、布朗運動、常態分配 |
| 12 | Black-Scholes 公式 | 逐項拆解 C = S·N(d₁) − K·e^{-rT}·N(d₂)；N(·) 為常態曲線左側面積；數值例 S=K=100、r=5%、σ=20%、T=1，C=10.45 | black-scholes-model、fe-03、normal-distribution | N(·)（累積機率）、d₁、d₂ |
| 13 | 公式兩項在算什麼 | N(d₂) 是到期被執行的機率；第二項為「付履約價」的期望現值，第一項為「拿到股票」的期望現值；40 萬次模擬驗證 | fe-07、fe-03 | — |
| 14 | 三條路，同一個答案 | 二元樹取極限、解偏微分方程（同熱傳導）、Martingale，推導方式不同、結果相同；各附推導連結 | fe-03、fe-06、fe-07、black-scholes-pde、heat-equation-method、martingale | 偏微分方程、Martingale |
| 15 | 重點整理 | 五個結論：權利有價、價格由無套利決定、不用猜漲跌、BS 為二元樹的極限、公式兩項的意義 | 以上各頁 | — |

## 附錄（推導，主線以連結進入）

| 附錄 | 內容 | 對應 Wiki 頁面 |
|---|---|---|
| A | 二元樹一般公式與 q 的推導 | binomial-option-pricing、fe-01 |
| B | Itô 定理與 BS PDE（先以白話說明微分、偏微分） | calculus-basics、itos-lemma、black-scholes-pde、fe-02、fe-03 |
| C | 由熱傳導方程式解出 BS 公式 | heat-equation-method、fe-06 |
| D | Martingale、測度轉換與 N(d₁)、N(d₂) 的機率意義 | martingale、measure-change-girsanov、fe-07 |

## 大綱階段的檢查結果

### v1
第 5 頁的「期望值」「折現」「無套利」在 Wiki 中沒有定義頁，未通過；退回 Wiki 補基礎知識頁。

### v2（補頁後重新檢查）

| 檢查項目 | 結果 |
|---|---|
| 每頁皆可對應至 Wiki 頁面 | 通過：第 5 頁改對應 probability-expected-value、discounting-continuous-compounding、no-arbitrage；第 11、12 頁另對應 normal-distribution |
| 術語先定義、後使用 | 通過：無套利、期望值、折現於第 5 頁定義，第 7、8 頁才使用；標準差與常態分配於第 11 頁定義，第 12 頁才使用 N(·) |
| 五份講義皆有對應頁面 | 通過：01 → 第 3、6–10 頁；02 → 第 11 頁；03 → 第 12、14 頁；06 → 第 14 頁、附錄 C；07 → 第 13、14 頁、附錄 D |
| 主線頁數 12–15 頁 | 通過（15 頁） |
| Wiki lint | 通過：70 頁，死連結、孤立頁、未進索引、缺區塊、空區塊皆為 0 |
