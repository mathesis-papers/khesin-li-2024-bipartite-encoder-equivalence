# When are two different encoder graphs equivalent?

Picture two banks of sockets: inputs on the left, outputs on the right. A wire connects a pair of sockets. If wires only go between the banks, write the drawing as a table of zeros and ones, one row per input and one column per output. Here is a drawing with two inputs and three outputs:

$$
\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}.
$$

The first two outputs have one wire each. The third is shared by both inputs. Try adding the second row to the first, with $1+1=0$: two marks at the same position cancel. This moves the shared output to the second column, but does not remove it. Could more flexible moves on the graph do better?

- [What survives the moves](moves.md) explains what can be measured even when a move makes a wire within one bank.
- [Two rows, three nonzero types](two-inputs.md) counts four kinds of columns to find the fewest shared outputs in the entire bipartite class.

This is a reading companion to Haobo Ma and Wenlin Zhang's [version 2 paper](https://doi.org/10.5281/zenodo.24404944) (CC BY 4.0). The historical question comes from [Khesin and Li, §8, p. 23](https://arxiv.org/abs/2406.12083v1); the paper also credits an earlier version in Li's 2023 report. The subject here is a specified graph relation without decorations, not a decision procedure for equivalence of arbitrary quantum codes.
