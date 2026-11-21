# Chapter 10 — Elementary Data Structures

**Reference:** CLRS, *Introduction to Algorithms*, Fourth Edition (2022), Chapter 10, printed pages 251–271.

This chapter studies pointer-based representations of dynamic sets and the trade-offs among arrays, matrices, stacks, queues, linked lists, and rooted trees. The goal is to understand representation invariants and the cost of each operation.

## 10.1 Simple array-based data structures

### Arrays and memory layout

An array occupies a contiguous memory region. If the first logical index is s, the base address is a, and each element occupies b bytes, element i begins at a+b(i−s). Thus, with 0-based indexing the address is a+bi; with 1-based indexing it is a+b(i−1). Under the RAM model, array access takes Θ(1) time independent of the index. If elements have variable sizes, an array commonly stores fixed-size references to separately allocated objects; following a reference is an additional memory access.

### Matrices

For an m×n matrix M, row-major layout stores complete rows consecutively; column-major layout stores complete columns consecutively.

With 0-based row and column indices:
- Row-major offset: ni+j.
- Column-major offset: i+mj.

With 1-based indices and a single array also indexed from 1:
- Row-major index: n(i−1)+j.
- Column-major index: i+m(j−1).

A multi-array representation can store one array per row (or per column), with a top-level array of references. It supports ragged rows/columns but adds indirection. A blocked representation stores small submatrices contiguously, improving locality for some access patterns.

### Stacks

A stack is a dynamic set with last-in, first-out (LIFO) deletion. For an array S[1…n], maintain a top attribute, the index of the most recently inserted element. The active stack is S[1…top]; top=0 means empty.

- STACK-EMPTY: test top == 0.
- PUSH(x): reject overflow if top == size; increment top, then store x.
- POP(): reject underflow if empty; save S[top], decrement top, return the saved value.

All three operations take Θ(1) time. The array may still contain a popped value beyond top; it is not logically part of the stack.

### Queues

A queue is a dynamic set with first-in, first-out (FIFO) deletion. Use a circular array Q[1…n] with head pointing to the first element and tail pointing to the next free slot. Advancing an index wraps n back to 1. The active elements run circularly from head up to, but not including, tail.

In CLRS's one-empty-slot representation:
- Empty iff head == tail.
- Full iff advancing tail once would make it equal to head.
- Capacity is n−1 elements, not n.

ENQUEUE writes at tail and advances it; DEQUEUE reads at head and advances it. Both are Θ(1). The one-empty-slot invariant distinguishes full from empty without an additional count or flag. Error checks must occur before changing the indices.

### Deques and queue/stack transformations

A deque supports insertion and deletion at both ends. A circular array supports all four operations in Θ(1) by moving head or tail in the appropriate direction with wraparound and checking full/empty conditions.

Two stacks can implement a queue: enqueue pushes onto an input stack; dequeue pops from an output stack, transferring all input elements only when the output stack is empty. Each element moves at most once in each direction, so the amortized cost per queue operation is Θ(1), although one operation can cost Θ(n).

A stack can be implemented with two queues by choosing which queue is kept nonempty and moving elements to make the most recently inserted element emerge first. One standard design makes PUSH Θ(n) and POP Θ(1); the alternative makes PUSH Θ(1) and POP Θ(n).

## 10.2 Linked lists

A linked list stores its linear order in pointers rather than array indices. In a doubly linked list, each node has key, next, and prev; the list object stores head. The head's prev and the tail's next are NIL. An empty list has head = NIL.

- LIST-SEARCH(L,k) follows next pointers: Θ(n) worst case.
- LIST-PREPEND(L,x) links x before the current head: Θ(1).
- LIST-INSERT(x,y) splices x immediately after a known node y: Θ(1).
- LIST-DELETE(L,x) unlinks a known node x and updates the head if needed: Θ(1).

Deleting by key still takes Θ(n) worst case because it first requires a search. Arrays provide Θ(1) indexed access and good locality, while linked lists support constant-time insertion/deletion when the node position is already known. A singly linked list cannot generally delete a given node in Θ(1) without its predecessor.

### Sentinels

A sentinel is a dummy node used in place of NIL boundary pointers. A circular doubly linked list with sentinel L.nil has L.nil.next pointing to the head and L.nil.prev to the tail. In an empty list, both point back to the sentinel. Every real node's next and prev are non-NIL, so insertion and deletion avoid separate head/tail cases.

LIST-INSERT'(x,y) inserts x after y; inserting after the sentinel prepends, and inserting after L.nil.prev appends. LIST-DELETE'(x) updates the two neighboring links. Never delete the sentinel unless destroying the entire list. A sentinel simplifies code but consumes one extra node per list and usually does not change asymptotic complexity.

## 10.3 Representing rooted trees

A binary-tree node stores p, left, and right pointers. T.root points to the root; the root's parent is NIL, and a missing child pointer is NIL.

For a rooted tree with an arbitrary number of children, storing a separate pointer for every child is wasteful or impossible when the degree is unbounded. The left-child, right-sibling representation stores:
- left-child: pointer to the node's leftmost child.
- right-sibling: pointer to its immediate right sibling.
- p: parent pointer.

This uses O(n) space for an n-node tree, independent of the maximum node degree. The first child is reached directly; later children are traversed through sibling pointers. A node's full child list therefore takes time proportional to its number of children.

Other representations may omit pointers that an application never follows. For example, a heap uses an array representation, while a structure that only traverses toward the root may need only parent pointers.

## Representation and operation trade-offs

| Structure | Key invariant | Typical operation costs |
|---|---|---|
| Array | Contiguous indexed storage | Access Θ(1); search Θ(n) unsorted |
| Stack | Active prefix S[1…top] | Push/pop Θ(1) |
| Circular queue | Head/tail move modulo capacity; one slot unused | Enqueue/dequeue Θ(1) |
| Doubly linked list | Neighbor pointers are reciprocal | Search Θ(n); insert/delete known node Θ(1) |
| Sentinel list | Circular links through dummy node | Insert/delete known node Θ(1) |
| Binary tree | Parent/left/right pointers | Traversal Θ(n) |
| Left-child/right-sibling tree | First-child and next-sibling links | All nodes Θ(n); children of x in Θ(degree(x)) |

## Engineering perspective

- Prefer arrays when indexed access, compact storage, and cache locality matter.
- Use a stack for nested scopes, parsing, backtracking, and depth-first traversal.
- Use a queue for breadth-first traversal and work scheduling; use a deque when both ends must be active.
- Use linked lists when stable node references and frequent local splicing matter more than random access.
- Treat capacity, empty/full state, and pointer invariants as part of the data structure's contract. Validate them at operation boundaries.
- In Python, list is a dynamic array, collections.deque is the usual efficient queue/deque, and custom node classes are useful when the algorithm specifically requires linked-list or tree pointers. Python's built-ins are engineering choices, not substitutes for understanding the underlying invariants.

**Status:** Chapter 10 notes drafted from the source. Exercise/problem solutions, diagrams, Python implementations, and the full audit remain in progress.
