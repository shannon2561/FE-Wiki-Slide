# Technical Indicators（技術指標）

## 定義

以公式量化價格趨勢、動能與波動的指標。常見者包括移動平均線 (MA) 與指數移動平均 (EMA)；MACD，`MACD = EMA12 − EMA26`、`Signal = EMA9(MACD)`；隨機指標 KD，`%D = SMA3(%K)`，以 80／20 為超買超賣門檻；平均真實範圍 ATR，常用於動態停損；平均方向指數 ADX，以 DI+ 與 DI− 判斷趨勢強弱與方向；費波那契回撤，比例為 23.6%、38.2%、50%、61.8%、78.6%。

---

## 在知識庫中的出現

- **[[ridge-xgboost-stock-return-prediction]]**：特徵包括動能類 (`mom_1`、`mom_3`、`mom_6`、`mom_12`) 與波動率類 (`vol_1m`、`vol_3m`、`vol_6m`、`vol_12m`)，屬於同一族的價格衍生統計量，而非傳統的圖表型指標。
- **[[macd-adx-fibonacci-futures-strategy]]**：結合 MACD、ADX 與費波那契回撤的台指期策略。
- **[[rsi-overbought-oversold-futures-strategy]]**：以 RSI 超買超賣為訊號的台指期策略。
- **[[adx-regime-switching-donchian-bollinger-strategy]]**：以 ADX 判斷趨勢強弱，在唐奇安突破（趨勢）與布林均值回歸（盤整）兩套子系統之間切換。
- **[[volatility-squeeze-breakout]]**：以 ATR 與已實現波動率 (RV) 判斷波動壓縮後的突破。
- **[[bollinger-trend-vs-reversion]]**：以布林通道分別設計順勢與逆勢兩種策略並對照。

---

## 關聯概念

[[momentum]]（動能類特徵與動能效應的量化定義部分重疊）
