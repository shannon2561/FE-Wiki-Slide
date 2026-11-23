# MACD-ADX-費波那契回撤 台指期策略（消融實驗）

**類型**：project
**期間**：2026-08 ~ 2026-08（v1 消融實驗 2026-08-11~08-22；v2 純多空獨立版與 v3 純多單版 2026-08-23~08-27）
**情境**：self-study（TMBA 程交部自主開發，比照部門 2023 成果發表簡報格式）
**原始檔**：TMBA\程交部\專案\macd-adx-fib-strategy
**技術棧**：Python（pandas、numpy）、Jupyter Notebook（`jupyter nbconvert --execute`）、自製單元測試（`test_*.py`，本機無 pytest，直接執行）

---

## 目標

以 ADX 判斷趨勢強弱、MACD 決定進出場方向，設計台指期（TX 大台，60 分 K，僅日盤）波段策略。**核心是一個消融實驗（ablation）**：用同一套回測引擎同時開發「無費波那契回撤濾網（base）」與「有費波那契回撤濾網（Fib，訊號確立後等拉回進場）」兩個版本，檢驗「趨勢確認後等拉回進場，能否改善風險調整後報酬」這個假說——無論 Fib 版較優、較差或無差異，都設計為可發表結論。

## 方法與架構

- **共用引擎**：MACD(12/26/9) + ADX/DMI(Wilder，週期14)；訊號於 t 根收盤產生、t+1 根開盤成交；持倉跨越換月（`is_roll`）額外扣一次轉倉成本；出場邏輯（`generate_exit_triggers`/`simulate_trades`）由 base 版與 Fib 版**共用同一份程式碼**，落實「消融實驗只讓進場規則有差異」的公平比較前提。
- **Fib 版進場模組**：用 Fractal 樞紐點法（左右各 N 根都更高/更低才成立，右側需延遲 N 根才可用，防未來函數）偵測波段高低點，訊號有效視窗內觸及 0.382/0.5/0.618 其中一位（±容忍帶）才進場，下一根開盤市價成交。
- **樣本切分**：IS 2008-01-01~2019-12-31（含 2008 空頭）、OOS 2020-01-01~2025-12-31（只碰一次）。兩版**各自**在 IS 上獨立優化（base 版僅 1 維：ADX 進場閾值；Fib 版 3 維：ADX 進場閾值×波段回看期×Fib 位），碰 OOS 前白紙黑字預先寫死比較判準（主判準 Calmar Ratio、交易數<30 不可信、±10% 內視為平手等 6 條規則）。
- **三個版本**：
  - **v1**：base vs Fib 消融實驗主體。
  - **v2**（`code/ver2/`）：把 v1 驗證後判定較優的「純 MACD+ADX（無 Fib）」獨立包裝成乾淨的單一策略交付物，從原始 1 分 K 完全獨立重跑一次。
  - **v3**（`code/ver3/`）：使用者要求做「只做多」版本，動工前已明確被告知這是 hindsight bias 情境（見下方「學到什麼」）。
- 每個版本最終都打包成可從頭執行到尾的單一 Jupyter Notebook（`backtest-bundle` skill），皆已用 `jupyter nbconvert --execute --inplace` 實際執行過、零錯誤，並抽查多組關鍵數字與對應 csv/報告逐一核對一致。

## 結果

依據 `implementation-notes.md` 記載的 `code/ver1/oos_out/`、`code/ver2/oos_out/`、`code/ver3/oos_out/` 實際輸出數字：

**v1 消融結果（OOS 2020-2025，只跑一次）**：
- base 版：200 筆交易，Calmar = −0.0549（CAGR −5.98%、MDD 108.9%、Sharpe 打 8 折 event-driven = −0.3409）、獲利因子 0.940
- Fib 版：96 筆交易，Calmar 為 **NaN**（OOS 期間淨值一度轉負，複利公式無實數解）、獲利因子僅 0.487，MDD 在 ×0/×1/×2 三種成本情境下全部高於 base 版（155~181% vs 107~121%）
- **結論：Fib 版在樣本外全面劣於 base 版**——逐年損益 6 年全部虧損（base 尚有 2024 年大賺打平其他年度）、多空拆解兩邊皆虧、Fib 版問題主要來自平均單筆虧損擴大（−87.5 點 vs base −7.0 點），不是單純「贏得少」
- **兩版 MDD 皆超過 100 萬本金**：以固定 1 口＋100 萬本金計，base 版 MDD 達 107~121%、Fib 版達 155~181%，代表歷史路徑上保證金會被打爆；改用 500 萬本金後統計量才回到可解讀量級（base MDD=22.8%、Sharpe 打 8 折=−0.034；Fib MDD=33.9%、Sharpe 打 8 折=−0.677）

**v2（純 MACD+ADX、多空都做，獨立重跑）**：OOS 200 筆交易、CAGR=−5.98%、MDD=108.9%、Calmar=−0.0549——與 v1 base 版逐一比對，數字**完全一致（到浮點數精度）**，確認獨立重跑管線正確。

**v3（純多單）**：IS 選中 ADX 進場閾值=26（與 v2 的 20 不同）；OOS 116 筆交易、勝率 42.24%、獲利因子 1.071、**CAGR=+3.21%、MDD=40.50%、Calmar=+0.0793、Sharpe 打 8 折=+0.2078**——四項核心指標從 v2 的全面為負轉為全面為正。但**此結果不構成獨立驗證**：v1/v2 已用盡同一段 2008-2025 資料觀察到「多單持續獲利、空單持續虧損」，v3 是在同一段已看過答案的資料上重新測試「拿掉已知虧錢的空單」，屬於使用者與本專案自己在 v1 就白紙黑字禁止過的「事後拔空單模組重報」情境的變體，notebook 與 implementation-notes.md 皆已顯著標註此方法論限制。

## 學到什麼

- **Hindsight bias 的自我防線**：v1 分析階段已明文預先寫下「空單大概率難看，誠實拆解呈現，不得事後拔空單模組重報」；v3 開工前，即使使用者主動要求做純多單版本，仍先明確告知這是同一條禁令描述的情境，因為 2008-2025 全部資料已被 v1/v2 用過，沒有乾淨資料可做真正的獨立測試。即使數字最終大幅轉正，仍在報告與 notebook 中如實標註「不構成已驗證的結論」，而非因為結果好看就悄悄降低揭露標準。
- **測試階段抓到的真實 bug**（非事後諸葛）：(1) `macd_crosses` 布林 Series 經 `.shift(1)` 塞入 NaN 後升成 object dtype，對其中的 Python bool 值取 `~` 變成 bitwise NOT（`~True==-2`）而非邏輯反相，導致交叉判定全錯；(2) `compute_adx` 在完全無波動（`smoothed_tr` 恰為 0，非 NaN）時方向性指標應定義為 0，原始寫法誤判成除以 0 產生 NaN。
- **固定本金假設會扭曲風險統計量，不只是策略優劣問題**：以 100 萬本金＋固定 1 口計算逐 bar mark-to-market 權益曲線時，部分日期權益貼近或跨越 0，造成日報酬率出現數千 % 的離群值，年化波動、Sharpe、Beta 全部失真、不可解讀；改用 500 萬本金後統計量才回到合理量級。MDD 本身（分母用歷史高點而非前一日權益）不受此影響，即使在失真的本金設定下 MDD>100% 仍是有效且重要的發現。

## 關聯概念
[[technical-indicators]]、[[sharpe-ratio]]、[[backtest-overfitting-and-validation]]（概念頁尚未建立，見本批 ingest log 說明）

## 關聯頁面
[[rsi-overbought-oversold-futures-strategy]]、[[adx-regime-switching-donchian-bollinger-strategy]]、tmba-trading-dept-2023-showcase、tmba-quant-trading-department-sessions
