# What survives the moves

Label the inputs and outputs separately. Four kinds of moves are allowed: **locally complement** at any vertex (toggle every edge between two of its neighbors); permute the inputs or outputs within their own bank; add one input row to a different row modulo two (change only the cross-bank wires); or delete an edge joining two inputs. The equivalence relation $\sim$ allows walking either way through these moves. In particular, the middle of a walk need not be bipartite. Only the endpoints are required to have cross-bank wires exclusively. We omit output Clifford decorations.

:::: {.theorem #thm-move-reduction title="Move reduction at bipartite endpoints" lean="D5/S3/Quantum/Codes/KhesinLiBipartiteEncoderEquivalence.result" mathesis="collected:khesin-li-2024-bipartite-encoder-equivalence:2:s1"}
For any nonnegative $k,n$, let $G,H$ be bipartite encoder graphs with $k$ inputs and $n$ outputs. If $G\sim H$, a finite sequence of output permutations, input permutations and additions of distinct binary input rows takes $G$ to $H$. Every graph along this sequence is bipartite. (Manuscript Theorem 1.)
::::

## 1. Count independent patterns across a cut

Pick a set $S$ of outputs and separate them from all the other vertices. Write a 0–1 table for just the wires crossing this cut. Its **rank** is the maximum number of independent row patterns under addition modulo two: a pattern you can make from the others does not add another independent row. For example, $10,01,11$ together have rank two because the third is the sum of the first two. Write $\rho_G(S)$ for the rank of the cut table.

:::: {.remark #rem-cut-ranks title="The output cut-rank invariant (manuscript Lemma 2)" mathesis="collected:khesin-li-2024-bipartite-encoder-equivalence:2:s2"}
If $G\sim H$, a single output relabeling makes their cut ranks agree for every output subset $S$. This statement does not require bipartite endpoints.
::::

If the center of a local complementation lies in $S$, add its row to the other rows on its side that are adjacent to it. If the center is on the other side, do the analogous column additions. These operations undo themselves and preserve rank. An input row addition becomes a *column* addition in the cut table because all inputs are outside $S$. Deleting an input–input edge does not touch the cut. Input permutations reorder columns; output permutations relabel the family of cuts. Combine the successive output relabelings to get one relabeling that works for every $S$.

## 2. Recover the choices of columns that sum to zero

At a bipartite endpoint, no wire crosses from $S$ to an output outside $S$. The cut rank is just the rank of the columns $B[:,S]$ of the cross-bank matrix. There are $2^{|S|-\operatorname{rank}B[:,S]}$ ways of selecting columns inside $S$ whose sum is zero: there is one free binary choice per missing independent constraint. The exact set of selected columns is called the **support**. Work up from smaller sets. Subtract the counts for all proper exact supports from the count for selections inside $S$, leaving the count for exact support $S$. In binary arithmetic there is only one selection with that support: every selected coefficient is one.

:::: {.remark #rem-kernel title="Subset ranks, zero sums and row space (manuscript Lemma 3)" mathesis="collected:khesin-li-2024-bipartite-encoder-equivalence:2:s3"}
For equal-size binary matrices, agreement of ranks on every column subset is equivalent to agreement of their kernels (the 0–1 vectors whose weighted column sums vanish), and to agreement of their row spaces (the sets of all binary row sums).
::::

The counting argument gives ranks to kernel. A zero-sum vector has dot product zero with every row. Taking the orthogonal complement twice returns the original space in finite-dimensional binary linear algebra, so the kernel and row space determine one another. Conversely, restrict the row-space vectors to coordinates in $S$: the dimension of this smaller space gives the rank of the columns in $S$.

## 3. Turn a row space back into a sequence of moves

:::: {.remark #rem-row-moves title="From equal row spaces to row moves (manuscript Lemma 4)" mathesis="collected:khesin-li-2024-bipartite-encoder-equivalence:2:s4"}
If $B,C$ are binary $k\times n$ matrices with equal row spaces, an invertible binary $k\times k$ matrix $R$ satisfies $C=RB$. Row swaps and additions of distinct rows take $B$ to $C$.
::::

Reduce both tables to the same reduced row echelon form and run the second reduction backwards. There is no scaling step other than multiplying by one. At bipartite endpoints the cross-bank matrix determines the entire graph, so every step can stay bipartite. For zero inputs or zero outputs the only bipartite graph is edgeless and the empty sequence suffices.

:::: {.remark #rem-criterion title="Three equivalent tests (manuscript Corollary 5)" mathesis="collected:khesin-li-2024-bipartite-encoder-equivalence:2:s5"}
For bipartite encoder graphs of the same size, these conditions are equivalent: equivalence under the original moves; equality of row spaces after some output relabeling; equality of all output cut ranks after some output relabeling. Steps 1 and 2 give graph equivalence to cut ranks to row spaces. Step 3 gives the reverse implication from row spaces to graph equivalence.
::::

:::: {.remark #rem-no-input-permutation title="Row additions can swap inputs (manuscript Corollary 6)" mathesis="collected:khesin-li-2024-bipartite-encoder-equivalence:2:s6"}
Permutations are made of swaps, and $(u,v)\mapsto(u+v,v)\mapsto(u+v,u)\mapsto(v,u)$. Thus output permutations and additions of distinct input rows suffice. With fewer than two inputs there is no input swap to replace.
::::

## Where the argument stops

The pinned Lean declaration for Theorem 1 matches the graph moves in the paper. The supporting and derived statements above explain its mechanism; the book does not present them as separately verified public declarations. Trying all output permutations is not a polynomial-time algorithm for general size. The step that reads a matrix from cut ranks needs bipartite endpoints, and the cut ranks tested here are not a complete invariant of arbitrary graphs. Completeness of the graph moves for quantum-code equivalence is the separate Khesin–Li Conjecture 6.3, not a consequence of this proof.
