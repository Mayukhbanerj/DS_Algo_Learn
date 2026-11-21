# Chapter 14 — Exercises and Problems

Original study solutions based on CLRS Fourth Edition, Sections 14.1–14.5. Working solutions are subject to final mathematical and source audit.

## 14.1 Rod cutting

**14.1-1. Call-count recurrence.** T(0)=1 and T(n)=1+Σ_{j=0}^{n−1}T(j). By induction, if T(j)=2^j, then T(n)=1+(2^n−1)=2^n.

**14.1-2. Density-greedy counterexample.** A high price-per-unit first piece need not leave a remainder with a good decomposition. Construct a price table where the best-density length does not divide the optimal combination; provide a minimal numerical counterexample in the final audit.

**14.1-3. Fixed cut cost c.** Let r[0]=0 and r[j]=max(p[i]+r[j−i]−c·I[j−i>0]) for i=1…j. A cut is charged only when a nonempty remainder follows the first piece. O(n²) time.

**14.1-4. Restrict first cut to floor(n/2).** Consider only i≤floor(n/2), but include the symmetric decomposition by allowing the first piece to be the larger side: use max over i≤floor(n/2) of r[i]+r[n−i], plus p[n] for no cut. For the one-sided recurrence p[i]+r[n−i], symmetry is not enough unless the price term is included for whichever side is chosen; state and verify the exact modification before final sign-off.

**14.1-5. Return an optimal solution.** Store s[j] whenever p[i]+r[j−i] improves r[j]. Reconstruct by repeatedly outputting s[j] and setting j←j−s[j].

**14.1-6. Fibonacci DP.** Set F[0]=0,F[1]=1; for i=2…n set F[i]=F[i−1]+F[i−2]. The subproblem graph has n+1 vertices (0…n) and 2n−3 edges for n≥2, from i to i−1 and i−2 where defined. Time Θ(n), space Θ(n), or O(1) rolling space.

## 14.2 Matrix-chain multiplication

**14.2-1. Dimensions 5,10,3,12,5,50,6.** Use MATRIX-CHAIN-ORDER; compute m and s by increasing chain length, then PRINT-OPTIMAL-PARENS. Numerical table to be filled and independently checked.

**14.2-2. Multiply recursively.** If i=j return A_i. Otherwise k=s[i,j], recursively compute L=MULTIPLY(A,s,i,k), R=MULTIPLY(A,s,k+1,j), and return RECTANGULAR-MATRIX-MULTIPLY(L,R). The recursion performs exactly the multiplications described by the optimal parenthesization.

**14.2-3. Catalan-scale parenthesizations.** The recurrence P(1)=1 and P(n)=Σ_{k=1}^{n−1}P(k)P(n−k) yields Catalan numbers C_(n−1), which are Θ(4^n/n^(3/2)); in particular P(n)=Ω(2^n). A substitution proof with constants remains to be expanded.

**14.2-4. Subproblem graph.** Vertices are index intervals (i,j), 1≤i≤j≤n: n(n+1)/2 vertices. There is an edge from (i,j) to each direct subinterval (i,k) and (k+1,j), for every i≤k<j. Count the edges by summing 2(j−i) over all intervals; simplify in final audit.

**14.2-5. Table-reference count.** Count references to m[i,j] as a subproblem in every larger interval and split. The stated total is n³/3−n/3; derive by summing over interval lengths and split positions.

**14.2-6. Parenthesis count.** A full parenthesization of n operands is a full binary expression tree with n leaves and n−1 internal multiplication nodes. Each internal node contributes one pair of parentheses, hence n−1 pairs.

## 14.3 Elements of dynamic programming

**14.3-1. Exhaustive parenthesization vs recursive recurrence.** Both are exponential, but RECURSIVE-MATRIX-CHAIN has less redundant work than enumerating all parenthesizations explicitly; it still repeats subproblems exponentially, while memoization/tabulation is O(n³).

**14.3-2. Merge-sort recursion tree.** The recursion tree has disjoint subarrays at each level. No identical nontrivial subproblem recurs, so memoization provides no asymptotic benefit and adds table overhead.

**14.3-3. Maximize scalar multiplications.** The problem still has optimal substructure: for a fixed split k, replacing either subchain by a parenthesization with a larger multiplication count improves the total. Use max instead of min in the recurrence.

**14.3-4. Greedy split counterexample.** Choosing k to minimize only p_(i−1)p_kp_j ignores the two subchain costs. Give a dimension sequence where the locally cheapest multiplication creates expensive subchains; numerical counterexample pending final audit.

**14.3-5. Limited piece counts.** The original state “best revenue for length n” is insufficient: the optimal solution for a remainder depends on how many pieces of each length have already been used. A counterexample should compare two histories with the same remainder length but different remaining inventories.

## 14.4 Longest common subsequence

**14.4-1. LCS example.** Compute the DP table for X=10010101 and Y=010110110; reconstruct one longest common subsequence. Verify length and order in the final audit.

**14.4-2. Reconstruct without b table.** Starting at (m,n), if x_i=y_j output that element and move diagonally; otherwise move to the adjacent cell with the same c value (up or left). Reverse the collected output. O(m+n) time.

**14.4-3. Memoized LCS.** Memoize c[i,j] for all prefix pairs; base row/column zero; use the same match/mismatch recurrence. O(mn) states and O(1) work per state, hence O(mn).

**14.4-4. Space reduction.** Keep two rows, swapping current/previous after each i, for 2·min(m,n) entries. One-row version scans j left-to-right while saving the old diagonal value before overwriting c[j−1]; O(min(m,n)) entries plus O(1).

**14.4-5. LIS in O(n²).** Let L[i]=1+max{L[j]:j<i and a_j<a_i}, default 1. Store predecessor; max L[i] is the LIS length. O(n²) time, O(n) space.

**14.4-6. LIS in O(n lg n).** Maintain tails[len] as the smallest possible ending value of an increasing subsequence of that length. For each x, binary-search the first tail≥x, replace it, and store predecessor links for reconstruction. O(n lg n) time.

## 14.5 Optimal binary search trees

**14.5-1. Construct optimal BST.** Recursively create key k_root[i,j] as root; build left interval [i,r−1] with dummy d_(i−1) at empty intervals and right interval [r+1,j] with dummy d_j. Output dummy leaves when j=i−1.

**14.5-2. Seven-key instance.** Run OPTIMAL-BST on the given p and q arrays, report e[1,7], root table and tree. Numerical result to be computed and independently verified.

**14.5-3. Recompute w directly.** Summing probabilities for each interval costs Θ(j−i+1) per state. Across Θ(n²) states, this adds Θ(n³) work; asymptotic time remains Θ(n³), though the constant factor increases.

**14.5-4. Knuth optimization.** Restrict the root search to root[i,j−1]…root[i+1,j], using the monotonicity theorem. The total number of candidate roots across all intervals is O(n²), giving Θ(n²) time. Store a valid root for every interval and handle base intervals separately.

## Problems

**14-1. Longest weighted path in a DAG.** Topologically order vertices. Set d[t]=0 and for vertices in reverse topological order compute d[u]=max_(u,v)∈E(w(u,v)+d[v]); unreachable states are −∞. Store the maximizing successor to reconstruct the path. O(V+E) time and O(V) space.

**14-2. Longest palindromic subsequence.** Let L[i,j] be the LPS length in substring x[i…j]. Base L[i,i]=1; if x[i]=x[j], L[i,j]=2+L[i+1,j−1]; otherwise max(L[i+1,j],L[i,j−1]). Fill by increasing interval length and store choices for reconstruction. O(n²) time and space.

**14-3. Bitonic Euclidean TSP.** Sort points by x. Let B[i,j] be the minimum length of two disjoint paths covering points 1…j whose endpoints are i and j (i<j). Recurrence: B[i,j]=B[i,j−1]+dist(j−1,j) for i<j−1; B[j−1,j]=min_{i<j−1}(B[i,j−1]+dist(i,j)). Answer B[n−1,n]+dist(n−1,n). O(n²) time, O(n) or O(n²) storage depending on reconstruction.

**14-4. Printing neatly.** Precompute badness(i,j)=(M−(j−i)−Σ_{k=i}^j l_k)^3 when the words fit, ∞ otherwise; last line has zero penalty. Let cost[j]=min_{1≤i≤j}(cost[i−1]+badness(i,j)), store the minimizing i, and reconstruct lines. O(n²) time and O(n²) space (or O(n) if badness is computed on demand).

**14-5. Edit distance.** DP over prefixes x[1…i], y[1…j], considering copy, replace, delete, insert, twiddle when adjacent source characters are swapped, and kill as a terminal operation. Add the operation-specific costs and store the best predecessor/action. The recurrence and initialization for kill require a full boundary audit before final sign-off.

**14-6. Company party.** For each employee v, define IN[v]=rating(v)+Σ OUT[child], OUT[v]=Σ max(IN[child],OUT[child]). Reconstruct by choosing IN only when it strictly beats OUT at the parent. O(n) time and space.

**14-7. Viterbi path.** For each time t and vertex v, mark whether a path from v0 to v emits the first t symbols. Transition only along edges labeled symbol t; store predecessor. For most probable path, replace Boolean reachability by max product probability and store the maximizing predecessor. O(kE) time and O(kV) space (or rolling rows plus backpointers).

**14-8. Seam carving.** (a) At each row after the first, at least two continuations exist when n>1, giving at least 2^(m−1) seams. (b) Let D[i,j]=d[i,j]+min(D[i−1,j−1],D[i−1,j],D[i−1,j+1]) over valid columns. Store predecessor; choose the minimum bottom-row endpoint and backtrack. O(mn) time and space.

**14-9. Breaking a string.** Add endpoints 0 and n to sorted break positions. Let c[i,j] be minimum cost to perform all breaks between endpoints i and j; c[i,i+1]=0 and c[i,j]=length(j−i)+min_{i<k<j}(c[i,k]+c[k,j]). Store the minimizing k and reconstruct. O(m³) time and O(m²) space.

**14-10. Investment strategy.** By linearity of returns and a single fixed switch fee, an optimal strategy can place all capital in one investment each year. DP state V[j,i]=maximum wealth after year j when invested in i; transition considers staying (fee f1) or switching from any h≠i (fee f2), then multiply by r_ij. O(Tn²) time, O(Tn) space. Need carefully model fees relative to investment amount and the exact year boundary.

**14-11. Inventory planning.** DP over months and ending inventory: F[i,j]=minimum cost through month i with j machines in inventory. Transition from prior inventory k with production max(0,d_i+j−k), overtime cost c·max(0,production−m), and holding cost h(j). Restrict feasible states 0…D. O(nD²) time and O(nD) space.

**14-12. Free-agent baseball.** This is a multiple-choice knapsack: for each position choose at most one player (or none), with budget X measured in $100,000 units. DP over positions and budget, maximizing total WAR; store choices to reconstruct signings. O(NPX) time and O(NX) space (or O(X) value space plus decision storage).
