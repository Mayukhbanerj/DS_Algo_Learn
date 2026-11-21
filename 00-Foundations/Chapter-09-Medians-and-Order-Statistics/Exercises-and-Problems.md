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
The required worst-case lower bound is \(\lceil 3n/2\rceil-2\). The exercise specifically asks for an adversary/candidate-count proof: track separately the elements still capable of being the minimum and those still capable of being the maximum, and bound how many candidates one comparison can eliminate. The short argument in this draft does not yet establish the parity-sensitive count rigorously, so this proof remains open rather than presenting an incomplete candidate-count sketch as a proof.

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
(c) Partition around the ordinary median and sum the weights strictly below and strictly above it. If the lower-side weight is at least 1/2, recurse on the lower side; if the upper-side weight is greater than 1/2, recurse on the upper side; otherwise the pivot is the weighted median. The strictness matters: the definition requires weight strictly below the answer to be <1/2 and weight strictly above it to be ≤1/2. Each recursive side has at most half the elements, so the total work is O(n).
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
For the explicit constant, the first double sum is at most n: group by d=k−j; for each d there are at most d+1 crossing pairs, each contributing 1/(d+1), so each of the at most n distance classes contributes at most 1. In the second sum, (k−i−1)/(k−i+1)≤1, and there are n−i terms. In the third, (i−j−1)/(i−j+1)≤1, and there are i−2 terms. Thus the expression in (b) is at most 2[n+(n−i)+(i−2)]≤4n. This proves (c). For (d), each partition takes time linear in the active subarray and its comparisons are bounded in expectation by the indicator-variable analysis, so the expected running time is O(n).

### 9-6 — Select with groups of three
(a) For group size 2t+1 with fixed t≥2, each group median certifies t elements on either side. The median of the group medians therefore certifies at least t·(g/2−O(1)) = tn/(2(2t+1))−O(1) elements on either side. The larger selection side is at most (1−t/(2(2t+1)))n+O(1). The pivot recursion has size at most n/(2t+1), and the two recursive fractions sum to
\[
\frac{1}{2t+1}+1-\frac{t}{2(2t+1)}
=1-\frac{t-2}{2(2t+1)}<1
\]
for t>2. For t=2 this is the standard groups-of-five case, whose sharper count gives 9/10. Thus every odd fixed group size at least five gives a linear recurrence.

(b) With groups of three, each group median certifies only one element on either side. The median of the g≈n/3 medians therefore guarantees about n/3 elements on either side, leaving a recursive side of at most 2n/3+O(1). Hence T(n)≤T(n/3)+T(2n/3+O(1))+O(n)=O(n log n).

(c) The supplied SELECT3 pseudocode first removes the minimum repeatedly until the active length is divisible by 9 (returning immediately if rank 1 is wanted). It then divides the active array into triples in a strided layout and sorts each triple. Their medians occupy the middle third. It next sorts triples of those first-level medians; their medians occupy the middle ninth. It recursively selects the median of these second-level medians, partitions the original active array around that pivot, and recurses into only the side containing the requested rank.

(d) Let the post-preprocessing active length be N=9h, so g=N/3=3h first-level triples and g'=g/3=h second-level triples. The recursive pivot is the ceil(h/2)-th second-level median. Excluding the second-level triple containing this pivot, at least ceil(h/2)-1 second-level medians are strictly smaller, and at least floor(h/2) are strictly larger. Each second-level median that is strictly smaller than the pivot has two first-level medians in its second-level triple that are also smaller. Each such first-level median is the median of an original triple, and certifies two original elements strictly smaller than itself. Thus at least 4(ceil(h/2)-1) original active elements are strictly smaller than the pivot. Symmetrically, at least 4 floor(h/2) are strictly larger. Both bounds are at least 2h−4 = 2N/9−4. Therefore, after partitioning, whichever strict side is recursively selected contains at most N−(2N/9−4)−1 = 7N/9+3 elements. The pivot-selection call has h=N/9 elements. Preprocessing removes at most eight elements; its repeated minimum scans cost O(n) total, and changing n to N=n−O(1) affects only additive constants. The recurrence is
\[
T(n)\le T(n/9)+T(7n/9+O(1))+O(n).
\]
Since 1/9+7/9=8/9<1, substitution proves T(n)=O(n) worst case.
---

## Audit notes

The six-comparison construction, simplified randomized-selection recurrence, indicator-variable comparison probabilities, and SELECT3 outline have been expanded. Remaining work is a source-by-source audit of every exercise and problem, including the exact preprocessing/rounding argument in SELECT3 and fuller derivations for the lower-bound and small-order-statistic exercises. This companion is not yet marked complete.
