# Chapter 14 — Exercises and Problems

Original study solutions based on CLRS Fourth Edition, Sections 14.1–14.5. Working solutions are subject to final mathematical and source audit.

## 14.1 Rod cutting

**14.1-1. Call-count recurrence.** T(0)=1 and T(n)=1+Σ_{j=0}^{n−1}T(j). By induction, if T(j)=2^j, then T(n)=1+(2^n−1)=2^n.

**14.1-2. Density-greedy counterexample.** For n=4, take prices p1=1,p2=5,p3=8,p4=9. The best density is length 3 (8/3), so greedy takes 3 then 1 for revenue 9. The optimum is 2+2 for revenue 10.

**14.1-3. Fixed cut cost c.** Let r[0]=0 and r[j]=max(p[i]+r[j−i]−c·I[j−i>0]) for i=1…j. A cut is charged only when a nonempty remainder follows the first piece. O(n²) time.

**14.1-4. Restrict first cut to floor(n/2).** Use r[0]=0 and r[n]=max(p[n], max_{1≤i≤floor(n/2)}(p[i]+r[n−i])). Any nontrivial optimal decomposition has a piece of length at most n/2; choose such a piece as the first cut, and the remainder is optimally cut. The no-cut choice p[n] is handled separately.

**14.1-5. Return an optimal solution.** Store s[j] whenever p[i]+r[j−i] improves r[j]. Reconstruct by repeatedly outputting s[j] and setting j←j−s[j].

**14.1-6. Fibonacci DP.** Set F[0]=0,F[1]=1; for i=2…n set F[i]=F[i−1]+F[i−2]. The subproblem graph has n+1 vertices (0…n) and 2n−1 edges for n≥1: n edges i→i−1 and n−1 edges i→i−2. Time Θ(n), space Θ(n), or O(1) rolling space.

## 14.2 Matrix-chain multiplication

**14.2-1. Dimensions 5,10,3,12,5,50,6.** For p=(5,10,3,12,5,50,6), the minimum cost is 2010 and the optimal parenthesization is ((A1A2)((A3A4)(A5A6))). The upper-triangular m table by rows is: [0,150,330,405,1655,2010]; [0,0,360,330,2430,1950]; [0,0,0,180,930,1770]; [0,0,0,0,3000,1860]; [0,0,0,0,0,1500]; [0,0,0,0,0,0].

**14.2-2. Multiply recursively.** If i=j return A_i. Otherwise k=s[i,j], recursively compute L=MULTIPLY(A,s,i,k), R=MULTIPLY(A,s,k+1,j), and return RECTANGULAR-MATRIX-MULTIPLY(L,R). The recursion performs exactly the multiplications described by the optimal parenthesization.

**14.2-3. Catalan-scale parenthesizations.** The recurrence P(1)=1 and P(n)=Σ_{k=1}^{n−1}P(k)P(n−k) yields Catalan numbers C_(n−1), which are Θ(4^n/n^(3/2)); in particular P(n)=Ω(2^n). A substitution proof with constants remains to be expanded.

**14.2-4. Subproblem graph.** Vertices are index intervals (i,j), 1≤i≤j≤n: n(n+1)/2 vertices. Each interval of length L has 2(L−1) outgoing dependency edges. Thus E=2Σ_(L=2…n)(n−L+1)(L−1)=(n³−n)/3.

**14.2-5. Table-reference count.** A fixed entry m[i,j] is referenced as the left subproblem by each interval [i,b] with b>j (n−j choices), and as the right subproblem by each interval [a,j] with a<i (i−1 choices). Thus it is referenced n−j+i−1 times. Summing over 1≤i≤j≤n gives Σ(n−j+i−1)=n³/3−n/3.

**14.2-6. Parenthesis count.** A full parenthesization of n operands is a full binary expression tree with n leaves and n−1 internal multiplication nodes. Each internal node contributes one pair of parentheses, hence n−1 pairs.

## 14.3 Elements of dynamic programming

**14.3-1. Exhaustive parenthesization vs recursive recurrence.** Enumerating all parenthesizations examines C_(n−1)=Θ(4^n/n^(3/2)) candidates. The recurrence T(1)=1, T(n)=2Σ_(i=1…n−1)T(i)+n implies T(n)=3T(n−1)+1, hence T(n)=Θ(3^n). It is asymptotically more efficient than enumerating all Catalan parenthesizations, Θ(4^n/n^(3/2)), although still exponential; memoization/tabulation reduces this to O(n³).

**14.3-2. Merge-sort recursion tree.** The recursion tree has disjoint subarrays at each level. No identical nontrivial subproblem recurs, so memoization provides no asymptotic benefit and adds table overhead.

**14.3-3. Maximize scalar multiplications.** The problem still has optimal substructure: for a fixed split k, replacing either subchain by a parenthesization with a larger multiplication count improves the total. Use max instead of min in the recurrence.

**14.3-4. Greedy split counterexample.** Choosing k to minimize only p_(i−1)p_kp_j ignores the two subchain costs. For dimensions p=(1,1,2,2,2), the root split products are 2,4,4,4, so the greedy rule uniquely chooses k=1 and produces (A1(A2(A3A4))) with cost 14. The optimal parenthesization is (A1((A2A3)A4)), with cost 10. Thus choosing a split before solving the subchains can be suboptimal.

**14.3-5. Limited piece counts.** The original state “best revenue for length n” is insufficient: the optimal solution for a remainder depends on how many pieces of each length have already been used. For example, let n=6, p1=1,p2=10,p3=9,p4=1,p5=p6=0, with at most two pieces of length 2. The constrained optimum is 2+2+1+1, revenue 22. If the first piece is length 2, the remainder has length 4 but only one length-2 piece remains; its best feasible decomposition is 2+1+1 (revenue 12), whereas the unconstrained length-4 optimum is 2+2 (revenue 20), which is infeasible. Thus remainder length alone does not identify the subproblem; remaining piece limits must be part of the state.

## 14.4 Longest common subsequence

**14.4-1. LCS example.** One LCS is 100110 (length 6). It is a subsequence of both inputs.

**14.4-2. Reconstruct without b table.** Starting at (m,n), if x_i=y_j output that element and move diagonally; otherwise move to the adjacent cell with the same c value (up or left). Reverse the collected output. O(m+n) time.

**14.4-3. Memoized LCS.** Memoize c[i,j] for all prefix pairs; base row/column zero; use the same match/mismatch recurrence. O(mn) states and O(1) work per state, hence O(mn).

**14.4-4. Space reduction.** Keep two rows, swapping current/previous after each i, for 2·min(m,n) entries. One-row version scans j left-to-right while saving the old diagonal value before overwriting c[j−1]; O(min(m,n)) entries plus O(1).

**14.4-5. LIS in O(n²).** Let L[i]=1+max{L[j]:j<i and a_j<a_i}, default 1. Store predecessor; max L[i] is the LIS length. O(n²) time, O(n) space.

**14.4-6. LIS in O(n lg n).** Maintain tails[len] as the smallest possible ending value of an increasing subsequence of that length. For each x, binary-search the first tail≥x, replace it, and store predecessor links for reconstruction. O(n lg n) time.

## 14.5 Optimal binary search trees

**14.5-1. Construct optimal BST.** Recursively create key k_root[i,j] as root; build left interval [i,r−1] with dummy d_(i−1) at empty intervals and right interval [r+1,j] with dummy d_j. Output dummy leaves when j=i−1.

**14.5-2. Seven-key instance.** The optimal expected search cost is 3.12. The root table (0-based indices) is [[0,1,1,1,2,2,4],[–,1,2,2,2,4,4],[–,–,2,2,3,4,4],[–,–,–,3,4,4,5],[–,–,–,–,4,5,5],[–,–,–,–,–,5,6],[–,–,–,–,–,–,6]]. The optimal tree has k5 at the root; k2 is its left child and k7 its right child; k2 has children k1 and k3, k3 has right child k4; k7 has left child k6. Attach the corresponding dummy leaves d0…d7.

**14.5-3. Recompute w directly.** Summing probabilities for each interval costs Θ(j−i+1) per state. Across Θ(n²) states, this adds Θ(n³) work; asymptotic time remains Θ(n³), though the constant factor increases.

**14.5-4. Knuth optimization.** Restrict the root search to root[i,j−1]…root[i+1,j], using the monotonicity theorem. The total number of candidate roots across all intervals is O(n²), giving Θ(n²) time. Store a valid root for every interval and handle base intervals separately.

## Problems

**14-1. Longest weighted path in a DAG.** Topologically order vertices. Set d[t]=0 and for vertices in reverse topological order compute d[u]=max_(u,v)∈E(w(u,v)+d[v]); unreachable states are −∞. Store the maximizing successor to reconstruct the path. O(V+E) time and O(V) space.

**14-2. Longest palindromic subsequence.** Let L[i,j] be the LPS length in substring x[i…j]. Base L[i,i]=1; if x[i]=x[j], L[i,j]=2+L[i+1,j−1]; otherwise max(L[i+1,j],L[i,j−1]). Fill by increasing interval length and store choices for reconstruction. O(n²) time and space.

**14-3. Bitonic Euclidean TSP.** Sort points by x. Let B[i,j] be the minimum length of two disjoint paths covering points 1…j whose endpoints are i and j (i<j). Base B[1,2]=dist(1,2). Recurrence: B[i,j]=B[i,j−1]+dist(j−1,j) for i<j−1; B[j−1,j]=min_{1≤i<j−1}(B[i,j−1]+dist(i,j)). Answer B[n−1,n]+dist(n−1,n). O(n²) time, O(n) or O(n²) storage depending on reconstruction.

**14-4. Printing neatly.** Precompute badness(i,j)=(M−(j−i)−Σ_{k=i}^j l_k)^3 when the words fit, ∞ otherwise; last line has zero penalty. Let cost[j]=min_{1≤i≤j}(cost[i−1]+badness(i,j)), store the minimizing i, and reconstruct lines. O(n²) time and O(n²) space (or O(n) if badness is computed on demand).

**14-5. Edit distance.** Let D[i,j] be the minimum cost to consume x[1…i] and produce y[1…j]. Base D[0,0]=0, D[i,0]=i·QD, D[0,j]=j·QI. Transitions: copy when x_i=y_j with D[i−1,j−1]+QC; replace when x_i≠y_j with D[i−1,j−1]+QR; delete with D[i−1,j]+QD; insert with D[i,j−1]+QI; twiddle if i,j≥2 and x_i=y_(j−1), x_(i−1)=y_j with D[i−2,j−2]+QT. Store the winning operation. Kill is a final alternative min_{0≤i≤m}(D[i,n]+QK), since it consumes all remaining source characters after the target is complete. Reconstruct from the chosen terminal state and predecessor actions. O(mn) time/space. For alignment in part (b), use copy cost −1, replace cost +1, and insert/delete cost +2; omit twiddle and kill.

**14-6. Company party.** For each employee v, define IN[v]=rating(v)+Σ OUT[child], OUT[v]=Σ max(IN[child],OUT[child]). Reconstruct by choosing IN only when it strictly beats OUT at the parent. O(n) time and space.

**14-7. Viterbi path.** For each time t and vertex v, mark whether a path from v0 to v emits the first t symbols. Transition only along edges labeled symbol t; store predecessor. For most probable path, replace Boolean reachability by max product probability and store the maximizing predecessor. O(kE) time and O(kV) space (or rolling rows plus backpointers).

**14-8. Seam carving.** (a) At each row after the first, at least two continuations exist when n>1, giving at least 2^(m−1) seams. (b) Let D[i,j]=d[i,j]+min(D[i−1,j−1],D[i−1,j],D[i−1,j+1]) over valid columns. Store predecessor; choose the minimum bottom-row endpoint and backtrack. O(mn) time and space.

**14-9. Breaking a string.** Add endpoints 0 and n to sorted break positions. Let c[i,j] be minimum cost to perform all breaks between endpoints i and j; c[i,i+1]=0 and c[i,j]=length(j−i)+min_{i<k<j}(c[i,k]+c[k,j]). Store the minimizing k and reconstruct. O(m³) time and O(m²) space.

**14-10. Investment strategy.** By linearity of returns and a single fixed switch fee, an optimal strategy can place all capital in one investment each year. Let V[j,i] be maximum wealth at the end of year j when invested in i. Transition: V[j,i]=max_h(V[j−1,h]·r_(i,j)−(f1 if h=i else f2)). The fee is subtracted at the end of the year, after applying the return. O(Tn²) time and O(Tn) space. (d) With a $15,000 cap per investment, total wealth alone is no longer a sufficient state. For example, two feasible allocations of $20,000 are (A=$15,000,B=$5,000) and (A=$10,000,B=$10,000). If next-year returns are 2 for A and 1 for B, their next-year wealths are $35,000 and $30,000, respectively. The same total wealth therefore has different continuation values depending on its distribution. The allocation vector is part of the state, so the original one-investment optimal-substructure recurrence no longer applies.

**14-11. Inventory planning.** DP over months and ending inventory: F[i,j]=minimum cost through month i with j machines in inventory. Transition from prior inventory k only when d_i+j−k≥0; production is d_i+j−k, overtime cost is c·max(0,production−m), and holding cost is h(j). Restrict feasible states 0…D. O(nD²) time and O(nD) space.

**14-12. Free-agent baseball.** This is a multiple-choice knapsack: for each position choose at most one player (or none), with budget X measured in $100,000 units. DP over positions and budget, maximizing total WAR; store choices to reconstruct signings. O(NPX) time and O(NX) space (or O(X) value space plus decision storage).
