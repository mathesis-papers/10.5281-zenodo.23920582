# 精确陈述与证明

本章保留原文共用计数器下的五项结果：Theorem 1、Lemma 2、Corollaries 3–5。为便于推理，先证明引理。纸面论证均依据 [Haobo Ma、Wenlin Zhang 的版本 1 论文](https://doi.org/10.5281/zenodo.23920583)。

## 约定与原问题

$A^*$ 是共轭转置，$M[S,S]$ 按递增顺序选取行列；$\lambda(M)$ 按代数重数列出特征值。定义

$$
e_k(t_1,\ldots,t_n)=\sum_{|S|=k}\prod_{i\in S}t_i,
\qquad e_0=1.
$$

空乘积、空行列式均为 $1$。Jordan 乘积不含 $1/2$。下面单独陈述推论 3 的正半定单向特例。

::: {.theorem #mo-positive title="Malkoun 的原不等式" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s3" lean="D5/S3/Quantum/Matrix/MalkounJordanElementary.result"}
设 $n\geq1$，$X,Y\in\mathbb C^{n\times n}$ 为正半定 Hermitian 矩阵。对每个整数 $1\leq k\leq n$，

$$
e_k(\lambda(XY+YX))\leq e_k(\lambda(X^2+Y^2)).
$$
:::

[公开 Lean 证明](lean:D5/S3/Quantum/Matrix/MalkounJordanElementary.result)把对称函数改写成主子式之和，再逐项使用单向界。下面的纸面证明得到更强的模界；它不属于上面形式声明的范围。

## 工具：Gram 行列式

::: {.lemma #gram-bound title="Gram 行列式界" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s2" status="written-proof" proof="pf-gram-bound" doi="10.5281/zenodo.23920583" source="Lemma 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/179"}
对非负整数 $m,k$ 和 $U,V\in\mathbb C^{m\times k}$，

$$
|\det(U^*V)|^2\leq\det(U^*U)\det(V^*V).
$$
:::

::: {.proof #pf-gram-bound}
对含 $k$ 个元素的行集合 $T\subseteq\{1,\ldots,m\}$，令 $u_T=\det U[T,:]$、$v_T=\det V[T,:]$。Cauchy–Binet 给出

$$
\begin{aligned}
\det(U^*V)&=\sum_{|T|=k}\overline{u_T}v_T,\\
\det(U^*U)&=\sum_{|T|=k}|u_T|^2,\\
\det(V^*V)&=\sum_{|T|=k}|v_T|^2.
\end{aligned}
$$

展开乘积的行列式时，重复选行的项为零；其余项按选行集合分组，得到这些恒等式。对两列复数 $(u_T)_T,(v_T)_T$ 使用普通 Cauchy–Schwarz 即得结论。若 $k>m$，列秩不足，三个行列式均为零；若 $k=0$，只有一个空子式，三个行列式均为 $1$。无需可逆性假设。
:::

可复用已有的 [Cauchy–Binet 形式声明](lean:D5/S3/Quantum/Schatten/CompoundMatrices.cauchyBinet)；它是乘积行列式的恒等式，不是本引理的整个不等式。

## 主定理：长方形矩阵

::: {.theorem #rectangular-bound title="长方形 Jordan 界" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s1" status="written-proof" proof="pf-rectangular-bound" doi="10.5281/zenodo.23920583" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/180"}
设 $p,n\geq1$，$A,B\in\mathbb C^{p\times n}$，并令

$$
\begin{aligned}
H&=A^*B+B^*A,\\
R&=A^*A+B^*B.
\end{aligned}
$$

对每个 $S\subseteq\{1,\ldots,n\}$，

$$
|\det H[S,S]|\leq\det R[S,S].
$$

因此对每个 $0\leq k\leq n$，

$$
\begin{aligned}
|e_k(\lambda(H))|&\leq\sum_{|S|=k}|\det H[S,S]|,\\
\sum_{|S|=k}|\det H[S,S]|&\leq e_k(\lambda(R)).
\end{aligned}
$$
:::

::: {.proof #pf-rectangular-bound}
固定 $S$，令 $k=|S|$，$A_S,B_S$ 是选出的 $p\times k$ 列矩阵。构造 $2p\times k$ 矩阵

$$
U=\begin{pmatrix}A_S\\B_S\end{pmatrix},\qquad
V=\begin{pmatrix}B_S\\A_S\end{pmatrix}.
$$

直接相乘得到

$$
\begin{aligned}
U^*U=V^*V&=R[S,S],\\
U^*V&=H[S,S].
\end{aligned}
$$

[Gram 引理](#gram-bound)给出 $|\det H[S,S]|^2\leq(\det R[S,S])^2$。$R[S,S]$ 是 Gram 矩阵，正半定，行列式非负；取非负平方根即得主子式界。空集也包含在内，此时为 $1\leq1$。

对任意 $n$ 阶方阵 $M$，在 $I+tM$ 中逐列展开：$S$ 上取 $tM$ 列，其余位置取单位矩阵列，留下 $t^{|S|}\det M[S,S]$。按集合大小收集得

$$
\det(I+tM)=\sum_{k=0}^n t^k\sum_{|S|=k}\det M[S,S].
$$

另一方面，特征多项式按代数重数分解，给出

$$
\det(I+tM)=\prod_{i=1}^n(1+t\lambda_i(M)).
$$

乘积的 $t^k$ 系数就是 $e_k(\lambda(M))$。这是多项式恒等式，不要求 $M$ 可逆或可对角化。比较系数，即得主子式恒等式。此处 $H,R$ 均 Hermitian，特征值与主子式均为实数。对总和用三角不等式，再逐项用主子式界，便得到定理中的两步不等式。

$k=0$ 时均为 $1$；$k>2p$ 时相关矩阵秩不足，子式均为零。奇异矩阵、零列和重特征值直接包含在证明中，没有扰动或取极限。
:::

## Hermitian 特化

::: {.corollary #hermitian-bound title="任意 Hermitian 输入" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s3" status="written-proof" proof="pf-hermitian-bound" doi="10.5281/zenodo.23920583" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/180"}
设 $n\geq1$，$X,Y\in\mathbb C^{n\times n}$ 为任意 Hermitian 矩阵。对每个 $0\leq k\leq n$，

$$
|e_k(\lambda(XY+YX))|\leq e_k(\lambda(X^2+Y^2)).
$$

特别地，正半定输入满足 Malkoun 原来的单向不等式。
:::

::: {.proof #pf-hermitian-bound}
在[主定理](#rectangular-bound)取 $p=n,A=X,B=Y$。Hermitian 条件给出 $X^*=X,Y^*=Y$，所以 $H=XY+YX$、$R=X^2+Y^2$。原单向界再使用实数 $a\leq|a|$。此直接特化与主定理共享形式化工作；上面的[原问题](#mo-positive)单独展示已有精确形式证据。
:::

## 行列式多项式与等号

::: {.corollary #determinant-bound title="多项式界与同时等号" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s4" status="written-proof" proof="pf-determinant-bound" doi="10.5281/zenodo.23920583" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/181"}
沿用主定理的 $A,B,H,R$。对每个 $z\in\mathbb C$，

$$
|\det(I+zH)|\leq\det(I+|z|R).
$$

此外，

$$
\begin{aligned}
|\det H|&\leq\det R,\\
\operatorname{tr}R-\operatorname{tr}H&=\|A-B\|_F^2.
\end{aligned}
$$

所有单向等式 $e_k(\lambda(H))=e_k(\lambda(R))$（$1\leq k\leq n$）同时成立，当且仅当 $A=B$。
:::

::: {.proof #pf-determinant-bound}
由主定理证明中的系数展开与三角不等式，

$$
\begin{aligned}
|\det(I+zH)|&\leq\sum_{k=0}^n|z|^k|e_k(\lambda(H))|,\\
&\leq\sum_{k=0}^n|z|^k e_k(\lambda(R))\\
&=\det(I+|z|R).
\end{aligned}
$$

$R$ 正半定，右边的系数非负。行列式界是 $k=n$ 的情形。又有 $R-H=(A-B)^*(A-B)$，其迹是各矩阵元模平方之和，即 Frobenius 范数平方。若所有单向等式成立，$k=1$ 即使该平方和为零，所以每个元素均为零，$A=B$。反之 $A=B$ 给出 $H=R$，所有单向等式成立。$z=0$ 时多项式界为 $1=1$；零矩阵也包括在内。这不是单个系数或所有绝对值等号的分类。
:::

## 可交换的三矩阵结果

::: {.corollary #commuting-schur title="可交换 Schur 推论" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s5" status="written-proof" proof="pf-commuting-schur" doi="10.5281/zenodo.23920583" source="Corollary 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/182"}
设 $A,B,C\in\mathbb C^{n\times n}$ 是两两可交换的正半定 Hermitian 矩阵，$n\geq1$，并定义

$$
\begin{aligned}
S&=A+B+C,\\
Q&=A^2+B^2+C^2,\\
F&=6(A^3+B^3+C^3)+S^3.
\end{aligned}
$$

则 $\det F\geq5^n\det S\det Q$。对每个 $0\leq k\leq n$，$e_k(\sigma(F))\geq e_k(\sigma(5SQ))$，其中 $\sigma$ 列出按重数计算的奇异值；并且

$$
e_k(\lambda(2F))\geq e_k(\lambda(5SQ+5QS)).
$$
:::

::: {.proof #pf-commuting-schur}
有限维 Hermitian 矩阵可酉对角化。两两可交换使每个矩阵的特征空间被其他矩阵保留，在这些空间内继续对角化，便得到共同的酉对角基。于是只需比较每个位置的非负对角元 $a,b,c$。令 $s=a+b+c$、$q=a^2+b^2+c^2$、$f=6(a^3+b^3+c^3)+s^3$。由对称性可重排为 $a\geq b\geq c\geq0$。直接展开：

$$
\begin{aligned}
f-5sq=2\bigl(& (a-b)^2(a+b-c)\\
&+c(a-c)(b-c)\bigr).
\end{aligned}
$$

$a+b-c\geq0$，其余各因子均非负，因此 $f\geq5sq\geq0$。在每个对角位置都有此界。对任意固定的下标集合逐项相乘，再相加，得到各阶 $e_k$ 界；全部相乘得到行列式界。正半定对角矩阵的奇异值就是这些非负对角元，酉变换保留奇异值。最后 $SQ=QS$，所以 $5SQ+5QS=10SQ$；把 $F$ 与 $5SQ$ 同时乘二便得到最后一条结论。$k=0$ 为空乘积等式，零对角元也不需要除法。证明独立于两矩阵主定理，但依赖可交换性。
:::

## 文献边界

问题与先前工作见[故事的来源段](README.md#来源与可继续推进的工作)。[MO answer 492315](https://mathoverflow.net/a/492315)、[MO 180293](https://mathoverflow.net/questions/180293) 以及 River Li 的 [Math.SE 4726142](https://math.stackexchange.com/questions/4726142) 涉及不同的三矩阵表达式。这里仅证明上述可交换情形，不包括其非交换版本或所提秩一约化。当前形式源码由[所钉提交](trureturing:)固定；每项纸面扩展的贡献入口就是结果旁的共享请求。
