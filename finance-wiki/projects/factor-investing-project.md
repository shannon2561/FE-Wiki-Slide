# 跨股票因子選股專案 (Factor Investing)

**類型**：project  
**期間**：2026-08 起，規劃中，尚未實作  
**情境**：self-study  
**原始檔**：TMBA/程交部/專案/factor-investing-project/（僅 `implementation-notes.md`，無程式碼或資料檔）  
**技術棧**：Python（規劃使用 pandas、numpy，階段 B 規劃 LightGBM 或簡單 NN）；資料規劃取自 TEJ Pro（手動匯出）與 FinMind、yfinance

---

## 目標

建立台股跨股票 (cross-sectional) 的因子選股策略：先完成人工設計因子的規則式版本（階段 A），再加入 ML 因子組合模型（階段 B），選配自動因子挖掘（階段 C），最後產出因子研究報告，並視情況接上 TradingView 或 XQ 觀察回測結果。社團過去的成果多為台指期或 BTC 單一標的的技術指標策略，屬時間序列型；此專案則為跨股票選股，策略型態不同。

## 方法與架構

規劃分為七步：(1) 確定標的池（0050／0051 成分股或中大型股，約 100–150 檔）與資料管線；(2) 從動能、營收動能、籌碼或隔日沖周轉率等 2–3 個候選因子中實作一個，並以 IC 檢驗訊號顯著性；(3) 組成 long-short 市場中性投組，進行規則式回測；(4) 撰寫績效報告，包括年化報酬、Sharpe、MDD、勝率、分年報酬、與 0050 比較及成本敏感度；(5) 行有餘力再做 ML 因子組合模型；(6) 選配自動因子挖掘；(7) 視進度接上 TradingView 或 XQ。

截至 ingest 時，專案僅完成目標設定與方向決策，資料夾內只有 `implementation-notes.md`，沒有程式碼、資料或報告；該檔的 Deviations 區塊亦記載「尚未開始實作，暫無偏離」。

已確定的決策（`implementation-notes.md` 的 Decisions）：策略主題為跨股票因子選股，而非多資產 CTA 或統計套利配對交易；AI／ML 先完成規則式基準版 A，再視餘裕推進；基本面資料由 TEJ Pro 手動匯出，技術面以 FinMind、yfinance 補充；方向採 long-short 市場中性，而非 long-only。

## 結果

尚無任何實作結果或數字，資料尚未抓取，亦未進行因子計算、IC 檢驗或回測，此頁不預估任何數字。

## 學到什麼

- 專案定位影響回測的嚴謹度要求：目前以研究報告為主，但未來可能接上 TradingView 或 XQ，故回測仍須完整，只是此階段不強制模擬下單。需求尚未明確時，先保留之後擴充的彈性，但不提早承諾範圍。
- 規劃階段即標出實務執行門檻：Open Questions 已記下台股放空須具融資融券資格，且有平盤以下的限制。回測可暫不受此限制，但實際下單前須確認，否則可能須改為 long-only 或設計替代的合成放空。事先寫下「回測可行」與「實務可執行」之間的差距，可作為其他策略專案規劃時的參考。

## 限制

資料授權（TEJ Pro 匯出的資料能否公開於社課成果發表）與倖存者偏差（以現在的 0050／0051 成分股回測過去，尚未規劃時點成分股 point-in-time universe）已記錄於 `implementation-notes.md` 的 Assumptions 與 Open Questions，但因尚未實作，處理方式未定。

## 關聯概念

[[factor-models]]

## 關聯頁面

尚無已完成的因子選股專案可連結；社團既有的時間序列型策略，如 [[volatility-squeeze-breakout]]、[[bollinger-trend-vs-reversion]]，屬不同策略型態，僅供對照。
