# Technical Indicators（技術指標）

## 定義

技術分析中用於量化價格趨勢、動能與波動性的一組公式化指標。常見指標包括：移動平均線（MA）與指數移動平均（EMA）、MACD（`MACD = EMA12 - EMA26`、`Signal = EMA9(MACD)`）、隨機指標 KD（`%K`、`%D = SMA3(%K)`，80/20 超買超賣門檻）、平均真實範圍 ATR（用於動態止損）、平均方向指數 ADX（DI+/DI- 判斷趨勢強弱與方向）、費波那契回調（23.6%/38.2%/50%/61.8%/78.6%）。

---

## 在知識庫中的出現

- **[[ridge-xgboost-stock-return-prediction]]**：特徵工程使用的動量類（`mom_1`/`mom_3`/`mom_6`/`mom_12`）與波動率類（`vol_1m`/`vol_3m`/`vol_6m`/`vol_12m`）特徵，可視為技術指標概念在量化模型中的延伸應用（非傳統圖表型技術指標，而是同一族的價格衍生統計量）
- **[[macd-adx-fibonacci-futures-strategy]]**：MACD、ADX、費波那契回撤三指標組合的台指期策略
- **[[rsi-overbought-oversold-futures-strategy]]**：RSI 超買超賣訊號的台指期策略
- **[[adx-regime-switching-donchian-bollinger-strategy]]**：ADX 判斷趨勢強弱以在唐奇安突破（趨勢）與布林均值回歸（盤整）兩套子系統間切換
- **[[volatility-squeeze-breakout]]**：以 ATR／已實現波動率（RV）判斷波動壓縮後的突破訊號
- **[[bollinger-trend-vs-reversion]]**：布林通道同時用於順勢與逆勢兩種相反邏輯的策略設計對照

---

## 關聯概念

[[momentum]]（動量類特徵與動能效應的量化定義部分重疊）
