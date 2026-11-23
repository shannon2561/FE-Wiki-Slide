# Factor Models（因子模型）

## 定義

以一組共同因子解釋不同資產之間報酬差異的資產定價模型，從 CAPM 的單一市場因子，發展至 Fama-French 系列的多因子模型，以及由資料萃取的統計因子。

---

## 發展脈絡

| 模型 | 因子 | 特色 |
|------|------|------|
| CAPM | 市場超額報酬 | 單一系統風險 |
| Fama-French 3-factor (1993) | 市場、規模 (SMB)、帳面市值比 (HML) | 以公司特徵建構 |
| Fama-French 5-factor (2015) | 上述三者，加上獲利能力 (RMW)、投資 (CMA) | 延伸特徵 |
| q-factor 模型 (Hou et al.) | 市場、規模、投資、獲利能力 | 以投資理論為基礎 |
| 統計因子 (PCA/RP-PCA) | 由資料萃取，不預設特徵 | 見 [[risk-premium-pca]]、[[principal-component-analysis]] |

---

## Factor Zoo 問題

Harvey et al. (2016) 指出，學術文獻中宣稱顯著的因子已有數百個，資料探勘的疑慮嚴重。[[machine-learning-asset-pricing]] 與 [[risk-premium-pca]] 的發展即與此有關。

---

## 在知識庫中的出現

- **[[empirical-asset-pricing-ml]]**：以 920 個預測變數預測股票報酬，再以 ML 方法從中篩選有效訊號。
- **[[capturing-risk-premia-taiwan]]**：指出以特徵建構因子有資料探勘問題，改用統計因子 (RP-PCA)；因子迴歸顯示 RP-PCA 因子可被傳統特徵因子部分解釋。
- **[[investments-course]]**：以 Fama-French 三因子作為 IVOL（[[idiosyncratic-volatility]]）分析的迴歸自變數。
- **[[ivol-fama-french-analysis]]**：同一份作業的專案頁，2330 台積電的 IVOL 為 0.00298。
- **[[dia-course-114-1]]**：第 11 週教授 CAPM、APT 與多因子模型；期末資料夾內有疑似 Fama-French 三因子 (`ff3`) 的檔案，內容尚未開啟確認。
- **[[factor-investing-project]]**：因子投資專案，目前僅完成方向與資料來源規劃，尚無實作數字。
- **[[quant-factor-mining-methodology]]**：業界的因子挖掘流程（窮舉、遺傳演算法、AI 挖掘、IC 篩選、監控衰退速率），與此頁的學術脈絡互補。

---

## 台灣市場的發現

[[capturing-risk-premia-taiwan]] 以 8 個因子（市場、規模、HML、RMW、CMA、動能、短期反轉、長期反轉）進行迴歸，結果顯示：樣本期間台灣市場成長股優於價值股（HML、RMW 為負），規模效應顯著，且 RP-PCA 的 γ 越高，對[[momentum|動能]]因子的捕捉越強。

---

## 關聯概念

[[machine-learning-asset-pricing]]、[[risk-premium-pca]]、[[principal-component-analysis]]、[[momentum]]、[[sharpe-ratio]]、[[portfolio-optimization]]
