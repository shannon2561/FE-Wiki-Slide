# Capturing Risk Premia in the Taiwanese Market: A Characteristic-Free Approach

**類型**：journal  
**作者**：[[vincent-kendro]]、Ching-Ting Lin、Kuei-Feng Tsai、Shun-Fa Wu  
**年份**：2025  
**期刊**：SSRN preprint（政大金融系）  
**原始檔**：raw/journals/Capturing_Risk_Premia_in_the_Taiwanese_Market.md

---

## 核心問題

傳統特徵基礎因子模型（Fama-French）有「factor zoo」與資料探勘疑慮。  
這篇問：**不靠任何公司特徵，純粹用統計方法，能不能在台灣股市抓到系統性風險溢酬？**

---

## 方法

### 主要方法：[[risk-premium-pca|RP-PCA]]

- 由 [[lettau-martin]]、[[pelger-markus]]（2020）提出，是 [[principal-component-analysis|PCA]] 的改良版
- 在目標函數加入**橫截面定價誤差項**（超參數 γ）
  - γ = -1：等同傳統 PCA
  - γ = 10 或 20：強調橫截面風險溢酬

### 對照方法：Convex-NMF
- 天生非負限制，相當於內建放空約束
- 與 RP-PCA 比較

### 投資組合權重調整

| 策略 | 說明 |
|------|------|
| 放空限制（Long-only） | 負權重歸零後重新正規化 |
| 130/30 策略 | 130% 做多 + 30% 放空 |
| 波動率標準化 | 各因子暴露於相同風險水準 |

### 資料
- TEJ 資料庫，2007–2023，873 週，911 家上市公司
- 每週取**交易量前 100 名**（聚焦流動性）
- 滾動窗口 T = 13、26、52 週

---

## 主要發現

| 方法 | 年化 [[sharpe-ratio\|Sharpe Ratio]] |
|------|------|
| 等權重基準（EW top-100） | 0.54 |
| RP-PCA (γ=10, T=13) 第一因子 | **0.82** |
| RP-PCA + 130/30 第一因子 | **0.84**（最優） |
| Convex-NMF 第一因子 | 0.49（低於基準） |

- γ 從 -1 → 10：SR 從 0.54 大幅提升至 0.82；γ 再升至 20 改善有限
- **短窗口（T=13）優於長窗口**：台灣股市結構變化快
- **3–5 個因子最佳**：太多因子引入雜訊
- 放空限制與 130/30 對第 2–5 因子改善顯著（隱性正規化）
- 波動率標準化效果不穩定

### 因子回歸
RP-PCA 因子主要被傳統特徵因子解釋（α 均不顯著）：
- 第一因子：市場(+)、規模(+)、[[momentum|動能]](+)、短期反轉(-)
- 第二因子：市場(+)、規模(+)、短期反轉(+)

→ RP-PCA **重新組合**現有風險來源，並非創造新的超額報酬

---

## 關聯概念

[[risk-premium-pca]]、[[principal-component-analysis]]、[[factor-models]]、[[momentum]]、[[sharpe-ratio]]、[[portfolio-optimization]]

## 關聯文獻

[[empirical-asset-pricing-ml]] — 同樣評估統計 vs. 特徵方法，聚焦美國市場  
