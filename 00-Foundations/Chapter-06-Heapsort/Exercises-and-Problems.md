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
- \(i=2\): swap 3 with 84, then with 9.
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

