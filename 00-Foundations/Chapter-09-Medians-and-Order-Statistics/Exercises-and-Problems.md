# Chapter 9 — Exercises and Problems

Original explanations aligned to CLRS Fourth Edition. The core analysis assumes distinct keys.

## Exercises 9.1 — Minimum and maximum

### 9.1-1 — Second smallest
Run a tournament to find the minimum, recording every element that loses directly to it. The second smallest must be among those direct losers. In a balanced tournament there are at most ceil(log₂ n) direct opponents. Find the minimum among them. Total comparisons: (n−1)+(ceil(log₂ n)−1)=n+ceil(log₂ n)−2.

### 9.1-2 — Neither minimum nor maximum
Compare any three distinct elements and return their median. Three comparisons suffice to order the triple. Fewer than three comparisons cannot guarantee that one element has both a smaller and a larger witness. Minimum: 3.

### 9.1-3 — Fastest three horses
Run five heats of five, then race the five heat winners (six races). Let the winners be A1 through E1 in order. Eliminate heats D and E; eliminate A4,A5; B3,B4,B5; and C2,C3,C4,C5. The remaining candidates for second and third are A2,A3,B1,B2,C1. Race these five once; the top two are second and third overall. Total: 7 races.

### 9.1-4 — Lower bound for simultaneous extrema
Initially all n elements could be either extreme. A comparison can eliminate the larger from being minimum and the smaller from being maximum. Counting the required eliminations yields ceil(3n/2)−2 comparisons. The pairwise algorithm in Section 9.1 meets this bound.

## Exercises 9.2 — Expected-linear selection

### 9.2-1 — No empty recursive call
The pivot belongs to the current nonempty subarray. If the requested rank is below the pivot rank, the lower partition must be nonempty; otherwise the pivot rank would be 1. Symmetrically, a request above the pivot rank implies a nonempty upper partition.

### 9.2-2 — Iterative version
Maintain p,r,i in a loop. Randomly partition; compute k=q−p+1. Return if i=k; set r=q−1 if i<k; otherwise set p=q+1 and i=i−k. When p=r, return A[p]. Recursion is eliminated without changing asymptotic bounds.

### 9.2-3 — Worst case for minimum
Repeatedly choose the maximum remaining element as pivot. Each partition removes only that maximum, leaving the minimum in play. For the given input, one possible pivot order is 9,8,7,6,5,4,3,2,1, then return 0. The work is quadratic.

### 9.2-4 — Permutation independence
A random pivot position selects each rank with probability 1/n, regardless of the physical order of distinct keys. After partitioning, the same property holds recursively. Induction on subarray size shows expected comparison count depends on n and i, not the input permutation.

## Exercises 9.3 — Worst-case linear selection

### 9.3-1 — Groups of seven
The median-of-seven pivot guarantees at least three elements per full group on either side, apart from the pivot group and rounding. The larger side is at most 5n/7+O(1). T(n)≤T(n/7)+T(5n/7+O(1))+O(n), whose recursive fractions sum to 6/7<1; hence Θ(n).

### 9.3-2 — Constant-size preprocessing
Use a direct base case for n≤n₀, form floor(n/5) complete groups, and leave fewer than five elements ungrouped. The recurrence is T(n)≤T(floor(n/5))+T(7n/10+O(1))+O(n). The constant leftovers do not change linearity.

### 9.3-3 — Worst-case O(n log n) quicksort
Use SELECT to find the median, partition around it, then recursively sort both sides. Q(n)≤2Q(n/2)+O(n)=O(n log n).

### 9.3-4 — Recover both sides without more comparisons
Retain the comparison/partition history from selection. The partition already establishes which elements are below and above the selected key. Traverse the partitioned array to list them; no further key comparisons are needed.

### 9.3-5 — Median of five
The exercise asks for a six-comparison method. A detailed decision-tree trace is still required; do not treat a generic sort of five (which may use more comparisons) as a solution.

### 9.3-6 — Selection with a median black box
Find the median in linear time, partition around it, and recurse only into the side containing rank i, adjusting the rank on the upper side. Each level discards at least half, so total partition work is n+n/2+n/4+…=O(n).

### 9.3-7 — One-dimensional pipeline
The objective is Σ|y_i−y|. A median y-coordinate minimizes the sum of absolute deviations. Select that median in linear time; x-coordinates do not affect north-south spur lengths.

### 9.3-8 — k-quantiles
Recursively select the middle quantile boundary, partition, and recurse on both portions with their assigned quantile counts. At each recursion depth the total partitioning work is O(n), and there are O(log k) levels, giving O(n log k).

### 9.3-9 — k values closest to the median
Find median m, compute |x−m| for each element, and use SELECT to find the kth smallest distance. Partition by that threshold and return k values. O(n), with a tie policy needed if distances tie.

### 9.3-10 — Median of two sorted arrays
Binary-search a partition i in X and j=n−i in Y so the left halves contain n values and every left value is smaller than every right value. Compare the two boundary pairs to move i. The overall median is the average of the largest left and smallest right values. O(log n).

## Problems for Chapter 9

### 9-1 — Largest i values
(a) Sort all: O(n log n). (b) Build max-heap and extract i times: O(n+i log n). (c) Select the (n−i+1)th smallest threshold, partition, then sort the i largest: O(n+i log i) worst case with deterministic SELECT.

### 9-2 — Simplified randomized select
(a) If pivot rank equals i, the simplified procedure recurses on a subarray that still includes the pivot and may repeat the same size; worst-case nontermination is possible.
(b) Let T(n,i) be expected time for rank i. A uniform pivot rank k gives T(n,i) ≤ an + (1/n)[Σ(k=1 to i−1) T(n−k,i−k) + Σ(k=i to n) T(k,i)]. The k=n term is T(n,i), with coefficient 1/n; move it to the left. Assuming inductively T(m,j)≤cm for m<n, the sum of recursive subproblem sizes is Σ(k=1 to i−1)(n−k)+Σ(k=i to n)k = n(n+1)/2+(i−1)n−i(i−1) ≤ 3n²/4+O(n). After moving the self-term left, choosing c sufficiently larger than a proves T(n,i)=O(n).

### 9-3 — Weighted median
(a) Equal weights 1/n make the weighted-median condition the ordinary lower-median condition.
(b) Sort by key and scan cumulative weights: O(n log n).
(c) Partition around ordinary median; sum weights on each side and recurse into a side whose total exceeds 1/2, otherwise the pivot is the weighted median. Each step discards at least half: O(n).
(d) In one dimension, weighted absolute-deviation cost is minimized at a weighted median.
(e) Under Manhattan distance, x and y contributions separate; choose weighted medians independently for each coordinate.

### 9-4 — Small order statistics
Pair elements and retain the smaller from each pair, then recurse among those candidates. The recurrence is U_i(n)=S(n) for i≥n/2, otherwise floor(n/2)+U_i(ceil(n/2))+S(2i). Repeated halving yields n+O(S(2i) log(n/i)); for constant i, n+O(log n).

### 9-5 — Indicator analysis of randomized selection
The exact probability depends on the target rank i as well as the pair j<k; it cannot be inferred merely from the first pivot in [j,k], because earlier pivots outside that interval may eliminate both keys before they are compared. The source's part (b) gives a specific three-sum upper bound for E[X_i]. I am retaining this exercise as an open proof item until the piecewise cases in (a) are derived and checked against that exact expression, rather than inserting an unverified probability formula.

### 9-6 — Groups of three
(a) For any odd group size greater than 3, the guaranteed discard fraction makes the recursive fractions sum to less than 1, yielding worst-case linear time.
(b) Groups of three give the direct recurrence with recursive fractions summing to 1, hence O(n log n).
(c)–(d) CLRS supplies SELECT3: form triples, then triples of their medians, and recursively select among second-level medians. Its detailed invariant, diagram, and linear recurrence remain to be completed.

---

## Audit notes

This is an initial draft, not a completion claim. Detailed proofs still needed include 9.3-5, Problem 9-2(b), Problem 9-5(a)–(d), and Problem 9-6(c)–(d). The exact SELECT3 pseudocode and source diagram must be checked before finalizing those parts.
