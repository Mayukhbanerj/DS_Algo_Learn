# Chapter 2 — Exercises and Problems

Original worked explanations based on CLRS Fourth Edition, Chapter 2. These are study solutions, not an official solutions manual.

## Exercises 2.1 — Insertion sort and basic procedures

### 2.1-1 — Trace insertion sort
Input: \(\langle31,41,59,26,41,58\rangle\).

Show the array after each outer-loop insertion:

| Stage | Array |
|---|---|
| Initial | 31, 41, 59, 26, 41, 58 |
| Insert 41 | 31, 41, 59, 26, 41, 58 |
| Insert 59 | 31, 41, 59, 26, 41, 58 |
| Insert 26 | 26, 31, 41, 59, 41, 58 |
| Insert second 41 | 26, 31, 41, 41, 59, 58 |
| Insert 58 | 26, 31, 41, 41, 58, 59 |

The final array is sorted and contains exactly the original values, including both occurrences of 41.

### 2.1-2 — SUM-ARRAY loop invariant
Procedure:
`SUM-ARRAY(A,n)`: initialize sum to zero; for (i=1,ldots,n), add (A[i]); return sum.

**Invariant:** At the start of iteration (i), the variable (	ext{sum}) equals \(\sum_{k=1}^{i-1}A[k]\).

- **Initialization:** Before iteration 1, no elements have been processed. The empty sum is 0, matching the initialized variable.
- **Maintenance:** Assume the invariant at the start of iteration (i). The body adds (A[i]), so the new value is \(\sum_{k=1}^{i}A[k]\). This is the invariant required at the start of iteration (i+1).
- **Termination:** After the loop, the counter has passed (n). The accumulated sum is \(\sum_{k=1}^{n}A[k]\), which is the required result.

### 2.1-3 — Decreasing insertion sort
To sort in monotonically decreasing order, reverse the comparison in the while condition:
`while j > 0 and A[j] < key`.
Move smaller values one position right and insert the key before them. The loop invariant becomes: the prefix already processed contains the original prefix's elements in nonincreasing order.

### 2.1-4 — Linear search and proof
```text
LINEAR-SEARCH(A, n, x)
1  for i = 1 to n
2      if A[i] == x
3          return i
4  return NIL
```

**Invariant:** At the start of each iteration (i), none of the positions \(1,\ldots,i-1\) contains (x).

- **Initialization:** Before (i=1), the examined prefix is empty, so it contains no occurrence of (x).
- **Maintenance:** If (A[i]=x), the procedure correctly returns (i). Otherwise position (i) also does not contain (x), so the invariant holds for the next iteration.
- **Termination:** If the loop finishes, all positions 1 through (n) have been examined and none contains (x); returning NIL is correct.

### 2.1-5 — Adding binary integers
The arrays are least-significant-bit first: \(a=\sum_{i=0}^{n-1}A[i]2^i\) and similarly for (b\). The result has (n+1) bits.

```text
ADD-BINARY-INTEGERS(A, B, n)
1  let C[0:n] be a new array
2  carry = 0
3  for i = 0 to n - 1
4      total = A[i] + B[i] + carry
5      C[i] = total mod 2
6      carry = floor(total / 2)
7  C[n] = carry
8  return C
```

At each bit, the total is 0, 1, 2, or 3. The remainder is the output bit and the quotient is the carry. The algorithm performs \(\Theta(n)\) work and returns all (n+1) bits, including a possible final carry.

## Exercises 2.2 — Analyzing algorithms

### RAM model
The chapter uses a one-processor random-access machine model: instructions execute sequentially; each primitive instruction and each data access is treated as constant time. Typical operations include arithmetic, data movement, and control flow. Array indexing is constant time under the model.

This is an abstraction. It does not model cache or virtual-memory behavior, and it must not be abused by assuming unrealistic primitive operations (for example, a single instruction that sorts an arbitrary array). The model assumes a bounded word size, commonly proportional to \(\lg n\), so that input indices fit in a word without allowing an arbitrarily large amount of data to be packed into one word.

### Input size
The input-size measure depends on the problem:
- Sorting: number of items.
- Integer multiplication: number of bits representing the integers.
- Graph algorithms: often both vertices and edges.

### Statement-count analysis of insertion sort
Let (t_i) be the number of times the while-condition is tested for a fixed outer-loop value (i). The while-body executes (t_i-1) times because the final test fails. Assign constant cost (c_k) to each executable line (k). The total can be expressed as:
[
T(n)=c_1n+c_2(n-1)+c_4(n-1)+c_5\sum_{i=2}^{n}t_i
+(c_6+c_7)\sum_{i=2}^{n}(t_i-1)+c_8(n-1).
]
The exact constants depend on the cost model, but the execution counts expose the dependence on the input.

**Best case:** the input is already sorted, so (t_i=1). The while-body never executes, and the running time is linear:
[
T(n)=an+b=\Theta(n).
]

**Worst case:** the input is reverse sorted, so (t_i=i). The relevant sums are:
[
\sum_{i=2}^{n}i=\frac{n(n+1)}2-1,
\qquad
\sum_{i=2}^{n}(i-1)=\frac{n(n-1)}2.
]
The leading term is quadratic:
[
T(n)=an^2+bn+c=\Theta(n^2).
]

**Why worst-case analysis:** it gives a bound that applies to every input of a given size; worst-case inputs can occur in practice; and average-case analysis needs an explicit probability model for inputs. For random permutations, insertion sort still has quadratic expected running time.

### 2.2-1 — Order of growth
For
[
\frac{n^3}{1000}+100n^2-100n+3,
]
the cubic term dominates for sufficiently large (n). Therefore:
[
\boxed{\Theta(n^3)}.
]

### 2.2-2 — Selection sort
For each position (i=1,ldots,n-1), scan the remaining suffix to find its minimum and exchange it into position (i). The comparison count is:
[
(n-1)+(n-2)+\cdots+1=\frac{n(n-1)}2.
]
The count does not depend on the initial order, so best- and worst-case running times are both \(\Theta(n^2)\). The algorithm uses \(\Theta(1)\) auxiliary space.

### 2.2-3 — Linear search
If a successful target is equally likely to occupy any of the (n) positions, the expected number of inspected elements is:
[
\frac{1+2+\cdots+n}{n}=\frac{n+1}{2}.
]
The worst case requires (n) inspections. Both are \(\Theta(n)\). If the target may be absent, the unsuccessful case also requires (n) inspections.

### 2.2-4 — Best-case improvement
Add a preliminary pass that checks whether the array is already sorted. If it is, return immediately. This makes the best case linear (the check itself examines the array), while the worst case remains quadratic because an unsorted input still requires insertion sort.

## Exercises 2.3 — Designing algorithms

### 2.3-1 — Merge-sort trace
Starting with \(\langle3,41,52,26,38,57,9,49\rangle\), recursively split into singletons and merge sorted adjacent groups:
- Pairs: \(\langle3,41\rangle,\langle26,52\rangle,\langle38,57\rangle,\langle9,49\rangle\).
- Groups of four: \(\langle3,26,41,52\rangle\) and \(\langle9,38,49,57\rangle\).
- Final merge: \(\boxed{\langle3,9,26,38,41,49,52,57\rangle}\).

### 2.3-2 — Why (p\ne r) is sufficient under the condition
The textbook's procedure tests (p\le r). Suppose the initial call is MERGE-SORT(A,1,n) with (n\ge1). Then initially (p\le r). A recursive call is made only when (p<r). The midpoint (q=\lfloor(p+r)/2\rfloor) satisfies (p\le q<r), so both child intervals ([p,q]) and ([q+1,r]) are nonempty and have valid ordered bounds. Thus no recursive call can have (p>r). Under this initial-call condition, the base test (p\ne r) distinguishes the one-element case from a larger interval, and is sufficient. The condition (n\ge1) matters: an initially empty interval would have (p>r).

### 2.3-3 — MERGE loop invariant and correctness
For the main loop (while both temporary arrays still contain elements), use this invariant:

**At the start of each iteration,** the prefix \(A[p:k-1]\) contains, in sorted order, the \(k-p\) smallest elements of the multiset formed by the original elements in (L) and (R); the unmerged suffixes of (L) and (R), together with that output prefix, contain exactly the original elements.

- **Initialization:** Initially (k=p), so the output prefix is empty. It is sorted and contains the zero smallest elements. All original values are in (L) and (R).
- **Maintenance:** The first unmerged element of each temporary array is its smallest remaining value. The algorithm copies the smaller of these two values to (A[k]), increments the corresponding pointer and (k), and therefore appends the smallest remaining value. Sorted order and the multiset accounting are preserved.
- **Termination:** The loop stops when at least one temporary array is exhausted. The output prefix is sorted and contains the smallest values already selected. The remaining elements in the other array are already sorted and are no smaller than the last selected value; copying that remainder with the appropriate final while loop preserves sorted order and copies every original element exactly once.
Therefore MERGE returns the original multiset in sorted order.

### 2.3-4 — Induction for the recurrence
For powers of two (n\ge2):
[
T(n)=
\begin{cases}
2,&n=2,\\
2T(n/2)+n,&n>2.
\end{cases}
]
Claim: (T(n)=n\lg n).

- **Base:** (n=2): (T(2)=2=2\lg2).
- **Inductive hypothesis:** Assume (T(n/2)=(n/2)\lg(n/2)).
- **Step:**
[
T(n)=2\left(\frac n2\lg\frac n2\right)+n
=n(\lg n-1)+n=n\lg n.
]
Thus the claim holds for all powers of two (n\ge2).

### 2.3-5 — Recursive insertion sort
```text
RECURSIVE-INSERTION-SORT(A, n)
1  if n <= 1
2      return
3  RECURSIVE-INSERTION-SORT(A, n - 1)
4  key = A[n]
5  insert key into sorted A[1:n-1] by shifting larger elements right
```
The recursive call sorts the first (n-1) elements. Inserting the last key can require shifting up to (n-1) elements, so the worst-case recurrence is:
[
T(n)=T(n-1)+\Theta(n),\quad T(1)=\Theta(1).
]
Expanding the sum gives \(\Theta(1+2+\cdots+n)=\Theta(n^2)\).

### 2.3-6 — Binary search
For a sorted array, maintain an interval that may contain the target:
```text
BINARY-SEARCH(A, low, high, x)
1  while low <= high
2      mid = floor((low + high) / 2)
3      if A[mid] == x
4          return mid
5      if A[mid] > x
6          high = mid - 1
7      else
8          low = mid + 1
9  return NIL
```
Each iteration discards at least half the remaining interval. After (k) iterations its size is at most approximately (n/2^k). The interval becomes empty after \(\Theta(\lg n)\) iterations, so worst-case time is \(\Theta(\lg n)\).

### 2.3-7 — Does binary search make insertion sort (Theta(n\lg n))?
No. Binary search can reduce the number of comparisons needed to find the insertion position, but insertion sort must still shift elements to make room. In the reverse-sorted case, the total number of shifts is:
[
1+2+\cdots+(n-1)=\Theta(n^2).
]
Therefore the overall worst-case running time remains \(\Theta(n^2)\).

### 2.3-8 — Two elements summing to (x)
Sort the (n) integers, then use two pointers:
- (i) starts at the smallest element; (j) starts at the largest.
- If (A[i]+A[j]=x), report success.
- If the sum is too small, increment (i).
- If the sum is too large, decrement (j).
Stop when (i\ge j). Sorting costs \(\Theta(n\lg n)\); the two-pointer scan costs \(\Theta(n)\). Total worst-case time is \(\Theta(n\lg n)\).

## Problems

### 2-1 — Insertion sort on small arrays in merge sort
Assume for the analysis that (k) divides (n), as in the stated (n/k) sublists.

**(a)** There are (n/k) sublists, each of length (k). Worst-case insertion sort costs \(\Theta(k^2)\) per sublist. Thus:
[
\frac nk\Theta(k^2)=\boxed{\Theta(nk)}.
]

**(b)** There are \(\lg(n/k)\) merge levels (up to floor/ceiling effects). Each level processes (n) elements in total, so each level costs \(\Theta(n)\). Total:
[
\boxed{\Theta(n\lg(n/k))}.
]

**(c)** The stated total is \(\Theta(nk+n\lg(n/k))\). To keep this within \(\Theta(n\lg n)\), the insertion-sort term must satisfy (nk=O(n\lg n)), hence (k=O(\lg n)). The largest asymptotic order allowed is:
[
\boxed{k=\Theta(\lg n)}.
]

**(d)** Choose the numeric cutoff empirically on the target machine and implementation. Benchmark representative data and workloads; account for cache behavior, allocation overhead, language/runtime costs, and data distribution. The asymptotic argument determines an order, not the best machine-specific constant.

### 2-2 — Correctness of bubblesort

Given:
```text
BUBBLESORT(A, n)
1  for i = 1 to n - 1
2      for j = n downto i + 1
3          if A[j] < A[j - 1]
4              exchange A[j] with A[j - 1]
```

**(a)** Sortedness alone is not enough to prove sorting correctness: an algorithm could output a sorted array while losing or inventing values. Also prove that the output is a permutation of the input. The loops have finite bounds, so the procedure terminates.

**(b) Inner-loop invariant:** At the start of an iteration with index (j), (A[j]) is the minimum value in the suffix (A[j:n]).
- Initialization: for (j=n), the suffix contains only (A[n]), so the claim holds.
- Maintenance: compare (A[j]) with (A[j-1]). If (A[j]) is smaller, swap; otherwise the smaller value is already at (A[j-1]). In either case, after the iteration the minimum of the old suffix is at (A[j-1]), which is the value considered by the next iteration.
- Termination: when the loop finishes at (j=i), the minimum of (A[i:n]) has been moved to (A[i]).

**(c) Outer-loop invariant:** At the start of iteration (i), the prefix (A[1:i-1]) contains the (i-1) smallest input elements in nondecreasing order. Initialization is the empty prefix. By part (b), the inner loop moves the minimum of the remaining suffix into (A[i]), extending the sorted prefix by one. At termination, the prefix is the entire array, proving the required sortedness.

**Permutation preservation:** Every modification is an exchange of two array elements; exchanges preserve the multiset of values. Combined with sortedness and termination, this proves correctness.

**(d)** The inner loop performs (n-i) comparisons for outer iteration (i). Total:
[
\sum_{i=1}^{n-1}(n-i)=\frac{n(n-1)}2=\Theta(n^2).
]
This is the same worst-case order as insertion sort. The comparison count of bubblesort is quadratic regardless of input order.

### 2-3 — Correctness of Horner's rule

The polynomial is:
[
P(x)=\sum_{k=0}^{n}a_kx^k
=a_0+x(a_1+x(a_2+\cdots+x(a_{n-1}+xa_n)\cdots)).
]

Procedure:
```text
HORNER(A, n, x)
1  p = 0
2  for i = n downto 0
3      p = A[i] + x * p
4  return p
```

**(a)** The loop executes (n+1) times with constant work per iteration, so time is \(\Theta(n)\).

**(b)** A direct algorithm computes each power from scratch:
```text
NAIVE-POLYNOMIAL(A, n, x)
1  total = 0
2  for k = 0 to n
3      power = 1
4      for j = 1 to k
5          power = power * x
6      total = total + A[k] * power
7  return total
```
The inner multiplications total \(\sum_{k=0}^{n}k=\Theta(n^2)\), so this implementation is \(\Theta(n^2)\), compared with Horner's \(\Theta(n)\).

**(c) Loop-invariant proof.** At the start of iteration (i):
[
p=\sum_{k=0}^{n-(i+1)}A[k+i+1]x^k.
]
- Initialization: for (i=n), the upper limit is (-1), so the sum is empty and equals 0, matching the initial (p).
- Maintenance: assume the invariant at the start of iteration (i). The update (p=A[i]+xp) gives:
[
p=A[i]+\sum_{k=0}^{n-i-1}A[k+i+1]x^{k+1}
=\sum_{k=0}^{n-i}A[k+i]x^k,
]
after reindexing the sum. This is precisely the invariant for the next iteration, whose index is (i-1).
- Termination: after processing (i=0), the accumulated value is \(\sum_{k=0}^{n}A[k]x^k\), the required polynomial value.

### 2-4 — Inversions

An inversion is a pair of positions \((i,j)\) such that (i<j) and (A[i]>A[j]).

**(a)** For \(\langle2,3,8,6,1\rangle\), the five position pairs are:
[
\boxed{(1,5),(2,5),(3,4),(3,5),(4,5)}.
]
Their corresponding value pairs are \((2,1),(3,1),(8,6),(8,1),(6,1)\).

**(b)** The reverse-sorted permutation \(\langle n,n-1,\ldots,1\rangle\) has every pair inverted, so the maximum is:
[
\boxed{\binom n2=\frac{n(n-1)}2}.
]

**(c)** In insertion sort, each shift moves a larger element one position to the right past the key being inserted. Each such shift removes one inversion involving that key. Across the entire algorithm, the number of shifts equals the initial inversion count. The running time is therefore \(\Theta(n+I)\), where (I) is the number of inversions (the linear term accounts for loop/control overhead). Thus sorted input ((I=0)) takes linear time, while reverse order ((I=\binom n2)) takes quadratic time.

**(d)** Modify merge sort to count inversions. Recursively count inversions in the left and right halves. During merge, when the next right-half element is strictly smaller than the current left-half element, it forms an inversion with every remaining element in the left half; add the number of remaining left elements to the count. Merge still costs \(\Theta(n)\), so:
[
T(n)=2T(n/2)+\Theta(n)=\boxed{\Theta(n\lg n)}.
]

## Chapter 2 final revision checklist
- [ ] Reproduce insertion sort and explain the playing-card analogy.
- [ ] State and prove the outer-loop invariant (initialization, maintenance, termination).
- [ ] Explain every pseudocode convention used in this chapter.
- [ ] Explain the RAM model, word-size assumption, and its limitations.
- [ ] Derive the insertion-sort statement-count expression and best/worst cases.
- [ ] Explain why worst-case analysis is useful and why average-case analysis needs a probability model.
- [ ] Explain order of growth and the role of leading terms.
- [ ] State the divide/conquer/combine framework.
- [ ] Explain MERGE, its three indices, and why every element is copied once.
- [ ] State the merge-sort recurrence and explain the recursion-tree cost at every level.
- [ ] Work through all exercises 2.1-1 to 2.3-8 and Problems 2-1 to 2-4 independently.
