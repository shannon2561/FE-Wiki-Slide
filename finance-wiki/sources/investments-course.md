# 投資學 (Investments)：課程資料夾

**類型**：course  
**授課教師**：未確認（資料夾內無署名講義或大綱）  
**學期**：113-2（推估為 2025 春季，依 IVOL 分析的資料期間 2025/02/14–2025/03/14 推斷）  
**原始檔**：投資學/（IVOL.py、小組IVOL.py、投資學IVOL.pdf、投資學IVOL.xlsx、0050.csv、2317.csv、2883.csv、stock returns.csv、data factors.csv、Data Factor.csv）

---

## 課程範圍

資料夾內沒有正式講義或投影片，內容為一份以 Fama-French 三因子模型估計特異性波動度 (Idiosyncratic Volatility, IVOL) 的作業，分為個人版與小組版。

### 個人作業：單一個股 IVOL

- 程式：投資學/IVOL.py
- 報告：投資學/投資學IVOL.pdf
- 方法：以 `statsmodels` 進行 OLS 迴歸，用 Fama-French 三因子（MKT、SMB、HML）解釋個股超額報酬（`Stock_Return − Risk_Free_Rate`），取殘差標準差為 IVOL。
- 標的與期間：2330 台積電，2025/02/14–2025/03/14。
- 資料來源：價格取自 Yahoo Finance，無風險利率與 Fama-French 因子取自 TEJ Pro。
- 結果：IVOL 為 0.00298，報告解讀為台積電排除三種系統性風險後，個體波動小、投資風險低。

### 小組作業：三檔標的 IVOL 比較

- 程式：投資學/小組IVOL.py
- 標的：0050（元大台灣50 ETF）、2317（鴻海）、2883（開發金）。
- 方法：與個人作業相同，對三檔標的分別估計並比較 IVOL。
- 資料檔：0050.csv、2317.csv、2883.csv（各自的報酬序列）與 Data Factor.csv（共用因子資料）。
- 注意：0050.csv 第二欄欄名顯示為「???」，推測原為中文欄名（如「收盤價」），匯出時編碼遺失。

### 其他檔案

- 投資學/tejapi.py：測試 TEJ API (`tejapi.get`) 連線與資料表查詢的練習程式。
- 投資學/試試看.py：空白測試檔。
- 投資學/活頁簿.xlsx：用途未確認。
- 投資學/TEJ Pro/：TEJ Pro 看盤下單軟體的安裝目錄，非課程內容，未 ingest。

---

## 主要概念

1. Fama-French 三因子模型：以市場風險溢酬 (MKT)、規模因子 (SMB)、價值因子 (HML) 解釋個股或投組的超額報酬。
2. 特異性波動度 (IVOL)：迴歸殘差的標準差，即無法被系統性因子解釋的個股波動。
3. TEJ Pro：台灣財務資料庫，用於取得無風險利率與因子資料。

## 限制

報告未討論以下問題：樣本期間僅約 1 個月，OLS 的觀測值少，係數與 IVOL 的標準誤可能偏大，報告亦未附標準誤或信賴區間；此外，未見缺值與極端值的檢查步驟。

## 關聯概念

[[factor-models]]（Fama-French 三因子屬於因子模型）、[[idiosyncratic-volatility]]（作業的主要指標）

## 關聯頁面

[[ivol-fama-french-analysis]]
