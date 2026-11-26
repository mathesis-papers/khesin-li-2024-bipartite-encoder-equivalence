# Khesin–Li (2024), Section 8, Conjecture 8.3: An elementary proof and a sharp correction to Proposition 8.2

**Authors:** Haobo Ma, Wenlin Zhang

We extend Khesin–Li (2024), Section 8, by proving the operation-generated, decoration-free graph formulation of Conjecture 8.3 (page 23) and correcting the shared-output bound in Proposition 8.2 (page 23). For bipartite encoder graphs in one class, local complementations and input-edge deletions can be eliminated: output permutations and binary input-row additions suffice. The output cut-rank function is invariant under the original operations, up to output relabelling. At a bipartite endpoint this function determines the binary kernel, hence the row space, of the input–output matrix. For two inputs, the number of zero columns and the unordered multiplicities of the three nonzero column types classify the graphs. Their smallest achievable number of shared outputs is the least of these multiplicities, at most floor((n-z)/3) for z zero columns. The [3,2] matrix with all three nonzero column types has minimum one, whereas the published bound gives zero.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24404944](https://doi.org/10.5281/zenodo.24404944)
- Concept DOI: [https://doi.org/10.5281/zenodo.24404943](https://doi.org/10.5281/zenodo.24404943)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [khesin-li-2024-bipartite-encoder-equivalence](https://mathesis-omega-research.apps.chrono-ai.fun/papers/khesin-li-2024-bipartite-encoder-equivalence?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Khesin–Li (2024), Section 8, Conjecture 8.3: An elementary proof and a sharp correction to Proposition 8.2. Mathesis, version 2. https://doi.org/10.5281/zenodo.24404944

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/5a1fca9e717166d9d52651194f897dda2b9ff37f/D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.lean) | No public receipt |
| Lemma (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/5a1fca9e717166d9d52651194f897dda2b9ff37f/D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.lean) | No public receipt |
| Lemma (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/5a1fca9e717166d9d52651194f897dda2b9ff37f/D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.lean) | No public receipt |
| Lemma (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/5a1fca9e717166d9d52651194f897dda2b9ff37f/D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/5a1fca9e717166d9d52651194f897dda2b9ff37f/D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/5a1fca9e717166d9d52651194f897dda2b9ff37f/D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.lean) | No public receipt |
| Corollary (s7) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/5a1fca9e717166d9d52651194f897dda2b9ff37f/D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.lean) | No public receipt |
| Corollary (s8) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/5a1fca9e717166d9d52651194f897dda2b9ff37f/D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.lean) | No public receipt |
| Corollary (s9) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/5a1fca9e717166d9d52651194f897dda2b9ff37f/D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/khesin-li-2024-bipartite-encoder-equivalence/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/khesin-li-2024-bipartite-encoder-equivalence/khesin-li-2024-bipartite-encoder-equivalence/zh/) · [Read in English](https://papers.trureturing.org/khesin-li-2024-bipartite-encoder-equivalence/khesin-li-2024-bipartite-encoder-equivalence/en/)

[Slides](https://papers.trureturing.org/khesin-li-2024-bipartite-encoder-equivalence/khesin-li-2024-bipartite-encoder-equivalence/slides/) ([sources](books/khesin-li-2024-bipartite-encoder-equivalence/slides/)) · [Videos](https://papers.trureturing.org/khesin-li-2024-bipartite-encoder-equivalence/khesin-li-2024-bipartite-encoder-equivalence/films/) ([sources](books/khesin-li-2024-bipartite-encoder-equivalence/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/khesin-li-2024-bipartite-encoder-equivalence/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `cor-connected` | variant | `D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.result` |
| `cor-two-inputs` | variant | `D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.result` |
| `rem-criterion` | variant | `D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.result` |
| `rem-cut-ranks` | variant | `D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.result` |
| `rem-kernel` | variant | `D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.result` |
| `rem-no-input-permutation` | variant | `D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.result` |
| `rem-one-input` | variant | `D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.result` |
| `rem-row-moves` | variant | `D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.result` |
| `thm-move-reduction` | same | `D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.result` |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/khesin-li-2024-bipartite-encoder-equivalence/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
