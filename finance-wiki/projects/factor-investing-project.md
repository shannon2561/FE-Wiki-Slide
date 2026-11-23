# 跨股票因子選股專案（Factor Investing）

**類型**：project
**期間**：2026-08 ~ 規劃中（尚未開始實作）
**情境**：self-study
**原始檔**：TMBA/程交部/專案/factor-investing-project/（僅 `implementation-notes.md`，無程式碼或資料檔案）
**技術棧**：Python（規劃 pandas/numpy，階段B規劃 LightGBM／簡單NN）；資料規劃來源 TEJ Pro（手動匯出）+ FinMind/yfinance

---

## 目標

建立台股跨股票（cross-sectional）因子選股策略，從人工設計因子的規則式版本（階段A）起步，逐步加入 ML 因子組合模型（階段B）與選配的自動因子挖掘（階段C），最終產出因子研究報告，並視情況銜接 TradingView/XQ 觀察回測結果。與部門過去 14 組成果發表全部是台指期/BTC 單一標的技術指標策略（time-series 型策略）不同，本專案是全新的策略「形狀」——cross-sectional 選股。

## 方法與架構

規劃分七步驟：(1) 確定標的池（0050/0051 成分股或中大型股，約 100–150 檔）與資料管線；(2) 實作 2–3 個候選因子（動能、營收動能、籌碼/隔日沖周轉率）之一並計算 IC 驗證訊號顯著性；(3) 組成 long-short 市場中性投組跑規則式回測；(4) 完整績效報告（年化報酬、Sharpe、MDD、勝率、分年報酬、對比 0050 benchmark、成本敏感度）；(5) 有餘力再做 ML 因子組合模型；(6) stretch 選配自動因子挖掘；(7) 視進度銜接 TradingView 或 XQ。

**截至本次 ingest，專案僅完成目標設定與方向性決策，尚未進入任何實作步驟**——資料夾底下只有 `implementation-notes.md`，沒有任何程式碼、資料檔案或報告產出，`implementation-notes.md` 本身的 Deviations 區塊明確記載「尚未開始實作，暫無偏離」。

已確定的關鍵設計決策（見 `implementation-notes.md` Decisions）：策略主題選跨股票因子選股（而非多資產CTA或統計套利配對交易）；AI/ML 導入採「先做完規則式基準版A、再視餘裕往ML推進」的保守路線；資料來源選 TEJ Pro 手動匯出（基本面）+ FinMind/yfinance（技術面補充）；多空方向選 long-short 市場中性（而非 long-only）。

## 結果

**本專案目前沒有任何可回報的實作結果或數字**——尚處於第一階段的規劃/決策記錄狀態，連資料都還沒抓取，遑論因子計算、IC 驗證或回測績效。本頁如實記錄目前僅止於規劃這個事實，不虛構或預估任何回測數字。

## 學到什麼

- **專案定位的取捨會直接影響回測嚴謹度要求**：`implementation-notes.md` 的 Decision 記錄了一個值得記住的判斷——「暫以學術研究報告為主，但可能會接 TradingView 或 XQ 看回測結果」的定位選擇，代表回測嚴謹度仍需完整（因為未來可能延伸到執行面），但這一階段不強制做模擬下單驗證。這是在需求尚未完全明朗時，用「保留未來擴充彈性、但不過早承諾範圍」的方式做決策，呼應全域三級決策制第2級的精神（選最容易之後 revert/擴充的做法）。
- **long-short 市場中性的規劃階段就先標記出實務執行門檻，而非等做完才發現做不到**：`implementation-notes.md` 的 Open Questions 已在規劃階段就記下「台股放空需要融資融券資格與平盤以下限制」這個實務門檻，並註明「回測可以先不受此限制，但真的要接 TradingView/XQ 下單前必須確認，否則策略可能無法照原樣執行，屆時需要退回 long-only 或設計替代的合成放空方式」——這種在動筆前就寫下「回測可行 ≠ 實務可執行」的差距記錄方式，值得作為其他策略專案規劃階段的參考模式。

## 已知限制

- 資料來源授權（TEJ Pro 匯出資料能否用於社課成果發表公開分享）與存活者偏差（標的池用現在的 0050/0051 成分股回測過去，尚未規劃時點成分股 point-in-time universe）等資料工程盲點，皆已記錄在 `implementation-notes.md` 的 Assumptions／Open Questions，但因專案尚未進入實作階段，實際處置方式仍未定案。

## 關聯概念
[[factor-models]]

## 關聯頁面
（尚無其他已完成因子選股相關專案可連結；與部門既有 time-series 型策略——如 [[volatility-squeeze-breakout]]、[[bollinger-trend-vs-reversion]]——屬不同策略形狀，僅供對照參考）
