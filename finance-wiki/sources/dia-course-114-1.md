# Data-driven Investment Analysis：政大課程（114-1）

**類型**：course
**課程代碼**：114-1 301048001
**授課教師**：[[chung-douglas|Douglas Chung]]（政大國際經營與貿易學系助理教授，PhD in Finance, BI Norwegian Business School，曾任香港金融管理局經濟學家）
**學期**：114-1（2025 秋季）
**上課時間**：週四 09:10–12:00
**原始檔**：DIA（相對於 `學校\`；內含 `ppt/`、`Homework/`、`midterm/`、`Final/`、`Group project 1/`、`Group Project 2/`、`inclass demo/`）

---

## 課程結構

課程目標（取自 `ppt/DIA Lecture 1.pdf`）：投資與資產定價的經濟理論、分析市場資料的工具（Excel、Python）、量化模型的實務應用、量化投資流程，以及市場近期趨勢。教科書為 *Investments*, 12th ed.（Bodie, Kane, Marcus）與 *Modern Portfolio Theory and Investment Analysis*, 9th ed.（Elton, Gruber, Brown, Goetzmann）。

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

> 註：Lecture 10 的簡報檔名沒有主題，Lecture 11 標為 Investment companies；第 13、14 週的主題依課程進度表比對得出，Lecture 2–7、10 的內文未逐頁確認。

### 成績組成

- 5 次線上作業（各 5%，共 25%）：`Homework/` 資料夾內為 HW1–HW5 的截圖，作答內容未開啟確認。
- 期中考（25%）：2 小時線上開書考。
- 小組專案（25%）：分組報告投資策略。
- 期末考（25%）：3 小時線上開書考。

---

## 課堂實作與教材（Python）

課程採 Anaconda 生態系（pandas、numpy、SciPy、yfinance、JupyterLab）。

### `inclass demo/114_TW50/114_TW50.ipynb`：台灣 50 指數複製

重建台灣 50 指數報酬：讀入 `TW50_Index.xlsx`（指數收盤價）與 `TW50_Stocks.xlsx`（50 檔成分股收盤價與市值），以 `pivot` 轉為寬表，計算個股報酬 `pct_change()`，再以市值計算每日權重。權重先 `weight.shift(1)` 再乘上當日報酬，避免以當日權重計算當日報酬而產生 look-ahead；加總後即為複製報酬，最後與指數實際報酬比較。

### `inclass demo/MPT Python Examples/1141_DIA.ipynb`、`Group project 1/ProjectExample/ProjectExample.ipynb`：MPT 投資組合最佳化範例

以 `yfinance` 下載 7 檔標的（GLD、TSLA、AAPL、GOOGL、MMM、COST、SPY），樣本內為 2017-12-01 至 2024-12-31，樣本外為 2024-12-31 之後。以 `scipy.optimize.minimize` (SLSQP) 求出 5 種投資組合權重：
- G：全域最小變異數 (Global minimum variance)
- M：最大化 Sharpe ratio（切線組合）
- Gn、Mn：加上不可放空限制 (`Bounds(0,1)`) 的 G 與 M
- EW：等權重 (1/N)

樣本外共 206 個交易日，績效如下（notebook 實際輸出）：

| 組合 | 平均日報酬 | 日報酬標準差 | [[sharpe-ratio\|Sharpe]]（日頻，未年化） |
|------|-----------|-------------|------|
| G | 0.001646 | 0.010261 | 0.1604 |
| Gn | 0.001647 | 0.010283 | 0.1601 |
| Mn | 0.001135 | 0.010142 | 0.1119 |
| M | 0.001048 | 0.010456 | 0.1002 |
| EW | 0.001105 | 0.014052 | 0.0787 |
| SPY（benchmark） | 0.000898 | 0.013075 | 0.0687 |

加上不可放空限制的最小變異數組合 (Gn) 與無限制版本 (G) 幾乎相同，兩者皆優於最大化 Sharpe 的 M、Mn，亦優於等權重與 SPY 買進持有。

---

## 小組專案

### Group Project 1：投資組合建構

`Group project 1/` 內含 `group project.xlsx`、`portfolio.xlsx` 與 `GroupXWeights(Example).xlsx`，以上述 `ProjectExample.ipynb` 為範例，各組自行決定投資組合權重。

### Group Project 2：策略追蹤

`Group Project 2/GroupProjectStrategyTracker/GroupProjectStrategyTracker.ipynb` 為教師追蹤全班 10 組策略的工具：各組回報自選標的（美股科技股與台股上市櫃股票）與權重，程式以 `yfinance` 下載 2025-11-05 起的股價，計算各組累積報酬與部位比例並繪圖比較。此為教學用的追蹤工具，並非個人專案成果。

---

## 期中考、期末考資料

- `midterm/`：`1141_DIA_MT_INDEX.xlsx`（指數）與 `1141_DIA_MT_MPT.xlsx`（MPT），對應期中考範圍，即統計、風險與報酬至投資組合選擇。
- `Final/`：`1141_fe_ff3.xlsx`、`1141_fe_sb6.xlsx` 及對應 PDF、`1141_perfeval_*.xlsx`（績效評估）與 `Linear Regression.xlsx`。檔名推測對應 [[factor-models|Fama-French 三因子模型 (ff3)]] 與另一組六分類模型 (sb6)，檔案內容尚未開啟確認。

---

## 關聯概念

[[portfolio-optimization]]、[[factor-models]]、[[sharpe-ratio]]

## 關聯頁面

[[derivatives-course-113-1]]（同為政大課程，主題互補：DIA 涵蓋 MPT、CAPM、APT 與投資組合實務，衍生性商品課程涵蓋選擇權與期貨定價）
