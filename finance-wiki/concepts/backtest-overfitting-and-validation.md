# Backtest Overfitting & Validation（回測過擬合防範與驗證方法論）

## 定義

量化策略回測中「識別結果為何可能失真」與「如何設計流程降低失真風險」的方法論工具箱。內容分兩層：學術/社課傳授的通用偏誤清單，與實際專案開發中演化出的具體工程驗證技術。

### 常見偏誤清單（回測七大偏誤）

生存者偏誤、參數過多（過度配適）、交易成本與滑價低估、放空成本忽略、未來函數（look-ahead bias，含資料前視偏誤）、樣本外持續虧損被忽視、離群值／黑天鵝事件。

### 具體驗證技術（工程實踐）

- **參數高原 vs 參數孤島判定**（plateau vs isolated peak）：績效在參數空間中呈連續穩定區域才可信，單一孤立高點多為過擬合假象。
- **One-standard-error rule**：借用機器學習正則化的保守選參邏輯，在高原內選相對簡單/保守的參數組合而非絕對最優點。
- **多重比較揭露**（multiple comparison disclosure）：如實揭露網格搜尋測試過幾組參數，避免忽視資料探勘代價導致高估顯著性。
- **Walk-forward 滾動式驗證**與**樣本內子期間穩定性檢查**。
- **無未來函數驗證法**：截斷未來資料（truncation）與竄改未來資料（perturbation）兩種手法，確認訊號產生邏輯未偷看未來。
- **績效指標打折原則**：回測 Sharpe 建議打 8 折估計實際表現（TMBA 程交部實務經驗法則）。

---

## 在知識庫中的出現

- **[[tmba-trading-dept-quant-intro-preread]]**：預習教材對 look-ahead bias、survivorship bias 的系統講解（教材原始定義互換的錯誤已在來源頁標註）
- **[[macd-adx-fibonacci-futures-strategy]]**：v3 純多單版 OOS 大幅優於 v2 的 hindsight bias 完整自我揭露案例（2008–2025 資料已被 v1/v2 用盡，非獨立驗證）
- **[[rsi-overbought-oversold-futures-strategy]]**：36 組參數網格找不到任何穩健高原（離散度 175%），報告自陳「不構成策略被嚴謹驗證的證據」
- **[[adx-regime-switching-donchian-bollinger-strategy]]**：優化三階段全數未通過穩健性 gate，未悄悄放寬門檻；損益歸因雙重拆解驗證法排除「切換成本吃光優勢」的討喜假說
- **[[volatility-squeeze-breakout]]**：v1→v2→v3 迭代中持續演化的高原判定、one-standard-error rule、多重比較揭露方法論；v3 提高交易頻率的代價（正常成本 Sharpe 趨零、壓力成本轉負）被要求誠實揭露不可片面呈現
- **[[bollinger-trend-vs-reversion]]**：完工後補做全域 blindspot-ml-quant.md 12 條逐條掃描的範例；零成本情境用來拆解「訊號方向對不對」與「成本吃掉多少」

---

## 關聯概念

[[technical-indicators]]（本頁的偏誤防範技術主要應用於技術指標型策略的回測）、[[quant-factor-mining-methodology]]（因子挖掘同樣面臨多重比較與過擬合風險）
