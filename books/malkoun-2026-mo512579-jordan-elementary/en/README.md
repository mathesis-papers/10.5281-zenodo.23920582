# Bringing the square-difference idea to matrices

For real numbers, $2xy\leq x^2+y^2$ because the difference is $(x-y)^2$. If numbers become matrices, can we still compare their sums of products? This paper by Haobo Ma and Wenlin Zhang answers the first question in Malkoun's MathOverflow 512579: yes. It even controls the absolute value of those sums when the mixed expression has negative eigenvalues.

Here is the answer before the machinery. Take any two Hermitian matrices $X,Y$ of size $n$. Choose $k$ eigenvalues of $XY+YX$, multiply them, and add over every choice. The absolute value of this total is at most the corresponding total for $X^2+Y^2$, for every $0\leq k\leq n$. The proof does not require simultaneous diagonalization. It stacks columns in opposite orders and turns the familiar Cauchy–Schwarz inequality into a determinant bound.

## Meet the question in a small square

A matrix is a table of numbers with a rule for multiplication. A real symmetric matrix satisfies $X_{ij}=X_{ji}$. A Hermitian matrix allows complex entries and satisfies $X_{ij}=\overline{X_{ji}}$, where the bar denotes complex conjugation. Its eigenvalues are real. An eigenvalue $\lambda$ means that $Mv=\lambda v$ for some nonzero vector: along that direction the matrix simply stretches or reverses the vector. An $n$ by $n$ Hermitian matrix has $n$ real eigenvalues, counting repetitions.

Positive semidefinite means $v^*Xv\geq0$ for every complex vector $v$; the star transposes a matrix and conjugates its entries. For Hermitian matrices this says that all eigenvalues are nonnegative. Think of a quadratic expression that never returns a negative number. Malkoun's question assumes both inputs have this property. Their mixed expression need not.

The paper gives this example:

$$
X=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Y=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
$$

Their quadratic expressions are $|v_1|^2$ and $|v_1+v_2|^2$, so both are positive semidefinite. Matrix multiplication gives

$$
\begin{aligned}
H=XY+YX&=\begin{pmatrix}2&1\\1&0\end{pmatrix},\\
R=X^2+Y^2&=\begin{pmatrix}3&2\\2&2\end{pmatrix}.
\end{aligned}
$$

The determinant of $H$ is $-1$, so its two real eigenvalues have opposite signs. Positive inputs have not produced a positive semidefinite mixed expression. The determinant of $R$ is $2$. The one-sided comparison $-1\leq2$ is loose; the paper also proves the stronger bound $|-1|\leq2$.

## What does “choose some and multiply” mean?

For three numbers $a,b,c$, record

$$
\begin{aligned}
e_1(a,b,c)&=a+b+c,\\
e_2(a,b,c)&=ab+ac+bc,\\
e_3(a,b,c)&=abc.
\end{aligned}
$$

These are the elementary symmetric functions, with $e_0=1$. Apply the same rule to a matrix's eigenvalues. Then $e_1$ is the trace, the sum of the diagonal entries; $e_n$ is the determinant. The intermediate quantities collect products of $k$ eigenvalues at a time. One result about all of them therefore includes both trace and determinant comparisons.

Our two-dimensional example has two comparisons:

$$
\begin{aligned}
|e_1(\lambda(H))|=2&\leq5=e_1(\lambda(R)),\\
|e_2(\lambda(H))|=1&\leq2=e_2(\lambda(R)).
\end{aligned}
$$

We did not have to solve for the eigenvalues. Here $\lambda(M)$ lists all eigenvalues with multiplicity. The general conclusion is

$$
|e_k(\lambda(XY+YX))|\leq e_k(\lambda(X^2+Y^2)).
$$

The paper's Jordan product is $XY+YX$, without a factor of $1/2$. This convention matters for every degree-$k$ quantity.

## Why the square difference is only a starting point

The identity survives:

$$
R-H=(X-Y)^2.
$$

The square of a Hermitian matrix is positive semidefinite, explaining part of the one-sided comparison. But $H$ may have negative eigenvalues. To bound the absolute value of a symmetric sum, we need a method that handles cancellation. The paper uses principal minors: choose the same set of row and column indices, extract that small square matrix, and take its determinant. In size two, choosing just the first index gives $H_{11}$; choosing both gives $\det H$.

The bridge is

$$
e_k(\lambda(M))=\sum_{|S|=k}\det M[S,S].
$$

Here $S$ is the chosen index set and $M[S,S]$ its principal submatrix. This converts an eigenvalue problem into many small determinant problems. Expand $\det(I+tM)$ in two ways: its $t^k$ coefficient is both the sum of the order-$k$ principal minors and $e_k(\lambda(M))$. The [precise statements and proofs](statements.md) justify each expansion.

## The decisive move: stack, then swap

The paper permits arbitrary complex rectangular matrices $A,B$, each with $p$ rows and $n$ columns. Define

$$
\begin{aligned}
H&=A^*B+B^*A,\\
R&=A^*A+B^*B.
\end{aligned}
$$

Fix a column set $S$, and call those selected columns $A_S,B_S$. Stack them into two matrices with $2p$ rows:

$$
U=\begin{pmatrix}A_S\\B_S\end{pmatrix},\qquad
V=\begin{pmatrix}B_S\\A_S\end{pmatrix}.
$$

Swapping the two blocks preserves column lengths and all pairwise column inner products. Thus

$$
U^*U=V^*V=R[S,S],
$$

whereas the cross product is $U^*V=H[S,S]$. A matrix $U^*U$ is called a Gram matrix: it records all the pairwise inner products of the columns. For a single real column, picture $u=(a,b)$ and $v=(b,a)$ with real $a,b$. They have the same length and inner product $2ab$. Cauchy–Schwarz gives $|2ab|\leq a^2+b^2$. The stacked matrices make this same move with several columns at once.

The several-column version is the Gram determinant inequality:

$$
|\det(U^*V)|^2\leq\det(U^*U)\det(V^*V).
$$

This too comes from ordinary Cauchy–Schwarz. Cauchy–Binet expands each determinant into a sum involving row minors. List all selected-row determinants of $U$, and do the same for $V$. Apply Cauchy–Schwarz to these two lists. Since the Gram matrices agree, the right side is a single nonnegative number squared, yielding

$$
|\det H[S,S]|\leq\det R[S,S].
$$

Finally, the triangle inequality replaces the absolute value of a sum by the sum of absolute values. Bound each term using the last display. The complete route is **select columns → swap stacked blocks → bound small determinants → sum to recover the spectral quantity**. Taking $A=X,B=Y$ removes the stars by Hermiticity and returns to the opening question. Everything is finite algebra: singular matrices, zero columns and repeated eigenvalues are included, with no perturbation or limiting argument.

The short film follows this example and stacking mechanism, with English narration and aligned English/Chinese subtitles.

::: {.film src="001-stacked-gram"}
From a negative determinant in size two to the swap-the-stacks proof mechanism.
:::

## What follows, and where does it stop?

Put the bounded coefficients back into a polynomial. For every complex number $z$,

$$
|\det(I+zH)|\leq\det(I+|z|R).
$$

Also $\operatorname{tr}R-\operatorname{tr}H=\|A-B\|_F^2$, where the squared Frobenius norm is the sum of the squared moduli of all entries. Hence all the one-sided equalities $e_k(\lambda(H))=e_k(\lambda(R))$, $1\leq k\leq n$, hold together exactly when $A=B$. The case $k=1$ already forces necessity. This does not classify equality in each individual coefficient. For instance, $A=-B\ne0$ gives equality in every absolute-value bound without $A=B$.

The paper also treats a neighboring three-matrix question, under pairwise commutation. Commutation allows simultaneous unitary diagonalization and reduces the problem to a Schur-type inequality for nonnegative numbers $a,b,c$. The [corollary and full proof](statements.md#commuting-schur) give the formulas. This has a narrower domain than the two-matrix result. The paper does not settle the noncommuting versions of those three-matrix inequalities or give a universal rule for promoting arbitrary scalar inequalities to matrices.

The academic presentation follows the same example, principal-minor bridge and stacking argument, with boundary cases and evidence scope in its appendix.

::: {.slides src="seminar"}
Aligned Chinese and English Beamer editions with speaker notes.
:::

## Sources and a concrete way to contribute

This explanation follows version 1 of the paper by Haobo Ma and Wenlin Zhang, [DOI:10.5281/zenodo.23920583](https://doi.org/10.5281/zenodo.23920583), licensed CC BY 4.0. Haobo Ma is affiliated with Chrono AI, Singapore; Wenlin Zhang with NUS and Chrono AI, Singapore. Their recorded names are retained.

The question is due to Malkoun (Joseph Malkoun), [MathOverflow 512579, revision 1](https://mathoverflow.net/questions/512579), 24 June 2026. J. K. Merikoski and A. Virtanen studied elementary symmetric spectral functions of sums and products of normal matrices in their [1992 paper](https://doi.org/10.21136/cmj.1992.128332). The present mechanism uses classical Cauchy–Binet and Cauchy–Schwarz. The paper also credits cubesteak's prior proof, posted on 26 August 2026 in [MO answer 514685](https://mathoverflow.net/a/514685), of a different normalized three-matrix determinant problem with $A+B+C=I$.

The [public Lean source](lean:D5/S3/Quantum/Matrix/MalkounJordanElementary.result) proves the original question: positive semidefinite Hermitian inputs, $n>0$, $1\leq k\leq n$, and the one-sided inequality without absolute values. The next chapter states that result separately from the broader written conclusions. Contributors can choose a focused scope from the shared requests for the [Gram determinant bound](https://github.com/the-omega-institute/trureturing-requests/issues/179), [rectangular extension and Hermitian specialization](https://github.com/the-omega-institute/trureturing-requests/issues/180), [determinant polynomial and simultaneous equality](https://github.com/the-omega-institute/trureturing-requests/issues/181), or the independent [commuting Schur case](https://github.com/the-omega-institute/trureturing-requests/issues/182). Reuse the existing Cauchy–Binet identity and follow the contribution route in the corresponding request.
