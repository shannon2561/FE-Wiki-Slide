# Backtest Overfitting & Validation（回測過擬合防範與驗證方法）

## 定義

回測結果容易高估策略的真實表現，此頁整理兩類工具：一是常見偏誤的檢查清單，二是實際開發策略時用來降低失真的驗證技術。

### 常見偏誤清單

生存者偏誤、參數過多（過度配適）、低估交易成本與滑價、忽略放空成本、未來函數 (look-ahead bias)、忽視樣本外持續虧損、離群值與黑天鵝事件。

### 驗證技術

- **參數高原與參數孤島** (plateau vs isolated peak)：績效在參數空間中呈連續、穩定的區域才可信；單一孤立的高點多為過擬合。
- **One-standard-error rule**：沿用機器學習選擇正則化強度的邏輯，在高原內選較簡單、較保守的參數組合，而非績效最高的單點。
- **多重比較揭露** (multiple comparison disclosure)：如實寫出網格搜尋共測試幾組參數，避免高估結果的顯著性。
- **Walk-forward 滾動驗證**，以及樣本內各子期間的穩定性檢查。
- **未來函數檢查**：截斷未來資料 (truncation) 與竄改未來資料 (perturbation)，若訊號因此改變，代表程式偷看了未來。
- **績效打折**：回測 Sharpe 打 8 折作為實際表現的估計，為社團量化交易實務上的經驗法則。

---

## 在知識庫中的出現

- **[[tmba-trading-dept-quant-intro-preread]]**：預習教材說明 look-ahead bias 與 survivorship bias；教材把兩者的定義寫反，已在來源頁標註。
- **[[macd-adx-fibonacci-futures-strategy]]**：v3 純多單版的樣本外表現遠優於 v2，但 2008–2025 的資料在 v1、v2 已經用過，並非獨立驗證，報告中已揭露此 hindsight bias。
- **[[rsi-overbought-oversold-futures-strategy]]**：36 組參數的網格中找不到穩健高原（離散度 175%），報告明確寫出結果不足以證明策略有效。
- **[[adx-regime-switching-donchian-bollinger-strategy]]**：優化的三個階段皆未通過穩健性門檻，門檻也未因此放寬；並以損益歸因的雙重拆解，排除「切換成本吃掉優勢」的假設。
- **[[volatility-squeeze-breakout]]**：v1 至 v3 的迭代中逐步加入高原判定、one-standard-error rule 與多重比較揭露；v3 提高交易頻率後，正常成本下 Sharpe 趨近 0、壓力成本下轉負，此代價須一併揭露。
- **[[bollinger-trend-vs-reversion]]**：完成後以 12 條盲點清單逐條檢查；並用零成本情境拆開「訊號方向是否正確」與「成本吃掉多少」兩個問題。

---

## 關聯概念

[[technical-indicators]]（此頁的驗證技術主要用於技術指標型策略）、[[quant-factor-mining-methodology]]（因子挖掘同樣面臨多重比較與過擬合）
