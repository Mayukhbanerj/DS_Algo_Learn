# Chapter 13 — Exercises and Problems

Original solutions based on CLRS Fourth Edition, Sections 13.1–13.4. These are working solutions and remain subject to source-by-source audit.

## 13.1 Properties of red-black trees

**13.1-1. Complete tree colorings.** The complete BST of height 3 on keys 1…15 has root 8; level 1 is 4,12; level 2 is 2,6,10,14; level 3 is 1,3,5,7,9,11,13,15. Add NIL leaves. With root BLACK: for black-height 2 color levels 1,2,3 as RED, BLACK, RED; for black-height 3 color them RED, BLACK, BLACK; for black-height 4 color all three levels BLACK. Each assignment has no adjacent red nodes and gives the stated equal black count on every path.

**13.1-2. Insert 36.** In Figure 13.1, 36 is inserted as the right child of 35. Color 36 RED. Its parent 35 and uncle 39 are RED, so case 1 recolors 35 and 39 BLACK, colors 38 RED, and moves z to 38. Now 38 is a right child of red node 30 and its uncle 47 is BLACK: case 2 left-rotates at 30, then case 3 colors 38 BLACK, 41 RED, and right-rotates at 41. The resulting local subtree is rooted at 38 BLACK, with left child 30 RED (children 28 BLACK and 35 BLACK, whose right child is 36 RED) and right child 41 RED (children 39 BLACK and 47 BLACK). If 36 were BLACK, the path through 36 would gain a black node while paths through the other NIL leaves under 35 would not, violating property 5.

**13.1-3. Relaxed root.** Changing a red root to black cannot violate properties 1, 2, 3, or 4. It increases by one the black count on every path from the root to a NIL leaf, so all such paths remain equal. Thus the result is a red-black tree.

**13.1-4. Absorbing red children.** A black node can absorb zero, one, or two red children. Each absorbed red child contributes its own (at most two) children, so the resulting black node has degree 2, 3, or 4. Equal black-height in the original tree implies that all leaves in the multiway tree have the same depth.

**13.1-5. Longest versus shortest path.** Every red-black path has no two consecutive red nodes. Therefore among any root-to-leaf path of length L, at least floor(L/2) nodes are black. Since all paths from x have the same black-height, the longest path is at most twice the shortest path (with the endpoint convention handled consistently).

**13.1-6. Internal-node bounds.** For black-height k, the minimum number of internal nodes is 2^k−1, achieved when every internal node is BLACK and the tree is perfect. The maximum is 4^k−1: alternate a BLACK level with a RED level, filling both children at every level, until the final RED internal level; this gives a perfect binary tree of height 2k−1.

**13.1-7. Red/black ratio.** The maximum red-to-black internal-node ratio is 2, achieved by the full alternating-color tree (each BLACK internal node has two RED children and each RED internal node has two BLACK children, ending at a RED level). The minimum is 0, achieved by an all-BLACK tree.

**13.1-8. Red node with one non-NIL child.** A red node's children must be black. If exactly one child were non-NIL, a path through that child would contain at least one more black node than the path through the NIL child, contradicting equal black-height.

## 13.2 Rotations

**13.2-1. RIGHT-ROTATE.** Mirror LEFT-ROTATE: let y=x.left; move y.right to x.left and repair its parent if non-NIL; give y x's parent and update the root/parent child link; set y.right=x and x.parent=y.

**13.2-2. Number of rotations.** Each of the n−1 parent-child edges supports exactly one rotation direction: a left rotation if the child is right, a right rotation if the child is left. Thus n−1 possible single rotations.

**13.2-3. Depth changes under left rotation.** For x with right child y and subtrees α, β, γ: nodes in α keep their depth; nodes in β move up one level; nodes in γ move up one level; x moves down one level and y moves up one level.

**13.2-4. Transform any BST into any other.** At most n−1 right rotations convert a BST into a right-going chain. Convert the target tree to the same chain using at most n−1 right rotations, then reverse that sequence (using left rotations) to obtain the target from the chain. Total O(n) rotations.

**13.2-5. Right-conversion.** Let T1 be the all-right chain on keys 1,2,3 and T2 the balanced tree with root 2 and children 1,3. T1 has no left child, so no RIGHT-ROTATE is possible and T2 is unreachable. For the bound, define Φ(T) as the number of ancestor-descendant pairs (u,v) with u.key>v.key. A right rotation at y with left child x removes the inversion pair (y,x), and removes every inversion pair (y,a) for a in the former left subtree α of x; it creates no new inversion pair. Thus Φ strictly decreases by at least 1. Since 0≤Φ≤binom(n,2), any right-rotation sequence has at most binom(n,2)=O(n²) calls.

## 13.3 Insertion

**13.3-1. Why insert RED?** Inserting a RED node leaves the black count on every root-to-leaf path unchanged. Inserting BLACK increases the count only on paths through the new node, violating property 5.

**13.3-2. Insert 41, 38, 31, 12, 19, 8.** Standard CLRS fixup trace to be added with each recoloring/rotation and resulting tree after every insertion.

**13.3-3. Black-height labels.** For Figures 13.5 and 13.6, assign each subtree root black-height k; count the black contribution of each displayed node on paths to α, β, γ, δ, ε and verify the transformations preserve each total. Detailed labels pending.

**13.3-4. Sentinel never becomes RED.** The fixup code recolors the parent, uncle, and grandparent of z. The uncle may be the sentinel only in the BLACK-uncle branches, where it is not recolored RED; in case 1 the uncle is RED and therefore cannot be the sentinel. Thus T.nil.color remains BLACK.

**13.3-5. At least one RED node for n>1.** If all internal nodes were BLACK, every root-to-NIL path would have black-height equal to its number of internal nodes. The newly inserted node remains RED throughout fixup: case 1 moves the z pointer upward but does not recolor the inserted node; cases 2–3 may move the pointer to its parent, but the inserted node remains RED. Since n>1, the inserted node is not the root, so at least one RED internal node remains.

**13.3-6. No parent pointers.** During insertion descent, retain the ancestor stack (or a stack of node/direction pairs). After inserting z, simulate fixup using the stack to access parent and grandparent; rotations update the relevant stack entries. The stack has O(lg n) entries in a red-black tree, so time and auxiliary space are O(lg n).

## 13.4 Deletion

**13.4-1. Deleting red y.** Removing or moving a RED y does not change any path's black count. If y is replaced by its child x, x is BLACK (or NIL); no red-red adjacency is introduced. If y is successor moved to z's position, it receives z's color, preserving the black count at the replacement position.

**13.4-2. Root black after fixup.** The loop exits only when x is the root or x is RED. If x is the root, line 44 colors it BLACK; if x is RED, line 44 also colors it BLACK. Thus the root is BLACK.

**13.4-3. Red x and red parent.** The extra black is attached to x. If x is RED, the loop condition fails and line 44 colors x BLACK, absorbing the extra black; its parent remains BLACK under the pre-fixup configuration, restoring property 4.

**13.4-4. Delete 8,12,19,31,38,41.** Start from the tree produced by Exercise 13.3-2 and trace RB-DELETE after each key. Full color/pointer trace pending.

**13.4-5. Sentinel accesses.** Lines that inspect sibling/child colors may read T.nil.color; RB-TRANSPLANT writes T.nil.p; the special assignment x.p=y may write the sentinel parent. In fixup, color assignments to a sibling or sibling child are safe only under the case invariants that rule out recoloring the sentinel RED.

**13.4-6. Black counts in deletion cases.** Use count(RED)=0 and count(BLACK)=1. Include the extra black at x in every path containing x. In each of cases 1–4, compare the sum from the local subtree root to each subtree root α,β,…,ζ before and after recoloring/rotation. Symbolic counts involving c and c′ must be shown case by case in the final audit.

**13.4-7. Parent black at start of case 1.** Case 1 has a RED sibling w. Since w is RED, its parent x.p must be BLACK by property 4. Therefore the color swap in lines 5–6 is valid.

**13.4-8. Insert then immediately delete.** Not necessarily the same tree. Start with root 2 BLACK and left child 1 RED. Insert 0: case 3 rotates right at 2 and yields root 1 BLACK with children 0 RED and 2 RED. Delete 0: the result is root 1 BLACK with right child 2 RED, not the original root 2 with left child 1.

**13.4-9. Range enumeration.** Since a and b are keys in the tree, search for a in O(lg n), then repeatedly output the current node and call TREE-SUCCESSOR until key b is output. There are m outputs and O(m) total successor traversal by amortization, giving O(m+lg n). If a and b need not be present, perform a lower-bound search for the smallest key ≥a in O(lg n), then enumerate successors while key≤b; same bound.

## Problems

**13-1. Persistent dynamic sets.** (a) Copy only nodes on the search path and share untouched subtrees. Insert copies the path to the insertion point; delete copies the search path and any successor-splice path. (b) Recursive path-copy insertion returns copied ancestors with one child replaced by the new subtree. (c) O(h) time and O(h) new nodes. (d) Parent pointers make shared children point to one parent only, so changing a copied ancestor's child requires updating the child's parent; that child may be shared with the old version, forcing further copying. In the worst case this propagates across Θ(n) nodes. (e) Use a persistent balanced representation with path copying and no parent pointers; red-black balancing requires carefully persistent rotations/recoloring and O(lg n) copied nodes. Details pending.

**13-2. RB-JOIN.** (a) Store bh(T) at the tree object. Recompute it by following one root-to-NIL path after an update, which costs O(lg n) and does not change the asymptotic update bound. During a descent, maintain the current node's black-height h; for a child c, set bh(c)=h−1 if c is BLACK and bh(c)=h if c is RED (NIL has bh 0). This is O(1) per visited node. (b) Assume bh(T1)≥bh(T2)=k. Descend the right spine of T1, maintaining bh. Find the BLACK node y on that spine with bh(y)=k and largest key; the right-spine order makes it the rightmost qualifying node. (c) Replace y at its parent by a new node x; set x.left=y, x.right=T2.root, and repair the three parent links. Since bh(y)=bh(T2)=k and x is RED, paths through either child have equal black count, and BST order follows from every T1 key≤x.key≤every T2 key. (d) Make x RED. Properties 1, 3, and 5 hold; insertion fixup restores properties 2 and 4 in O(lg n). (e) If bh(T1)<bh(T2), exchange the roles and descend the left spine of the taller T2 to find the leftmost BLACK y with bh(y)=bh(T1); join with x.left=T1 and x.right=y. (f) One spine descent and one insertion fixup each cost O(lg n), so RB-JOIN is O(lg n).

**13-3. AVL trees.** (a) Let N_h be the minimum number of nodes in an AVL tree of height h, with empty-tree height −1. The sparsest height-h tree has child heights h−1 and h−2, so N_h=1+N_(h−1)+N_(h−2), with N_−1=0 and N_0=1. Thus N_h is Fibonacci-growth, Ω(φ^h), and h=O(lg n). (b) Let y be the taller child of x. If the right subtree is taller by 2, perform a left rotation at x when y's right subtree is at least as tall as y's left; otherwise right-rotate y then left-rotate x. Mirror these cases when the left subtree is taller by 2. Update heights bottom-up and return the new subtree root. (c) Recursively insert by BST order; on return update x.h and call BALANCE(x), reconnecting the returned subtree root to its parent. (d) The recursion follows one root-to-leaf path of O(lg n) nodes. Each balance step costs O(1), so time is O(lg n); at most a constant number of rotations per visited ancestor gives O(lg n) rotations (indeed standard AVL insertion needs at most two rotations).
