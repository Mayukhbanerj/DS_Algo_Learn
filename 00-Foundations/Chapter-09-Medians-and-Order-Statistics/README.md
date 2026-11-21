# Chapter 9 — Medians and Order Statistics

**Reference:** CLRS, *Introduction to Algorithms*, Fourth Edition (2022), Chapter 9, printed pages 227–247.

Selection returns the element of a set having a specified rank, not the entire sorted order. The minimum has rank 1, the maximum rank n, and CLRS consistently calls the lower median the median: rank floor((n+1)/2). The chapter assumes distinct keys for analysis; the algorithms generally extend to duplicates.

## Learning objectives
- Prove the optimal n−1 comparison bound for minimum or maximum.
- Find both extrema in at most 3 floor(n/2) comparisons.
- Explain randomized selection and its expected linear-time proof.
- Implement median-of-medians selection with a worst-case linear bound.
- Distinguish selection from sorting: selection need not order every pair.

## 9.1 Minimum and maximum

A scan initialized with A[1] finds the minimum in n−1 comparisons. This is optimal: every nonminimum element must lose at least one comparison, and one comparison can make at most one new element a known loser. The same argument applies to maximum.

### Simultaneous minimum and maximum
The independent algorithms use 2n−2 comparisons. A better method processes pairs:
1. If n is odd, initialize both extrema to the first element. If n is even, compare the first two elements once to initialize them.
2. For each remaining pair, compare its members.
3. Compare the smaller with the current minimum and the larger with the current maximum.

Each pair costs three comparisons. The total is 3 floor(n/2): for odd n, 3(n−1)/2; for even n, 1+3(n−2)/2=3n/2−2.

## 9.2 Selection in expected linear time

Partition the active subarray around a uniformly random pivot. Let k be the pivot's rank within that subarray. If i=k, return it; if i<k, recurse only left with rank i; otherwise recurse only right with rank i−k. Unlike quicksort, selection follows one partition side.

Worst case is Θ(n²), when every pivot is an extreme. Expected time is Θ(n).

### Helpful partitionings
CLRS calls a partition helpful when at most 3n/4 elements remain in play. Its middle half excludes the smallest and largest ceil(n/4)−1 ranks. A pivot in this middle half discards at least ceil(n/4) elements, leaving at most floor(3n/4). The probability of missing the middle half is at most
2(ceil(n/4)−1)/n ≤ 1/2.
Thus each partition is helpful with probability at least 1/2.

### Expected-time proof by generations
Group partitionings into generations, each beginning with a helpful partition. If generation k begins with n_k active elements, then n_k ≤ (3/4)^k n. The number X_k of partitionings in a generation is bounded in expectation by a geometric waiting time with success probability at least 1/2, so E[X_k]≤2. Each partition costs at most n_k comparisons:
E[C_n] ≤ Σ E[X_k](3/4)^k n ≤ 2n Σ(3/4)^k = 8n.
The first partition costs Ω(n), so expected running time is Θ(n).

## 9.3 Selection in worst-case linear time

Median-of-medians SELECT guarantees a sufficiently balanced pivot:
1. Remove up to four minima until the active size is divisible by five, returning immediately if rank 1 is requested.
2. Divide the remaining elements into groups of five (CLRS uses a strided layout).
3. Sort each group and collect its median.
4. Recursively select the median of the group medians.
5. Partition around that pivot and recurse only into the side containing the requested rank.

With g=n/5 groups, at least about half the group medians are on either side of the pivot. Each such group contributes its median and two elements on the same side. Thus at least about 3n/10 elements are guaranteed on each side, up to rounding, and the larger recursive side has at most 7n/10+O(1) elements.

T(n) ≤ T(ceil(n/5))+T(7n/10+O(1))+O(n).
The recursive fractions sum to 9/10<1, so substitution gives T(n)=O(n). The group sorting/partition work is Ω(n), hence T(n)=Θ(n) worst case.

## Algorithm choice

| Method | Worst case | Expected case |
|---|---:|---:|
| Sort, then index | Θ(n log n) | depends on sort |
| Randomized select | Θ(n²) | Θ(n) |
| Median of medians | Θ(n) | Θ(n) |

## Engineering notes
- Define rank conventions explicitly: CLRS is 1-based; Python indexing is 0-based.
- Partition-based selection mutates the array; copy it if callers require original order.
- For duplicates, use a three-way partition (< pivot, = pivot, > pivot) to avoid repeatedly processing equal keys. CLRS's core analysis assumes distinct keys.
- Randomized pivots should use a sound pseudorandom generator; do not confuse randomization with a deterministic pivot rule.

**Status:** Initial source-aligned draft. Companion solutions, implementations, and proof audit are in progress.
