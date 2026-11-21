# Chapter 6 — Exercises and Problems

Original worked solutions aligned to CLRS Fourth Edition, Chapter 6. The textbook uses 1-based heap indexing. These are study explanations, not an official solutions manual.

## Exercises 6.1 — Heaps

### 6.1-1 — Minimum and maximum nodes at height h

A heap of height \(h\) has all levels \(0,\ldots,h-1\) full, so the minimum number of nodes is
\[
1+2+\cdots+2^{h-1}+1=2^h.
\]
The maximum is a full binary tree through level \(h\):
\[
1+2+\cdots+2^h=2^{h+1}-1.
\]
Thus the range is \(\boxed{2^h\le n\le2^{h+1}-1}\).

### 6.1-2 — Height of an n-element heap

For height \(h\), the node count satisfies \(2^h\le n\le2^{h+1}-1\). Taking logarithms gives \(h\le\lg n<h+1\), so
\[
\boxed{h=\lfloor\lg n\rfloor}.
\]

### 6.1-3 — Root of a max-heap subtree

For every node, its value is at least the values of its children. Repeatedly applying this inequality along any downward path shows that the subtree root is at least every descendant. Therefore it contains the largest value in that subtree.

### 6.1-4 — Location of the smallest element

The smallest element can occur only at a leaf. If it were at an internal node, it would be no greater than its children, while the max-heap property says it is no smaller than them. With distinct keys this is impossible. Any leaf is a possible location.

### 6.1-5 — Possible levels of the kth largest key

Every ancestor of a node has a strictly larger key when all keys are distinct. A node at depth \(d\) therefore has at least \(d\) larger keys. For it to be the \(k\)-th largest, \(d\le k-1\). Thus it can occur only at levels \(0,1,\ldots,k-1\), subject to the tree's actual height.

### 6.1-6 — Is an increasing sorted array a min-heap?

Yes. In a 1-based increasing array, \(A[i]\le A[2i]\) and \(A[i]\le A[2i+1]\) whenever the children exist, because child indices exceed the parent index. This is the min-heap property.

### 6.1-7 — Test the supplied array

For \(A=\langle33,19,20,15,13,10,2,13,16,12\rangle\), check each internal node:
- \(33\ge19,20\)
- \(19\ge15,13\)
- \(20\ge10,2\)
- \(15\ge13,16\) is false because \(15<16\).

Therefore it is **not** a max-heap.

### 6.1-8 — Leaf indices

A node \(i\) has a left child exactly when \(2i\le n\), or \(i\le\lfloor n/2\rfloor\). Every node with index at most \(\lfloor n/2\rfloor\) is internal; every larger index has no children. Hence the leaves are
\[
\boxed{\lfloor n/2\rfloor+1,\ldots,n}.
\]

## Exercises 6.2 — Maintaining the heap property

### 6.2-1 — MAX-HEAPIFY(A, 3)

Start with \(A=\langle27,17,3,16,13,10,1,5,7,12,4,8,9,0\rangle\). At index 3, compare 3 with children 10 and 1; swap with 10:
\[
\langle27,17,10,16,13,3,1,5,7,12,4,8,9,0\rangle.
\]
At index 6, compare 3 with 8 and 9; swap with 9:
\[
\boxed{\langle27,17,10,16,13,9,1,5,7,12,4,8,3,0\rangle}.
\]
Index 13 is a leaf, so stop.

### 6.2-2 — Child subtree size and alpha

The larger child subtree is the left subtree. In a complete binary tree it contains at most \(\lfloor2n/3\rfloor\) nodes, while the right subtree contains no more. Thus \(\alpha=2/3\) is the smallest constant that works for all heap sizes (asymptotically). The recurrence \(T(n)\le T(2n/3)+\Theta(1)\) solves to \(O(\lg n)\).

### 6.2-3 — MIN-HEAPIFY

    MIN-HEAPIFY(A, i)
        l = LEFT(i); r = RIGHT(i); smallest = i
        if l <= A.heap_size and A[l] < A[smallest]
            smallest = l
        if r <= A.heap_size and A[r] < A[smallest]
            smallest = r
        if smallest != i
            exchange A[i] with A[smallest]
            MIN-HEAPIFY(A, smallest)

It follows one downward path, so its running time is \(O(\lg n)\), the same as MAX-HEAPIFY.

### 6.2-4 — A[i] is already larger than both children

MAX-HEAPIFY makes no exchange and returns immediately. The subtree already satisfies the max-heap property at its root, given the precondition that the child subtrees are heaps.

### 6.2-5 — Calling MAX-HEAPIFY on a leaf

For \(i>\lfloor A.heap\text{-}size/2\rfloor\), index \(i\) is a leaf. Both child indices exceed heap_size, so no exchange occurs. The procedure returns immediately.

### 6.2-6 — Iterative MAX-HEAPIFY

    MAX-HEAPIFY-ITERATIVE(A, i)
        while true
            l = LEFT(i); r = RIGHT(i); largest = i
            if l <= A.heap_size and A[l] > A[largest]
                largest = l
            if r <= A.heap_size and A[r] > A[largest]
                largest = r
            if largest == i
                return
            exchange A[i] with A[largest]
            i = largest

The loop follows the same path as the recursive procedure and performs \(O(\lg n)\) work using \(O(1)\) extra space.

### 6.2-7 — Tight worst-case bound

Choose keys so that at every node on a root-to-leaf path, the child on that path is larger than the other child, and the value initially at the root is smaller than every node on the path. MAX-HEAPIFY swaps at each level until it reaches a leaf. A complete heap has a root-to-leaf path of length \(\lfloor\lg n\rfloor\), so it performs \(\Omega(\lg n)\) work. Together with the upper bound, the worst case is \(\boxed{\Theta(\lg n)}\).

## Exercises 6.3 — Building a heap

### 6.3-1 — BUILD-MAX-HEAP example

Input: \(\langle5,3,17,10,84,19,6,22,9\rangle\). Start at \(i=\lfloor9/2\rfloor=4\):
- \(i=4\): swap 10 with child 22.
- \(i=3\): swap 17 with child 19.
- \(i=2\): swap 3 with 84.
- \(i=1\): swap 5 with 84, then 22, then 10.

The final max-heap is
\[
\boxed{\langle84,22,19,10,3,17,6,5,9\rangle}.
\]

### 6.3-2 — Show the ceiling is at least one-half

For \(h\le\lfloor\lg n\rfloor\), \(2^h\le n\), so \(n/2^{h+1}\ge1/2\). The ceiling is therefore at least \(1/2\) (indeed, it is at least 1). This permits the bound \(\lceil x\rceil\le2x\) for \(x\ge1/2\) in the BUILD-MAX-HEAP summation.

### 6.3-3 — Why the loop runs downward

When processing node \(i\), MAX-HEAPIFY requires both child subtrees to already be heaps. Each child has a larger index than its parent. Decreasing \(i\) ensures that all descendants have been processed before their parent. Increasing order would not establish this precondition.

### 6.3-4 — Number of nodes of height h

For a complete heap with \(n\) elements, the height of the node at array index \(i\) is \(\lfloor\lg(n/i)\rfloor\). Therefore a node has height exactly \(h\) when
\[
2^h\le n/i<2^{h+1},
\quad\text{or}\quad
\frac{n}{2^{h+1}}<i\le\frac{n}{2^h}.
\]
The number of integer indices in this interval is at most its length rounded up, giving
\[
\boxed{\left\lceil\frac{n}{2^{h+1}}\right\rceil}.
\]

## Exercises 6.4 — The heapsort algorithm

### 6.4-1 — Heapsort example

Input: \(\langle5,13,2,25,7,17,20,8,4\rangle\). BUILD-MAX-HEAP produces
\[
\langle25,13,20,8,7,17,2,5,4\rangle.
\]
The array after each extraction and heap repair is:
\[
\begin{aligned}
&\langle20,13,17,8,7,4,2\mid25\rangle\\
&\langle17,13,5,8,7,4,2\mid20,25\rangle\\
&\langle13,8,5,2,7,4\mid17,20,25\rangle\\
&\langle8,7,5,2,4\mid13,17,20,25\rangle\\
&\langle7,4,5,2\mid8,13,17,20,25\rangle\\
&\langle5,4,2\mid7,8,13,17,20,25\rangle\\
&\langle4,2\mid5,7,8,13,17,20,25\rangle\\
&\langle2\mid4,5,7,8,13,17,20,25\rangle.
\end{aligned}
\]
The vertical bar separates the active heap from the sorted suffix. The resulting sorted array is
\[
\boxed{\langle2,4,5,7,8,13,17,20,25\rangle}.
\]
The invariant is that the heap prefix contains the smallest remaining keys and the suffix contains the largest keys in sorted order.

### 6.4-2 — Prove the heapsort loop invariant

Initially the entire array is a max-heap and the suffix is empty, so the invariant holds. At iteration \(i\), the root is the largest of the \(i\) heap elements. Swapping it with \(A[i]\) appends it to the beginning of the already sorted suffix, in correct order. Decreasing heap_size removes it from the heap, and MAX-HEAPIFY restores the heap property in \(A[1:i-1]\). When \(i=1\), the remaining heap element is the smallest; the full array is sorted.

### 6.4-3 — Already sorted input

For both increasing and decreasing input, the asymptotic running time remains \(\boxed{\Theta(n\lg n)}\). BUILD-MAX-HEAP is \(O(n)\), and the algorithm performs \(n-1\) heap repairs. The shape of the input may change the number of swaps and comparisons, but not the asymptotic bound.

### 6.4-4 — Worst-case lower bound

Use an input in decreasing order. It is already a max-heap. At each extraction, the last (smallest remaining) element moves to the root and must sift down to a leaf, following a path of length \(\lfloor\lg i\rfloor-O(1)\) while the heap has \(i\) elements. Summing over the loop gives \(\sum_{i=2}^{n}\Theta(\lg i)=\Theta(n\lg n)\). Thus the worst-case running time is \(\boxed{\Theta(n\lg n)}\).

### 6.4-5 — Best case with distinct keys

Consider a perfect heap with \(n=2^k-1\). During the first \(n/2\) extractions, the algorithm removes the largest half of the keys. The nodes containing those keys form an ancestor-closed subtree: if a node is in the set, every ancestor has a larger key and is also in the set. This subtree has \(m=2^{k-1}\) nodes.

A rooted binary tree with \(m\) nodes has \(m-1\) edges, and each internal node has at most two children. It therefore has at least \((m-1)/2=\Theta(n)\) internal nodes. Call their number \(d\).

Each of these internal elements must be promoted toward the root before it can be extracted. To minimize the total number of promotions, pack \(d\) nodes as shallowly as possible in a binary tree. Since the first \(j\) levels contain fewer than \(2^j\) positions, a linear fraction of these \(d\) nodes must have depth \(\Omega(\lg d)\). The total number of promotions is consequently \(\Omega(d\lg d)=\Omega(n\lg n)\). This lower bound is incurred during the first half of the sorting phase alone. Since heapsort always has an \(O(n\lg n)\) upper bound, its best-case running time with distinct keys is
\[
\boxed{\Theta(n\lg n)}.
\]

This is a nontrivial structural lower-bound argument; the chapter notes credit Schaffer and Sedgewick with the best-case movement analysis.

## Exercises 6.5 — Priority queues

### 6.5-1 — EXTRACT-MAX trace

For \(A=\langle15,13,9,5,12,8,7,4,0,6,2,1\rangle\), remove 15, move the last key 1 to the root, and sift down:
\[
\langle1,13,9,5,12,8,7,4,0,6,2\rangle
\to\langle13,1,9,5,12,8,7,4,0,6,2\rangle
\to\langle13,12,9,5,1,8,7,4,0,6,2\rangle
\to\boxed{\langle13,12,9,5,6,8,7,4,0,1,2\rangle}.
\]

### 6.5-2 — MAX-HEAP-INSERT(A, 10)

Append 10 to the supplied heap:
\[
\langle15,13,9,5,12,8,7,4,0,6,2,1,10\rangle.
\]
Its parent is 8, so exchange:
\[
\boxed{\langle15,13,10,5,12,9,7,4,0,6,2,1,8\rangle}.
\]
The new key stops because its new parent 15 is larger.

### 6.5-3 — Min-priority queue pseudocode

    MIN-HEAP-MINIMUM(A)
        if A.heap_size < 1: error "heap underflow"
        return A[1]

    MIN-HEAP-EXTRACT-MIN(A)
        if A.heap_size < 1: error "heap underflow"
        answer = A[1]
        A[1] = A[A.heap_size]
        A.heap_size -= 1
        if A.heap_size > 0: MIN-HEAPIFY(A, 1)
        return answer

    MIN-HEAP-DECREASE-KEY(A, i, key)
        if key > A[i].key: error "new key is larger"
        A[i].key = key
        while i > 1 and A[PARENT(i)].key > A[i].key
            exchange A[i] with A[PARENT(i)]
            i = PARENT(i)

    MIN-HEAP-INSERT(A, x)
        if A.heap_size == A.capacity: error "heap overflow"
        A.heap_size += 1
        key = x.key
        x.key = +infinity
        A[A.heap_size] = x
        MIN-HEAP-DECREASE-KEY(A, A.heap_size, key)

The operation costs are \(O(1)\) for MINIMUM and \(O(\lg n)\) for the other operations.

### 6.5-4 — MAX-HEAP-DECREASE-KEY

    MAX-HEAP-DECREASE-KEY(A, i, key)
        if key > A[i].key: error "new key is larger"
        A[i].key = key
        MAX-HEAPIFY(A, i)

Decreasing a key can violate the max-heap property only with its children, so sift downward. The running time is \(O(\lg n)\).

### 6.5-5 — Why initialize the new key to negative infinity?

MAX-HEAP-INSERT first appends a new leaf. Setting its key to \(-\infty\) ensures that the heap property is valid before the key is raised. MAX-HEAP-INCREASE-KEY can then use one uniform upward-repair routine. The sentinel also guarantees the new key is no smaller than the temporary key.

### 6.5-6 — Why MAX-HEAPIFY cannot replace the upward loop

After increasing a key, the node may be larger than its parent, while its child subtrees remain max-heaps. MAX-HEAPIFY assumes the child subtrees are heaps and moves a too-small parent value downward. Here the violation is upward, so the key must move toward the root by comparing with parents.

### 6.5-7 — Loop invariant for INCREASE-KEY

The invariant states that all heap relations hold except possibly between \(i\) and its parent, and that the parent of \(i\) remains at least as large as the roots of the two child subtrees of \(i\). Initially, only the increased key may violate its parent relation; its children were no larger before the increase and remain no larger afterward. If the while test is true, swap \(i\) with its parent. The promoted key is now at the parent, and the displaced parent key is no larger than the promoted key; the only possible violation moves to the new index \(PARENT(i)\). The two sibling-subtree conditions remain valid. When the loop stops, either \(i=1\) or its parent is at least its key, so no violation remains and the max-heap property holds.

### 6.5-8 — Reduce exchanges to one assignment

Use a hole-based upward sift. Save the inserted object's key/pointer in a temporary variable, then shift each smaller parent down into the hole:
    
    x = A[i]
    while i > 1 and A[PARENT(i)].key < x.key
        A[i] = A[PARENT(i)]
        update_index(A[i], i)
        i = PARENT(i)
    A[i] = x
    update_index(x, i)

Each level uses one array assignment rather than a three-assignment swap. The final placement uses one more assignment.

### 6.5-9 — Implement FIFO queue and stack with a priority queue

For a FIFO queue, assign each inserted item a monotonically increasing timestamp and use a min-priority queue; extract the smallest timestamp first. For a stack, use a monotonically increasing timestamp and a max-priority queue; extract the newest timestamp first. If equal priorities are possible, include a unique sequence number as a tie-breaker.

### 6.5-10 — MAX-HEAP-DELETE in O(lg n)

Given a handle to object \(x\), find its heap index \(i\) in \(O(1)\) mapping time. Replace \(A[i]\) with the final heap element, decrement heap_size, and update the moved object's handle. If the replacement key is larger than its parent, sift it upward with the INCREASE-KEY loop; otherwise call MAX-HEAPIFY at \(i\). The path length is \(O(\lg n)\), so deletion takes \(O(\lg n)\) plus mapping overhead.

### 6.5-11 — Merge k sorted lists

Insert the first unconsumed element of each nonempty list into a min-heap, storing its list identifier and position. Repeatedly:
1. Extract the minimum and append it to the output.
2. From that same list, insert its next element if one remains.

The heap contains at most \(k\) elements. Each of the \(n\) total elements is inserted and extracted at most once, each in \(O(\lg k)\), so the total running time is \(\boxed{O(n\lg k)}\), with \(O(k)\) auxiliary heap space.

---

## Problems for Chapter 6

### 6-1 — Building a heap using insertion

**(a) Do BUILD-MAX-HEAP and BUILD-MAX-HEAP' always create the same heap?**

No. For example, use input \(\langle1,2,3\rangle\). Bottom-up BUILD-MAX-HEAP first heapifies node 1 and produces \(\langle3,2,1\rangle\). Repeated insertion starts with 1, inserts 2 to obtain \(\langle2,1\rangle\), then inserts 3 to obtain \(\langle3,1,2\rangle\). The resulting heaps differ.

**(b) Worst-case time of repeated insertion**

The \(i\)-th insertion can move its key from a leaf to the root, costing \(\Theta(\lg i)\). Choose an increasing input order so each newly inserted key is larger than all previous keys. Then every insertion traverses the full path to the root. The total is
\[
\sum_{i=2}^{n}\Theta(\lg i)=\Theta(n\lg n).
\]

### 6-2 — Analysis of d-ary heaps

**(a) Array representation.** With 1-based indexing, the parent of \(i>1\) is
\[
PARENT_d(i)=\left\lfloor\frac{i-2}{d}\right\rfloor+1,
\]
and the children are
\[
d(i-1)+2,\ d(i-1)+3,\ldots,di+1,
\]
when their indices do not exceed heap_size.

**(b) Height.** A full d-ary tree of height \(h\) has \((d^{h+1}-1)/(d-1)\) nodes. Therefore \(h=\Theta(\log_d n)\).

**(c) EXTRACT-MAX.** Save the root, move the last element to the root, shrink the heap, and sift down by finding the largest among the node and up to \(d\) children. Each level costs \(O(d)\), and there are \(O(\log_d n)\) levels:
\[
O(d\log_d n).
\]

**(d) INCREASE-KEY.** Raise the key and repeatedly compare it with its parent, swapping upward while it is larger. One comparison and constant work per level gives \(O(\log_d n)\).

**(e) INSERT.** Append a leaf with key \(-\infty\), then apply INCREASE-KEY. The time is \(O(\log_d n)\).

### 6-3 — Young tableaux

**(a) A 4-by-4 tableau.** One valid arrangement of the nine values is
\[
\begin{bmatrix}
2&3&5&8\\
4&9&14&\infty\\
12&16&\infty&\infty\\
\infty&\infty&\infty&\infty
\end{bmatrix}.
\]
Rows and columns are nondecreasing.

**(b) Empty and full tests.** If \(Y[1,1]=\infty\), every entry to its right or below must be at least infinity, hence infinity; the tableau is empty. If \(Y[m,n]<\infty\), every entry above or left is no larger than this finite value and therefore finite; the tableau is full.

**(c) EXTRACT-MIN.** Save \(Y[1,1]\), put infinity there, then recursively compare the right and lower neighbors and move the smaller one into the vacancy. Continue the vacancy into the neighbor's old cell until it reaches the last row or column. Each step moves one row down or one column right, so there are at most \(m+n-2\) steps. The cost is \(O(m+n)\).

**(d) INSERT.** Put the new key in the bottom-right empty cell. While it is smaller than its upper or left neighbor, swap it with the larger of those violating neighbors. Each swap moves one row up or one column left; there are at most \(m+n-2\) moves, so the cost is \(O(m+n)\).

**(e) Sort \(n^2\) numbers.** Build an \(n\times n\) Young tableau by inserting the \(n^2\) values, each in \(O(n)\) time, for \(O(n^3)\). Then extract-min \(n^2\) times, each \(O(n)\), again \(O(n^3)\). The extracted sequence is sorted, and the total is \(\boxed{O(n^3)}\).

**(f) Search.** Start at the top-right cell. If it equals the target, return its location. If it is greater, move left (everything below is at least as large); if it is smaller, move down (everything to the left is at most as small). Each move eliminates a row or column, so there are at most \(m+n-1\) moves and the running time is \(O(m+n)\).

---

## Final Chapter 6 checklist

- [ ] Derive heap index arithmetic and height.
- [ ] Prove MAX-HEAPIFY's precondition and correctness.
- [ ] Explain the linear-time BUILD-MAX-HEAP summation.
- [ ] Prove the HEAPSORT loop invariant.
- [ ] Implement all priority-queue operations and update handles.
- [ ] Analyze d-ary heap operations.
- [ ] Implement Young-tableau insertion, extraction, and search.
