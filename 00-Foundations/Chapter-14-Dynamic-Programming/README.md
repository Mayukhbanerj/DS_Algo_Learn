# Chapter 14 — Dynamic Programming

**Reference:** CLRS, Fourth Edition (2022), Sections 14.1–14.5, printed pages 361–416.

Dynamic programming (DP) solves problems with overlapping subproblems by solving each distinct subproblem once and storing its result. It is especially useful for optimization problems, where many feasible solutions exist and the goal is to minimize or maximize a value.

## The four-step method

1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value, usually bottom-up or with memoization.
4. Reconstruct an optimal solution from the stored choices.

The first three steps compute the optimum value. The fourth reconstructs an actual optimum; store choices during step 3 when that makes reconstruction efficient.

## 14.1 Rod cutting

Given prices p_i for rods of integer length i, maximize revenue for a rod of length n. Let r_0=0. The first-piece recurrence is

r_n = max_{1≤i≤n}(p_i + r_{n−i}).

The option i=n means no cut. Naive recursion explores all 2^(n−1) cut patterns and has exponential running time. Its call count obeys T(0)=1 and T(n)=1+Σ_{j=0}^{n−1}T(j)=2^n.

### Memoized top-down
Initialize r[0…n] to unknown. A recursive helper returns a stored value if known; otherwise evaluates every first cut, stores the maximum, and returns it.

### Bottom-up
Set r[0]=0. For j=1…n, compute r[j]=max_{1≤i≤j}(p[i]+r[j−i]). There are Θ(n) subproblems and O(n) choices each, so Θ(n²) time and Θ(n) space.

To reconstruct cuts, store s[j], the first piece length attaining r[j]. Repeatedly output s[n] and subtract it from n.

## 14.2 Matrix-chain multiplication

Given matrices A_i of dimensions p_(i−1)×p_i, find a full parenthesization minimizing scalar multiplications. Multiplication order matters for cost, not for the product value.

Let m[i,j] be the minimum cost for A_i…A_j. Base case m[i,i]=0. For i<j,

m[i,j] = min_{i≤k<j}(m[i,k]+m[k+1,j]+p_(i−1)p_kp_j).

Store s[i,j]=k for an optimal split. Fill the tables by increasing chain length, so both subproblems are already solved. There are Θ(n²) subproblems and O(n) splits per subproblem: Θ(n³) time and Θ(n²) space. Reconstruct parentheses recursively from s.

A direct recursive algorithm is exponential (the number of full parenthesizations is Catalan-scale); memoization computes each of the Θ(n²) subproblems once and also takes O(n³).

## 14.3 Elements of dynamic programming

### Optimal substructure
An optimal solution contains optimal solutions to the subproblems it uses. Prove this with cut-and-paste: replacing a nonoptimal subsolution with a better one would improve the full solution, a contradiction.

### Independent subproblems
Subproblems are independent when one subproblem's solution does not consume resources needed by another. Matrix-chain subchains are disjoint. Shortest-path subpaths can be spliced; longest simple-path subproblems can share vertices and therefore may not be independent.

### Overlapping subproblems
A recursive solution repeatedly encounters the same parameterized subproblems. If the number of distinct subproblems is small (often polynomial), memoization or bottom-up tabulation avoids repeated work.

### Choosing a method
- Bottom-up: solve smaller subproblems first; avoids recursion overhead and often has better constants.
- Top-down memoization: preserves the natural recursive structure and may avoid solving unreachable/unneeded subproblems.

A useful rough cost model is (number of distinct subproblems) × (choices examined per subproblem), plus reconstruction.

## 14.4 Longest common subsequence

A subsequence preserves relative order but need not be contiguous. For sequences X[1…m], Y[1…n], let c[i,j] be the LCS length of prefixes X[1…i], Y[1…j]. Set c[i,0]=c[0,j]=0. Then

- if x_i=y_j: c[i,j]=c[i−1,j−1]+1;
- otherwise: c[i,j]=max(c[i−1,j],c[i,j−1]).

Store direction choices (diagonal, up, left) to reconstruct an LCS. The table takes Θ(mn) time and space. The recurrence follows by considering whether the last elements match; when they differ, at least one is excluded from an optimal common subsequence.

The length alone can be computed with two rows, using 2·min(m,n) entries, or with one row plus a saved diagonal value.

## 14.5 Optimal binary search trees

Given sorted distinct keys k_1…k_n, successful-search probabilities p_1…p_n, and unsuccessful-search (dummy-key) probabilities q_0…q_n, build a BST minimizing expected search cost. The probabilities sum to 1. A search cost is depth+1, so expected cost is 1 plus the probability-weighted sum of node depths.

Let e[i,j] be optimal expected cost for keys k_i…k_j and dummy leaves d_(i−1)…d_j. Empty subtree base: e[i,i−1]=q_(i−1). Let

w[i,j]=Σ_(l=i…j)p_l + Σ_(l=i−1…j)q_l.

If k_r is the root, both subtrees become one level deeper, adding their probability mass. Thus

e[i,j]=min_{i≤r≤j}(e[i,r−1]+e[r+1,j]+w[i,j]).

Store root[i,j]=r. Compute w incrementally: w[i,j]=w[i,j−1]+p_j+q_j. Fill by increasing interval length. Standard OPTIMAL-BST takes Θ(n³) time and Θ(n²) space. Knuth's monotonicity property permits an O(n²) optimization.

## Visual aids

- [Matrix-chain split recurrence](images/matrix-chain-split.svg)
- [LCS table dependencies](images/lcs-dependencies.svg)

## Engineering checklist

- Define state precisely, including indices and empty-subproblem boundaries.
- Prove optimal substructure before trusting a recurrence.
- Verify that the state captures all information needed for future decisions.
- Choose a topological evaluation order so dependencies are ready.
- Store choices if the actual solution must be reconstructed.
- Audit tie-breaking and unreachable states explicitly.
- Compare the number of states and transitions, not just recursion depth.
