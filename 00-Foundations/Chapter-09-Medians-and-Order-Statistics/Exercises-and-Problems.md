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
Use six comparisons as follows. Compare a with b and c with d, renaming so a≤b and c≤d (2 comparisons). Compare b with d; if needed, swap the two pairs so b≤d (3). Compare b with c (4).
- If b≤c, then a≤b≤c≤d, so the median of the five is the median of b,c,e. Find the median of these three with two comparisons.
- If c<b, then a<b and c<b, while d>b. Thus a and c are both below b and d is above b; the median of all five is the median of b,d,e. Find that median with two comparisons.
Total: 4+2=6 comparisons.

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
For j<k, the exact comparison probability is
\[
E[X_{ijk}]=
\begin{cases}
\dfrac{2}{k-j+1},&j\le i\le k,\\[4pt]
\dfrac{2}{k-i+1},&i<j<k,\\[4pt]
\dfrac{2}{i-j+1},&j<k<i.
\end{cases}
\]
The cases correspond to whether the pair straddles (or touches) the target rank, lies entirely above it, or lies entirely below it. If both keys are on the same side of the target, pivots outside the pair but between the pair and the target can eliminate one or both before the pair is compared; consequently the probability depends on the distance to i, not just on k−j.

Let X_i be the total number of element-to-element comparisons. By linearity of expectation, sum E[X_{ijk}] over all j<k. Splitting the pairs into the three cases gives exactly the upper-bound expression in CLRS part (b):
\[
E[X_i]\le 2\left(
\sum_{j=1}^{i}\sum_{k=i}^{n}\frac{1}{k-j+1}
+\sum_{k=i+1}^{n}\frac{k-i-1}{k-i+1}
+\sum_{j=1}^{i-2}\frac{i-j-1}{i-j+1}
\right).
\]
The first double sum is O(n): for each fixed distance d=k−j, at most d+1 pairs straddle i, and each contributes 1/(d+1), so each distance contributes O(1), across at most n distances. Each of the other two sums has at most n terms, each bounded by 1, and is therefore O(n). CLRS further asks to establish the explicit bound E[X_i]≤4n in part (c); the linear bound above establishes the required O(n) result, while the sharper constant-bound arithmetic is retained for a final line-by-line check. Part (d) follows because each partition's work is proportional to the number of comparisons, giving O(n) expected running time.

### 9-6 — Select with groups of three
(a) For groups of odd size 2t+1 with t≥2, the median-of-medians pivot discards a fixed fraction on both sides. The pivot recursion has size about n/(2t+1), and the selection recursion is bounded by a fraction whose sum with 1/(2t+1) is strictly below 1. The recurrence is linear.

(b) For triples, the first-level medians number n/3. Their median guarantees only about n/3 elements on either side, so the direct recurrence is
\[
T(n)\le T(n/3)+T(2n/3)+O(n),
\]
which yields O(n log n).

(c) SELECT3 repeats grouping one level deeper. First, sort triples and place their medians in the middle third of the array. Next, group those first-level medians into triples, sort each second-level triple, and recursively select the median of the second-level medians. This pivot is a median of medians of medians. Partition the original array around it and recurse only into the side containing rank i.

(d) Let g=n/3 and g'=g/3=n/9 after the preprocessing removes at most eight elements to make the active size divisible by 9. At least about half of the g' second-level medians lie on either side of their median. Each such second-level triple contributes two first-level medians on that side; each first-level median certifies two original elements on that side. Thus at least about 4(g'/2)=2n/9 original elements are guaranteed on either side, up to constant rounding. The recursive selection side has at most 7n/9+O(1) elements, and the pivot-selection recursion has size n/9:
\[
T(n)\le T(n/9)+T(7n/9+O(1))+O(n).
\]
The recursive fractions sum to 8/9<1, so SELECT3 runs in O(n) worst-case time. The exact constant-rounding details should be checked against the line-by-line preprocessing before this proof is considered final.

---

## Audit notes

This is an initial draft, not a completion claim. Detailed proofs still needed include 9.3-5, Problem 9-2(b), Problem 9-5(a)–(d), and Problem 9-6(c)–(d). The exact SELECT3 pseudocode and source diagram must be checked before finalizing those parts.
