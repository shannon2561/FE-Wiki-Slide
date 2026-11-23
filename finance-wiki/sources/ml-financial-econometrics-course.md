# 機器學習與財務計量 — 政大課程

**類型**：course
**授課教師**：未確認
**學期**：未確認（依作業繳交日期推測為 114 學年度下學期／2026 年春季，HW1 截止 2026-04-09、HW2 截止 2026-04-23、Final Project 截止 2026-06-04）
**原始檔**：機器學習與財務計量（資料夾）

---

## 課程結構

### 講義（Markdown 版，講義簡報/Markdown講義/）

| 週次/章節 | 檔名（相對路徑：機器學習與財務計量\講義簡報\Markdown講義\） | 主題 |
|---|---|---|
| 1 | 01_Introduction.md | Risk minimization 框架：迴歸／分類任務的 loss function、條件期望與條件機率、bias-variance trade-off、Kelly criterion 與投資組合權重 |
| 2 | 02_LinearReg.md | 線性迴歸 |
| 3 | 03_CurseDimNN.md | 維度詛咒與最近鄰方法 |
| 4 | 04_PrimerMatrix.md | 矩陣代數基礎 |
| 5 | 05_DimReduc.md | 降維（PCA/PCR/PLS 一類） |
| 6 | 06_Regularization.md | 正則化（Ridge／Lasso／Elastic Net） |
| 7 | 07_Resampling.md | 重抽樣與交叉驗證 |
| 8 | 08_Classification.md | 分類方法 |
| 9 | 09_Splines.md | 樣條函數 |
| 10 | 10_TreeModels.md | 樹模型（含 Boosting／Random Forest） |
| 11 | 11_NeuralNetwork.md | 神經網路 |
| 12 | 12_InterpretableML.md | 可解釋機器學習（含 SHAP） |
| 13 | 13_RNN.md | 遞迴神經網路 |

同一批講義另有對應 PDF 簡報版（機器學習與財務計量\講義簡報\1 Introduction.pdf 等），內容與上表 Markdown 版一致，未重複列出。第 1 章內容經實際讀取確認：以 loss function 定義 regression（squared error → 條件期望）與 classification（cross-entropy → 條件機率）任務，並連結到因子投組排序與 Kelly bet sizing 等財務應用。第 2–13 章僅由標題與課程脈絡歸類主題，未逐章詳讀內文。

### 範例程式（範例程式/）

- `Example-TreeModels/random_forest.R`：Random Forest 範例（含 BoostingPackageParameters.pdf 參數說明）
- `IML_Plot/ICE_Plot.R`、`IML_Plot/SHAP_plot.R`：Individual Conditional Expectation 圖與 SHAP 圖繪製
- `R example-Classification/`：logistic regression 形狀、marginal effects 計算、ROC/AUC 繪製
- `R example-Neural Network/`：Perceptron、單層／多層神經網路範例
- `R example-Regularization/`：LARS path、Lasso path、Lasso 一致性、標準化 Lasso

### 作業

**HW1**（機器學習與財務計量\作業\HW1，截止 2026-04-09）：給定訓練/測試兩期股票報酬與預測變數，(1) 對訓練集做 PCA，以 2-fold CV、AIC、Onatski criterion 三種方法各自決定主成分數；(2) 用所選主成分估計 PCR；(3) 用 PLS 估計單成分模型；(4) 在測試集用四個模型（PCR 對應的最多 3 組 + PLS）算 RMSE 並比較。

**HW2**（機器學習與財務計量\作業\HW2，截止 2026-04-23）：沿用 HW1 資料，定義「崩盤」二元標籤（報酬 ≤ -10%，若訓練集無此樣本則改用下四分位數為門檻）。(1) 用 5-fold CV 選 λ 估計 Lasso／Ridge 分類模型，並與 scaled/square-root Lasso（理論 λ）比較混淆矩陣、precision/recall/F1 與選中變數；(2) 改以 F1-score 選 λ；(3) 討論訓練/測試集的類別不平衡問題，套用 oversampling／SMOTE／class-weight 其中一種方法重估模型並比較前後結果。

**Final Project**（截止 2026-06-04）：完整內容見專案頁 [[ridge-xgboost-stock-return-prediction]]。

### 例題／模擬考

- `例題/Mock_Exam.pdf`（2026-05-07）：考題涵蓋 Ridge 高 λ 的 bias-variance 判斷、異質變異數是否造成迴歸係數偏誤、PCR 與 PLS 的差異、Random Forest 如何去相關化樹之間的關聯、vanishing gradient 問題與解法、給定 OLS 係數後手算 Lasso/Ridge 收縮後的係數、稀有事件分類為何 PR 曲線優於 ROC 曲線、Partial Dependence Plot 在特徵高度相關時是否仍為無偏估計。
- `例題/ML 25 Exam.pdf`：檔案存在，未開啟確認內容。

### 推薦論文（推薦論文/）

- `hhaa009.pdf` = Gu, Kelly & Xiu (2020), *Empirical Asset Pricing via Machine Learning*, Review of Financial Studies — **本篇已存在於 wiki**，見 [[empirical-asset-pricing-ml]]，不重複建檔。
- `ssrn-5476348.pdf` = Vincent, Lin, Tsai & Wu (2025), *Capturing Risk Premia in the Taiwanese Market: A Characteristic-Free Approach*（RP-PCA 應用於台股）— 經比對作者與內容，**與 wiki 既有的 [[capturing-risk-premia-taiwan]] 為同一篇論文**，不重複建檔。
- `principal-component-analysis.pdf`、`llmwiki.pdf`：存在於資料夾，本次未開啟確認內容（標題與課程主題相符，留待後續 ingest 批次處理）。

### 上課錄音

`上課錄音/` 資料夾內共 32 個 `.m4a` 錄音檔（含子資料夾 `drive-download-20260505T185856Z-3-001/` 內的重複/額外錄音），涵蓋 2/26、3/5、3/12、3/19、3/26、4/9、4/23、4/30、5/28 等課次，本次批次 ingest **未處理**。其中 5/28 課程已有逐字稿（`上課錄音/5-28逐字稿/` 內 4 個 .txt 檔，含「老師補充.txt」），以及 4-23、4-30 課程有對應的 PDF 講義（`4-23 機器學習與財務計量1.pdf`、`4-30 機器學習與財務計量1.pdf`），這些逐字稿與講義 PDF 同樣未展開讀取。

---

## 核心概念

課程以「risk minimization」統一框架貫穿迴歸與分類任務，逐步從線性模型（含正則化、降維）過渡到非線性模型（樣條、樹、神經網路、RNN），並在最後納入可解釋機器學習（SHAP、ICE）。多處講義與作業明確連結財務應用：投組排序、Kelly criterion 押注比例、資產崩盤事件分類、股票報酬預測的 expanding window 架構。

## 關聯概念

[[machine-learning-asset-pricing]]、[[neural-networks]]、[[principal-component-analysis]]、[[regularization]]

## 關聯文獻

[[empirical-asset-pricing-ml]]、[[capturing-risk-premia-taiwan]]

## 關聯頁面

[[ridge-xgboost-stock-return-prediction]]
