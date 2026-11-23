# Multi-Agent Review（多代理協作與跨模型驗證）

## 定義

由不同模型分別擔任規劃與驗證，而非以同一模型搭配不同 prompt。同一模型負責規劃又負責驗證時，規劃階段的盲點在驗證階段往往仍看不出來 (self-review bias)；由不同公司、不同訓練資料的模型驗證，才能得到較獨立的第二意見。驗證又可依互動方式分為兩種：Plan-Advisor 為諮詢模式，可反駁並經多輪討論取得共識；Impl-Validator 為守門模式，只判定 PASS 或 FAIL。兩者的互動節奏與結束條件不同，共用同一個 session 或 prompt 會造成角色混淆。

---

## 在知識庫中的出現

- **[[harness-wiki-llm]]**：以 Claude 規劃、Codex 驗證，設計演進記錄於 ADR-0002（驗證代理選用 Codex，而非同一模型家族）、ADR-0003（拆分 Plan-Advisor 與 Impl-Validator）、ADR-0006（重試上限統一為 3 輪）與 ADR-0007（審查標準加入基線錨定）。

---

## 關聯概念

[[llm-knowledge-base-architecture]]（同一專案的另一項設計主題）
