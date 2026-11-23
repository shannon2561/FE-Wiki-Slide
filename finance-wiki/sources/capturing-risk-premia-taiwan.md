# Capturing Risk Premia in the Taiwanese Market: A Characteristic-Free Approach

**類型**：journal  
**作者**：[[vincent-kendro]]、Ching-Ting Lin、Kuei-Feng Tsai、Shun-Fa Wu  
**年份**：2025  
**期刊**：SSRN preprint（政大金融系）  
**原始檔**：raw/journals/Capturing_Risk_Premia_in_the_Taiwanese_Market.md

---

## 核心問題

以公司特徵建構的因子模型（如 Fama-French）有 factor zoo 與資料探勘的疑慮。此文探討：不使用任何公司特徵、僅以統計方法，能否在台灣股市捕捉系統性的風險溢酬。

---

## 方法

1. **主要方法：[[risk-premium-pca|RP-PCA]]**：由 [[lettau-martin]] 與 [[pelger-markus]] (2020) 提出，為 [[principal-component-analysis|PCA]] 的改良，在目標函數中加入以 γ 加權的橫截面定價誤差項。γ = −1 時等同傳統 PCA，γ = 10 或 20 時偏重橫截面風險溢酬。
2. **對照方法：Convex-NMF**：本身具非負限制，相當於內建放空限制。
3. **權重調整**：放空限制 (Long-only) 將負權重歸零後重新正規化；130/30 策略為 130% 做多、30% 放空；波動率標準化使各因子暴露於相同風險水準。
4. **資料**：TEJ 資料庫，2007–2023 年，共 873 週、911 家上市公司；每週取成交量前 100 名以確保流動性；滾動窗口 T 為 13、26、52 週。

---

## 主要發現

| 方法 | 年化 [[sharpe-ratio\|Sharpe Ratio]] |
|------|------|
| 等權重基準 (EW top-100) | 0.54 |
| RP-PCA (γ = 10, T = 13) 第一因子 | 0.82 |
| RP-PCA 搭配 130/30，第一因子 | 0.84（最佳） |
| Convex-NMF 第一因子 | 0.49（低於基準） |

- γ 由 −1 提高至 10，SR 由 0.54 升至 0.82；γ 再提高至 20，改善有限。
- 短窗口 (T = 13) 優於長窗口，推測原因在於台灣股市的結構變化較快。
- 3–5 個因子最佳，因子過多會引入雜訊。
- 放空限制與 130/30 策略對第 2–5 因子的改善明顯，具隱性正則化效果；波動率標準化的效果則不穩定。
- 因子迴歸顯示，RP-PCA 因子主要可由傳統特徵因子解釋，α 皆不顯著。第一因子與市場、規模、[[momentum|動能]]正相關，與短期反轉負相關；第二因子與市場、規模、短期反轉正相關。可見 RP-PCA 是重新組合既有的風險來源，並未創造新的超額報酬。

---

## 關聯概念

[[risk-premium-pca]]、[[principal-component-analysis]]、[[factor-models]]、[[momentum]]、[[sharpe-ratio]]、[[portfolio-optimization]]

## 關聯文獻

[[empirical-asset-pricing-ml]]：同樣比較統計方法與特徵方法，以美國市場為對象。
