# Data-driven Investment Analysis — 政大課程（114-1）

**類型**：course
**課程代碼**：114-1 301048001
**授課教師**：[[chung-douglas|Douglas Chung]]（政大國際經營與貿易學系助理教授；PhD in Finance, BI Norwegian Business School；曾任香港金融管理局經濟學家）
**學期**：114-1（2025 秋季）
**上課時間**：週四 09:10–12:00
**原始檔**：DIA（相對於 `學校\`；內含 `ppt/`、`Homework/`、`midterm/`、`Final/`、`Group project 1/`、`Group Project 2/`、`inclass demo/`）

---

## 課程結構

課程目標（取自 `ppt/DIA Lecture 1.pdf`）：教導投資與資產定價的經濟理論、介紹分析市場資料的電腦工具（Excel、Python）、展示量化模型的實務應用、說明量化投資流程、討論市場近期趨勢。教科書為 *Investments*, 12th ed.（Bodie, Kane, Marcus）與 *Modern Portfolio Theory and Investment Analysis*, 9th ed.（Elton, Gruber, Brown, Goetzmann）。

### 每週進度（Lecture 1 簡報第 14–17 頁）

| 週次 | 主題 | 對應簡報 |
|------|------|---------|
| 1 | 課程總覽 | DIA Lecture 1 |
| 2 | 統計與最佳化技巧複習 | DIA Lecture 2 |
| 3 | 金融市場與證券交易 | DIA Lecture 3 |
| 4 | 市場資料的風險與期望報酬 | DIA Lecture 4 |
| 5 | 風險性資產的資金配置 | DIA Lecture 5 |
| 6 | 投資組合選擇 | DIA Lecture 6 |
| 7 | 現代投資組合理論（[[portfolio-optimization\|MPT]]）應用 | DIA Lecture 7 |
| 8 | 期中考（線上、開書） | — |
| 9 | CAPM | DIA Lecture 8 - CAPM |
| 10 | 投資策略專案報告（一） | — |
| 11 | 套利定價理論（APT）與多因子模型 | DIA Lecture 9 - APT |
| 12 | 因子模型應用 | — |
| 13 | 績效評估（Performance evaluation） | DIA Lecture 10 |
| 14 | 投資公司（Investment companies） | DIA Lecture 11 - Investment companies |
| 15 | 投資策略專案報告（二） | — |
| 16 | 期末考（線上、開書） | — |

> 註：Lecture 10、11 的簡報檔名沒有主題後綴（Lecture 10）或標為 Investment companies（Lecture 11），對應週 13、14 主題是依課程進度表比對得出，未逐頁開啟 Lecture 2–7、10 簡報內文確認逐頁細節。

### 成績組成

- 5 次線上作業（各 5%，共 25%）：`Homework/` 資料夾內為 HW1–HW5 的截圖（`HW1 截圖.JPG` ~ `HW5 截圖.JPG`），未開啟細看作答內容。
- 期中考（25%）：2 小時線上開書考。
- 小組專案（25%）：分組報告投資策略。
- 期末考（25%）：3 小時線上開書考。

---

## 課堂實作與教材（Python）

課程採 Anaconda 生態系（pandas、numpy、SciPy、yfinance、JupyterLab）。

### `inclass demo/114_TW50/114_TW50.ipynb`：台灣 50 指數複製

實際重建台灣 50 指數報酬的流程：讀入 `TW50_Index.xlsx`（指數收盤）與 `TW50_Stocks.xlsx`（50 檔成分股收盤與市值），用 `pivot` 轉成寬表、計算個股報酬 `pct_change()`、以市值計算每日權重、**`weight.shift(1)` 後再乘上當日報酬**（避免用當日權重對當日報酬做 look-ahead），加總得到複製報酬，最後與台灣 50 指數實際報酬比較。

### `inclass demo/MPT Python Examples/1141_DIA.ipynb`、`Group project 1/ProjectExample/ProjectExample.ipynb`：MPT 投資組合最佳化範例

以 `yfinance` 下載 7 檔標的（GLD、TSLA、AAPL、GOOGL、MMM、COST、SPY），切分樣本內（2017-12-01 ~ 2024-12-31）與樣本外（2024-12-31 之後）。用 `scipy.optimize.minimize`（SLSQP）解出 5 種投資組合權重：
- **G**：全域最小變異數（Global minimum variance）
- **M**：最大化 Sharpe ratio（切線組合）
- **Gn / Mn**：加上不可放空限制（`Bounds(0,1)`）的 G、M
- **EW**：等權重（1/N）

樣本外（206 個交易日）績效摘要（notebook 實際輸出）：

| 組合 | 平均日報酬 | 日報酬標準差 | [[sharpe-ratio\|Sharpe]]（日頻，未年化） |
|------|-----------|-------------|------|
| G | 0.001646 | 0.010261 | 0.1604 |
| Gn | 0.001647 | 0.010283 | 0.1601 |
| Mn | 0.001135 | 0.010142 | 0.1119 |
| M | 0.001048 | 0.010456 | 0.1002 |
| EW | 0.001105 | 0.014052 | 0.0787 |
| SPY（benchmark） | 0.000898 | 0.013075 | 0.0687 |

不放空限制下的最小變異數組合（Gn）與無限制版本（G）幾乎沒有差異；但兩者皆優於最大化 Sharpe 的 M/Mn，且優於等權重與 SPY 買進持有基準。

---

## 小組專案

### Group Project 1：投資組合建構

`Group project 1/` 內含 `group project.xlsx`、`portfolio.xlsx`、`GroupXWeights(Example).xlsx`，搭配上述 `ProjectExample.ipynb` 作為範例。學生分組決定投資組合權重。

### Group Project 2：策略追蹤

`Group Project 2/GroupProjectStrategyTracker/GroupProjectStrategyTracker.ipynb` 是教師端用來追蹤全班 10 組策略的工具：每組回報自選標的（美股科技股、台股上市/上櫃股票混合）與權重，程式用 `yfinance` 下載近期（2025-11-05 起）股價，計算各組的累積報酬與部位比例並繪圖比較。這是教學追蹤工具而非單一學生的個人專案成果。

---

## 期中考、期末考資料

- `midterm/`：`1141_DIA_MT_INDEX.xlsx`（指數相關）、`1141_DIA_MT_MPT.xlsx`（MPT 相關），對應期中考涵蓋範圍（統計/風險報酬到投資組合選擇）。
- `Final/`：`1141_fe_ff3.xlsx`、`1141_fe_sb6.xlsx` 及對應 PDF、`1141_perfeval_*.xlsx`（績效評估）、`Linear Regression.xlsx`。檔名疑似對應 [[factor-models|Fama-French 三因子模型（ff3）]] 與另一組六分類模型（sb6），但未開啟檔案確認內容細節，此推測待後續查證。

---

## 關聯概念

[[portfolio-optimization]]、[[factor-models]]、[[sharpe-ratio]]

## 關聯頁面

[[derivatives-course-113-1]]（同為政大課程，主題互補：DIA 涵蓋 MPT/CAPM/APT/投資組合實務，衍生性商品課程涵蓋選擇權/期貨定價）
