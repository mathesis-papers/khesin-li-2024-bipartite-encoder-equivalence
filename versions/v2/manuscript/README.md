# Bipartite encoder equivalence

The note extends Khesin–Li (2024), arXiv:2406.12083v1, Section 8: it proves Conjecture 8.3 (page 23) for the operation-generated, decoration-free graph relation and corrects Proposition 8.2 (page 23). Bipartite endpoints related by local complementation, input/output permutations, binary input-row additions and input-edge deletion are related using only permutations and row additions.

For two inputs, zero-column count and the unordered multiplicities of the three nonzero column types give a complete classification and a linear-time equivalence test. The exact minimum shared-output count is the least multiplicity, at most floor((n-z)/3) for z zero columns. The full-rank matrix with columns (1,0), (0,1), (1,1) has minimum one, contradicting the published bound of zero at n=3. The note gives the sharp replacement and reproves the connected [4,2] classification with credit to Khesin–Li (2024).

## Build

Use Tectonic 0.17.0:

```sh
tectonic --untrusted note.tex
```

Alternatively use a LaTeX installation with `pdflatex`, the standard AMS packages, `lmodern`, `geometry`, `booktabs`, and `hyperref`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is embedded in `note.tex`; no external images or bibliography database are needed.

## Mathematical checks

The cut-rank argument builds on Oum (2005), Proposition 2.6, and binary-matroid representation uniqueness, as recorded in Oxley (2011), Proposition 6.6.5. The note distinguishes the all-vertex-cut theorem of Kim–Oum (2024), the classical-code correspondence of Danielsen–Parker (2007/2008), and the later CSS conversion results of Wang–Krastanov (2026) and Albert (2026) from the fixed-partition encoder relation. The three-basis observation already appears in Li's report dated 19 August 2023, Section VII, before its February and June 2024 presentations. Exact locators and source links are in the note. No priority claim is made.

Python 3.10 or later, standard library only:

```sh
python3 verify.py > verification-new.json
```

The output equals the supplied `verification.json`. The script checks all 6,115 binary matrices with 0–3 rows, 0–5 columns and at most 12 entries. It reconstructs kernel membership from every subset rank, checks row-space uniqueness, and compares complete graph-operation components with restricted components at all bipartite endpoints for all 6,505 labelled graph/partition cases with at most five vertices, checking 116,872 generator instances. It also checks all 21,845 binary 2-by-n matrices with 0 <= n <= 7 and all six changes of input basis, the exact shared-output minimum, classification signatures, and the three-output counterexample. The ternary and total-rank boundary examples concern extensions not asserted in the posing source. These are finite checks; the note contains the proofs for arbitrary sizes.

The linked Lean declaration `D5.S3.Quantum.Codes.KhesinLiBipartiteEncoderEquivalence.result` proves the all-size restricted-move implication, with its operation definitions in the imported module:

- https://github.com/the-omega-institute/trureturing/blob/5a1fca9e717166d9d52651194f897dda2b9ff37f/D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.lean
- https://github.com/the-omega-institute/trureturing/blob/5a1fca9e717166d9d52651194f897dda2b9ff37f/D5/S3/Quantum/Codes/KhesinLiEquivalenceClasses.lean

The equivalence criterion, two-input classification, sharp bound, connectedness criterion, correction and boundary examples have written proofs in the note; they are not conclusions of the linked declaration. The imported module supplies the `Step` and `addInputRow` definitions. The graph relation is separate from the quantum-code completeness assertion of Khesin–Li Conjecture 6.3. Conjecture 7.1 on normalized class sizes and classes without bipartite forms are not covered.

## Authors and license

Haobo Ma — ChronoAI Pte Ltd, Singapore.

Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

Copyright 2026 Haobo Ma and Wenlin Zhang. Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0): https://creativecommons.org/licenses/by/4.0/.
