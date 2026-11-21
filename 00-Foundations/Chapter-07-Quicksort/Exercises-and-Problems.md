# Chapter 7 — Exercises and Problems

Original worked solutions aligned to CLRS Fourth Edition, Chapter 7. The textbook uses 1-based indexing; Python uses 0-based indexing.

## Exercises 7.1 — Description of quicksort

### 7.1-1 — PARTITION trace

Input \(\langle13,19,9,5,12,8,7,4,21,2,6,11\rangle\), pivot \(x=11\). The scan places 9, 5, 8, 7, 4, 2, and 6 into the low side in that order. After the final pivot exchange:
\[
\boxed{\langle9,5,8,7,4,2,6,11,21,13,19,12\rangle}
\]
The pivot index is \(q=8\) (1-based). Every key to its left is at most 11; every key to its right is greater than 11.

### 7.1-2 — All elements equal

With all values equal to pivot \(x\), the test \(A[j]\le x\) always succeeds. Each iteration increments \(i\), so the pivot is returned at \(q=r\). To return \(q=\lfloor(p+r)/2\rfloor\) in this special case, first test whether all elements equal \(A[p]\). If so, return the midpoint; otherwise run ordinary PARTITION. The check is linear, so the asymptotic partition cost remains \(\Theta(n)\).

### 7.1-3 — Running time of PARTITION

The loop visits each of the \(n-1\) nonpivot elements exactly once. Each iteration performs constant work, and the final exchange is constant work. Thus \(T(n)=an+b=\Theta(n)\).

### 7.1-4 — Decreasing-order quicksort

Reverse the partition comparison: place values greater than or equal to the pivot on the left and smaller values on the right. Recursively sort both sides in decreasing order. Alternatively sort ascending and reverse the result in a separate linear pass.

## Exercises 7.2 — Performance of quicksort

### 7.2-1 — Solve \(T(n)=T(n-1)+\Theta(n)\)

For constants \(a,b>0\), suppose \(an\le f(n)\le bn\) for sufficiently large \(n\). Expanding gives \(T(n)=T(0)+\sum_{i=1}^{n}f(i)\). Since \(\sum_{i=1}^n i=n(n+1)/2=\Theta(n^2)\), we obtain \(T(n)=\Theta(n^2)\).

### 7.2-2 — All keys equal

With the textbook PARTITION test \(A[j]\le x\), every item goes to the low side. The pivot ends at \(r\), leaving subarrays of sizes \(n-1\) and 0. The recurrence is \(T(n)=T(n-1)+\Theta(n)\), hence \(\Theta(n^2)\).

### 7.2-3 — Decreasing sorted input

For distinct keys in decreasing order, the final element is the minimum. PARTITION returns the first index, leaving subproblems of sizes 0 and \(n-1\). Each call scans the remaining subarray, so the total is \(\Theta(n^2)\).

### 7.2-4 — Almost-sorted transactions

Insertion sort is adaptive to the number of inversions. If checks are already close to check-number order, each element moves only a small distance and insertion sort performs near-linear work. Quicksort still partitions active subarrays and can be sensitive to input order; a poor deterministic pivot can cause quadratic time. Insertion sort can therefore win on this workload.

### 7.2-5 — Leaf depths for constant split proportions

If the low and high proportions are \(\alpha\) and \(\beta\), with \(0<\alpha\le\beta<1\) and \(\alpha+\beta=1\), repeatedly following the smaller side reaches a leaf after approximately \(\log_{1/\alpha}n\) levels; following the larger side takes approximately \(\log_{1/\beta}n\) levels. Ignore integer rounding.

### 7.2-6 — Probability of a sufficiently balanced split

The pivot rank is uniform over the \(n\) ranks. A split at least as balanced as \((1-\alpha)\)-to-\(\alpha\) occurs when the pivot rank lies between approximately \(\alpha n\) and \((1-\alpha)n\). There are approximately \((1-2\alpha)n\) such ranks, so the probability is
\[
\boxed{1-2\alpha}.
\]

## Exercises 7.3 — A randomized version of quicksort

### 7.3-1 — Why expected time?

The worst-case time remains \(\Theta(n^2)\), but it depends on an unlikely sequence of poor random pivots. Randomization makes expected performance independent of the input's original order. Expected time captures typical performance over the algorithm's random choices.

### 7.3-2 — Calls to RANDOM

Every nontrivial recursive call makes one random-pivot selection. A quicksort recursion tree with \(n\) distinct elements has \(n\) pivot placements (one per element, with the last singleton/base calls not partitioned); hence both best- and worst-case counts are \(\Theta(n)\).

## Exercises 7.4 — Analysis of quicksort

### 7.4-1 — Quadratic lower bound

The maximum includes \(q=0\), so \(T(n)\ge T(n-1)+\Theta(n)\). Summing yields \(T(n)=\Omega(n^2)\).

### 7.4-2 — Best-case lower bound

Every level of a balanced recursion processes a total of \(\Theta(n)\) elements, and there are \(\Theta(\lg n)\) levels. Therefore best-case time is \(\Omega(n\lg n)\). The balanced recurrence supplies the matching upper bound, so it is \(\Theta(n\lg n)\).

### 7.4-3 — Maximum of the sum of squares

\[
q^2+(n-1-q)^2=(n-1)^2-2q(n-1-q)\le(n-1)^2.
\]
Equality holds at \(q=0\) or \(q=n-1\), where the product is zero.

### 7.4-4 — Expected-time lower bound

From the pairwise comparison analysis, the expected number of comparisons is
\[
E[X]=\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}\frac{2}{j-i+1}.
\]
For each \(i\), substitute \(k=j-i+1\). The inner sum is \(\sum_{k=2}^{n-i+1}2/k=\Theta(\lg(n-i+1))\). Summing over \(i\) gives \(\Theta(n\lg n)\), since a constant fraction of the \(i\)-values have \(n-i+1\ge n/2\). Thus the expected comparisons, and hence expected running time, are \(\Omega(n\lg n)\). Theorem 7.4 gives the matching \(O(n\lg n)\) upper bound.

### 7.4-5 — Insertion sort for subarrays smaller than k

Stop partitioning below size \(k\), and sort the leaves with insertion sort. The upper partition levels contribute expected \(O(n\lg(n/k))\) work. The leaf subarrays contain \(n\) elements total and each has fewer than \(k\) elements, so insertion-sort work is \(O(nk)\). Total:
\[
\boxed{O(nk+n\lg(n/k))}.
\]
Theory favors a small constant cutoff to retain \(O(n\lg n)\); practice requires benchmarking because call overhead and cache behavior affect the best threshold.

### 7.4-6 — Probability for median-of-three

For rank \(i\), the median of a 3-element sample equals that key when the sample contains one lower key, the key itself, and one higher key. Thus
\[
p_i=\frac{(i-1)(n-i)}{\binom n3/3}
=\frac{6(i-1)(n-i)}{n(n-1)(n-2)},\quad 2\le i\le n-1,
\]
and \(p_1=p_n=0\). The exact median has probability asymptotic to \(3/(2n)\), versus \(1/n\) for uniform pivot selection, a limiting ratio \(3/2\). For a good split with \(\alpha n\le i\le(1-\alpha)n\), the limiting probability is
\[
\int_\alpha^{1-\alpha}6x(1-x)\,dx=1-6\alpha^2+4\alpha^3.
\]
Uniform selection gives \(1-2\alpha\). The improvement changes constants, not the expected \(\Theta(n\lg n)\) order.

## Problems for Chapter 7

### 7-1 — Hoare partition correctness

**(a) Trace.** Input \(\langle13,19,9,5,12,8,7,4,11,2,6,21\rangle\), pivot \(x=13\), with 1-based indices. Initially \(i=0,j=13\).

| Iteration | Right scan | Left scan | Action and resulting array | \(i,j\) |
|---|---|---|---|---|
| 1 | Stops at 6, position 11 | Stops at pivot 13, position 1 | Exchange positions 1 and 11: \(\langle6,19,9,5,12,8,7,4,11,2,13,21\rangle\) | \(1,11\) |
| 2 | Stops at 2, position 10 | Stops at 19, position 2 | Exchange positions 2 and 10: \(\langle6,2,9,5,12,8,7,4,11,19,13,21\rangle\) | \(2,10\) |
| 3 | Stops at 11, position 9 | Stops at 19, position 10 | Scans cross; return \(j=9\), no exchange | \(10,9\) |

The returned boundary is \(j=9\). Every value in \(A[1:9]\) is at most 13 and every value in \(A[10:12]\) is at least 13.

**(b) Equal keys.** With all keys equal, Lomuto PARTITION sends every scanned value to the low side and returns \(r\), producing a maximally unbalanced split. Hoare partition advances both scans inward and returns a middle boundary. This is advantageous for duplicate-heavy data.

**(c) No out-of-range access.** The pivot \(A[p]=x\) stops the left scan no later than \(p\). The right scan begins at \(r+1\) and decrements before testing. The pivot and crossing condition bound both scans within \(p,\ldots,r\).

**(d) Return range.** With at least two elements, the scans cross only after the right scan has stopped at or above \(p\); the return boundary is at least \(p\). The crossing condition ensures it is strictly less than \(r\). Thus \(p\le j<r\).

**(e) Partition property.** Maintain that every element in \(A[p:i-1]\) is at most \(x\), and every element in \(A[j+1:r]\) is at least \(x\). A misplaced pair is exchanged, expanding both classified regions. When the scans cross, the regions cover the subarray and every left-side element is at most every right-side element.

**(f) Quicksort with Hoare partition.**

    HOARE-QUICKSORT(A, p, r)
        if p < r
            q = HOARE-PARTITION(A, p, r)
            HOARE-QUICKSORT(A, p, q)
            HOARE-QUICKSORT(A, q + 1, r)

Hoare partition returns a boundary, not the final pivot position, so both recursive ranges include their respective boundary sides.

### 7-2 — Quicksort with equal element values

**(a)** If all keys are equal, Lomuto PARTITION returns the final index every time. Randomized quicksort still recurses on sizes \(n-1\) and 0, so its time is \(\Theta(n^2)\).

**(b)** Use three-way partitioning with regions less than pivot, equal to pivot, unknown, and greater than pivot. If the current value is smaller, swap it into the low region and advance both low and scan indices; if equal, advance scan; if greater, swap it with the last unknown value and shrink the unknown region without advancing scan. Return the inclusive equal-region endpoints. Each item is examined a constant number of times, so the partition is linear.

**(c)** RANDOMIZED-PARTITION' chooses a uniform random pivot, moves it to the pivot position, and calls the three-way partition. QUICKSORT' recurses only on the less-than and greater-than regions, skipping the equal block.

**(d)** With \(m\) distinct key values, the recursion is over distinct-key classes and each partition scans the current items. The expected bound is \(O(n\lg m+n)\); when all values are equal, one linear partition finishes the work. This removes the distinct-key limitation of the two-way expected-comparison analysis.

### 7-3 — Alternative quicksort analysis

**(a)** Every one of the \(n\) elements is equally likely to be the pivot, so \(P(X_i=1)=1/n\) and \(E[X_i]=1/n\).

**(b)** Condition on pivot rank \(q\). The subarrays have sizes \(q-1\) and \(n-q\), and partitioning costs \(\Theta(n)\). Summing over the mutually exclusive pivot-rank indicators yields the stated expectation identity.

**(c)** By symmetry and re-indexing the sum:
\[
E[T(n)]=\frac{2}{n}\sum_{q=1}^{n-1}E[T(q)]+\Theta(n).
\]

**(d)** Split the sum at \(\lceil n/2\rceil\), bound the logarithm by \(\lg n\), and pair the upper and lower halves. The resulting estimate is
\[
\sum_{q=1}^{n-1}q\lg q\le\frac{n^2}{2}\lg n-\frac{n^2}{8},\quad n\ge2.
\]

**(e)** Substitute \(E[T(q)]\le aq\lg q\) into the recurrence. Part (d) gives
\[
E[T(n)]\le an\lg n-\frac{a}{4}n+cn.
\]
Choose \(a\ge4c\); then the final two terms are nonpositive, proving \(E[T(n)]=O(n\lg n)\).

### 7-4 — Stooge sort

**(a)** Exchange the endpoints if they are out of order, then recursively sort the first two-thirds, last two-thirds, and first two-thirds again. The first call puts the minimum in the prefix; the second puts the maximum in the suffix; the third orders the prefix. Induction proves correctness.

**(b)** Three recursive calls each operate on approximately \(2n/3\) elements:
\[
T(n)=3T(2n/3)+\Theta(1)=\Theta(n^{\log_{3/2}3}).
\]

**(c)** Since \(\log_{3/2}3\approx2.7095\), stooge sort is asymptotically slower than insertion sort's quadratic worst case and much slower than \(n\lg n\) sorts.

### 7-5 — Stack depth for quicksort

**(a)** Repeated extreme pivots create recursive sizes \(n-1,n-2,\ldots,1\), so stack depth is \(\Theta(n)\).

**(b)** Tail-recursion elimination still recurses on the low side. If that side has size \(n-1\) each time, stack depth remains \(\Theta(n)\).

**(c)** Recurse on the smaller side and iterate over the larger:

    BOUNDED-STACK-QUICKSORT(A, p, r)
        while p < r
            q = PARTITION(A, p, r)
            if q - p < r - q
                BOUNDED-STACK-QUICKSORT(A, p, q - 1)
                p = q + 1
            else
                BOUNDED-STACK-QUICKSORT(A, q + 1, r)
                r = q - 1

Each recursive call receives at most half the elements of its caller, so stack depth is \(O(\lg n)\). Partition work is unchanged, preserving expected \(O(n\lg n)\) time.

### 7-6 — Median-of-three partition

**(a)** For rank \(i\), choose one sample key below it, the key itself, and one above it. There are \((i-1)(n-i)\) such 3-subsets out of \(\binom n3\), so
\[
p_i=\frac{6(i-1)(n-i)}{n(n-1)(n-2)},\quad 2\le i\le n-1.
\]

**(b)** For the median rank \(i\approx n/2\), \(p_i\approx3/(2n)\). Uniform random selection has probability \(1/n\), so the limiting ratio is \(3/2\).

**(c)** For a good split, approximate the rank sum by
\[
\int_\alpha^{1-\alpha}6x(1-x)\,dx=1-6\alpha^2+4\alpha^3.
\]
Ordinary random selection gives \(1-2\alpha\).

**(d)** Median-of-three changes the distribution of split sizes and the constants in the expected comparison count. It does not change the expected \(\Theta(n\lg n)\) order.

### 7-7 — Fuzzy sorting of intervals

Choose a random pivot interval \(I\). Maintain the intersection \(J\) of the pivot and intervals overlapping it, updating \(J=[\max a_i,\min b_i]\). Partition intervals into those wholly left of \(J\), those intersecting \(J\), and those wholly right of \(J\). Recurse on the left and right groups; the middle intervals can be placed in any order because each contains a point in \(J\).

**Correctness:** Every left interval ends before every point in \(J\), and every right interval starts after every point in \(J\). Each middle interval contains a point in \(J\). Choose one such point for each middle interval and concatenate the recursively sorted left group, middle group, and right group. The representative points are nondecreasing.

**Expected time:** Partitioning costs \(\Theta(n)\) and the general expected recursion has the randomized-quicksort \(O(n\lg n)\) bound. If all intervals overlap, their common intersection is nonempty and all intervals enter the middle group after one linear pass, giving \(\Theta(n)\) expected time.

---

## Final Chapter 7 checklist

- [ ] Re-derive PARTITION invariant without notes.
- [ ] Trace Lomuto and Hoare partition by hand.
- [ ] Explain the constant-proportion recursion-tree argument.
- [ ] Derive pairwise comparison probability \(2/(j-i+1)\).
- [ ] Implement three-way partitioning for duplicate keys.
- [ ] Prove the smaller-side recursion stack bound.
- [ ] Review median-of-three and fuzzy sorting.
