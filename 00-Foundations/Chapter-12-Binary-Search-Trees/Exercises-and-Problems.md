# Chapter 12 — Exercises and Problems

Original solutions based on CLRS Fourth Edition, Sections 12.1–12.3. Keys follow the source's non-strict BST invariant.

## 12.1 What is a binary search tree?

**12.1-1. Heights 2–6.** Heights count edges. The following trees use exactly the seven given keys:
- Height 2: root 10; children 4 and 17; grandchildren 1,5,16,21.
- Height 3: root 10; left chain 1→right 4→right 5; right subtree 17 with children 16 and 21.
- Height 4: root 5; left child 4 with left child 1; right chain 10→right 16→right 17→right 21.
- Height 5: root 4; left child 1; right chain 5→10→16→17→21.
- Height 6: the right-going chain 1→4→5→10→16→17→21.

**12.1-2. BST versus min-heap.** A min-heap guarantees parent.key≤child.key but gives no ordering between left and right subtrees. A BST globally partitions keys at each node. Heap extraction of the minimum takes O(lg n) per removal, so printing all keys by repeated extract-min takes O(n lg n), not O(n); a heap does not support sorted output by a simple O(n) traversal.

**12.1-3. Nonrecursive inorder.** Push the current node and descend left until NIL; pop and visit; then set current to the popped node's right child. Repeat while current is non-NIL or the stack is nonempty. Θ(n) time and O(h) space.

**12.1-4. Preorder/postorder.** Preorder(x): if x≠NIL, visit x, recurse left, recurse right. Postorder(x): if x≠NIL, recurse left, recurse right, visit x. Each visits n nodes in Θ(n).

**12.1-5. Construction lower bound.** If a comparison-based algorithm could construct a BST from arbitrary n distinct keys in o(n lg n) worst-case time, an inorder traversal (Θ(n)) would sort them faster than the comparison-sorting lower bound Ω(n lg n). Therefore construction requires Ω(n lg n) worst-case comparisons/time.

## 12.2 Querying a binary search tree

**12.2-1. Impossible search traces.** Maintain an interval [low,high] of possible keys, initially [1,1000]. After examining x, if x>363, tighten high to x−1; if x<363, tighten low to x+1. The next examined key must lie in the resulting interval. Sequences **(c)** and **(e)** are impossible:
- (c): after 925,202,911,240, the target lies in [241,910], but the next key is 912.
- (e): after 935,278,347,621, the target lies in [348,620], but the next key is 299.
The other three sequences respect the interval constraints.

**12.2-2. Recursive minimum/maximum.** MINIMUM(x): if x.left=NIL return x; otherwise return MINIMUM(x.left). MAXIMUM is symmetric.

**12.2-3. Predecessor.** If x.left≠NIL return TREE-MAXIMUM(x.left). Otherwise set y=x.p; while y≠NIL and x=y.left, set x=y and y=y.p; return y.

**12.2-4. Counterexample.** A smallest counterexample has six nodes. Use root 2, its right child 4, 4's left child 3 and right child 6, and give 3 the children 2.5 and 3.5 (or use order-isomorphic integer keys 2,4,6,8,10,12 with the same shape). Search for k=3.5 follows 2→4→3→3.5 and ends at a leaf. The off-path node a=2.5 lies to the left of the search path, b=2 lies on it, and c=6 lies to its right, yet a>b. Thus A≤B≤C is false. (The integer relabeling 2,4,6,8,10,12 maps 2.5,3,3.5,4,5,6 respectively.)

**12.2-5. Successor/predecessor child.** If x has two children, its successor is the minimum of x.right, so it has no left child. Symmetrically, predecessor is maximum of x.left and has no right child.

**12.2-6. Lowest ancestor.** With no right subtree, climb while x is a right child. The first ancestor y for which x lies in y.left is the lowest ancestor whose left child is an ancestor of the original x. Any lower ancestor on the path was reached from its right child and fails the condition.

**12.2-7. Minimum plus successors.** The initial minimum search costs O(h). During n−1 successor calls, each edge is traversed downward at most once into a right subtree and upward at most once while climbing. Thus total work is O(n+h)=O(n), and output itself costs Ω(n), giving Θ(n).

**12.2-8. k successive successors.** The first successor costs at most O(h). Across the next k−1 calls, every downward edge traversal enters a subtree that will not be revisited, and every upward traversal leaves a node/edge permanently behind in inorder order. The total is O(k+h).

**12.2-9. Parent of a leaf.** For leaf x with parent y, if x=y.left then no key lies strictly between x and y in that local subtree; any key greater than x that is smaller than y would have to be in y.left, but x is the maximum there because it is a leaf and the path's rightmost node. Thus y is the successor. Symmetrically if x=y.right, y is the predecessor.

## 12.3 Insertion and deletion

**12.3-1. Recursive insertion.** Recurse from root: if subtree is NIL, attach z with parent p and NIL children; otherwise compare z.key with x.key, recurse left if smaller and right otherwise, and return x. Keep the parent argument or set child.parent after recursion. O(h).

**12.3-2. Search path versus insertion path.** The insertion search for a key follows exactly the comparisons that a later search for that key follows, stopping at the newly inserted node. Therefore later successful search examines one more node than the insertion's prior comparison path.

**12.3-3. BST sort.** Worst case, sorted/reverse-sorted insertion order creates height n−1 and Θ(n²) total insertion time; inorder traversal adds Θ(n), so Θ(n²). Best case, balanced insertion paths total Θ(n lg n), plus Θ(n) traversal, so Θ(n lg n).

**12.3-4. NIL transplant argument.** v can be NIL whenever the replacement subtree is empty: deleting a leaf, deleting a node whose only child is absent, or splicing out a successor y that has no right child. TRANSPLANT updates v.parent only when v is non-NIL.

**12.3-5. Commutativity.** Deletion is not commutative as a structural operation. Insert keys in order 1,0,3,2, giving root 1 with left child 0 and right subtree rooted at 3 with left child 2. Delete 0 then 1: the result is root 3 with left child 2. Delete 1 then 0: deleting 1 promotes successor 2 to the root with right child 3; deleting 0 then leaves root 2 with right child 3. The resulting shapes differ.

**12.3-6. Successor pointers instead of parent pointers.** Store left, right, and succ; do not store parent.
- `PARENT(v)`: search from the root by key, retaining the previous node, until the search reaches v; return the previous node (NIL for root). O(h).
- SEARCH is the ordinary root-to-leaf search.
- INSERT descends as in TREE-INSERT while maintaining predecessor pred and successor succ candidates: when z.key<x.key, set succ=x and go left; otherwise set pred=x and go right. Attach z at the NIL link, set z.succ=succ, and if pred≠NIL set pred.succ=z. O(h).
- DELETE first find pred (the maximum node below z.key, via a search retaining the last left-turn candidate) and set pred.succ=z.succ if pred exists. If z has at most one child, use PARENT(z) to replace z by its only child or NIL. If z has two children, y=z.succ is the minimum of z.right and has no left child. Find PARENT(y), replace y by y.right there, set y.right=z.right, then find PARENT(z), replace z by y, and set y.left=z.left. A constant number of root searches each costs O(h), so all operations remain O(h). The successor link of y already points to z's former successor, so it remains correct after y is moved.

**12.3-7. Predecessor-based deletion.** Replace successor with TREE-MAXIMUM(z.left); splice predecessor y from its old position using y.left (since y has no right child); if y≠z.left, set y.left=z.left and repair parent; transplant z with y; set y.right=z.right and repair parent. For fairness, alternate predecessor/successor choices with one deterministic bit per deletion or choose randomly.

## Problems

**12-1. Equal keys.**
(a) Basic TREE-INSERT sends equality right, so n identical keys form a chain; total insertion time Θ(n²).
(b) At each node, alternating the direction for successive equal-key insertions splits the arrivals to that node between its two children as evenly as possible. The resulting recursive split has height Θ(lg n), and the total insertion work is Θ(n lg n).
(c) Store equal keys in a list at one tree node: first insertion O(1), subsequent list prepends O(1), so total Θ(n) and tree height remains 0 for identical keys.
(d) Randomly choose left/right independently at each equality. Worst case remains Θ(n²), since all choices can follow one direction. In expectation the arrivals split like fair coin flips at each node; the expected total number of node visits is Θ(n lg n) (the same order as the expected path length in a random binary search tree).

**12-2. Radix trees.** Insert each distinct bit string by following its bits from the root, creating missing child nodes. Mark terminal nodes. To output lexicographically, perform a preorder traversal that emits a terminal string before visiting child 0 then child 1. If keys are not stored, maintain the current path buffer. Every input bit creates at most one trie edge, and traversal visits O(n) nodes/edges because the total key length is n. Total Θ(n).

**12-3. Average node depth in a random BST.**
(a) Average depth is P(T)/n by definition.
(b) Root contributes depth 0; each of the n−1 nodes in the two subtrees gains one depth level, so P(T)=P(TL)+P(TR)+n−1.
(c) The root's rank is uniform i∈{0,…,n−1}; left and right subtree sizes are i and n−i−1. Average the recurrence over i.
(d) Symmetry gives P(n)=(2/n)Σ_{k=0}^{n−1}P(k)+(n−1), and P(0)=0, so the sum may start at k=1; the additive term is Θ(n).
(e) This is the same recurrence shape as randomized quicksort's expected comparison recurrence; therefore P(n)=O(n lg n), and expected average node depth is O(lg n).
(f) Use randomized quicksort with pivot chosen uniformly from the current subarray; partition comparisons compare each element against the pivot. In BST insertion, each new key is compared against the ancestor pivots along its search path. Across all pairs, both algorithms compare exactly those pairs for which the earlier pivot/key is the first among the pair in the random permutation; hence comparison sets coincide.

**12-4. Number of binary trees.**
(a) Choose the left-subtree size k from 0 to n−1; independently choose left and right shapes: b_n=Σ b_k b_(n−1−k), b_0=1.
(b) Multiply the recurrence by x^n and sum: B(x)−1=xB(x)^2, so B(x)=1+xB(x)^2. Solve the quadratic and choose the branch finite at x=0: B(x)=(1−√(1−4x))/(2x).
(c) Expanding the square root by the generalized binomial theorem gives b_n=(1/(n+1))·binom(2n,n), the nth Catalan number.
(d) Stirling's approximation gives binom(2n,n)~4^n/√(πn), hence b_n~4^n/(√π n^(3/2))=4^n/(√π n^(3/2))(1+O(1/n)).
