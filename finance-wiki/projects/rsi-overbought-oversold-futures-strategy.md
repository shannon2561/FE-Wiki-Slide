# RSI 超買超賣 台指期策略

**類型**：project
**期間**：2026-08（單次密集開發，2026-08-27）
**情境**：self-study（TMBA 程交部自主開發，沿用部門既有回測慣例）
**原始檔**：TMBA\程交部\專案\rsi-strategy
**技術棧**：Python（pandas、numpy、matplotlib）、Jupyter Notebook（`jupyter nbconvert --execute`）、自製單元測試（`test_*.py`，本機無 pytest，直接執行）

---

## 目標

用 Wilder's RSI 設計台指期（TX 大台，60 分 K）多空對稱的超買超賣波段策略，訊號採「穿越式」觸發（而非持續處於區間），完成含樣本外驗證的完整回測。

## 方法與架構

- **資料**：從原始 1 分 K（`資料/台指期分鐘連續月_20260811/`）重新聚合出含日盤與夜盤的 60 分 K；夜盤時段錨點用時鐘時間分支判斷（非 `trade_date-1天`，避免跨週末錯位）。
- **指標**：RSI 用「simple mean 種子 + `ewm(alpha=1/period, adjust=False)`」向量化實作，完全走平（avg_gain=avg_loss=0）時明確定義為 50（避免與暖機期 NaN 混淆）。
- **訊號與撮合**：`signal` 欄（訊號根 t）與 `fill_price` 欄（成交根 t+1 開盤）分離存放，用專門測試斷言 fill_price 必為訊號當根下一根的 open，防止未來重構誤引入 look-ahead。
- **樣本切分**：訊號生成用資料起點(1998)~2019 底完整連續資料（避免從 2011 重新暖機失真），IS 評估窗口 2011-2019、OOS 2020-2026/08（只碰一次）。
- **參數優化**：RSI 週期 [9,14,21,25] × oversold [25,30,35] × overbought [65,70,75]，共 36 組，停損 offset 固定=10 不進網格；挑選準則為 Calmar Ratio，且要求鄰域（3 維座標各±1格）離散度 <20% 才視為穩健高原。
- 最終打包為單一可從頭執行到尾的 `final_report.ipynb`（`backtest-bundle` skill），從最上游 raw data 重新聚合 60 分 K，已用 `jupyter nbconvert --execute` 實跑通過並逐一核對關鍵數字與原始報告一致。

## 結果

依據 `optimize_report.md`、`oos_validation_report.md`（步驟 4、5 正式報告）：

- **IS（2011-2019）**：Calmar=0.3195（CAGR 7.10%、MDD 22.22%、年化 Sharpe 0.6122、勝率 60.00%、獲利因子 1.8522、75 筆交易）
- **OOS（2020-2026/08）**：Calmar=0.2552（CAGR 22.82%、MDD 89.42%、Sharpe 0.4468、勝率 55.56%、獲利因子 1.3539、100 筆交易）；同期 Buy&Hold（以同一份 TX 期貨資料模擬，非真正大盤指數）CAGR=36.81%、Sharpe=1.0014——**策略明顯跑輸 Buy&Hold**
- **參數穩健性——本專案最重要的誠實揭露**：36 組網格中**找不到任何鄰域穩健的高原**（所有組合離散度皆 >20%），最終選用的 best cell（RSI週期=25, oversold=35, overbought=75）本身鄰域離散度高達 175.23%，屬孤立尖峰。±10% 參數微擾測試中有 3 組指標變動超過 50%（最大達 186%），進一步佐證結果對參數選擇高度敏感。
- 逐年報酬顯示 2022 年單年虧損達假設本金 98.41%；2017、2020、2021 等明確多頭年份策略報酬皆低於同期 Buy&Hold，量化印證「RSI 均值回歸策略在趨勢行情失效」的預期。
- **`oos_validation_report.md` 第七節「誠實總結」明確聲明**：IS/OOS Calmar 方向一致（皆為正）不能視為策略被嚴謹驗證的證據，只能視為「用一組高度敏感於參數選擇的設定跑出的單一次觀察」。

## 學到什麼

- **MTM 權益曲線重建的 off-by-one 陷阱（可遷移的具體工程教訓）**：`signals.py` 為防 look-ahead 把訊號欄（t 根）與成交欄（t+1 根開盤）分開存放。後續重建逐根 mark-to-market 權益曲線時，若直接套用部門既有的 `macd-adx-fib-strategy` 專案 `metrics.py` 的 `build_mtm_equity_curve`（該寫法假設 entry_ts 本身就是實際成交根），會產生 off-by-one 錯誤。修法是先做「entry_ts（訊號根 t）→ +1 找到實際成交根」的映射，再用成交根重建逐根持倉方向序列；用手算 7 根 K 棒的合成範例與全歷史 942 筆交易雙重驗證，MTM 總和與已實現損益總和誤差為 0.0 才過關。**通則：兩個獨立專案即使用同一套「防 look-ahead」設計哲學，內部欄位語義（entry_ts 記的是訊號根還是成交根）未必相同，移植別的專案的 reconciliation 程式碼前必須先確認兩邊欄位定義是否對得上。**（此教訓已被使用者記入全域 `blindspot-ml-quant.md` 教訓紀錄區）
- **夜盤時段錨點不能用「trade_date-1天」**：實測發現在跨週末時（如 trade_date=週一，其夜盤實際落在週五晚上）該固定錨點會產生 39.75 萬筆負 offset；改用時鐘時間分支判斷（>=15:00 用當天日期、否則用前一日曆日）後驗證通過。
- **年化係數不能用全歷史單一常數**：TX 夜盤 2017-05-15 才上線，2011-2016 每年約 1220-1250 根（僅日盤）、2018 起每年約 4500-4670 根（日盤+夜盤），相差約 3.7 倍；若用單一全歷史平均常數會讓 IS（混合兩種頻率）與 OOS（純夜盤時代）兩段的年化 Sharpe/CAGR 都套錯係數，改為每個評估期間用自己實際的「根數/年數」計算。

## 關聯概念
[[technical-indicators]]、[[sharpe-ratio]]、[[backtest-overfitting-and-validation]]（概念頁尚未建立，見本批 ingest log 說明）

## 關聯頁面
[[macd-adx-fibonacci-futures-strategy]]、[[adx-regime-switching-donchian-bollinger-strategy]]、tmba-quant-trading-department-sessions
