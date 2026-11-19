# 把平方差的直觉带进矩阵

对两个实数，$2xy\leq x^2+y^2$，因为右边减左边是 $(x-y)^2$。把数换成矩阵后，还能比较它们的“乘积总和”吗？Haobo Ma 与 Wenlin Zhang 的这篇论文回答了 Malkoun 在 MathOverflow 512579 第一问中的问题：可以，而且即使混合项出现负特征值，仍能控制这些总和的绝对值。

最重要的结论可以先用一句话说清：对任意同阶 Hermitian 矩阵 $X,Y$，从 $XY+YX$ 的特征值中每次选 $k$ 个相乘，再把所有选择相加，其绝对值不超过对 $X^2+Y^2$ 做同样计算的结果。这里 $0\leq k\leq n$，$n$ 是矩阵的阶数。证明不需要把两个矩阵同时变成对角矩阵；它把列上下堆叠，用熟悉的 Cauchy–Schwarz 不等式比较行列式。

## 从小方阵认识问题

矩阵是一张按规则相乘的数表。实对称矩阵满足 $X_{ij}=X_{ji}$；Hermitian 矩阵允许复数，条件变为 $X_{ij}=\overline{X_{ji}}$，横线表示复共轭。后者的特征值都是实数。若存在非零向量 $v$ 满足 $Mv=\lambda v$，就称 $\lambda$ 是特征值：沿这个方向，矩阵只作伸缩。一个 $n$ 阶 Hermitian 矩阵有 $n$ 个实特征值，重复的也要计入。

“正半定”表示 $v^*Xv\geq0$ 对每个复向量 $v$ 都成立；星号表示转置再取复共轭。对 Hermitian 矩阵，这等价于所有特征值非负。可以把它理解为一个永不输出负数的二次式。原问题要求 $X,Y$ 都正半定，但它们的混合项不一定如此。

看论文中的例子：

$$
X=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Y=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
$$

二次式分别是 $|v_1|^2$ 与 $|v_1+v_2|^2$，所以二者都正半定。按矩阵乘法计算，得到

$$
\begin{aligned}
H=XY+YX&=\begin{pmatrix}2&1\\1&0\end{pmatrix},\\
R=X^2+Y^2&=\begin{pmatrix}3&2\\2&2\end{pmatrix}.
\end{aligned}
$$

$H$ 的行列式是 $-1$，因此它的两个实特征值一正一负。正半定输入没有保证正半定输出。$R$ 的行列式则是 $2$。这时仅比较行列式的大小，$-1\leq2$ 很宽松；论文还得到更有力的 $|-1|\leq2$。

## “每次选几个相乘”是什么意思？

对三个数 $a,b,c$，可以记录

$$
\begin{aligned}
e_1(a,b,c)&=a+b+c,\\
e_2(a,b,c)&=ab+ac+bc,\\
e_3(a,b,c)&=abc.
\end{aligned}
$$

这些就是初等对称函数；规定 $e_0=1$。对矩阵的特征值使用同样的规则：$e_1$ 是迹，即对角元之和；$e_n$ 是行列式；中间的 $e_k$ 记录各种 $k$ 项乘积的总和。研究它们，就同时研究了迹、行列式以及二者之间的一整套量。

上面的二维例子只有两项需要比较：

$$
\begin{aligned}
|e_1(\lambda(H))|=2&\leq5=e_1(\lambda(R)),\\
|e_2(\lambda(H))|=1&\leq2=e_2(\lambda(R)).
\end{aligned}
$$

不必先解出特征值。这里 $\lambda(M)$ 表示 $M$ 的全部特征值列表，按重数计算。一般结论为

$$
|e_k(\lambda(XY+YX))|\leq e_k(\lambda(X^2+Y^2)).
$$

论文采用的 Jordan 乘积是 $XY+YX$，没有乘 $1/2$。这个约定影响每一个 $k$ 次齐次量，不能省略。

## 为什么直接用平方差还不够？

恒等式仍成立：

$$
R-H=(X-Y)^2.
$$

Hermitian 矩阵的平方是正半定的，故它能解释一部分单向比较。但 $H$ 本身可能有负特征值；要控制对称总和的绝对值，需要能处理符号抵消的方法。论文选用主子式：选出同一组行和列，取出一个小方阵，再算它的行列式。例如二维时，选第一行列给出 $H_{11}$，选全部行列给出 $\det H$。

关键桥梁是

$$
e_k(\lambda(M))=\sum_{|S|=k}\det M[S,S].
$$

$S$ 是选中的下标集合；$M[S,S]$ 是相应主子矩阵。这个等式把特征值问题变成很多小行列式的问题。它来自同一个多项式的两种展开：一方面 $\det(I+tM)$ 的 $t^k$ 系数是所有 $k$ 阶主子式之和，另一方面是 $e_k(\lambda(M))$。完整推导见[精确陈述与证明](statements.md)。

## 核心动作：堆叠，再交换

论文实际上允许 $A,B$ 是任意复数长方形矩阵，有 $p$ 行、$n$ 列。先定义

$$
\begin{aligned}
H&=A^*B+B^*A,\\
R&=A^*A+B^*B.
\end{aligned}
$$

固定一组列 $S$，记选出的列为 $A_S,B_S$。上下堆叠成两张有 $2p$ 行的数表：

$$
U=\begin{pmatrix}A_S\\B_S\end{pmatrix},\qquad
V=\begin{pmatrix}B_S\\A_S\end{pmatrix}.
$$

交换上下两块，没有改变每列的长度或列与列之间的内积。所以

$$
U^*U=V^*V=R[S,S],
$$

而交叉相乘给出 $U^*V=H[S,S]$。形如 $U^*U$ 的矩阵叫 Gram 矩阵，它收集各列两两的内积。一个实向量版本的画面是：取实数 $a,b$，令 $u=(a,b)$、$v=(b,a)$ 长度相同，内积为 $2ab$；Cauchy–Schwarz 给出 $|2ab|\leq a^2+b^2$。堆叠矩阵把同一个动作推广到了多列。

多列版本是 Gram 行列式不等式：

$$
|\det(U^*V)|^2\leq\det(U^*U)\det(V^*V).
$$

它也来自普通 Cauchy–Schwarz：用 Cauchy–Binet 展开后，把 $U$ 的所有选行行列式排成一列数，把 $V$ 的对应行列式排成另一列数，再对两列数使用 Cauchy–Schwarz。两个 Gram 矩阵相同，右边便是同一个非负数的平方，于是

$$
|\det H[S,S]|\leq\det R[S,S].
$$

最后先用三角不等式，把“总和的绝对值”放大到“绝对值的总和”，再对每一项使用刚才的界。这是整篇论文的推理主线：**选列 → 交换堆叠 → 比较小行列式 → 相加得到特征值结论**。令 $A=X,B=Y$，Hermitian 条件就把星号消去，回到开头的问题。所有步骤都是有限代数运算；奇异矩阵、零列和重特征值都包含在内，不需要扰动或取极限。

这部短片按同一条主线展示例子和堆叠动作，英文旁白配中英字幕。

::: {.film src="001-stacked-gram"}
从二维负行列式的例子走到交换堆叠的证明机制。
:::

## 能得到什么，又在哪里停下？

把各阶系数放回多项式，还得到对每个复数 $z$ 的界：

$$
|\det(I+zH)|\leq\det(I+|z|R).
$$

另外 $\operatorname{tr}R-\operatorname{tr}H=\|A-B\|_F^2$，其中 Frobenius 范数平方是所有矩阵元模平方之和。因此，所有单向等式 $e_k(\lambda(H))=e_k(\lambda(R))$（$1\leq k\leq n$）同时成立，当且仅当 $A=B$；只用 $k=1$ 就能证明必要性。这不是每个单独系数的等号分类。例如 $A=-B\ne0$ 也会令绝对值界全部取等，却不满足 $A=B$。

论文还讨论三个矩阵的一个邻近问题，但只证明两两可交换的情形。可交换使它们能在同一组坐标下同时对角化，问题降成非负数 $a,b,c$ 的 Schur 型不等式；[推论与完整证明](statements.md#commuting-schur)给出确切公式。这与两矩阵主结果的普遍性不同。论文没有解决这些三矩阵式子的非交换版本，也没有给出把任意标量不等式一律“提升”为矩阵不等式的规则。

正式报告沿同样的例子、主子式和堆叠路径展开，并在附录保留边界与证据范围。

::: {.slides src="seminar"}
中英文逐帧对应的学术 Beamer 报告，附讲者备注。
:::

## 来源与可继续推进的工作

本解读依据 Haobo Ma、Wenlin Zhang 的版本 1 论文，[DOI:10.5281/zenodo.23920583](https://doi.org/10.5281/zenodo.23920583)，CC BY 4.0。Haobo Ma 的机构为 Chrono AI，Singapore；Wenlin Zhang 的机构为 NUS 与 Chrono AI，Singapore。保留作者的原记录姓名。

问题来自 Malkoun（Joseph Malkoun），[MathOverflow 512579，revision 1](https://mathoverflow.net/questions/512579)，2026 年 6 月 24 日。J. K. Merikoski 与 A. Virtanen 在 [1992 年论文](https://doi.org/10.21136/cmj.1992.128332)中研究了正规矩阵和与积的初等对称谱函数。本文的方法利用经典的 Cauchy–Binet 与 Cauchy–Schwarz。论文另直接引用 cubesteak 于 2026 年 8 月 26 日在 [MO answer 514685](https://mathoverflow.net/a/514685) 对不同的、满足 $A+B+C=I$ 的三矩阵行列式问题所给的先前证明。

[公开 Lean 源码](lean:D5/S3/Quantum/Matrix/MalkounJordanElementary.result)证明的是原问题：正半定 Hermitian 输入、$n>0$、$1\leq k\leq n$、不带绝对值的单向不等式。下一章把它单独陈述，并将更广的纸面结论与之区分。若想参与形式化，可从 [Gram 行列式界](https://github.com/the-omega-institute/trureturing-requests/issues/179)、[长方形推广及 Hermitian 特化](https://github.com/the-omega-institute/trureturing-requests/issues/180)、[行列式多项式与同时等号](https://github.com/the-omega-institute/trureturing-requests/issues/181)、或独立的[可交换 Schur 情形](https://github.com/the-omega-institute/trureturing-requests/issues/182)选择一个明确范围，复用已有的 Cauchy–Binet 结果，并按共享请求中的贡献路径提交。
