# Factor Models（因子模型）

## 定義

資產定價因子模型試圖用一組共同因子解釋資產橫截面報酬的差異。從 CAPM 的單一市場因子，到 Fama-French 系列的多因子模型，再到統計因子方法。

---

## 主要發展脈絡

| 模型 | 因子 | 特色 |
|------|------|------|
| CAPM | 市場超額報酬 | 單一系統風險 |
| Fama-French 3-factor (1993) | 市場、規模（SMB）、帳面市值比（HML） | 特徵基礎 |
| Fama-French 5-factor (2015) | 上述 + 獲利能力（RMW）、投資（CMA） | 延伸特徵 |
| q-factor 模型 (Hou et al.) | 市場、規模、投資、獲利能力 | 投資驅動 |
| 統計因子（PCA/RP-PCA） | 由資料萃取，無預設特徵 | [[risk-premium-pca]]、[[principal-component-analysis]] |

---

## Factor Zoo 問題

Harvey et al. (2016) 指出學術界有數百個被宣稱顯著的因子，存在嚴重的資料探勘疑慮。這是 [[machine-learning-asset-pricing]] 和 [[risk-premium-pca]] 興起的背景之一。

---

## 在知識庫中的出現

- **[[empirical-asset-pricing-ml]]**：用 920 個因子預測股票報酬，代表因子動物園的極端；ML 方法用來從中選擇有效因子
- **[[capturing-risk-premia-taiwan]]**：批評特徵基礎因子的資料探勘問題，改用統計因子（RP-PCA）；因子迴歸顯示 RP-PCA 因子可被傳統特徵因子部分解釋
- **[[investments-course]]**：Fama-French 三因子模型作為 IVOL（[[idiosyncratic-volatility]]）分析的迴歸自變數
- **[[ivol-fama-french-analysis]]**：同上，專案層級的實際應用（2330 台積電 IVOL = 0.00298）
- **[[dia-course-114-1]]**：第 11 週教授 CAPM、APT 與多因子模型；期末考資料夾內有疑似 Fama-French 三因子（`ff3`）相關檔案，內容未開啟確認
- **[[factor-investing-project]]**：TMBA 程交部因子投資專案，目前僅完成方向與資料來源規劃、尚未動工，無實作數字可報
- **[[quant-factor-mining-methodology]]**：業界因子挖掘實務流程（窮舉/遺傳演算法/AI 挖掘、IC 篩選、監控衰退速率），與本頁學術脈絡角度不同但主題相關

---

## 台灣市場特有發現

[[capturing-risk-premia-taiwan]] 的 8 因子迴歸（市場、規模、HML、RMW、CMA、動能、短期反轉、長期反轉）顯示：
- 台灣市場期間，成長股優於價值股（HML、RMW 為負）
- 規模效應顯著
- RP-PCA 的 γ 越高，[[momentum|動能]] 因子捕捉越強

---

## 關聯概念

[[machine-learning-asset-pricing]]、[[risk-premium-pca]]、[[principal-component-analysis]]、[[momentum]]、[[sharpe-ratio]]、[[portfolio-optimization]]
