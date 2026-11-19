# 逐项陈述比较

原文定理、引理、推论共用计数器：Theorem 1、Lemma 2、Corollaries 3–5。本记录区分纸面结论与公开形式声明，不更改冻结论文、平台状态或验证收据。

| Result | Verdict | Compared declaration | Commit | Scope |
|---|---|---|---|---|
| mo-positive | same | D5/S3/Quantum/Matrix/MalkounJordanElementary.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 公开 claim 的精确范围：复数 Fin n 方阵，n>0，X,Y 正半定，1≤k≤n，单向 e_k 不等式。正文仅在此处陈述原推论 3 的这一特例，不附加绝对值或任意 Hermitian 输入。 |
| gram-bound | variant | D5/S3/Quantum/Schatten/CompoundMatrices.cauchyBinet | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原 Lemma 2 为任意复 m×k 矩阵 U,V 的模平方乘积界，包含 k=0、k>m。公开 cauchyBinet 是任意交换环上的乘积行列式恒等式，并非不等式。私有 gram_det_le 要求两个 Gram 矩阵相同，只给出实部的单向界，不是完整引理。 |
| rectangular-bound | special case | D5/S3/Quantum/Matrix/MalkounJordanElementary.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原 Theorem 1 允许任意复 p×n 矩阵 A,B、所有列集合（含空集）、主子式模界及 0≤k≤n 的两步对称和界。公开 result 仅覆盖方阵正半定的单向推论。私有 principal_det_le 只给方阵 Hermitian 输入的单向主子式界，无绝对值；可复用堆叠机制与公共 cauchyBinet。 |
| hermitian-bound | special case | D5/S3/Quantum/Matrix/MalkounJordanElementary.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原 Corollary 3 允许任意 Hermitian 输入、绝对值及 k=0。公开 result 是正半定单向特例，另在 mo-positive 精确展示。两行都映射 s3，正文明确说明特化关系。完整推论直接来自 Theorem 1，共享其请求，不重复构造。 |
| determinant-bound | none | — | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原 Corollary 4 对所有复数 z 给出多项式界，并含行列式界、迹与 Frobenius 范数恒等式以及所有 k=1,…,n 单向等号同时成立当且仅当 A=B。在已检模块未找到这一完整公开陈述。复用 Theorem 1 的系数界；不声称单个 k 或所有绝对值等号的分类。 |
| commuting-schur | none | — | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 原 Corollary 5 要求 A,B,C 两两可交换、正半定、Hermitian。保留行列式、奇异值对称函数及对称化特征值的全部结论，0≤k≤n。其同时对角化与标量证明独立于 Theorem 1。SchurMinimum 是无关的分块二次型极小化。非交换版本与秩一约化不在本论文结论内。 |

## 检索范围与逻辑依赖

已读完整提交 `8a24ea4e79de962725aab9d9b49cc605fcc211d8` 上的 MalkounJordanElementary.lean、CompoundMatrices.lean 及对应 Frozen/state 文件，并检查 Quantum/Matrix、Quantum/Schatten 目录与邻近的 MonomialGram、MonomialColumnGram、ExpandingGram、SchurMinimum。锁文件只是选中的本地索引，没有把索引缺项当成上游缺失。私有辅助声明虽然列入冻结状态片，但并非同名公开结果，且其陈述弱于纸面模界。公开 result 的 claim 定义与 elementarySymmetric 定义已展开比较。检索不是全库穷尽证明，未重新编译 Lean。

依赖顺序：公共 Cauchy–Binet → Lemma 2 → Theorem 1 → Corollary 3 与 Corollary 4；Corollary 5 独立，使用同时对角化与标量 Schur 恒等式。读者证明处理了空子式、奇异矩阵、k=0、k>行数、z=0 和同时等号，无极限交换。

DOI 经 discovery 与公开 Zenodo API 核对：版本 `10.5281/zenodo.23920583`，概念 `10.5281/zenodo.23920582`。正文与请求使用版本 DOI，冻结输入保持不变。已在开放及关闭请求中按 DOI、Malkoun、Gram determinant、elementary symmetric、Schur 检索，再登记 179–182；Corollary 3 复用 Theorem 1 请求。
