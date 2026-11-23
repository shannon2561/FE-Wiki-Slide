# MACD、ADX 與費波那契回撤台指期策略（消融實驗）

**類型**：project  
**期間**：2026-08（v1 消融實驗 2026-08-11 ~ 08-22；v2 純 MACD+ADX 獨立版與 v3 純多單版 2026-08-23 ~ 08-27）  
**情境**：self-study（量化交易社團自主開發，比照社團成果發表的簡報格式）  
**原始檔**：TMBA\程交部\專案\macd-adx-fib-strategy  
**技術棧**：Python（pandas、numpy）、Jupyter Notebook（`jupyter nbconvert --execute`）、自製單元測試（`test_*.py`，本機無 pytest，直接執行）

---

## 目標

以 ADX 判斷趨勢強弱、MACD 決定進出場方向，設計台指期（TX 大台，60 分 K，僅日盤）的波段策略。主體為消融實驗 (ablation)：以同一套回測引擎開發不含費波那契回撤濾網的 base 版，以及含濾網、訊號確立後等待拉回才進場的 Fib 版，檢驗「趨勢確認後等拉回進場，能否改善風險調整後報酬」。不論 Fib 版較好、較差或無差異，皆可作為結論。

## 方法與架構

- 共用引擎：MACD (12/26/9) 與 ADX／DMI（Wilder，週期 14）；訊號於第 t 根收盤產生、第 t+1 根開盤成交；持倉跨越換月 (`is_roll`) 時另扣一次轉倉成本。出場邏輯（`generate_exit_triggers`、`simulate_trades`）由兩版共用同一份程式碼，確保消融實驗只有進場規則不同。
- Fib 版進場：以 Fractal 樞紐點法偵測波段高低點，左右各 N 根皆較高或較低才成立，右側須延遲 N 根才能使用，以避免未來函數；訊號有效期間內觸及 0.382、0.5、0.618 其中一位（含容忍帶）才進場，下一根開盤市價成交。
- 樣本切分：樣本內 (IS) 2008-01-01 至 2019-12-31（含 2008 年空頭），樣本外 (OOS) 2020-01-01 至 2025-12-31，只跑一次。兩版各自於 IS 獨立優化，base 版僅 1 維（ADX 進場門檻），Fib 版 3 維（ADX 進場門檻 × 波段回看期 × Fib 位）。進入 OOS 前先寫定比較判準，共 6 條，包括以 Calmar Ratio 為主判準、交易數少於 30 視為不可信、差距在 ±10% 內視為平手。
- 三個版本：v1 為 base 與 Fib 的消融實驗主體；v2（`code/ver2/`）將 v1 判定較優的純 MACD+ADX（不含 Fib）獨立包裝為單一策略，自原始 1 分 K 重新完整執行；v3（`code/ver3/`）為依要求製作的純多單版本，動工前已說明此屬 hindsight bias 情境。
- 每個版本皆打包為可從頭執行到尾的單一 Jupyter Notebook，已以 `jupyter nbconvert --execute --inplace` 實際執行且無錯誤，並抽查多組關鍵數字與對應 csv、報告核對一致。

## 結果

依 `implementation-notes.md` 記載的 `code/ver1/oos_out/`、`code/ver2/oos_out/`、`code/ver3/oos_out/` 實際輸出：

1. v1 消融結果（OOS 2020–2025，只跑一次）：
   - base 版：200 筆交易，Calmar −0.0549（CAGR −5.98%、MDD 108.9%、打 8 折的 event-driven Sharpe −0.3409），獲利因子 0.940。
   - Fib 版：96 筆交易，Calmar 為 NaN（OOS 期間淨值一度轉負，複利公式無實數解），獲利因子僅 0.487；成本 ×0、×1、×2 三種情境下 MDD 皆高於 base 版（155–181% 對 107–121%）。
   - 結論：Fib 版在樣本外全面劣於 base 版。逐年損益 6 年全數虧損，base 版尚有 2024 年大賺抵銷其他年度；多空拆解兩邊皆虧。Fib 版的問題主要來自平均單筆虧損擴大（−87.5 點，base 版為 −7.0 點），而非僅是獲利變少。
   - 兩版 MDD 皆超過 100 萬本金：以固定 1 口、本金 100 萬計，base 版 MDD 為 107–121%，Fib 版為 155–181%，代表歷史路徑上保證金會被打爆。改以 500 萬本金計算，統計量才回到可解讀的範圍（base MDD 22.8%、打 8 折 Sharpe −0.034；Fib MDD 33.9%、打 8 折 Sharpe −0.677）。
2. v2（純 MACD+ADX，多空皆做，獨立重跑）：OOS 200 筆交易，CAGR −5.98%、MDD 108.9%、Calmar −0.0549，與 v1 base 版逐一比對，數字完全一致至浮點數精度，確認獨立重跑的管線正確。
3. v3（純多單）：IS 選出的 ADX 進場門檻為 26（v2 為 20）；OOS 116 筆交易，勝率 42.24%，獲利因子 1.071，CAGR +3.21%、MDD 40.50%、Calmar +0.0793、打 8 折 Sharpe +0.2078，四項主要指標由 v2 的全面為負轉為全面為正。然而此結果不構成獨立驗證：v1、v2 已用同一段 2008–2025 資料觀察到「多單持續獲利、空單持續虧損」，v3 是在已看過答案的資料上拿掉已知虧損的空單，即 v1 事先明文禁止的「事後拔除空單模組重報」的變體；notebook 與 `implementation-notes.md` 皆已明顯標註此限制。

## 學到什麼

- 防範 hindsight bias：v1 分析時即事先寫下「空單大概率難看，須如實拆解呈現，不得事後拔除空單模組重報」。v3 開工前，即使是主動要求製作純多單版，仍先說明此即為該禁令描述的情境，因 2008–2025 的資料已被 v1、v2 用過，沒有乾淨資料可做獨立測試。數字最終大幅轉正，仍於報告與 notebook 中標註「不構成已驗證的結論」，未因結果好看而降低揭露標準。
- 測試階段發現的實際 bug：(1) `macd_crosses` 布林 Series 經 `.shift(1)` 填入 NaN 後變成 object dtype，對其中的 Python bool 取 `~` 成為位元 NOT（`~True == -2`）而非邏輯反相，導致交叉判定全錯；(2) `compute_adx` 在完全無波動、`smoothed_tr` 恰為 0（而非 NaN）時，方向性指標應定義為 0，原寫法誤判為除以 0 而產生 NaN。
- 固定本金的假設會扭曲風險統計量：以 100 萬本金、固定 1 口逐根計算 mark-to-market 權益曲線時，部分日期的權益接近或跌破 0，日報酬率出現數千 % 的離群值，年化波動、Sharpe 與 Beta 皆失真；改以 500 萬本金計算才回到合理範圍。MDD 的分母為歷史高點而非前一日權益，不受此影響，故 MDD 超過 100% 仍為有效且重要的發現。

## 關聯概念

[[technical-indicators]]、[[sharpe-ratio]]、[[backtest-overfitting-and-validation]]

## 關聯頁面

[[rsi-overbought-oversold-futures-strategy]]、[[adx-regime-switching-donchian-bollinger-strategy]]
