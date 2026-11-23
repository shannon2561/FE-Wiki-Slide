# 投資學（Investments）— 課程資料夾

**類型**：course
**授課教師**：未確認（資料夾內無署名講義或大綱）
**學期**：113-2（推估，2025 春季；依 IVOL 分析資料期間 2025/02/14–2025/03/14 推斷）
**原始檔**：投資學/（IVOL.py、小組IVOL.py、投資學IVOL.pdf、投資學IVOL.xlsx、0050.csv、2317.csv、2883.csv、stock returns.csv、data factors.csv、Data Factor.csv）

---

## 課程範圍

`投資學` 資料夾內**未包含**正式課程講義或投影片檔案，內容以一份圍繞「Fama-French 三因子模型與個股／投組特異性風險（Idiosyncratic Volatility, IVOL）」的作業/專案為主，分個人版與小組版兩份程式碼與一份報告：

### 個人作業：單一個股 IVOL 分析

- **程式**：投資學/IVOL.py
- **報告**：投資學/投資學IVOL.pdf（作者：本人）
- **方法**：以 `statsmodels` OLS 迴歸，用 Fama-French 三因子（MKT、SMB、HML）解釋個股超額報酬（`Stock_Return − Risk_Free_Rate`），取迴歸殘差之標準差作為 IVOL
- **標的**：2330 台積電，資料期間 2025/02/14–2025/03/14
- **資料來源**（依報告內文）：價格取自 Yahoo Finance，無風險利率與 Fama-French 因子取自 TEJ Pro
- **結果**（報告內載明的數字）：IVOL = 0.00298，報告解讀為「台積電排除三種系統性風險後，個體波動性小、投資風險低」

### 小組作業：三檔標的 IVOL 對比

- **程式**：投資學/小組IVOL.py
- **標的**：0050（元大台灣50 ETF）、2317（鴻海）、2883（開發金）
- **方法**：與個人作業相同的 Fama-French 三因子 OLS 迴歸，對三檔標的分別估計並比較 IVOL
- **資料檔**：0050.csv、2317.csv、2883.csv（各自的報酬序列）＋ Data Factor.csv（共用因子資料）
- **注意**：0050.csv 的第二欄欄名顯示為亂碼「???」，推測是原始中文欄名（如「收盤價」）在匯出時編碼流失，屬於典型的中文欄位編碼問題（對照全域 blindspot D9）

### 其他檔案

- 投資學/tejapi.py：測試 TEJ API（`tejapi.get`）連線與資料表查詢的練習腳本
- 投資學/試試看.py：空白/測試檔
- 投資學/活頁簿.xlsx：未開啟確認內容（Excel 活頁簿，未確認用途）
- 投資學/TEJ Pro/：TEJ Pro 看盤下單軟體安裝目錄（.dll/.exe/.mdb 等二進位檔），非課程內容，本次 ingest 已排除

---

## 核心概念

1. **Fama-French 三因子模型**：市場風險溢酬（MKT）、規模因子（SMB）、價值因子（HML）解釋個股/投組超額報酬
2. **特異性波動度（Idiosyncratic Volatility, IVOL）**：迴歸殘差的標準差，代表無法被系統性因子解釋的個股波動
3. **TEJ Pro 資料庫**：台灣本地財務資料庫，用於取得無風險利率與因子資料

## 已知限制（未在報告中討論，但屬本領域常見坑）

- 樣本期間僅約 1 個月（2025/02/14–2025/03/14），OLS 迴歸的觀測值數量很少，係數與 IVOL 估計的標準誤可能很大，報告未附標準誤或信賴區間
- 未見到對缺值、極端值的資料驗證步驟（對照全域 blindspot D7）

## 關聯概念

[[factor-models]]（Fama-French 三因子屬於本頁面涵蓋的資產定價因子模型家族）、[[idiosyncratic-volatility]]（課程作業核心指標）

## 關聯頁面
[[ivol-fama-french-analysis]]
