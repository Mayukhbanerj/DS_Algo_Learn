# Chapter 2 — Exercises and Problems

These are original study responses based on CLRS Fourth Edition, Chapter 2, not an official solutions manual. See [Chapter 2 notes](README.md) for the underlying concepts and proofs.

## Exercises 2.1

- **2.1-1:** `[31, 41, 59, 26, 41, 58]` sorts to `[26, 31, 41, 41, 58, 59]`.
- **2.1-2:** SUM-ARRAY invariant: at the start of iteration (i), sum equals the sum of (A[1:i-1]). Initialization is the empty sum zero; each iteration adds (A[i]); termination gives the complete sum.
- **2.1-3:** For decreasing order, change the comparison to `A[j] < key`.
- **2.1-4:** Linear search returns a matching index or NIL. Invariant: the scanned prefix contains no target occurrence.
- **2.1-5:** Binary addition, least-significant bit first: compute `total=A[i]+B[i]+carry`, output `total % 2`, update `carry=total // 2`, and store the final carry.

## Exercises 2.2

- **2.2-1:** (n^3/1000+100n^2-100n+3=Theta(n^3)).
- **2.2-2:** Selection sort makes ((n-1)+cdots+1=n(n-1)/2) comparisons, so both best and worst cases are (Theta(n^2)).
- **2.2-3:** Successful linear search with equally likely target positions averages ((n+1)/2) checks. Worst case is (n). Both are (Theta(n)).
- **2.2-4:** Check whether the input is already sorted and return early if it is; the check costs linear time.

## Exercises 2.3

- **2.3-1:** ([3,41,52,26,38,57,9,49]) sorts to ([3,9,26,38,41,49,52,57]).
- **2.3-2:** For a nonempty interval with (p<r), the midpoint gives two nonempty subintervals. Thus no recursive call has (p>r), and testing (p\ne r) suffices under the stated (n\ge1) initial-call condition.
- **2.3-3:** Merge invariant: the output prefix contains the smallest elements of (L) and (R), in sorted order. Each iteration copies the smaller front element; then the remaining sorted suffix is copied.
- **2.3-4:** For (T(2)=2) and (T(n)=2T(n/2)+n), induction proves (T(n)=n\lg n) for powers of 2.
- **2.3-5:** Recursive insertion sort has worst-case recurrence (T(n)=T(n-1)+\Theta(n)), hence (Theta(n^2)).
- **2.3-6:** Binary search repeatedly halves the sorted search interval; worst-case time is (Theta(\lg n)).
- **2.3-7:** Binary search reduces comparisons but not worst-case shifts; insertion sort remains (Theta(n^2)).
- **2.3-8:** Sort, then scan with two pointers. Sorting dominates, giving (Theta(n\lg n)).

## Problems

### 2-1 Insertion sort on small arrays in merge sort

- (a) (n/k) groups of size (k), each costing (Theta(k^2)), total (Theta(nk)).
- (b) Merging costs (Theta(n)) per level for (lg(n/k)) levels, total (Theta(n\lg(n/k))).
- (c) To preserve (Theta(n\lg n)), require (k=O(\lg n)); largest asymptotic order (k=\Theta(\lg n)).
- (d) Benchmark the cutoff on the actual machine and workload.

### 2-2 Correctness of bubblesort

- (a) Prove both sortedness and permutation preservation; finite loop bounds establish termination.
- (b) Inner invariant: (A[j]) is the minimum of suffix (A[j:n]) at the beginning of an inner iteration. The minimum moves left.
- (c) Outer invariant: (A[1:i-1]) contains the (i-1) smallest elements in sorted order.
- (d) The comparison count is (Theta(n^2)), matching insertion sort's worst-case order.

### 2-3 Correctness of Horner's rule

The Horner procedure performs (n+1) iterations, each with constant work, so it takes (Theta(n)). A naive repeated-multiplication evaluation takes (Theta(n^2)). The supplied loop invariant describes the polynomial suffix already accumulated; initialization is the empty sum, the update adds the next coefficient, and termination yields the complete polynomial.

### 2-4 Inversions

- (a) For ([2,3,8,6,1]), position pairs are ((1,5),(2,5),(3,4),(3,5),(4,5)).
- (b) Reverse order has (n(n-1)/2) inversions.
- (c) Each insertion-sort shift corresponds to removing one inversion.
- (d) During merge, when a right element is copied before the current left element, add the number of remaining left elements. The modified merge sort takes (Theta(n\lg n)).
