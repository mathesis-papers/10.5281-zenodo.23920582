# Precise statements and proofs

The source uses one counter for its five results: Theorem 1, Lemma 2, Corollaries 3–5. We prove the tool lemma first. All written arguments follow [Haobo Ma and Wenlin Zhang, version 1](https://doi.org/10.5281/zenodo.23920583).

## Conventions and the original question

$A^*$ denotes conjugate transpose, $M[S,S]$ selects rows and columns in increasing order, and $\lambda(M)$ lists eigenvalues with algebraic multiplicity. Define

$$
e_k(t_1,\ldots,t_n)=\sum_{|S|=k}\prod_{i\in S}t_i,
\qquad e_0=1.
$$

Empty products and determinants are $1$. The Jordan product has no factor $1/2$. We first separate the positive semidefinite, one-sided special case of Corollary 3.

::: {.theorem #mo-positive title="Malkoun’s original inequality" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s3" lean="D5/S3/Quantum/Matrix/MalkounJordanElementary.result"}
Let $n\geq1$ and let $X,Y\in\mathbb C^{n\times n}$ be positive semidefinite Hermitian matrices. For every integer $1\leq k\leq n$,

$$
e_k(\lambda(XY+YX))\leq e_k(\lambda(X^2+Y^2)).
$$
:::

The [public Lean proof](lean:D5/S3/Quantum/Matrix/MalkounJordanElementary.result) rewrites symmetric functions as sums of principal minors, then bounds each minor on one side. The written proof below obtains the stronger modulus bound; that stronger statement is outside the formal result above.

## Tool: Gram determinants

::: {.lemma #gram-bound title="Gram determinant bound" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s2" status="written-proof" proof="pf-gram-bound" doi="10.5281/zenodo.23920583" source="Lemma 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/179"}
For nonnegative integers $m,k$ and $U,V\in\mathbb C^{m\times k}$,

$$
|\det(U^*V)|^2\leq\det(U^*U)\det(V^*V).
$$
:::

::: {.proof #pf-gram-bound}
For each row set $T\subseteq\{1,\ldots,m\}$ of size $k$, put $u_T=\det U[T,:]$ and $v_T=\det V[T,:]$. Cauchy–Binet gives

$$
\begin{aligned}
\det(U^*V)&=\sum_{|T|=k}\overline{u_T}v_T,\\
\det(U^*U)&=\sum_{|T|=k}|u_T|^2,\\
\det(V^*V)&=\sum_{|T|=k}|v_T|^2.
\end{aligned}
$$

In the product determinant expansion, repeated intermediate rows give zero; group the other terms by their row set to obtain these identities. Apply ordinary Cauchy–Schwarz to the complex lists $(u_T)_T,(v_T)_T$. If $k>m$, insufficient column rank makes all three determinants zero. If $k=0$, the single empty minor and all three determinants are $1$. No invertibility assumption is needed.
:::

The existing [formal Cauchy–Binet statement](lean:D5/S3/Quantum/Schatten/CompoundMatrices.cauchyBinet) is reusable: it is a determinant-of-product identity, not the whole inequality of this lemma.

## Main theorem: rectangular matrices

::: {.theorem #rectangular-bound title="Rectangular Jordan bounds" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s1" status="written-proof" proof="pf-rectangular-bound" doi="10.5281/zenodo.23920583" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/180"}
Let $p,n\geq1$, $A,B\in\mathbb C^{p\times n}$, and put

$$
\begin{aligned}
H&=A^*B+B^*A,\\
R&=A^*A+B^*B.
\end{aligned}
$$

For every $S\subseteq\{1,\ldots,n\}$,

$$
|\det H[S,S]|\leq\det R[S,S].
$$

Consequently, for every $0\leq k\leq n$,

$$
\begin{aligned}
|e_k(\lambda(H))|&\leq\sum_{|S|=k}|\det H[S,S]|,\\
\sum_{|S|=k}|\det H[S,S]|&\leq e_k(\lambda(R)).
\end{aligned}
$$
:::

::: {.proof #pf-rectangular-bound}
Fix $S$, put $k=|S|$, and let $A_S,B_S$ be the selected $p\times k$ column matrices. Form the $2p\times k$ matrices

$$
U=\begin{pmatrix}A_S\\B_S\end{pmatrix},\qquad
V=\begin{pmatrix}B_S\\A_S\end{pmatrix}.
$$

Direct multiplication gives

$$
\begin{aligned}
U^*U=V^*V&=R[S,S],\\
U^*V&=H[S,S].
\end{aligned}
$$

The [Gram lemma](#gram-bound) yields $|\det H[S,S]|^2\leq(\det R[S,S])^2$. As a Gram matrix, $R[S,S]$ is positive semidefinite and has nonnegative determinant. Taking nonnegative square roots proves the principal-minor bound. For the empty set this reads $1\leq1$.

For any square matrix $M$ of size $n$, expand $I+tM$ column by column: choose $tM$ columns on $S$ and identity columns elsewhere. The contribution is $t^{|S|}\det M[S,S]$. Grouping by set size gives

$$
\det(I+tM)=\sum_{k=0}^n t^k\sum_{|S|=k}\det M[S,S].
$$

On the other hand, factoring the characteristic polynomial with algebraic multiplicity gives

$$
\det(I+tM)=\prod_{i=1}^n(1+t\lambda_i(M)).
$$

The coefficient of $t^k$ in the product is $e_k(\lambda(M))$. This is a polynomial identity requiring neither invertibility nor diagonalizability. Compare coefficients to obtain the principal-minor identity. Here $H,R$ are Hermitian, so their eigenvalues and principal determinants are real. Apply the triangle inequality to the sum, then the principal-minor bound to each term, to obtain the two inequalities.

At $k=0$ all quantities are $1$. If $k>2p$, insufficient rank makes the relevant minors zero. Singular matrices, zero columns and repeated eigenvalues are covered directly; there is no perturbation or limiting passage.
:::

## Hermitian specialization

::: {.corollary #hermitian-bound title="Arbitrary Hermitian inputs" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s3" status="written-proof" proof="pf-hermitian-bound" doi="10.5281/zenodo.23920583" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/180"}
Let $n\geq1$ and let $X,Y\in\mathbb C^{n\times n}$ be arbitrary Hermitian matrices. For every $0\leq k\leq n$,

$$
|e_k(\lambda(XY+YX))|\leq e_k(\lambda(X^2+Y^2)).
$$

In particular, positive semidefinite inputs satisfy Malkoun’s original one-sided inequality.
:::

::: {.proof #pf-hermitian-bound}
In the [main theorem](#rectangular-bound), take $p=n,A=X,B=Y$. Hermiticity gives $X^*=X,Y^*=Y$, hence $H=XY+YX$ and $R=X^2+Y^2$. The original one-sided bound also uses $a\leq|a|$ for real $a$. This direct specialization shares its parent’s formalization task; the [original question](#mo-positive) above separately displays the exact existing formal evidence.
:::

## Determinant polynomial and equality

::: {.corollary #determinant-bound title="Polynomial bound and simultaneous equality" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s4" status="written-proof" proof="pf-determinant-bound" doi="10.5281/zenodo.23920583" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/181"}
With $A,B,H,R$ as in the main theorem, for every $z\in\mathbb C$,

$$
|\det(I+zH)|\leq\det(I+|z|R).
$$

Moreover,

$$
\begin{aligned}
|\det H|&\leq\det R,\\
\operatorname{tr}R-\operatorname{tr}H&=\|A-B\|_F^2.
\end{aligned}
$$

Equality in all one-sided inequalities $e_k(\lambda(H))\leq e_k(\lambda(R))$, $1\leq k\leq n$, holds simultaneously if and only if $A=B$.
:::

::: {.proof #pf-determinant-bound}
The coefficient expansion in the main proof and the triangle inequality give

$$
\begin{aligned}
|\det(I+zH)|&\leq\sum_{k=0}^n|z|^k|e_k(\lambda(H))|,\\
&\leq\sum_{k=0}^n|z|^k e_k(\lambda(R))\\
&=\det(I+|z|R).
\end{aligned}
$$

$R$ is positive semidefinite, so the coefficients on the right are nonnegative. The determinant bound is the case $k=n$. Also $R-H=(A-B)^*(A-B)$, whose trace is the sum of the squared moduli of all entries, the squared Frobenius norm. If all one-sided equalities hold, $k=1$ forces this sum to vanish, hence every entry is zero and $A=B$. Conversely, $A=B$ makes $H=R$, giving all one-sided equalities. At $z=0$ the polynomial bound is $1=1$; zero matrices are included. This is not an equality classification for an individual coefficient or for all absolute-value equalities.
:::

## A commuting three-matrix result

::: {.corollary #commuting-schur title="Commuting Schur siblings" mathesis="collected:malkoun-2026-mo512579-jordan-elementary:1:s5" status="written-proof" proof="pf-commuting-schur" doi="10.5281/zenodo.23920583" source="Corollary 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/182"}
Let $A,B,C\in\mathbb C^{n\times n}$ be pairwise commuting positive semidefinite Hermitian matrices, $n\geq1$, and define

$$
\begin{aligned}
S&=A+B+C,\\
Q&=A^2+B^2+C^2,\\
F&=6(A^3+B^3+C^3)+S^3.
\end{aligned}
$$

Then $\det F\geq5^n\det S\det Q$. For every $0\leq k\leq n$, $e_k(\sigma(F))\geq e_k(\sigma(5SQ))$, where $\sigma$ lists singular values with multiplicity; also

$$
e_k(\lambda(2F))\geq e_k(\lambda(5SQ+5QS)).
$$
:::

::: {.proof #pf-commuting-schur}
Finite-dimensional Hermitian matrices are unitarily diagonalizable. Pairwise commutation makes the eigenspaces of each invariant under the others; diagonalizing within those spaces gives a common unitary eigenbasis. It suffices to compare the nonnegative entries $a,b,c$ at each diagonal position. Put $s=a+b+c$, $q=a^2+b^2+c^2$, and $f=6(a^3+b^3+c^3)+s^3$. By symmetry arrange $a\geq b\geq c\geq0$. Direct expansion gives

$$
\begin{aligned}
f-5sq=2\bigl(& (a-b)^2(a+b-c)\\
&+c(a-c)(b-c)\bigr).
\end{aligned}
$$

Since $a+b-c\geq0$ and the other factors are nonnegative, $f\geq5sq\geq0$. This holds at every diagonal position. Multiply over any fixed index set and sum to obtain the $e_k$ inequalities; the full product gives the determinant bound. For positive semidefinite diagonal matrices singular values are these nonnegative entries, and unitary transformations preserve them. Finally $SQ=QS$, so $5SQ+5QS=10SQ$; scaling both $F$ and $5SQ$ by two gives the last assertion. For $k=0$ the empty products agree, and zero entries need no division. This proof is independent of the two-matrix theorem but uses commutation.
:::

## Literature boundary

The question and earlier work are credited in the [story’s sources](README.md#sources-and-a-concrete-way-to-contribute). The related [MO answer 492315](https://mathoverflow.net/a/492315), [MO 180293](https://mathoverflow.net/questions/180293), and River Li’s [Math.SE 4726142](https://math.stackexchange.com/questions/4726142) involve different three-matrix expressions. Only the commuting cases above are proved here, not the noncommuting versions or the proposed rank-one reduction. The formal source is fixed by the [book pin](trureturing:); each written extension’s contribution route is its adjacent shared request.

<section hidden="hidden">

```{=typst}
#pagebreak()
```

</section>
