# RSI 超買超賣台指期策略

**類型**：project  
**期間**：2026-08-27（單次集中開發）  
**情境**：self-study（量化交易社團自主開發，沿用社團既有的回測慣例）  
**原始檔**：TMBA\程交部\專案\rsi-strategy  
**技術棧**：Python（pandas、numpy、matplotlib）、Jupyter Notebook（`jupyter nbconvert --execute`）、自製單元測試（`test_*.py`，本機無 pytest，直接執行）

---

## 目標

以 Wilder's RSI 設計台指期（TX 大台，60 分 K）多空對稱的超買超賣波段策略，訊號以「穿越」觸發，而非價格持續處於區間內即觸發，並完成含樣本外驗證的回測。

## 方法與架構

- 資料：自原始 1 分 K（`資料/台指期分鐘連續月_20260811/`）重新聚合出含日盤與夜盤的 60 分 K。夜盤的日期錨點以時鐘時間判斷，而非 `trade_date − 1 天`，避免跨週末錯位。
- 指標：RSI 以 simple mean 作為初始值，再以 `ewm(alpha=1/period, adjust=False)` 向量化計算；完全沒有波動（avg_gain = avg_loss = 0）時定義為 50，以免與暖機期的 NaN 混淆。
- 訊號與成交：`signal` 欄（訊號根 t）與 `fill_price` 欄（成交根 t+1 開盤）分開存放，並以專門測試確認 fill_price 必為訊號根下一根的開盤價，防止日後重構時誤引入 look-ahead。
- 樣本切分：訊號以 1998 年至 2019 年底的完整連續資料產生，避免自 2011 年重新暖機而失真；樣本內 (IS) 評估期間為 2011–2019，樣本外 (OOS) 為 2020 至 2026/08，只跑一次。
- 參數優化：RSI 週期 [9, 14, 21, 25] × oversold [25, 30, 35] × overbought [65, 70, 75]，共 36 組；停損 offset 固定為 10，不列入網格。以 Calmar Ratio 為挑選準則，且鄰近參數（三個維度各 ±1 格）的離散度須小於 20% 才視為穩健高原。
- 最終打包為單一 `final_report.ipynb`，由最上游的原始資料重新聚合 60 分 K，已以 `jupyter nbconvert --execute` 實際執行，並逐一核對關鍵數字與原始報告一致。

## 結果

依 `optimize_report.md` 與 `oos_validation_report.md`：

1. IS（2011–2019）：Calmar 0.3195（CAGR 7.10%、MDD 22.22%、年化 Sharpe 0.6122），勝率 60.00%，獲利因子 1.8522，共 75 筆交易。
2. OOS（2020 至 2026/08）：Calmar 0.2552（CAGR 22.82%、MDD 89.42%、Sharpe 0.4468），勝率 55.56%，獲利因子 1.3539，共 100 筆交易。同期 Buy&Hold（以同一份 TX 期貨資料模擬，並非大盤指數）CAGR 為 36.81%、Sharpe 1.0014，策略明顯落後。
3. 參數穩健性：36 組網格中找不到任何穩健高原，所有組合的離散度皆大於 20%。最終選用的最佳格（RSI 週期 25、oversold 35、overbought 75）鄰近離散度高達 175.23%，屬孤立尖峰；±10% 的參數微擾測試中，有 3 組指標變動超過 50%（最大 186%），可見結果對參數高度敏感。
4. 逐年報酬：2022 年單年虧損達假設本金的 98.41%；2017、2020、2021 等多頭年份的報酬皆低於同期 Buy&Hold，與「RSI 均值回歸策略在趨勢行情失效」的預期一致。
5. `oos_validation_report.md` 第七節說明，IS 與 OOS 的 Calmar 皆為正，不能視為策略經過嚴謹驗證，只能視為一組對參數高度敏感的設定所得到的單次觀察。

## 學到什麼

- MTM 權益曲線重建的 off-by-one 錯誤：`signals.py` 為防 look-ahead，將訊號欄（第 t 根）與成交欄（第 t+1 根開盤）分開存放。若直接沿用 `macd-adx-fib-strategy` 專案 `metrics.py` 中的 `build_mtm_equity_curve`（該寫法假設 entry_ts 即為實際成交根），重建逐根 mark-to-market 權益曲線時會錯位一根。修正方式為先將 entry_ts（訊號根 t）加 1 對應至實際成交根，再以成交根重建逐根持倉方向；並以手算 7 根 K 棒的合成範例與全歷史 942 筆交易雙重驗證，MTM 總和與已實現損益總和的誤差為 0.0 才通過。兩個專案即使採用相同的防 look-ahead 設計，內部欄位的意義（entry_ts 記錄訊號根或成交根）未必相同，沿用其他專案的核對程式前，須先確認欄位定義一致。
- 夜盤的日期錨點不能用 `trade_date − 1 天`：跨週末時（trade_date 為週一，其夜盤實際在週五晚上）會產生 39.75 萬筆負 offset；改以時鐘時間判斷（15:00 以後用當天日期，否則用前一個日曆日）後驗證通過。
- 年化係數不能用全期單一常數：TX 夜盤於 2017-05-15 才上線，2011–2016 年每年約 1,220–1,250 根（僅日盤），2018 年起每年約 4,500–4,670 根（日盤加夜盤），相差約 3.7 倍。若以全期平均作為單一常數，IS（混合兩種頻率）與 OOS（夜盤時代）的年化 Sharpe 與 CAGR 皆會套錯係數，故改以各評估期間實際的「根數 ÷ 年數」計算。

## 關聯概念

[[technical-indicators]]、[[sharpe-ratio]]、[[backtest-overfitting-and-validation]]

## 關聯頁面

[[macd-adx-fibonacci-futures-strategy]]、[[adx-regime-switching-donchian-bollinger-strategy]]
