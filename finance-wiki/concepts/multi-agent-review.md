# Multi-Agent Review（多代理協作與跨模型驗證）

## 定義

用不同模型（而非同一模型的不同 prompt）分別擔任「規劃」與「驗證」角色，避免同源誤差（self-review bias）——同一模型規劃又驗證，規劃時的盲點在驗證時往往仍看不到，只有跨公司、跨訓練資料、跨對齊取向的模型才能提供真正獨立的第二意見。進一步可依互動節奏拆分兩種驗證模式：**Plan-Advisor**（諮詢協商模式，可反駁、多輪共識）與 **Impl-Validator**（PASS/FAIL 對抗式守門模式），因為兩階段的互動節奏與終局規則本質不同，共用同一 session/prompt 會造成角色錯亂。

---

## 在知識庫中的出現

- **[[harness-wiki-llm]]**：以 Claude 規劃、Codex 作跨模型對抗式驗證，透過 ADR-0002（驗證代理選用 Codex 而非同一模型家族）、ADR-0003（Plan-Advisor / Impl-Validator 兩階段拆分）、ADR-0006（max retry 統一 3 輪）、ADR-0007（引入基線錨定審查標準）記錄設計演進

---

## 關聯概念

[[llm-knowledge-base-architecture]]（同一專案內的另一核心設計主題）
