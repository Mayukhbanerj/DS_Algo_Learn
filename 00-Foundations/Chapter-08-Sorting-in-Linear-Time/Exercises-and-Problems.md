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

Restrict attention to valid inputs in which every element initially at a position divisible by 4 is already in its final position. The remaining \(m=n-\lfloor n/4\rfloor=\Theta(n)\) elements may appear in any of their \(m!\) orders among the unrestricted positions. A correct comparison decision tree must distinguish all these possibilities, so its height is at least
\[
\lg(m!)=\Theta(m\lg m)=\Theta(n\lg n).
\]
Thus the restriction on every fourth position does not remove the comparison-sorting lower bound.

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

At recursion depth \\(j\\), a pass is needed only for a prefix group containing at least two cards; a singleton is already sorted and needs no further sorting. At most \\(10^j\\) prefixes can occur, and at most \\(\\lfloor n/2\\rfloor\\) groups can each contain at least two cards. The worst-case number of passes is therefore
\\[
\\boxed{\\sum_{j=0}^{d-1}\\min(10^j,\\lfloor n/2\\rfloor)}.
\\]
This bound is attainable by distributing cards among as many distinct prefixes as possible while keeping at least two cards in each group at every level. In the straightforward depth-first procedure, the operator may need to set aside the other nine digit piles at each of the \\(d\\) levels, plus the pile currently being processed, for at most \\(\\boxed{9d+1}\\) piles.



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

Let \\(c_i=\\lfloor10A[i]\\rfloor\\). Since \\(n>10\\), the residual term \\(y_i/n<1/10\\), so \\(c_i=\\lfloor10x_i\\rfloor\\). Within coarse group \\(c\\), the residual is \\(y_i/n\\), with \\(y_i\\) uniform on \\([0,1)\\). Set \\(m=\\lceil n/10\\rceil\\), and divide each coarse group's residual interval \\([0,1/n)\\) into \\(m\\) equal subintervals. Use bucket index
\\[
\\boxed{c_i m+\\lfloor m y_i\\rfloor}
\\]
where \\(y_i=n(A[i]-c_i/10)\\). There are \\(10m=O(n)\\) buckets. Each input element independently lands in any particular bucket with probability \\(1/(10m)\\), so expected occupancy is \\(n/(10m)\\le1\\). The sum of expected squared bucket sizes is therefore \\(O(n)\\), and insertion sort within buckets plus concatenation takes \\(O(n)\\) expected time. The ceiling handles values of \\(n\\) not divisible by 10.

### 8.4-5 — Points uniformly distributed in the unit disk

For a point uniform in area, the squared radius \(R^2=x^2+y^2\) is uniform on \((0,1]\), because the area within radius \(r\) is \(\pi r^2\). Bucket by \(nR^2\), not by \(nR\). Expected occupancy is uniform, and sorting within buckets plus concatenation gives expected \(\Theta(n)\) time.

### 8.4-6 — Bucket sort for a known continuous distribution

The probability-integral transform says that if the cumulative distribution function \(P\) is continuous, then \(U_i=P(X_i)\) is uniform on \([0,1]\). Compute each \(U_i\) in constant time, retain its associated original value \(X_i\), and bucket-sort the pairs by \(U_i\). Since \(P\) is nondecreasing, ordering by \(U_i\) also orders the original values; the transformed samples are uniform, so the expected running time is \(\Theta(n)\).

**Source-wording caveat:** the exercise parenthetical specifically states that, given \(y\), one can find \(x\) with \(P(x)=y\) in \(O(1)\) time—an inverse-CDF operation. The algorithm above needs the forward evaluation \(P(X_i)\) in \(O(1)\) time. An inverse-CDF operation alone does not establish that forward-evaluation bound, so the exercise as printed appears to leave a computational assumption unstated. The probability-integral-transform solution is valid when forward CDF evaluation is also available in constant time.

## Problems for Chapter 8

### 8-1 — Probabilistic lower bounds on comparison sorting

**(a)** For a deterministic comparison sort and uniformly random input permutation, each of the \(n!\) permutations reaches exactly one correct leaf, with probability \(1/n!\). All other leaves are unreachable and receive probability 0.

**(b)** If a tree has \(k\) leaves and root subtrees \(L_T,R_T\), every leaf depth is one greater than its depth in the corresponding subtree. Summing depths adds \(k\), so \(D(T)=D(L_T)+D(R_T)+k\).

**(c)** If the root's left subtree has \(i\) leaves and the right has \(k-i\), then the minimum possible external path length satisfies
\[
d(k)=\min_{1\le i<k}\{d(i)+d(k-i)+k\}.
\]

**(d)** The function \(f(i)=i\lg i+(k-i)\lg(k-i)\) is symmetric and convex. Its derivative is \(\lg(i/(k-i))\), which is zero at \(i=k/2\), where the minimum occurs. The recurrence bound can be made explicit by induction. With \(d(1)=0\), assume \(d(t)\ge t\lg t\) for smaller positive \(t\). Then
\[
d(k)\ge \min_i\{i\lg i+(k-i)\lg(k-i)+k\}
= k\lg(k/2)+k=k\lg k.
\]
Thus \(d(k)\ge k\lg k=\Omega(k\lg k)\).

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

**(d)** Consider the alternating interleaving
\\[
A_1 < B_1 < A_2 < B_2 < \\cdots < A_n < B_n.
\\]
Every one of its \\(2n-1\\) adjacent pairs consists of elements from different lists. By part (c), each such pair must be compared by any correct merging algorithm. Hence some input requires at least \\(\\boxed{2n-1}\\) comparisons.



### 8-7 — The 0-1 sorting lemma and columnsort

**(a) The threshold construction.** Let \(p\) be the position containing the smallest value that the algorithm places incorrectly, and let \(A[q]\) be the value moved into the position where \(A[p]\) belongs. The value \(A[q]\) must be larger than \(A[p]\): if it were smaller, that smaller misplaced value would contradict the choice of \(A[p]\). Distinctness rules out equality. Define \(B[i]=0\) when \(A[i]\le A[p]\), and \(B[i]=1\) otherwise. Then \(B[p]=0\) and the value moved to position \(p\) maps to 1.

**(b) Why the binary input also fails.** Thresholding at \(A[p]\) commutes with compare-exchange: for any pair \(x,y\), sorting \(x,y\) and then mapping each value to its threshold bit gives the same pair as thresholding first and compare-exchanging the two bits. The fixed sequence of compared indices is identical on \(A\) and \(B\), because the algorithm is oblivious. Thus the final binary array is the thresholded final array from the execution on \(A\). The value moved into position \(p\) maps to 1, while the value that belongs there maps to 0. Hence the binary output is not sorted. This proves the contrapositive of the 0-1 sorting lemma.

**(c) Columnsort is oblivious.** For fixed \(r,s\), each column sort can be implemented by a fixed compare-exchange network on the \(r\) positions in that column. Step 2 and step 4 are inverse fixed permutations. Step 6 and step 8 are also inverse fixed permutations (with fixed empty padding positions). None of these index operations depends on key values or earlier comparison outcomes. Relabeling wires through the permutations yields one prespecified compare-exchange sequence, so columnsort is oblivious.

**(d) Clean rows after steps 1–3 when \(s\mid r\).** Consider a 0-1 input. After step 1, each original column is a sequence of 0s followed by 1s, so it has at most one \(0\to1\) transition. In step 2, each original column is laid out as one consecutive block of \(r/s\) rows. Reading that block in row-major order, its only possible within-row transition is the original \(0\to1\) transition; any \(1\to0\) change occurs only at the boundary between consecutive rows. Thus, across the \(s\) blocks, at most \(s\) rows are dirty after step 2.

To see why step 3 leaves at most \(s\) dirty rows, let \(z_j\) be the number of 0s in column \(j\) immediately after step 2. Sorting a column does not change \(z_j\); it merely places those zeros at the top. Every clean row after step 2 is either all 0 or all 1 and therefore contributes equally to every column's zero count. Only the at most \(s\) dirty rows can make the counts \(z_j\) differ. Hence \(\max_j z_j-\min_j z_j\le s\). After step 3, row \(i\) can be dirty only when it lies between the smallest and largest column zero counts. There are therefore at most \(s\) dirty rows, with clean 0-rows above and clean 1-rows below. Either clean region may be empty.

**(e) The dirty interval after step 4.** Step 4 reverses the reshape permutation. The clean zero rows and clean one rows from (d) become a clean prefix and a clean suffix when the array is read in column-major order. There are at most \(s\) dirty rows, each containing \(s\) entries, so the middle dirty region contains at most \(s^2\) elements.

**(f) Why steps 5–8 finish the 0-1 sort.** By (e), immediately after step 4 the column-major sequence is a clean prefix of 0s, followed by one contiguous dirty interval \(D\) of length at most \(s^2\le r/2\), followed by a clean suffix of 1s. Thus \(D\) either lies within one column or crosses exactly one boundary between adjacent columns.

If \(D\) lies within one column, step 5 sorts that column and therefore removes its dirty status. The entire array is then sorted. Steps 6–8 preserve this order: step 6 pairs the lower half of each column with the upper half of the next, step 7 sorts each such pair, and step 8 restores the halves. Since the input to these paired sorts was already globally ordered, restoring the sorted pairs leaves the global order unchanged.

Otherwise, \(D\) crosses from column \(j\) into column \(j+1\). Because \(|D|\le r/2\), its part in column \(j\) is contained in the bottom half of that column, and its part in column \(j+1\) is contained in the top half of that column. Step 5 sorts the columns. The left column has all its 1s confined to its bottom half (its top half is therefore all 0s), and the right column has all its 0s confined to its top half (its bottom half is therefore all 1s). Step 6 moves the bottom half of column \(j\) into the top half of column \(j+1\), and moves the top half of column \(j+1\) into its bottom half. It therefore brings the entire possible disorder into this one column. Step 7 sorts that column, placing all 0s above all 1s. Step 8 reverses step 6. The top half of the sorted joined column returns to the bottom half of column \(j\), and its bottom half returns to the top half of column \(j+1\). Because the joined column is sorted, every value in its top half is no greater than every value in its bottom half. The original top half of column \(j\) is all 0, and the original bottom half of column \(j+1\) is all 1, so the restored boundary is globally ordered. Every other column was already clean and remains in order. The full column-major sequence is therefore sorted. By the 0-1 sorting lemma, columnsort sorts arbitrary distinct keys as well.

**(g) When \(s\nmid r\).** Unequal block heights in step 2 allow the dirty band to expand: the bound becomes at most \(2s-1\) dirty rows. Its inverse image after step 4 can therefore contain at most \(s(2s-1)\) dirty entries. The sufficient row condition given by the problem's analysis is
\[
r\ge 2s(2s-1).
\]
This supplies enough clean separation for the half-column shift and final column sort.

**(h) Modify step 1 by padding each column.** Choose \\(r'\\) to be the smallest positive multiple of \\(\\operatorname{lcm}(s,2)\\) that is at least \\(\\max(r,2s^2)\\):
\\[
r'=\\operatorname{lcm}(s,2)\\left\\lceil\\frac{\\max(r,2s^2)}{\\operatorname{lcm}(s,2)}\\right\\rceil.
\\]
Then \\(r'\\) is even, divisible by \\(s\\), and at least \\(2s^2\\). In step 1, append \\(r'-r\\) dummy keys of value \\( +\\infty\\) to each original column and sort each augmented column. Perform steps 2–8 on this \\(r'\\times s\\) array. The divisible-case columnsort theorem now applies. Since every dummy key is \\( +\\infty\\), all real keys precede all dummy keys in the final sorted order; deleting the dummy keys leaves the original real keys sorted. This modifies only step 1 and ensures all three structural requirements (even row count, \\(s\\mid r'\\), and \\(r'\\ge2s^2\\)) hold.



---

## Final Chapter 8 checklist

- [ ] Prove the decision-tree lower bound from the leaf count.
- [ ] Trace counting sort and explain its stability.
- [ ] Prove LSD radix sort by induction.
- [ ] Derive the radix digit-width tradeoff.
- [ ] Derive \(E[n_i^2]=2-1/n\) for bucket sort.
- [ ] Explain when distribution assumptions make a linear-time sort appropriate.
