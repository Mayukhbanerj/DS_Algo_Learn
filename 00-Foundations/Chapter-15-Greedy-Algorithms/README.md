# Chapter 15 — Greedy Algorithms

**Reference:** CLRS, Fourth Edition (2022), Sections 15.1–15.4, printed pages 417–446.

A greedy algorithm repeatedly makes a locally best choice and commits to it, then solves the remaining subproblem. It is not generally optimal. Correctness requires a proof—usually the greedy-choice property plus optimal substructure.

## A practical proof workflow

1. Identify the optimal substructure.
2. State the proposed greedy choice precisely.
3. Prove an exchange argument: some optimal solution can be modified to contain the greedy choice without becoming worse.
4. Show that after this choice, the remaining problem is a smaller instance of the same form.
5. Implement the choices efficiently (sorting, heaps, selection, etc.).

Unlike dynamic programming, a greedy choice is made before solving the remaining subproblem and does not depend on its optimal value.

## 15.1 Activity selection

Each activity i occupies the half-open interval [s_i,f_i). Two activities are compatible if one finishes no later than the other starts. The goal is a maximum-cardinality compatible subset.

### Greedy rule: earliest finish

Sort activities by nondecreasing finish time. Select the first activity, then scan once from left to right, selecting activity i exactly when s_i≥f_last, where last is the most recently selected activity.

Why it is optimal: take any optimal schedule and let a be its first-finishing activity. The greedy activity g finishes no later than a. Replacing a by g preserves compatibility with every later activity and does not reduce the number selected. Thus some optimum begins with g. The remaining compatible activities form the same problem, so induction proves optimality.

The recursive version searches for the first compatible activity and recurses on the suffix. The iterative version maintains the last selected finish time. If input is already sorted, both take Θ(n) time; sorting first costs O(n lg n).

### Other activity-selection variants

- Latest start: scan in nonincreasing start time, choosing the last-starting activity compatible with those already selected. This is the time-reversed symmetric greedy rule.
- Minimum lecture halls (interval partitioning): sort by start time and assign each activity to a hall whose current finish time is earliest, if that finish≤the new start; otherwise open a new hall. A min-heap of hall finish times gives O(n lg n). The number of halls used equals the maximum number of simultaneous overlapping activities, which is a lower bound on any schedule.
- Weighted activities: sort by finish time. Let p(j) be the largest i<j with f_i≤s_j. Set OPT[0]=0 and OPT[j]=max(v_j+OPT[p(j)],OPT[j−1]). Store choices to reconstruct. Binary search computes all p(j) in O(n lg n); DP takes O(n).

## 15.2 Elements of the greedy strategy

### Greedy-choice property
A globally optimal solution exists that begins with the greedy choice. The exchange proof typically takes an optimal solution, replaces one of its choices with the greedy choice, and shows feasibility and no worse objective value.

### Optimal substructure
After making the greedy choice, the remainder must be an optimal solution to the remaining subproblem. Otherwise replacing it with a better remainder would improve the original solution.

### Fractional knapsack
Each item has value v_i and weight w_i; fractions are allowed. Sort by density v_i/w_i in nonincreasing order and take as much as possible from each item until capacity W is filled. An exchange argument proves optimality: if a solution takes weight from a lower-density item while a higher-density item is not full, shifting a small amount of weight upward increases value. Sorting dominates at O(n lg n). With linear-time selection by density, the optimum can be found in O(n).

This rule does not solve 0-1 knapsack: an item cannot be split, and leaving unused capacity can make the highest-density item a poor choice. The 0-1 problem has a dynamic-programming solution O(nW).

## 15.3 Huffman codes

A binary prefix-free code has no codeword that is a prefix of another. Its code tree is a full binary tree: characters label leaves, and left/right edges represent 0/1. Decoding is unambiguous because every codeword ends at a leaf.

If character c has frequency f_c and its leaf depth is d_T(c), the total encoded length is

B(T)=Σ_c f_c d_T(c).

### Huffman's algorithm

1. Put every character in a min-priority queue keyed by frequency.
2. Repeatedly extract the two minimum-frequency trees x and y.
3. Create a new internal node z with children x and y and frequency f_x+f_y.
4. Insert z into the queue.
5. The final remaining node is the root.

There are n−1 merges. With a binary min-heap, initialization is O(n), each merge uses two extracts and one insert, and total time is O(n lg n).

### Correctness structure

- Greedy-choice property: the two least-frequent characters can be siblings at maximum depth in some optimal tree. Swap them with two deepest sibling leaves; because the least frequencies are no larger and the depths are no smaller, the swaps do not increase cost.
- Optimal substructure: merge the two least-frequent characters x,y into a pseudo-character z with frequency f_z=f_x+f_y. An optimal code for the reduced alphabet expands to an optimal code for the original alphabet by replacing z with an internal node whose children are x,y.
- The cost of the final tree equals the sum of the frequencies merged at every internal node.

## 15.4 Offline caching

A cache holds at most k blocks and begins empty. A request is a hit if its block is present; otherwise it is a miss, and a full cache must evict one block.

When the entire request sequence is known in advance, the optimal offline policy is **furthest-in-future**: on a full-cache miss, evict the cached block whose next request is latest (or which is never requested again).

The greedy-choice proof exchanges the victim chosen by an arbitrary optimum with the furthest-in-future victim. Until the furthest block is next needed, the two cache configurations differ by at most one block; the exchange cannot increase misses, and after that request the configurations can be made identical. Optimal substructure then completes the proof.

A simple implementation scans the cache on each miss and computes each block's next-use index, taking O(nk) time. Precomputed next-occurrence positions plus a max-heap can improve practical performance.

Offline optimal caching is a benchmark, not a realistic online policy: real caches do not know future requests. LRU is a practical online heuristic but is not always optimal.

## Visual aids

- [Activity-selection exchange argument](images/activity-selection-exchange.svg)
- [Huffman merge step](images/huffman-merge.svg)

## Engineering checklist

- State tie-breaking explicitly; many greedy optima are not unique.
- Separate proof of the greedy choice from proof of optimal substructure.
- Sort once when the greedy rule needs an order; avoid repeated sorting.
- Use heaps for changing minimum/maximum priorities.
- Distinguish fractional and indivisible decisions (fractional vs 0-1 knapsack).
- For Huffman, validate prefix-freeness and compute weighted path length.
- For caching, handle blocks never used again as having next-use index +∞.
