# 衍生性金融商品：政大課程（113-1）

**類型**：course  
**課程代碼**：1141_302045001  
**學期**：113-1（2025 秋季）  
**平台**：NCCU Moodle  
**原始檔**：raw/courses/衍生性金融商品_簡報索引.md、raw/courses/衍生性金融商品_講義.md

---

## 課程結構

### 主要章節

| 章節 | 主要內容 |
|------|---------|
| 第一章 | [[derivatives\|衍生性商品]]簡介：期貨、遠期、選擇權、交換 |
| 第二章 | 期貨市場結構與定價 |
| 第三章 | 選擇權基本性質與界限 |
| 第四章 | 選擇權交易策略 |
| 第六章 | 二項式樹 (Binomial Tree) 定價 |
| 第九章 | Black-Scholes-Merton 模型 |
| 第十章 | 希臘字母 (Greeks) 與避險 |
| 第十一章 | 波動度微笑與隱含波動度 |

### 補充教材

| 主題 | 重點 |
|------|------|
| Financial Engineering | 衍生性商品交易實務分享 |
| Binomial Tree Call Option | 二項式樹選擇權定價實作 |
| 股價動態過程 | 布朗運動與幾何布朗運動 |
| BS 訂價公式 | Black-Scholes 公式推導 |
| BS 模型與 BS 選擇權定價 | BSM 架構 |
| Merton 模型（含股息） | 考量連續股息的選擇權定價 |
| Black 模型 | 期貨選擇權定價 |
| 期末報告案例（`衍生性商品/上學期/期末報告/oy09-ch-ts.pdf`） | 瑞銀「每日觀察記憶式提前出場固定配息連結股票」產品說明書（Autocallable/Memory Coupon Equity-Linked Note，代號 OY09，2025/01/07 印製，風險等級 5，不保本），為[[structured-notes|結構型商品]]的真實案例 |

---

## 定價架構

[[derivatives]] 課程的主要定價方法依序為：

1. 無套利定價原則：界限條件與平價關係。
2. 二項式樹：風險中立機率與多期定價。
3. BSM 模型：由幾何布朗運動推導 Black-Scholes 公式。
4. Greeks：Delta 避險。
5. 隱含波動度：波動度微笑與 Skew。

---

## 與其他來源的連結

[[fe-01-options-binomial-tree]]（四上財工講義 01）延續第六章的二項樹，進一步說明風險中立機率、複製與動態 Delta 避險。

> 學期標註疑義：raw 檔內文寫「113-1（2025 秋季）」，但 113 學年度第 1 學期應為 2024 年秋季，可能為民國年與西元年換算錯誤；既有標註未修改，待確認。

---

## 關聯概念

[[derivatives]]、[[portfolio-optimization]]、[[black-scholes-model]]、[[structured-notes]]
