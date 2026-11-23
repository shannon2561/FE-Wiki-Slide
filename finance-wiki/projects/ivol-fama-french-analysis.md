# IVOL：Fama-French 三因子殘差分析（投資學課程作業）

**類型**：project  
**期間**：2025-02 ~ 2025-03（113-2 學期，依分析資料期間推估）  
**情境**：course-project  
**原始檔**：投資學/（IVOL.py、小組IVOL.py、tejapi.py、投資學IVOL.pdf、投資學IVOL.xlsx、0050.csv、2317.csv、2883.csv、stock returns.csv、data factors.csv、Data Factor.csv）  
**技術棧**：Python（pandas、numpy、statsmodels）

---

## 目標

以 Fama-French 三因子（市場 MKT、規模 SMB、價值 HML）對個股或投組的超額報酬進行 OLS 迴歸，取殘差標準差作為特異性波動度 (Idiosyncratic Volatility, IVOL)，檢驗穩定的股票是否 IVOL 較低。

## 方法與架構

個人版與小組版使用相同方法，差別僅在標的與資料檔：

1. 以 `pd.read_csv` 讀入股票報酬與因子資料，依 `Date` 欄位 `merge`。
2. 以 `data.replace([np.inf, -np.inf], np.nan).dropna()` 清除無限值與缺值，未報告缺值比例。
3. 自變數 `X = [MKT, SMB, HML]`，以 `sm.add_constant` 加入常數項；依變數 `y = 個股報酬 − 無風險利率`。
4. 以 `sm.OLS(y, X).fit()` 估計，取 `model.resid` 的標準差為 IVOL。

個人版 (IVOL.py) 的標的為 2330 台積電，資料檔為 `stock returns.csv` 與 `data factors.csv`。小組版 (小組IVOL.py) 的標的為 0050（元大台灣50 ETF）、2317（鴻海）、2883（開發金），三檔各自的 csv 搭配共用的 `Data Factor.csv`，分別執行相同的迴歸並輸出結果。

`tejapi.py` 為測試 TEJ API（`tejapi.get`、`tejapi.list_datatables()`）存取權限的腳本，不屬於正式分析程式。

## 結果

依報告（投資學IVOL.pdf）：

- 標的：2330 台積電
- 資料期間：2025.02.14–2025.03.14
- 資料來源：價格取自 Yahoo Finance，無風險利率與 Fama-French 因子取自 TEJ Pro
- IVOL：0.00298
- 結論：數值很小，與穩定股票 IVOL 應接近 0 的預期相符，代表台積電排除三種系統性風險後，個體波動小、投資風險低。

> 小組版程式已完成，但未找到對應的報告文件，三檔標的的 IVOL 數字未確認，僅程式碼可佐證方法。

## 學到什麼

- 因子模型的殘差可作為衡量個股特有風險的簡單指標，數值越小，代表報酬越能被系統性因子解釋。
- 中文欄名在 csv 匯出、匯入時容易因編碼問題變成亂碼（0050.csv 的欄名顯示為「???」），資料清理時須特別處理。

## 限制

- 樣本期間僅約 1 個月（約 20 個交易日），估計的顯著性與穩健性存疑；報告未附標準誤、信賴區間，亦未做樣本外驗證。
- 未檢查資料本身，例如報酬是否有異常值、資料筆數是否與交易日數相符。

## 關聯概念

[[factor-models]]、[[idiosyncratic-volatility]]

## 關聯頁面

[[investments-course]]
