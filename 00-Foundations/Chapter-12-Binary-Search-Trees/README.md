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

## Visual aid

[Search-path counterexample for Exercise 12.2-4](images/search-path-counterexample.svg)

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


## Algorithm patterns and proof obligations

### Iterative search

```text
ITERATIVE-TREE-SEARCH(x, k)
    while x ≠ NIL and k ≠ x.key
        if k < x.key
            x = x.left
        else
            x = x.right
    return x
```

At every iteration, if k exists in the current subtree, it must be in the subtree rooted at x. When k<x.key, the BST invariant rules out x and the entire right subtree; the symmetric argument applies when k>x.key. The algorithm therefore never discards the only possible location of k. Each iteration descends one level, so it performs O(h) work.

### Successor: why the two cases are exhaustive

If x.right exists, every key in x's right subtree is greater than or equal to x.key, and its minimum is the least key encountered after x in inorder. If x.right is NIL, no later node can be below x. Move upward while x is a right child: each such parent has already appeared before x in inorder. The first ancestor reached from its left child is visited after x and before any higher candidate. If the climb reaches NIL, x was the maximum.

### Inorder traversal: exact call count

For n internal nodes, every internal node generates exactly two recursive calls, one for each child pointer, and the recursion tree has n internal-call nodes and n+1 NIL-call leaves. Total calls are 2n+1. Each call does constant nonrecursive work, so the total is Θ(n), independent of tree shape. The recursion stack can nevertheless be Θ(h), which becomes Θ(n) for a chain.

### Insertion loop invariant

At the start of each iteration, y is the parent of x, and every node above x has already been classified relative to z.key: z belongs in the subtree rooted at x. The comparison chooses the only child subtree consistent with the BST invariant. When x becomes NIL, the child link just followed is exactly the unique insertion position; attaching z there preserves the invariant. The search path has at most h+1 nodes.

### Deletion: pointer-update checklist

The two-child case is easiest to audit by separating splicing out the successor from moving it into z's position:

```text
TREE-DELETE(T, z)
    if z.left == NIL
        TRANSPLANT(T, z, z.right)
    elseif z.right == NIL
        TRANSPLANT(T, z, z.left)
    else
        y = TREE-MINIMUM(z.right)
        if y != z.right
            TRANSPLANT(T, y, y.right)
            y.right = z.right
            y.right.p = y
        TRANSPLANT(T, z, y)
        y.left = z.left
        y.left.p = y
```

Why does this preserve order? y is the minimum of z.right, so every key in z.left is ≤ z.key ≤ y.key, and every key remaining in z.right is ≥ y.key. When y is not z.right, it has no left child, so replacing y by y.right at its old location preserves that subtree. When y=z.right, it is already in the position where it must remain and only its left link changes. This is why the direct-child branch must not splice y out first.

The procedure moves the successor node object rather than copying its key. Thus a caller holding a pointer to z can rely on z itself being the deleted object; other node identities remain intact.

### Adversarial shape and sorting connection

Inserting already sorted keys creates a chain: the i-th insertion compares against i−1 existing nodes, for total Σ(i−1)=n(n−1)/2=Θ(n²). Conversely, if each insertion sees height O(lg n), total insertion cost is O(n lg n). Inorder output then adds Θ(n). This is the BST-sort reduction behind Exercise 12.1-5's comparison-sorting lower bound.
