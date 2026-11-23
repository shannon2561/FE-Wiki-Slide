# IVOL / Fama-French 三因子殘差分析（投資學課程作業）

**類型**：project
**期間**：2025-02 ~ 2025-03（113-2 學期，投資學課程作業，依分析資料期間推估）
**情境**：course-project
**原始檔**：投資學/（IVOL.py、小組IVOL.py、tejapi.py、投資學IVOL.pdf、投資學IVOL.xlsx、0050.csv、2317.csv、2883.csv、stock returns.csv、data factors.csv、Data Factor.csv）
**技術棧**：Python（pandas、numpy、statsmodels）

---

## 目標

以 Fama-French 三因子模型（市場風險 MKT、規模 SMB、價值 HML）對個股/投組的超額報酬做 OLS 迴歸，取迴歸殘差的標準差作為「特異性波動度」（Idiosyncratic Volatility, IVOL），驗證「風險趨避者偏好的穩定股票，其 IVOL 是否確實較低」。

## 方法與架構

兩個版本共用同一套方法，差異僅在標的與資料檔：

1. `pd.read_csv` 讀入股票報酬與因子資料，以 `Date` 欄位 `merge`
2. `data.replace([np.inf, -np.inf], np.nan).dropna()` 清除無限值與缺值（未見缺值比例報告，對照全域 blindspot D7）
3. 自變數 `X = [MKT, SMB, HML]` 加常數項（`sm.add_constant`），依變數 `y = 個股報酬 − 無風險利率`
4. `sm.OLS(y, X).fit()`，取 `model.resid` 的標準差為 IVOL

**個人版**（IVOL.py）：單一標的 2330（台積電），資料檔 `stock returns.csv` + `data factors.csv`
**小組版**（小組IVOL.py）：三個標的 0050（元大台灣50 ETF）、2317（鴻海）、2883（開發金），資料檔各自的 csv + `Data Factor.csv`，三檔標的個別跑一次相同的迴歸流程並列印結果

`tejapi.py` 為練習串接 TEJ API（`tejapi.get`、`tejapi.list_datatables()`）的測試腳本，用於確認資料存取權限，非正式分析程式碼的一部分。

## 結果（依報告書 投資學IVOL.pdf 內文）

- 標的：2330 台積電
- 資料期間：2025.02.14–2025.03.14
- 資料來源：價格取自 Yahoo Finance；無風險利率與 Fama-French 因子取自 TEJ Pro
- **IVOL = 0.00298**
- 報告結論：數字很小，與「風險趨避者偏好的穩定股票 IVOL 應接近 0」的預期相符，代表台積電排除三種系統性風險後的個體波動性小、投資風險低

> 小組版（0050/2317/2883）程式已完整撰寫，但本次 ingest 未發現對應的小組版報告文件（PDF/Word），三檔標的實際估計出的 IVOL 數字**未確認**，僅程式碼可佐證方法。

## 學到什麼

- 因子模型殘差可作為衡量「個股特有風險」的簡單指標，數值愈小代表個股報酬愈能被系統性因子解釋
- 實務操作面：中文欄名在 csv 匯出/匯入過程中容易因編碼問題變成亂碼（如 0050.csv 的欄名顯示為「???」），需要在資料清洗階段特別處理（對照全域 blindspot D9）

## 已知限制

- 樣本期間僅約 1 個月（約 20 個交易日），OLS 估計的統計顯著性與穩健性存疑，報告未附標準誤或信賴區間，也未做樣本外驗證
- 未見對資料本身的驗證（如報酬是否有異常值、資料筆數是否與預期交易日數相符）

## 關聯概念
[[factor-models]]、[[idiosyncratic-volatility]]

## 關聯頁面
[[investments-course]]
