# Exponential & Natural Logarithm（指數與自然對數）

## 定義

- **指數函數** $e^x$：自然常數 $e\approx2.718$ 的 $x$ 次方。連續複利下，1 元以年利率 $r$ 成長 $T$ 年後為 $e^{rT}$ 元。
- **自然對數** $\ln x$：指數的反運算，回答「$e$ 要幾次方才會等於 $x$」。$\ln(e^x)=x$，$e^{\ln x}=x$。
- 常用性質：$\ln1=0$；$x$ 大於 1 時 $\ln x$ 為正，小於 1 時為負；$\ln(ab)=\ln a+\ln b$，故乘法可轉為加法。
- **對數報酬率**：$\ln(S_T/S_0)$，衡量股價由 $S_0$ 變為 $S_T$ 的報酬；股價上漲時為正、下跌時為負，且可直接相加（見 [[return-rate]]）。

## 例子

- 一期二元樹中，股價由 20 元漲至 22 元，對數報酬率為 $\ln(22/20)=0.0953$。
- 連續複利 3 個月的成長倍數 $e^{0.03}=1.0305$，取自然對數即回到 $0.03$（見 [[discounting-continuous-compounding]]）。
- Black-Scholes 公式中的 $\ln(S/K)$ 衡量目前股價高於履約價多少。$S=K=100$ 時 $\ln(S/K)=\ln1=0$，故 $d_1=\frac{(0.05+0.02)\times1}{0.2}=0.35$（見 [[fe-03-black-scholes-formula]]）。

## 在知識庫中的出現

- [[black-scholes-model]]、[[fe-03-black-scholes-formula]]：$d_1$、$d_2$ 中的 $\ln(S/K)$。
- [[heat-equation-method]]、[[fe-06-bs-pde-derivation]]：變數轉換 $x=\ln\frac SK+(r-\frac12\sigma^2)\tau$。
- [[geometric-brownian-motion]]、[[fe-02-stock-dynamics-ito]]：習題 4 推導 $\ln S$ 的變動過程。
- [[discounting-continuous-compounding]]：$e^{-rT}$ 為連續複利的折現因子。

## 關聯概念

[[discounting-continuous-compounding]]、[[return-rate]]、[[black-scholes-model]]

## 來源說明

定義為數學基礎知識的整理；例子的數字依 [[fe-01-options-binomial-tree]] 與 [[fe-03-black-scholes-formula]] 的例題以 Python 重算。
