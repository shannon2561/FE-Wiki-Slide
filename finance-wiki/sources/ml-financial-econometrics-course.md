# 機器學習與財務計量：政大課程

**類型**：course  
**授課教師**：未確認  
**學期**：未確認（依作業截止日推測為 114 學年度下學期，即 2026 年春季；HW1 截止 2026-04-09、HW2 截止 2026-04-23、Final Project 截止 2026-06-04）  
**原始檔**：機器學習與財務計量（資料夾）

---

## 課程結構

### 講義（講義簡報/Markdown講義/）

| 章節 | 檔名 | 主題 |
|---|---|---|
| 1 | 01_Introduction.md | Risk minimization 架構：迴歸與分類任務的 loss function、條件期望與條件機率、bias-variance trade-off、Kelly criterion 與投資組合權重 |
| 2 | 02_LinearReg.md | 線性迴歸 |
| 3 | 03_CurseDimNN.md | 維度詛咒與最近鄰方法 |
| 4 | 04_PrimerMatrix.md | 矩陣代數基礎 |
| 5 | 05_DimReduc.md | 降維（PCA、PCR、PLS） |
| 6 | 06_Regularization.md | 正則化（Ridge、Lasso、Elastic Net） |
| 7 | 07_Resampling.md | 重抽樣與交叉驗證 |
| 8 | 08_Classification.md | 分類方法 |
| 9 | 09_Splines.md | 樣條函數 |
| 10 | 10_TreeModels.md | 樹模型（含 Boosting、Random Forest） |
| 11 | 11_NeuralNetwork.md | 神經網路 |
| 12 | 12_InterpretableML.md | 可解釋機器學習（含 SHAP） |
| 13 | 13_RNN.md | 遞迴神經網路 |

同一批講義另有 PDF 版（如 `講義簡報\1 Introduction.pdf`），內容與 Markdown 版相同。第 1 章已讀取確認：以 loss function 定義迴歸任務（squared error 對應條件期望）與分類任務（cross-entropy 對應條件機率），並連結至因子投組排序與 Kelly bet sizing 等財務應用；第 2–13 章僅依標題與課程脈絡歸類，未逐章詳讀。

### 範例程式（範例程式/）

- `Example-TreeModels/random_forest.R`：Random Forest 範例，附 BoostingPackageParameters.pdf 參數說明。
- `IML_Plot/ICE_Plot.R`、`IML_Plot/SHAP_plot.R`：繪製 Individual Conditional Expectation 圖與 SHAP 圖。
- `R example-Classification/`：logistic regression 的形狀、marginal effects 計算與 ROC/AUC 繪製。
- `R example-Neural Network/`：Perceptron、單層與多層神經網路。
- `R example-Regularization/`：LARS path、Lasso path、Lasso 一致性與標準化 Lasso。

### 作業

**HW1**（截止 2026-04-09）：給定訓練與測試兩期的股票報酬與預測變數。(1) 對訓練集進行 PCA，分別以 2-fold CV、AIC、Onatski criterion 決定主成分個數；(2) 以所選主成分估計 PCR；(3) 以 PLS 估計單成分模型；(4) 於測試集計算各模型的 RMSE 並比較。

**HW2**（截止 2026-04-23）：沿用 HW1 資料，以報酬 ≤ −10% 定義「崩盤」標籤，若訓練集沒有此類樣本，則改以下四分位數為門檻。(1) 以 5-fold CV 選擇 λ，估計 Lasso 與 Ridge 分類模型，並與 scaled／square-root Lasso（理論 λ）比較混淆矩陣、precision、recall、F1 與選中的變數；(2) 改以 F1-score 選擇 λ；(3) 討論類別不平衡問題，以 oversampling、SMOTE 或 class-weight 其中一種方法重新估計並比較。

**Final Project**（截止 2026-06-04）：見專案頁 [[ridge-xgboost-stock-return-prediction]]。

### 例題與模擬考

- `例題/Mock_Exam.pdf`（2026-05-07）：題目包括 Ridge 高 λ 的 bias-variance 判斷、異質變異數是否造成係數偏誤、PCR 與 PLS 的差異、Random Forest 如何降低樹之間的相關、vanishing gradient 的成因與解法、給定 OLS 係數手算 Lasso 與 Ridge 收縮後的係數、稀有事件分類為何以 PR 曲線優於 ROC 曲線，以及特徵高度相關時 Partial Dependence Plot 是否仍為無偏估計。
- `例題/ML 25 Exam.pdf`：內容未開啟確認。

### 推薦論文（推薦論文/）

- `hhaa009.pdf`：Gu, Kelly & Xiu (2020), *Empirical Asset Pricing via Machine Learning*，已收錄為 [[empirical-asset-pricing-ml]]，不重複建檔。
- `ssrn-5476348.pdf`：Vincent, Lin, Tsai & Wu (2025), *Capturing Risk Premia in the Taiwanese Market*，比對作者與內容後，與 [[capturing-risk-premia-taiwan]] 為同一篇，不重複建檔。
- `principal-component-analysis.pdf`、`llmwiki.pdf`：內容未開啟確認，留待之後 ingest。

### 上課錄音

`上課錄音/` 內共 32 個 `.m4a` 檔（含子資料夾 `drive-download-20260505T185856Z-3-001/` 的重複或額外錄音），涵蓋 2/26、3/5、3/12、3/19、3/26、4/9、4/23、4/30、5/28 等課次，尚未處理。其中 5/28 已有逐字稿（`上課錄音/5-28逐字稿/` 內 4 個 .txt 檔），4/23 與 4/30 有對應的 PDF 講義，皆尚未讀取。

---

## 主要概念

課程以 risk minimization 貫穿迴歸與分類，由線性模型（含正則化、降維）逐步延伸至非線性模型（樣條、樹、神經網路、RNN），最後納入可解釋機器學習（SHAP、ICE）。講義與作業多處連結財務應用，包括投組排序、Kelly criterion 押注比例、崩盤事件分類，以及以 expanding window 預測股票報酬。

## 關聯概念

[[machine-learning-asset-pricing]]、[[neural-networks]]、[[principal-component-analysis]]、[[regularization]]

## 關聯文獻

[[empirical-asset-pricing-ml]]、[[capturing-risk-premia-taiwan]]

## 關聯頁面

[[ridge-xgboost-stock-return-prediction]]
