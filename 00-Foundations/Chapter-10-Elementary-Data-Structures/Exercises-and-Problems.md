# Chapter 10 — Exercises and Problems

Solutions follow the CLRS Fourth Edition statements and notation. Array indices in pseudocode follow the book unless noted.

## Exercises 10.1 — Array-based structures

### 10.1-1 — Binary index for a 2×2 block layout

Let i have bits i_(lg m−1)…i_0 and j have bits j_(lg n−1)…j_0. In row-major order, the ordinary flat offset is ni+j. Since m and n are powers of two, this offset's binary representation is the concatenation

\[
\boxed{i_{lg m-1}\cdots i_0\;j_{lg n-1}\cdots j_0}.
\]

The high lg m bits select the block row and the high lg n bits select the block column; the remaining bits select the position within that block. The 2×2 block decomposition therefore does not require a different index formula: it is exactly the bit concatenation above.

### 10.1-2 — Stack operation trace

Starting with an empty stack, bottom-to-top contents after each operation are:

| Operation | Stack contents | Returned value |
|---|---|---:|
| PUSH(4) | [4] | — |
| PUSH(1) | [4, 1] | — |
| PUSH(3) | [4, 1, 3] | — |
| POP() | [4, 1] | 3 |
| PUSH(8) | [4, 1, 8] | — |
| POP() | [4, 1] | 8 |

Final top is 2; array positions 1 and 2 contain 4 and 1. Values left in higher array slots after POP are not part of the stack.

### 10.1-3 — Two stacks in one array

Let stack 1 grow from the left and stack 2 grow from the right. Maintain top1=0 and top2=n+1. PUSH1 increments top1; PUSH2 decrements top2. Overflow occurs exactly when top1+1=top2. POP1 is invalid when top1=0; otherwise return A[top1] and decrement top1. POP2 is invalid when top2=n+1; otherwise return A[top2] and increment top2. Every operation takes Θ(1), and no space is permanently reserved for either stack.

### 10.1-4 — Circular queue trace

Use Q[1…6], head=tail=1 initially, and the one-empty-slot convention.

| Operation | Returned value | head | tail | Logical queue |
|---|---:|---:|---:|---|
| ENQUEUE(4) | — | 1 | 2 | [4] |
| ENQUEUE(1) | — | 1 | 3 | [4,1] |
| ENQUEUE(3) | — | 1 | 4 | [4,1,3] |
| DEQUEUE() | 4 | 2 | 4 | [1,3] |
| ENQUEUE(8) | — | 2 | 5 | [1,3,8] |
| DEQUEUE() | 1 | 3 | 5 | [3,8] |

### 10.1-5 — Queue overflow and underflow checks

For a circular array of length n, define NEXT(i)=1 if i=n, otherwise i+1.

- ENQUEUE(Q,x): compute nextTail=NEXT(tail). If nextTail=head, report overflow. Otherwise write Q[tail]=x and set tail=nextTail.
- DEQUEUE(Q): if head=tail, report underflow. Otherwise save x=Q[head], set head=NEXT(head), and return x.

The full test must occur before writing; the empty test must occur before reading or advancing. Both procedures remain Θ(1).

### 10.1-6 — Deque operations

Use a circular array with head pointing to the first element and tail pointing to the next free slot. Keep one slot unused to distinguish full from empty.

- PUSH-FRONT(x): compute newHead=PREV(head); if newHead=tail, overflow; set head=newHead and Q[head]=x.
- PUSH-BACK(x): if NEXT(tail)=head, overflow; set Q[tail]=x and tail=NEXT(tail).
- POP-FRONT(): if head=tail, underflow; save Q[head], set head=NEXT(head), return saved value.
- POP-BACK(): if head=tail, underflow; set tail=PREV(tail), return Q[tail].

PREV(1)=n and PREV(i)=i−1 otherwise. Each operation changes a constant number of indices or array cells and takes Θ(1).

### 10.1-7 — Queue using two stacks

Maintain input stack I and output stack O. ENQUEUE(x) pushes x onto I. DEQUEUE() transfers every element from I to O only when O is empty, then pops O. If both stacks are empty, report underflow. Each element is pushed onto I once, transferred to O at most once, and popped once. Thus any one DEQUEUE can cost Θ(n), but over a sequence of operations the total work is Θ(number of operations); amortized time per operation is Θ(1).

### 10.1-8 — Stack using two queues

One implementation keeps the stack in queue Q1 with its top at the front. PUSH(x): enqueue x into empty Q2, transfer all Q1 elements to Q2, then swap Q1 and Q2. This costs Θ(n). POP(): dequeue Q1, costing Θ(1). The alternative leaves PUSH at Θ(1) and rotates the queue during POP, costing Θ(n).

## Exercises 10.2 — Linked lists

### 10.2-1 — Singly linked insertion and deletion

INSERT at the head changes the new node's next pointer and the list's head pointer, so it takes Θ(1). To delete a specified node while preserving a singly linked list, one must update its predecessor's next pointer. In the worst case, finding that predecessor requires traversing the list from the head, taking Θ(n). If the operation is given only a pointer to the target node, copying the successor's contents is not a general solution: it fails for the tail and changes object identity.

### 10.2-2 — Stack using a singly linked list

Use the list head as the stack top. PUSH(x) prepends x; POP() checks for empty, removes and returns the head. Both take Θ(1). No additional list attribute beyond the head pointer is required.

### 10.2-3 — Queue using a singly linked list

Maintain both head and tail pointers. ENQUEUE(x) appends after tail (or initializes head if empty) and updates tail. DEQUEUE() removes head, updates head to its successor, and sets tail=NIL if the queue becomes empty. Both operations take Θ(1); the tail attribute is essential for constant-time enqueue.

### 10.2-4 — UNION in Θ(1)

Represent each set by a circular, doubly linked list with a sentinel. Given disjoint lists S1 and S2, splice the two circular chains together by changing a constant number of next/prev pointers, then discard one sentinel and retain the other as the representative. No elements need to be copied or traversed. UNION takes Θ(1). The disjointness assumption prevents duplicate-set semantics from complicating the splice.

### 10.2-5 — Reverse a singly linked list

Use three pointers prev, cur, and nxt. Initially prev=NIL and cur=head. Repeatedly save nxt=cur.next, set cur.next=prev, advance prev=cur and cur=nxt. At termination set head=prev. Every link is reversed once, so time is Θ(n) and auxiliary space Θ(1).

### 10.2-6 — XOR linked list

Store one field np per node, equal to the bitwise XOR of the integer representations of its predecessor and successor pointers. The list object must retain both the head and tail pointers (or head plus enough information to recover the tail). To traverse forward, given prev and cur, compute next=ptr(cur.np XOR ptr(prev)); then advance (prev,cur)=(cur,next). Search is a traversal.

To insert x between adjacent nodes a and b, replace a's neighbor contribution b by x in a.np: a.np ^= ptr(b) ^ ptr(x); similarly b.np ^= ptr(a) ^ ptr(x); set x.np=ptr(a) XOR ptr(b). Boundary insertions use NIL=0 and update head/tail. To delete x, first traverse to obtain its predecessor a and successor b, then replace x in each neighbor's XOR field by the other neighbor; update head/tail if x is an endpoint. Reversing the list swaps the stored head and tail and takes Θ(1), since each node's XOR of its two neighbors is unchanged.

This representation depends on pointer values being safely convertible to fixed-width integers and makes memory-safe debugging and ordinary pointer tooling harder; it is primarily a representation exercise.

## Exercises 10.3 — Rooted trees

### 10.3-1 — Draw the binary tree

Root index 6 has key 15. Its left child is index 1 (key 17) and right child index 4 (key 20). Index 1 has children 8 (22) and 9 (13); index 4 has left child 10 (25). Index 9 has children 3 (12) and 7 (28). Index 10 has right child 5 (33), and index 5 has left child 2 (14). All omitted children are NIL.

### 10.3-2 — Recursive traversal

Use preorder traversal:

\[
PRINT(x):\quad \text{if }x\ne NIL:\; print(x.key); PRINT(x.left); PRINT(x.right).
\]

Each node is visited once, so the running time is Θ(n). Recursion stack space is O(h), where h is tree height.

### 10.3-3 — Nonrecursive traversal using a stack

Push the root if non-NIL. While the stack is nonempty, pop x and print x.key; push x.right first, then x.left, so that the left subtree is processed first. Every node is pushed and popped once: Θ(n) time and O(h) auxiliary space for a depth-first traversal.

### 10.3-4 — Print an arbitrary rooted tree

For the left-child, right-sibling representation, recursively print x.key, then traverse the child chain beginning at x.left-child. For each child c, call PRINT(c), then advance c=c.right-sibling. Each node is visited once, so the time is Θ(n). The recursion stack is proportional to tree height.

### 10.3-5 — Nonrecursive traversal with O(1) extra space and no modification

Use parent pointers to walk the tree without a stack. Maintain previous and current nodes. On entering a node from its parent, print it, then descend to its left child if present, otherwise its right child if present, otherwise ascend. On returning from the left child, descend right if present; otherwise ascend. On returning from the right child, ascend. Stop after returning from the root. Each edge is traversed at most twice and each node is printed once, giving Θ(n) time and O(1) extra space. The tree is never modified.

### 10.3-6 — Sharing parent and child pointer storage

The node needs to retain enough information to distinguish whether its shared pointer denotes its parent or its leftmost child; the boolean is the tag for that interpretation, and the other pointer is used for the sibling link. The representation must be arranged consistently across each parent-child chain so that following sibling links reaches the designated first child and its stored parent reference. The exact pointer/tag invariant should be stated before implementing accessors; see the accompanying audit note, since the exercise's wording is easy to misread and this solution is not yet considered verified.

## Problems for Chapter 10

### 10-1 — Comparisons among lists

Worst-case operation times (n is the list length):

| Operation | Unsorted singly | Sorted singly | Unsorted doubly | Sorted doubly |
|---|---:|---:|---:|---:|
| SEARCH | Θ(n) | Θ(n) | Θ(n) | Θ(n) |
| INSERT | Θ(1) | Θ(n) | Θ(1) | Θ(n) |
| DELETE (given node pointer) | Θ(n) | Θ(n) | Θ(1) | Θ(1) |
| SUCCESSOR (given node) | Θ(n) | Θ(1) | Θ(n) | Θ(1) |
| PREDECESSOR (given node) | Θ(n) | Θ(n) | Θ(n) | Θ(1) |
| MINIMUM | Θ(n) | Θ(1) | Θ(n) | Θ(1) |
| MAXIMUM | Θ(n) | Θ(n) | Θ(n) | Θ(1) |

For singly linked lists, predecessor and deletion require traversal from the head. For sorted lists, successor can be obtained from next; in a doubly linked sorted list, predecessor is also directly available. Sorted insertion must find the insertion position, which is Θ(n) in the worst case. The table assumes DELETE receives a pointer to the element, as in the dynamic-set operation definition.

### 10-2 — Mergeable heaps using linked lists

Let n be the size of the heap being operated on and m the size of the other heap in UNION.

**(a) Sorted lists.** Store elements in increasing order in a doubly linked list with head and tail pointers. MAKE-HEAP Θ(1); INSERT Θ(n) to find the position (pointer splicing is Θ(1)); MINIMUM Θ(1) at the head; EXTRACT-MIN Θ(1); UNION Θ(n+m) by merging the two sorted chains.

**(b) Unsorted lists.** Store elements in an unsorted doubly linked list. MAKE-HEAP Θ(1); INSERT Θ(1) at the head; MINIMUM Θ(n) scan; EXTRACT-MIN Θ(n) to find and remove the minimum; UNION Θ(1) by concatenating the lists.

**(c) Unsorted lists, disjoint sets.** The same concatenation supports UNION in Θ(1) because no duplicate detection is needed. The other costs are the same as in (b). Disjointness is relevant to set semantics; it does not make finding a minimum faster.

### 10-3 — Searching a sorted compact list

Let the desired key have rank r in the sorted linked order. Since the key array is compact, every physical index in 1…n is a valid list node, but the physical order is a random permutation of the sorted ranks.

**(a)** The randomized skips in the original algorithm and the t-step for-loop in the modified algorithm use the same random index sequence. Every successful skip moves i forward in sorted-list order but never past k. The original algorithm's loop iterations correspond to successful random skips plus ordinary next-pointer advances; the modified algorithm performs at most t random trials and then completes the remaining sequential walk. Both stop at k or at the first key greater than k/end, so they return the same result. The original sequential advances are no more numerous than the total for-loop and final while-loop advances of the modified procedure.

**(b)** The modified algorithm performs t random trials, each O(1), then walks from its current node to k. If that remaining linked-list distance is X_t, its expected running time is O(t+E[X_t]).

**(c)** At each random trial, the probability of selecting any one physical array index is 1/n. Among the r physical positions whose keys are at most the target, the probability of not selecting a useful position in one trial is 1−r/n. After t independent trials, the probability that the remaining distance is at least r is (1−r/n)^t. Summing tail probabilities gives
\[
E[X_t]=\sum_{r=1}^{n}\left(1-\frac{r}{n}\right)^t.
\]

**(d)** Since f(x)=(1−x/n)^t is decreasing on [0,n], the right-endpoint sum is bounded by the corresponding integral:
\[
\sum_{r=1}^{n-1}\left(1-\frac{r}{n}\right)^t
\le \int_0^n\left(1-\frac{x}{n}\right)^t dx
=\frac{n}{t+1}.
\]

**(e)** The expression in (c) is no larger than the sum in (d) (the r=n term is zero), so E[X_t]≤n/(t+1).

**(f)** Substitute into (b): expected time is O(t+n/(t+1))=O(t+n/t) for t≥1.

**(g)** Choose t=ceil(sqrt(n)). Then t+n/t=O(sqrt(n)), proving O(sqrt(n)) expected search time.

**(h)** Distinct keys ensure that each key rank identifies one node and that the useful random-skip interval has a single target boundary. With repeated keys, many physical positions can carry the target value; a random index may land on a duplicate that does not advance the search past a long run of equal keys. Thus random skips need not reduce the asymptotic traversal work; an input with a long block of equal keys can still force linear-time behavior.

---

**Audit status:** Draft solutions cover all listed exercises and problems. Exercise 10.3-6 and the compact-list probability argument in Problem 10-3 require a final proof audit before this chapter can be marked complete.
