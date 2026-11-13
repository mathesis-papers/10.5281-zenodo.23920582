# MathOverflow 512579, revision 1: a Hermitian Jordan-product inequality

Haobo Ma (ChronoAI Pte Ltd, Singapore), followed by Wenlin Zhang
(National University of Singapore; ChronoAI Pte Ltd, Singapore).
License: Creative Commons Attribution 4.0 International, `cc-by-4.0`.

## Result

For arbitrary complex rectangular matrices `A,B` of the same size, put
`H=A*B+B*A` and `R=A*A+B*B`, where `*` denotes conjugate transpose.
For every principal index set `S`, `abs(det H[S,S]) <= det R[S,S]`.
Thus `abs(e_k(lambda(H))) <= e_k(lambda(R))` for every `0 <= k <= n`.
For Hermitian `X,Y`, taking `A=X`, `B=Y` proves the first question in
[MathOverflow 512579, revision 1](https://mathoverflow.net/questions/512579),
and removes the positivity assumption on `X,Y`.

The note also proves `abs(det(I+zH)) <= det(I+abs(z)R)` for every complex `z`,
and characterizes simultaneous equality in the one-sided coefficient
inequalities by `A=B`.
For the linked three-matrix Schur questions, it also proves every stated
determinant, singular-value and symmetrized eigenvalue inequality in the
pairwise commuting case, by an explicit scalar identity.

## Build

The only TeX input is `note.tex`; the bibliography is included in that file.
Build with Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively use a standard LaTeX distribution containing `amsmath`,
`amssymb`, `amsthm`, `geometry`, `booktabs`, `array`, `lmodern` and `hyperref`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

No BibTeX step, network data, figures or external bibliography are required
after the TeX packages are available.

## Verification coverage

| Statement | Mathematical support |
| --- | --- |
| Original positive-semidefinite assertion, all `n>0`, `1<=k<=n` | `D5.S3.Quantum.Matrix.MalkounJordanElementary.result` in the [pinned Lean file](https://github.com/the-omega-institute/trureturing/blob/57b811cedb64c8065c6afac0da57d0fe2c8aa5ab/D5/S3/Quantum/Matrix/MalkounJordanElementary.lean) |
| Cauchy–Binet identity used by that declaration | `cauchyBinet` in the [pinned compound-matrix file](https://github.com/the-omega-institute/trureturing/blob/57b811cedb64c8065c6afac0da57d0fe2c8aa5ab/D5/S3/Quantum/Schatten/CompoundMatrices.lean) |
| Absolute principal-minor bound; arbitrary rectangular and Hermitian extensions | Theorem 1, Lemma 2 and Corollary 3, written proofs in `note.tex` |
| Complex determinant-polynomial bound and equality criterion | Corollary 4, written proof in `note.tex` |
| Commuting three-matrix Schur inequalities | Corollary 5, written proof in `note.tex` |
| Gaussian-integer controls, singular and indefinite examples | `verify.py` and `verification.json`, with exact ranges and counts |

The finite checks complement the written arguments; they are not a proof
for all matrices. They use the Python 3 standard library and exact integers:

```sh
python3 verify.py > verification-regenerated.json
cmp verification.json verification-regenerated.json
```

`verification.json` is deterministic for the stated script and seed.
The source archive contains this README, the TeX source, metadata, checker and
its exact output. The separately supplied PDF renders the same TeX source.

## Source coverage

The coverage table in the PDF distinguishes the two-matrix question and its
duplicate in MathOverflow answer 492315 from the general promotion question
and the different three-matrix Schur conjectures. The normalized determinant
problem in MathOverflow 180293 has a posted proof by cubesteak, answer 514685
(August 26, 2026); the note cites it rather than treating that problem as open.
The commuting cases of the linked Schur conjectures and Math.SE 4726142
are proved; their general noncommuting versions and the proposed rank-one
reduction are outside the coverage of this note.
Only the existing problem ID `malkoun-2026-mo512579-jordan-elementary` is
listed in `metadata.json`.

## References and license

The bibliography gives the exact MathOverflow locators and the related paper
by J. K. Merikoski and A. Virtanen, *Czechoslovak Mathematical Journal* 42
(1992), 193–198, DOI `10.21136/cmj.1992.128332`.
The original proofs and exposition in this package are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
The cited MathOverflow contributions are separately attributed and retain
their CC BY-SA 4.0 terms. The linked Lean files retain their own licenses.
