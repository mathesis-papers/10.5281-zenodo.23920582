# MathOverflow 512579, revision 1: The elementary symmetric inequality for a Hermitian Jordan product

**Authors:** Haobo Ma, Wenlin Zhang

We answer the first question in Malkoun's MathOverflow 512579, revision 1: for positive semidefinite Hermitian X,Y, every elementary symmetric function of the eigenvalues of XY+YX is at most its counterpart for X^2+Y^2. The written proof establishes the stronger absolute-value inequality for arbitrary Hermitian X,Y and for H=A*B+B*A, R=A*A+B*B with arbitrary rectangular complex A,B. Cauchy-Binet and Cauchy-Schwarz bound each principal determinant, including singular cases. The pinned Lean declaration proves the original positive-semidefinite assertion; the extensions have written proofs and accompanying exact finite checks.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23920583](https://doi.org/10.5281/zenodo.23920583)
- Concept DOI: [https://doi.org/10.5281/zenodo.23920582](https://doi.org/10.5281/zenodo.23920582)
- License: CC-BY-4.0
- Version: 1
- Mathesis record: [malkoun-2026-mo512579-jordan-elementary](https://mathesis-omega-research.apps.chrono-ai.fun/papers/malkoun-2026-mo512579-jordan-elementary?version=1)

## How to cite

Haobo Ma, Wenlin Zhang (2026). MathOverflow 512579, revision 1: The elementary symmetric inequality for a Hermitian Jordan product. Mathesis, version 1. https://doi.org/10.5281/zenodo.23920583

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/57b811cedb64c8065c6afac0da57d0fe2c8aa5ab/D5/S3/Quantum/Matrix/MalkounJordanElementary.lean) | No public receipt |
| Lemma (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/57b811cedb64c8065c6afac0da57d0fe2c8aa5ab/D5/S3/Quantum/Matrix/MalkounJordanElementary.lean) | No public receipt |
| Corollary (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/57b811cedb64c8065c6afac0da57d0fe2c8aa5ab/D5/S3/Quantum/Matrix/MalkounJordanElementary.lean) | No public receipt |
| Corollary (s4) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/57b811cedb64c8065c6afac0da57d0fe2c8aa5ab/D5/S3/Quantum/Matrix/MalkounJordanElementary.lean) | No public receipt |
| Corollary (s5) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/57b811cedb64c8065c6afac0da57d0fe2c8aa5ab/D5/S3/Quantum/Matrix/MalkounJordanElementary.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/10.5281-zenodo.23920582/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/10.5281-zenodo.23920582/malkoun-2026-mo512579-jordan-elementary/zh/) · [Read in English](https://papers.trureturing.org/10.5281-zenodo.23920582/malkoun-2026-mo512579-jordan-elementary/en/)

[Slides](https://papers.trureturing.org/10.5281-zenodo.23920582/malkoun-2026-mo512579-jordan-elementary/slides/) ([sources](books/malkoun-2026-mo512579-jordan-elementary/slides/)) · [Videos](https://papers.trureturing.org/10.5281-zenodo.23920582/malkoun-2026-mo512579-jordan-elementary/films/) ([sources](books/malkoun-2026-mo512579-jordan-elementary/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/10.5281-zenodo.23920582/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `mo-positive` | same | `D5/S3/Quantum/Matrix/MalkounJordanElementary.result` |
| `gram-bound` | variant | `D5/S3/Quantum/Schatten/CompoundMatrices.cauchyBinet` |
| `rectangular-bound` | special case | `D5/S3/Quantum/Matrix/MalkounJordanElementary.result` |
| `hermitian-bound` | special case | `D5/S3/Quantum/Matrix/MalkounJordanElementary.result` |
| `determinant-bound` | none | — |
| `commuting-schur` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/malkoun-2026-mo512579-jordan-elementary/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
