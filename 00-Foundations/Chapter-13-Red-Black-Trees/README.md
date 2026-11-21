# Chapter 13 — Red-Black Trees

**Reference:** CLRS, Fourth Edition (2022), Sections 13.1–13.4, printed pages 331–359.

A red-black tree is a binary search tree augmented with one color bit per node. Its color constraints guarantee logarithmic height, so search, minimum, maximum, successor, predecessor, insertion, and deletion all run in O(lg n) worst-case time.

## 13.1 Properties of red-black trees

### Five properties

A red-black tree satisfies:
1. Every node is RED or BLACK.
2. The root is BLACK.
3. Every NIL leaf is BLACK.
4. A RED node has two BLACK children (no red parent-child edge).
5. For every node, every simple path from that node to a descendant NIL leaf contains the same number of BLACK nodes.

CLRS models NIL leaves as external nodes. A single sentinel T.nil represents all NILs and the root's parent. Its color is BLACK. Its parent field is assigned during operations so that fixup code can safely inspect the parent of a NIL replacement.

The black-height bh(x) is the number of BLACK nodes on any path from (but not including) x down to a NIL leaf. Property 5 makes it well-defined. A NIL sentinel has black-height 0.

### Height lemma

**Lemma:** A red-black tree with n internal nodes has height h ≤ 2 lg(n+1).

Proof outline:
- A subtree rooted at x contains at least 2^bh(x)−1 internal nodes. Induct on subtree height. Each child has black-height bh(x) or bh(x)−1, and each child subtree therefore has at least 2^(bh(x)−1)−1 internal nodes.
- Since red nodes cannot be adjacent, at least half the nodes on any root-to-NIL path (excluding the root) are black. Thus bh(root) ≥ h/2.
- Hence n ≥ 2^(h/2)−1, so h ≤ 2 lg(n+1).

Consequently, every ordinary BST search/query operation takes O(lg n) worst-case time. Ordinary BST insertion/deletion pointer changes are not sufficient by themselves: they can violate the color/black-height invariants.

## 13.2 Rotations

A left rotation at x requires x.right=y≠NIL. It makes y the root of the local subtree, x its left child, and y's former left subtree β become x.right. The inorder key order α < x < β < y < γ is unchanged. Right rotation is symmetric.

Rotations modify O(1) pointers and take Θ(1) time. They preserve the BST property and do not change node colors or keys. In a tree with n nodes, there are exactly n−1 possible single rotations: each parent-child edge permits exactly one rotation direction, depending on whether the child is left or right.

## 13.3 Insertion

RB-INSERT inserts z as in ordinary BST insertion, uses T.nil for absent children, and colors z RED. Coloring z red preserves every path's black count; coloring it black would add one black only to paths through z and could violate property 5. The only possible new violation is property 2 (if z is root) or property 4 (if z's parent is red).

RB-INSERT-FIXUP uses z, its parent, grandparent, and uncle. The code has symmetric branches depending on whether z's parent is a left or right child.

### Insertion cases (parent is a left child)

- **Case 1: uncle RED.** Recolor parent and uncle BLACK, grandparent RED, then move z to the grandparent. This pushes the possible red-red violation upward; no rotation.
- **Case 2: uncle BLACK and z is a right child.** Left-rotate at z's parent. This converts the configuration to case 3.
- **Case 3: uncle BLACK and z is a left child.** Recolor parent BLACK and grandparent RED, then right-rotate at the grandparent. This resolves the red-red edge.

The right-parent branch exchanges left and right. Case 2 falls through into case 3. The fixup loop repeats only after case 1, moving z two levels upward. It performs at most two rotations. Finally color the root BLACK.

Loop-invariant idea: z is RED; if z.parent is root then that parent is BLACK; any violation is at most one and is either root-red or a single red-red parent-child edge involving z. Cases preserve equal black-height and eliminate or move the sole violation. The final root recoloring restores property 2. Total insertion time O(lg n).

## 13.4 Deletion

RB-DELETE follows BST deletion but records:
- y: the node physically removed from its original position (z if z has at most one child; otherwise z's successor),
- y-original-color: its color before movement,
- x: the child that replaces y at its old position (possibly T.nil).

If y was RED, no black-height changes and no fixup is needed. If y was BLACK, x receives an implicit extra black. It is conceptually doubly black or red-and-black; the extra black is represented by the pointer x, not a third stored color.

RB-TRANSPLANT always assigns v.p = u.p, even when v is the sentinel. This is essential because fixup reads x.p even when x is NIL. In the two-child case, if y is z.right, explicitly set x.p=y when x is NIL.

### Deletion fixup: four cases (x is a left child)

Let w=x.p.right.
1. **Case 1: w RED.** Recolor w BLACK and parent RED; left-rotate at parent; recompute w. This converts to a case with BLACK sibling.
2. **Case 2: w BLACK and both children BLACK.** Color w RED and move x up to its parent. The extra black moves upward. This is the only case that repeats.
3. **Case 3: w BLACK, w.left RED, w.right BLACK.** Color w.left BLACK and w RED; right-rotate at w; recompute w. This converts to case 4.
4. **Case 4: w BLACK and w.right RED.** Give w the parent's color; color parent BLACK and w.right BLACK; left-rotate at parent; set x to root to terminate.

The right-child branch is the mirror image. Case 1 falls through to cases 2, 3, or 4; case 3 falls through to case 4. Cases 1, 3, and 4 use at most three rotations total. Case 2 may repeat O(lg n) times but uses no rotations. Finally color x BLACK. Thus RB-DELETE runs in O(lg n) time and performs at most three rotations.

### Why the extra black is necessary

Removing a BLACK node decreases the black count on paths through its old position. Treating x as carrying one extra black restores property 5 while fixup proceeds. The cases redistribute this extra black, absorb it into a RED x, or eliminate it at the root. The loop terminates when x is RED-and-black, x reaches the root, or case 4 resolves the deficit.

## Visual aids

- [Insertion fixup cases](images/insertion-fixup-cases.svg)
- [Deletion fixup cases](images/deletion-fixup-cases.svg)

## Engineering checklist

- Use one shared sentinel per tree and keep its parent correct during deletion.
- Keep the root BLACK after every public operation.
- Validate ordering, parent pointers, root color, red-parent rule, and equal black-height recursively.
- Test all insertion and deletion fixup cases, including mirrored cases and NIL replacement.
- Distinguish rotations from recolorings: insertion uses at most 2 rotations; deletion at most 3.
- Do not assume an arbitrary BST delete implementation preserves red-black properties.
