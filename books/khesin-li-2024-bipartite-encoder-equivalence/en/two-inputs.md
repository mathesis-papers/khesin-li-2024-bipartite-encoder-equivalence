# Two rows, three nonzero types

With two inputs a column has only four possible types: $00$ has no wire, $10$ and $01$ have one wire each, and $11$ is shared. Write $z,a,b,c$ for their counts in that order. Our opening example has no zero columns and one of each nonzero type. Changing rows can change *which* type is shared, but it cannot squeeze three distinct nonzero types into two.

::: {.film src="001-three-column-types"}
Follow the three columns: why can the shared output move but not disappear?
:::

:::: {.corollary #cor-two-inputs title="Two-input classification and the exact shared-output minimum" status="written-proof" proof="pf-two-inputs" doi="10.5281/zenodo.24404944" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/531" mathesis="collected:khesin-li-2024-bipartite-encoder-equivalence:2:s7"}
Two bipartite encoder graphs with two inputs and the same $n$ outputs are equivalent exactly when $z$ and the sorted triple of counts $a,b,c$ agree, retaining repetitions. Over equivalent bipartite drawings, the least shared-output count is $m=\min(a,b,c)\leq\lfloor(n-z)/3\rfloor$, and the least edge count is $n-z+m$. In rank two the minimum is attainable with two identity pivot columns. The upper bound is sharp for each $n-z\geq2$. With output labels fixed, cut ranks on singletons and pairs already determine the row space. (Manuscript Corollary 7.)
::::

:::: {.proof #pf-two-inputs}
Any two distinct nonzero columns form a basis, so choosing two distinct nonzero images specifies an invertible row change. The third column is their sum and goes to the remaining type. Thus the three nonzero types can be permuted at will, while zero stays zero. The row-space test and output permutations now give the classification.

Send a least frequent type to $11$ to minimize sharing. Every nonzero column contributes one wire, and each shared column contributes one extra wire. The three counts sum to $n-z$, so their minimum is at most their average. Rank two means at least two types occur; once the least frequent type is sent to $11$, both $10$ and $01$ occur and can serve as pivots. To attain the bound, distribute $n-z$ columns among the three types as evenly as possible. At least two types occur when $n-z\geq2$, and the least count is exactly $\lfloor(n-z)/3\rfloor$.

A one-column cut has rank zero exactly for the zero type. For two nonzero columns the cut has rank one exactly when the columns coincide. This recovers the partition by type with labels fixed. The names of the nonzero types can be permuted by an invertible row change, so the partition determines the row space.
::::

In the opening $[3,2]$ example, the three counts are all one. Every equivalent bipartite drawing therefore needs one shared output, though the old upper bound $\lfloor n/2-1\rfloor$ in Khesin–Li Proposition 8.2 (p. 23) gives zero. The example already has two identity pivot columns. The new bound $\lfloor(n-z)/3\rfloor$ is the best uniform upper bound on the minimum; for a particular drawing, the exact answer still comes from counting its types. Sorting the counts also gives a canonical representative without enumerating output permutations.

:::: {.remark #rem-one-input title="One input: count the wires (manuscript Corollary 8)" mathesis="collected:khesin-li-2024-bipartite-encoder-equivalence:2:s8"}
With one input the only invertible binary row change is the identity. The row-space criterion reduces to permuting a single row, so its weight, the number of ones, completely classifies the drawing. This includes no outputs and no wires.
::::

## One connected drawing, or a connected class?

The identity matrix $I_2$ draws two separate wires. Add its second row to its first and the result draws a path through all four vertices. A class can thus contain both a connected drawing and a disconnected drawing. Ask instead: **Does this class contain any disconnected drawing at all?**

:::: {.corollary #cor-connected title="Connectedness of the whole two-input class" status="written-proof" proof="pf-connected" doi="10.5281/zenodo.24404944" source="Corollary 9" request="https://github.com/the-omega-institute/trureturing-requests/issues/532" mathesis="collected:khesin-li-2024-bipartite-encoder-equivalence:2:s9"}
For a rank-two bipartite encoder graph with two inputs, every graph in its equivalence class is connected, including the nonbipartite members, exactly when $z=0$ and $a,b,c$ are all positive. These classes correspond to unordered triples of positive integers summing to $n$; for $n=4$ there is just $\{1,1,2\}$. (Manuscript Corollary 9.)
::::

:::: {.proof #pf-connected}
A zero column isolates an output in the original drawing. If one nonzero type is missing, rank two means the other two occur. Send them to $10$ and $01$ to get two disjoint stars.

Conversely suppose an equivalent graph $H$ is disconnected. Let $I_j,S_j$ be the inputs and outputs in its $j$-th component, using the output relabeling from the cut-rank invariant. The only possible wires across the cut of $S_j$ are to inputs in its own component. Hence $\operatorname{rank}B[:,S_j]=\rho_H(S_j)\leq |I_j|$. The sum of the column-block ranks is at least the whole rank, two, and the total input count is also two. Equality holds throughout. An input-free component would therefore give zero columns, and an output-free component cannot contain an input. Disconnectedness would require two components of one input each. Each corresponding block has rank one and can contain only one nonzero type, contradicting the presence of all three. The classification by counts now gives the positive triples.
::::

The [version 2 manuscript](https://doi.org/10.5281/zenodo.24404944) proves the two-input classification, minimum and class connectedness on paper. The pinned Lean theorem for move reduction does not assert them; the two linked requests give the exact scopes for contributing formal proofs. The $n=4$ connected-class result appears already in Li's Claim F and Khesin–Li Proposition 8.1; the criterion here works for every $n$.
