# Chapter 12 — Binary Search Trees

**Reference:** CLRS, Fourth Edition (2022), Sections 12.1–12.3, printed pages 313–330.

A binary search tree (BST) stores one key per node and maintains an ordering invariant that makes a search follow one root-to-leaf path. The cost of the standard operations is proportional to the tree height h; an unbalanced BST can therefore take linear time.

## 12.1 What is a binary search tree?

### Representation and invariant

Each node x stores `key`, `left`, `right`, `p` (parent). The tree object stores `root`. NIL denotes an absent child or parent. The root is the only node whose parent is NIL.

For every node x:
- every key in x's left subtree is ≤ x.key;
- every key in x's right subtree is ≥ x.key.

The invariant applies to entire subtrees, not merely immediate children. Equal keys are permitted by this non-strict formulation; the basic insertion procedure sends equality to the right, although rotations can later place equal keys on either side while preserving the non-strict invariant.

### Tree walks

- Inorder: recursively walk left, visit x, walk right. The output is nondecreasing.
- Preorder: visit x, then left, then right.
- Postorder: left, right, then visit x.

An inorder walk visits each node once, so its running time is Θ(n). More precisely, each nonempty call makes two recursive calls, and the total number of calls (including NIL calls) is 2n+1.

A nonrecursive inorder walk uses an explicit stack: descend left while pushing nodes, pop/visit, then move right. It uses O(h) auxiliary space and Θ(n) time.

### Height and cost

A path-shaped BST has h=n−1, while a well-shaped tree can have h=Θ(lg n). Search-tree algorithms in this chapter are parameterized by h; they are not automatically logarithmic. A BST is not a heap: a heap orders each parent against its children but does not impose a global left/right partition, so it cannot support inorder sorted output by a linear traversal in general.

## 12.2 Querying a binary search tree

### Search

At node x, compare k with x.key. If equal, return x; if smaller, continue left; otherwise continue right. The recursive and iterative algorithms follow the same path and take O(h) time. The iterative version avoids call-stack overhead.

### Minimum and maximum

`TREE-MINIMUM(x)` follows left pointers until NIL; `TREE-MAXIMUM(x)` follows right pointers. Each takes O(h).

### Successor and predecessor

The successor is the next node in inorder order (this definition also handles duplicate keys).
- If x has a right subtree, successor(x) is the minimum of that subtree.
- Otherwise climb parent pointers while x is a right child. The first ancestor reached from its left side is the successor; if none exists, return NIL.

Predecessor is symmetric:
- If x has a left subtree, return its maximum.
- Otherwise climb while x is a left child; the first ancestor reached from its right side is the predecessor.

Both operations take O(h). A complete inorder traversal implemented as minimum followed by n−1 successor calls is Θ(n), not Θ(nh): across the whole traversal, each tree edge is traversed only a constant number of times. Similarly, k successive successor calls from any starting node cost O(k+h).

## 12.3 Insertion and deletion

### Insertion

Walk from the root while maintaining x (current node) and y (the parent of x). Go left when the new key is smaller; otherwise go right. When x becomes NIL, attach the new node to y (or make it the root if the tree was empty). Set the new node's parent and initialize both children to NIL. Running time O(h).

Recursive insertion returns the updated subtree root and sets parent links carefully. For a production API, an iterative insertion is often easier to audit.

### Transplant

`TRANSPLANT(T,u,v)` replaces the subtree rooted at u with the subtree rooted at v:
1. If u is root, make v the root.
2. Otherwise replace u in its parent's appropriate child link with v.
3. If v is non-NIL, set v.parent=u.parent.

TRANSPLANT does not set v.left or v.right; its caller owns those changes.

### Deletion

Delete the exact node z supplied; this preserves the identity of every other node.

1. If z.left is NIL, transplant z with z.right.
2. Else if z.right is NIL, transplant z with z.left.
3. Otherwise let y be the minimum node in z.right (the successor; it has no left child).
   - If y is z.right, transplant z with y and make y.left=z.left.
   - Otherwise first transplant y with y.right, then set y.right=z.right and repair that child's parent; transplant z with y; finally set y.left=z.left and repair its parent.

The successor's original right child, if any, moves into the successor's old position. The case distinction is essential: when y=z.right, y must retain its existing right subtree and must not be transplanted out of its own position first. The search for the successor costs O(h); all pointer rewiring is O(1), so deletion is O(h).

### Duplicate keys

With the basic insertion rule, equal keys descend right. Repeated identical keys therefore form a chain and take Θ(n²) total insertion time. Alternatives in Problem 12-1 include alternating sides, storing equal keys in a list at one node, or randomizing the direction. The list-at-node strategy avoids height growth due solely to duplicates.

## Engineering perspectives

- A plain BST is not a balanced tree. If worst-case logarithmic operations are required, use a self-balancing tree (Chapter 13).
- Parent pointers simplify successor/predecessor and deletion but add one pointer per node.
- Preserve node identity when callers may retain node handles. CLRS's deletion physically moves the successor node rather than copying its key into z.
- Define duplicate-key semantics explicitly: set, multiset, or key-to-list map.
- Test root deletion, leaf deletion, one-child deletion, both successor cases, duplicate keys, and empty/singleton trees.
- Recursive traversals can hit recursion-depth limits on a degenerate tree; iterative traversal is safer for adversarial height.

## Operation summary

| Operation | Time |
|---|---:|
| Search, minimum, maximum | O(h) |
| Successor, predecessor | O(h) |
| Inorder/preorder/postorder traversal | Θ(n) |
| Insert | O(h) |
| Delete | O(h) |
| Space for tree | Θ(n) |
