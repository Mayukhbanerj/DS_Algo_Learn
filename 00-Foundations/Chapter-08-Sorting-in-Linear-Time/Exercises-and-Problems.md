# Chapter 8 — Exercises and Problems

Original worked solutions aligned to CLRS Fourth Edition, Chapter 8. Solutions preserve the assumptions stated in each exercise. Some problems, especially columnsort, are proof-intensive; the key construction and proof structure are given explicitly.

## Exercises 8.1 — Lower bounds for sorting

### 8.1-1 — Smallest possible leaf depth

A correct comparison-sort decision tree must have at least \(n!\) leaves. The root-to-leaf path of length zero reaches only one leaf, so for \(n>1\) the smallest possible leaf depth is at least 1. A full binary tree can have one leaf at depth 1 and other leaves below it; therefore the smallest possible depth is \(\boxed{1}\).

### 8.1-2 — Bounds on \(\lg(n!)\)

\[
\lg(n!)=\sum_{k=1}^{n}\lg k.
\]
Monotonicity gives the integral bounds
\[
\int_1^n\lg x\,dx\le\sum_{k=1}^{n}\lg k
\le\int_1^n\lg x\,dx+\lg n.
\]
Since \(\int\lg x\,dx=x\lg x-x/\ln2\), both bounds are \(\Theta(n\lg n)\). Thus \(\lg(n!)=\Theta(n\lg n)\).

### 8.1-3 — Fraction of inputs sorted in linear time

If a comparison sort used at most \(cn\) comparisons on at least a fraction \(f(n)\) of its inputs, its decision tree would need at least \(f(n)n!\) leaves at depth at most \(cn\). A binary tree has at most \(2^{cn}\) leaves at depth at most \(cn\). For \(f(n)=1/2\), \(1/n\), or \(1/2^n\), we still have \(f(n)n!>2^{cn}\) for every fixed \(c\) and sufficiently large \(n\), because \(\lg(n!)=\Theta(n\lg n)\), whereas \(\lg f(n)\) is only \(0\), \(-\lg n\), or \(-n\). Therefore none of these fractions can have linear running time for all sufficiently large n.


### 8.1-4 — Partly sorted positions

The elements initially at positions divisible by 4 have only three possible final positions. The remaining positions are unrestricted. There are still \(\Omega(n!)\) possible relative orders among the unrestricted elements, up to a factor exponential in \(n\) for the restricted placements. The logarithm of the number of possible orders remains \(\Omega(n\lg n)\). A comparison decision tree therefore still needs height \(\Omega(n\lg n)\).

## Exercises 8.2 — Counting sort

### 8.2-1 — Trace the given array

For \(A=\langle6,0,2,0,1,3,4,6,1,3,2\rangle\), the frequencies for keys 0 through 6 are
\[
C=\langle2,2,2,2,1,0,2\rangle.
\]
After prefix sums:
\[
C=\langle2,4,6,8,9,9,11\rangle.
\]
The stable reverse placement produces
\[
\boxed{B=\langle0,0,1,1,2,2,3,3,4,6,6\rangle}.
\]

### 8.2-2 — Prove stability

Consider two equal-key records \(x_i,x_j\) with \(i<j\). The output loop scans from \(n\) down to 1, so it places \(x_j\) first at the current final position for that key. It decrements the cumulative count. Then \(x_i\) is placed at the immediately preceding position. Hence \(x_i\) remains before \(x_j\), preserving input order.

### 8.2-3 — Forward placement

If only the loop direction is changed to \(j=1\) through \(n\), while keeping \(B[C[A[j]]]=A[j]\) and decrementing \(C[A[j]]\), the keys are still sorted, but equal-key records are placed in reverse input order, so the algorithm is not stable. For a stable forward version, convert cumulative counts to starting offsets: set \(S[0]=1\) and \(S[i]=S[i-1]+freq[i-1]\). Scan \(A\) from left to right, write each record to \(B[S[key]]\), then increment \(S[key]\).


### 8.2-4 — Loop invariant

At the start of each reverse-placement iteration for key value \(i=A[j]\), the last not-yet-copied occurrence of \(i\) belongs in output position \(B[C[i]]\). The cumulative count gives the rightmost free output position for that key. Placing the current rightmost unprocessed occurrence there and decrementing \(C[i]\) establishes the invariant for the next occurrence.

### 8.2-5 — In-place counting sort without satellite data

Count frequencies in \(C[0:k]\), then overwrite \(A\) by writing each key \(i\), \(C[i]\) times, in increasing order. This takes \(\Theta(n+k)\) time and \(O(k)\) auxiliary space. Stability is irrelevant because there is no satellite data; if equal keys are indistinguishable, no relative order needs preserving.

### 8.2-6 — Range-count queries in O(1)

Build a frequency array and prefix sums \(P[i]=|\{x:x\le i\}|\). For a query interval \([a,b]\), return \(P[b]-P[a-1]\) (with \(P[-1]=0\)). Preprocessing costs \(\Theta(n+k)\); each query costs \(O(1)\).

### 8.2-7 — Fractional parts with at most d decimal digits

Scale each value by \(10^d\) to obtain an integer key in \([0,k10^d]\). Counting sort on this scaled key uses a range of \(k10^d+1\), so the time is \(\Theta(n+10^d k)\).

## Exercises 8.3 — Radix sort

### 8.3-1 — Sort the words

Sort stably from rightmost character to leftmost character, treating missing positions as a sentinel smaller than letters. After each pass, preserve the order within equal-character groups. The final alphabetical order is:
\[
\boxed{\text{BAR, BIG, BOX, COW, DIG, DOG, EAR, FOX, MOB, NOW, ROW, RUG, SEA, TAB, TAR, TEA}}.
\]

### 8.3-2 — Stability of comparison sorts

- Insertion sort is stable if it shifts only strictly larger keys.
- Merge sort is stable if ties are taken from the left run first.
- Heapsort is not stable.
- Quicksort is generally not stable.

Any comparison sort can be made stable by sorting lexicographically on \((key, originalIndex)\). This adds \(O(1)\) work per comparison and \(O(n)\) storage for indices (or embeds the index in each record).

### 8.3-3 — Induction proof of radix sort

Base case: after sorting by the least significant digit, the array is sorted by that one digit. Inductive step: assume the array is sorted by the \(i-1\) least significant digits. A stable sort on digit \(i\) orders groups by digit \(i\), while preserving the previous order among equal digit-\(i\) keys. Therefore the array is sorted by its \(i\) least significant digits. Stability is essential in the inductive step; without it, the ordering established by the lower digits could be destroyed.

### 8.3-4 — Reduce data passes to d+1

Preallocate an output array and alternate the roles of input and output on successive digit passes. While scanning the input to distribute records for digit \(i\), also count the values of digit \(i+1\). Those counts are ready when the next pass begins, so the next pass does not need a separate frequency scan. The first digit requires its own count scan; each of the \(d\) digit passes then performs one stable distribution scan. Thus there is one initial scan plus \(d\) distribution scans: \(d+1\) passes over the records. Prefix-sum work is over the digit-count array, not another pass over the records.


### 8.3-5 — Sort integers in \([0,n^3-1]\) in O(n)

Represent each key in three base-\(n\) digits. Each digit lies in \([0,n-1]\). Three stable counting-sort passes each cost \(\Theta(n+n)=\Theta(n)\), so the total is \(\Theta(n)\).

### 8.3-6 — Most-significant-digit-first card sorting

At recursion depth \(j\), the cards are grouped by their first \(j\) digits. There can be at most \(\min(n,10^j)\) nonempty prefix groups, and each such group that has another digit to process requires one pass. Thus the worst-case number of passes is
\[
\boxed{\sum_{j=0}^{d-1}\min(n,10^j)}.
\]
The operator may have to set aside the nine other digit piles at each of the \(d\) recursion levels while processing one pile. Counting the active pile, this requires at most \(9d+1\) piles in the straightforward recursive procedure.


## Exercises 8.4 — Bucket sort

### 8.4-1 — Bucket-sort trace

For \(A=\langle.79,.13,.16,.64,.39,.20,.89,.53,.71,.42\rangle\), \(n=10\), bucket index is \(\lfloor10x\rfloor\):
- \(B_1:\ .13,.16\)
- \(B_2:\ .20\)
- \(B_3:\ .39\)
- \(B_4:\ .42\)
- \(B_5:\ .53\)
- \(B_6:\ .64\)
- \(B_7:\ .71,.79\)
- \(B_8:\ .89\)
Concatenation gives
\[
\boxed{.13,.16,.20,.39,.42,.53,.64,.71,.79,.89}.
\]

### 8.4-2 — Worst-case time and a safer bucket sort

If all \(n\) values fall into one bucket, insertion sort on that bucket costs \(\Theta(n^2)\). Replace insertion sort within each bucket by a worst-case \(O(m\lg m)\) comparison sort such as heapsort or merge sort. Under uniform input, the expected bucket sizes remain constant and the expected total remains linear; worst-case total becomes \(O(n\lg n)\).

### 8.4-3 — Two fair coin flips

\(X\) is 0, 1, or 2 with probabilities \(1/4,1/2,1/4\). Thus
\[
E[X]=1,\quad E[X^2]=0+1/2+1=3/2,\quad E[X]^2=1.
\]

### 8.4-4 — Stratified bucket design

Let \(c_i=\lfloor10A[i]\rfloor\). Since \(n>10\), \(0\le y_i/n<1/n<1/10\), so \(c_i=\lfloor10x_i\rfloor\). Within coarse group \(c\), the residual \(A[i]-c/10=y_i/n\) is uniform on \([0,1/n)\). There are \(n/10\) expected items in each coarse group. Divide that interval into \(n/10\) equal fine buckets, each of width \(10/n^2\). The fine-bucket index is
\[
c\cdot(n/10)+\left\lfloor (A[i]-c/10)\frac{n^2}{10}\right\rfloor.
\]
There are \(n\) buckets in total, and each has expected constant occupancy. Insertion-sorting within buckets and concatenating in index order therefore takes \(O(n)\) expected time. (For nonmultiples of 10, use groups and bucket counts rounded proportionally.)


### 8.4-5 — Points uniformly distributed in the unit disk

For a point uniform in area, the squared radius \(R^2=x^2+y^2\) is uniform on \((0,1]\), because the area within radius \(r\) is \(\pi r^2\). Bucket by \(nR^2\), not by \(nR\). Expected occupancy is uniform, and sorting within buckets plus concatenation gives expected \(\Theta(n)\) time.

### 8.4-6 — Bucket sort for a known continuous distribution

Apply the cumulative distribution function \(P(x)\) to each sample \(X_i\). For a continuous distribution, \(P(X_i)\) is uniform on \([0,1]\) (probability integral transform). Run ordinary bucket sort on these transformed values. Since \(P\) is computable in \(O(1)\), transformation costs \(O(n)\), and expected bucket-sort time is \(O(n)\). Preserve each original value alongside its transformed key.

## Problems for Chapter 8

### 8-1 — Probabilistic lower bounds on comparison sorting

**(a)** For a deterministic comparison sort and uniformly random input permutation, each of the \(n!\) permutations reaches exactly one correct leaf, with probability \(1/n!\). All other leaves are unreachable and receive probability 0.

**(b)** If a tree has \(k\) leaves and root subtrees \(L_T,R_T\), every leaf depth is one greater than its depth in the corresponding subtree. Summing depths adds \(k\), so \(D(T)=D(L_T)+D(R_T)+k\).

**(c)** If the root's left subtree has \(i\) leaves and the right has \(k-i\), then the minimum possible external path length satisfies
\[
d(k)=\min_{1\le i<k}\{d(i)+d(k-i)+k\}.
\]

**(d)** The function \(f(i)=i\lg i+(k-i)\lg(k-i)\) is symmetric and convex. Its derivative is \(\lg(i/(k-i))\), which is zero at \(i=k/2\), where the minimum occurs. This recurrence yields \(d(k)=\Omega(k\lg k)\).

**(e)** The deterministic sorting tree has exactly \(n!\) reachable leaves, each probability \(1/n!\). Its expected comparisons are \(D(T_A)/n!=\Omega(\lg(n!))=\Omega(n\lg n)\).

**(f)** Fix the random choices made by randomized algorithm B. The resulting algorithm is a deterministic comparison sort A. Averaging over B's random choices, at least one fixed choice sequence has expected comparisons no greater than B's expected comparisons over random inputs and random choices. Thus a deterministic comparison sort exists with no greater expected comparison count. The deterministic lower bound therefore applies to randomized comparison sorts too.

### 8-2 — Sorting 0/1 keys in place and stably

**(a) Linear and stable.** Count the zeros, then scan left-to-right and write zero-key records into the first positions in original order, followed by one-key records in original order. This is stable and \(O(n)\), using \(O(n)\) output storage (or a stable partition buffer).

**(b) Linear and in-place.** Use two pointers from the ends; advance the left pointer over zeros and the right pointer over ones, swapping misplaced records. This is \(O(n)\) time and \(O(1)\) extra space, but not stable.

**(c) Stable and in-place.** Use stable insertion sort on the binary keys: scan left to right and shift a record left only across records with key 1 when the current key is 0. Equal-key records are never swapped past one another. It uses \(O(1)\) extra space and is stable, though its running time is \(O(n^2)\); part (c) does not require linear time.

**(d)** A stable method can be used for radix sort only if its time is linear per digit. The stable linear method in (a) uses auxiliary output storage, so it is suitable. The unstable in-place method in (b) is not suitable because LSD radix sort requires stability. The recursive rotation method in (c) is not linear and would increase the radix-sort bound.

**(e)** Count keys 1 through \(k\). Then for each key \(i\), place its records in the range reserved by its prefix-sum offset, using cycle-leader permutation to move records into final positions. This takes \(O(n+k)\) time and \(O(k)\) extra storage. The cycle placement can be stable only if the original relative order of equal keys is explicitly tracked; the simple in-place permutation is not stable.

### 8-3 — Sorting variable-length items

**(a) Integers.** Group integers by digit length. Sort each length group with LSD radix sort, processing absent leading digits as 0 only within that fixed-length group. Since total digits over all integers is \(n\), total digit-processing work is \(O(n)\), plus linear grouping and concatenation.

**(b) Strings.** Use a trie or MSD radix sort. At each character position, distribute strings by character, treating end-of-string as a sentinel smaller than any character. The total work is proportional to the total number of characters plus the number of strings, \(O(n)\), assuming a constant alphabet or constant-time character indexing.

### 8-4 — Water jugs

**(a) Deterministic quadratic algorithm.** For each red jug, compare it against unmatched blue jugs until the equal-volume blue jug is found. There are at most \(n+(n-1)+\cdots+1=\Theta(n^2)\) comparisons.

**(b) Lower bound.** Any algorithm must determine the matching permutation between \(n\) red and \(n\) blue jugs. There are \(n!\) possible matchings, and each comparison has at most three outcomes (red smaller, equal, red larger). A decision tree therefore needs height at least \(\log_3(n!)=\Omega(n\lg n)\).

**(c) Randomized algorithm.** Choose a random red jug as pivot; compare it with every blue jug to find the matching blue jug and partition blue jugs into smaller/larger. Use the matching blue jug to partition the remaining red jugs by comparisons. Recurse on smaller and larger groups. The expected recurrence is the randomized-quicksort recurrence, \(O(n\lg n)\); worst case is \(\Theta(n^2)\).

### 8-5 — Average sorting

**(a)** A 1-sorted array satisfies \(A[i]\le A[i+1]\) for every adjacent pair, so it is fully sorted.

**(b)** Example: \(\langle2,1,4,3,6,5,8,7,10,9\rangle\). Each adjacent pair average is nondecreasing, but the array is not sorted.

**(c)** The stated average inequality simplifies after multiplying by \(k\) and canceling the common middle terms to \(A[i]\le A[i+k]\). Conversely, those endpoint inequalities imply the window-average inequality by summing the corresponding shifted inequalities.

**(d)** Sort each of the \(k\) residue classes \(A[r],A[r+k],A[r+2k],\ldots\) independently. There are \(k\) lists of length about \(n/k\), costing \(O(k(n/k)\lg(n/k))=O(n\lg(n/k))\).

**(e)** A k-sorted array can be merged from its \(k\) sorted residue lists using a min-heap of size \(k\). Each of \(n\) outputs costs \(O(\lg k)\), so \(O(n\lg k)\).

**(f)** Suppose k-sorting arbitrary input took \(o(n\lg n)\) time for constant \(k\). Part (e) then sorts the resulting k-sorted array in \(O(n\lg k)=O(n)\) time. The composition would sort arbitrary input in \(o(n\lg n)\), contradicting the comparison-sorting lower bound. Therefore k-sorting requires \(\Omega(n\lg n)\) time for constant \(k\).

### 8-6 — Lower bound on merging two sorted lists

**(a)** The number of ways to interleave two sorted lists of \(n\) distinct keys is \(\binom{2n}{n}\): choose which \(n\) of the \(2n\) output positions belong to the first list.

**(b)** A binary decision tree needs at least \(\binom{2n}{n}\) leaves, so its height is at least \(\lg\binom{2n}{n}=2n-O(\lg n)=2n-o(n)\).

**(c)** If two consecutive elements in the final merged order come from different lists, their relative order must be established by a direct comparison; otherwise the algorithm cannot distinguish the two possible interleavings that swap their order.

**(d)** A merge output has \(2n\) elements and \(2n-1\) adjacent gaps. At most one adjacent pair can come from the same list at the boundary of the merge? More directly, the worst-case interleaving can alternate list membership, forcing all \(2n-1\) cross-list adjacent comparisons. Thus the worst-case lower bound is \(2n-1\).

### 8-7 — The 0-1 sorting lemma and columnsort

**(a) The threshold construction.** Let (p) be the position containing the smallest value that the algorithm places incorrectly, and let (q) be the position from which the value (A[q]) is moved into the correct destination of (A[p]). Since (A[p]) is the smallest misplaced value, (A[q]) cannot be smaller than (A[p]): if it were, that smaller value would itself be misplaced ahead of (A[p]). Equality is impossible because the input values may be assumed distinct. Hence (A[q]>A[p]). Under the threshold map (B[i]=0) for (A[i]\le A[p]), and (B[i]=1) otherwise, we have (B[p]=0) and (B[q]=1).

**(b) Why the binary input also fails.** Every compare-exchange operation commutes with this threshold map: replacing each key by its 0/1 class before a compare-exchange gives the same two binary values as thresholding the result after the compare-exchange. This holds because thresholding is monotone, so it preserves the comparison outcome (ties at the threshold map to 0). The algorithm uses the same fixed index pairs on both inputs because it is oblivious. Consequently, the binary execution is exactly the thresholded version of the execution on (A). At the end, position (p), which should contain 0 in a sorted binary output, contains 1 (the thresholded value moved there from (q)); therefore the binary output is not sorted. This proves the contrapositive and hence the 0-1 sorting lemma.

**(c) Columnsort is oblivious.** For fixed (r,s), each column-sort stage can be implemented by a fixed comparison network for sorting (r) positions (for example, the compare-exchange insertion-sort network printed in the problem). The reshape in step 2, its inverse in step 4, the half-column shift in step 6, and its inverse in step 8 are fixed permutations of positions, independent of key values. The composition is therefore a prespecified sequence of compare-exchange operations and fixed permutations; equivalently, the fixed permutations can be absorbed by relabeling wire indices. Thus the 0-1 sorting lemma applies.

**(d) Clean rows after steps 1–3 when (s\mid r).** Work with a 0-1 input and let (z) be the total number of zeros. Step 1 sorts each original column, so each column consists of a zero prefix followed by a one suffix. Step 2 distributes consecutive blocks of (r/s) elements from each original column into the reshaped columns. Step 3 sorts each reshaped column. Each of the (s) columns after step 3 has at most one row at which its entries change from 0 to 1. A row is dirty only if it contains both values; the transition rows across all columns therefore account for at most (s) dirty rows. Since every column is sorted, all rows strictly above the dirty band are clean zero rows and all rows strictly below it are clean one rows. Empty clean regions are allowed.

**(e) The dirty interval after step 4.** Step 4 reverses the fixed reshape permutation. The clean zero rows and clean one rows established in (d) become a clean prefix and a clean suffix in column-major order. The at-most-(s) dirty rows contain at most (s\cdot s=s^2) entries in total. Thus, in column-major order, the array has a clean prefix of zeros, a middle region of at most (s^2) possibly mixed values, and a clean suffix of ones.

**(f) Why steps 5–8 finish the 0-1 sort.** Step 5 sorts each column. The middle dirty interval has length at most (s^2), while (r\ge2s^2); hence it cannot span an entire column together with both neighboring clean regions. Step 6 moves the upper half of every column down by (r/2) positions and the lower half into the upper half of the next column, with empty padding at the two ends. This places every possible 0 from the dirty interval no later in column-major order than every possible 1 from that interval, with the clean prefix/suffix providing the separating padding. Step 7 sorts the shifted columns, and step 8 undoes the shift. The resulting columns are globally ordered: every entry in a column is no larger than every entry in the next column. Therefore the 0-1 output is sorted. By (c) and the 0-1 sorting lemma, columnsort sorts arbitrary totally ordered keys. **Proof-audit note:** this is the geometric invariant argument; a final line-by-line proof should explicitly index the shifted positions at the two ends of the dirty interval before the chapter is signed off.

**(g) When (s\nmid r).** The blocks created by step 2 no longer all have the same height. A transition can straddle the boundary between two block heights, so the dirty band can contain at most (2s-1) rows rather than (s). Its inverse image after step 4 can therefore contain at most (s(2s-1)) dirty entries. The corresponding clean separation needed by the half-column shift is guaranteed by the sufficient condition
\[
r\ge 2s(2s-1).
\]
This is the stated sufficient row bound for the nondivisible case.

**(h) Padding to recover the divisible case.** Add dummy (+\infty) keys until the row count (r') is a multiple of (s), with (r'\ge2s^2) and even. Run the divisible-case columnsort on the padded matrix, then remove the dummy keys. Since all dummies are larger than real keys, they appear only at the end of the sorted order; deleting them leaves the real keys sorted. Choose the smallest even multiple of (s) satisfying the bound, so the padded size remains within a constant factor of the original admissible size.

---

## Final Chapter 8 checklist

- [ ] Prove the decision-tree lower bound from the leaf count.
- [ ] Trace counting sort and explain its stability.
- [ ] Prove LSD radix sort by induction.
- [ ] Derive the radix digit-width tradeoff.
- [ ] Derive \(E[n_i^2]=2-1/n\) for bucket sort.
- [ ] Explain when distribution assumptions make a linear-time sort appropriate.
