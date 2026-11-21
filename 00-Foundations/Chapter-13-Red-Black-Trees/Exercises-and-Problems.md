# Chapter 13 — Exercises and Problems

Original solutions based on CLRS Fourth Edition, Sections 13.1–13.4. These are working solutions and remain subject to source-by-source audit.

## 13.1 Properties of red-black trees

**13.1-1. Complete tree colorings.** The complete BST of height 3 on keys 1…15 is the perfect tree with root 8, children 4 and 12, and levels 1,3,5,7,9,11,13,15 below. Add NIL leaves. Three valid uniform colorings with black-heights 2, 3, and 4 are to be specified and checked in the final audit.

**13.1-2. Insert 36.** In the displayed tree of Figure 13.1, ordinary BST insertion places 36 as the appropriate leaf. Coloring it RED preserves black-height and can only create a red-red violation if its parent is red. Coloring it BLACK increases the black count only on the new leaf path and violates property 5. Therefore the red insertion is the correct starting point; whether it is already a red-black tree depends on the parent color and must be checked in the figure.

**13.1-3. Relaxed root.** Changing a red root to black cannot violate properties 1, 2, 3, or 4. It increases by one the black count on every path from the root to a NIL leaf, so all such paths remain equal. Thus the result is a red-black tree.

**13.1-4. Absorbing red children.** A black node can absorb zero, one, or two red children. Each absorbed red child contributes its own (at most two) children, so the resulting black node has degree 2, 3, or 4. Equal black-height in the original tree implies that all leaves in the multiway tree have the same depth.

**13.1-5. Longest versus shortest path.** Every red-black path has no two consecutive red nodes. Therefore among any root-to-leaf path of length L, at least floor(L/2) nodes are black. Since all paths from x have the same black-height, the longest path is at most twice the shortest path (with the endpoint convention handled consistently).

**13.1-6. Internal-node bounds.** For black-height k, the minimum number of internal nodes is 2^k−1, achieved by a perfectly black tree. The maximum is achieved by alternating red and black levels while maintaining equal black-height; derive the exact recurrence and closed form in the final audit.

**13.1-7. Red/black ratio.** The ratio is maximized by making every black internal node have two red children and every red node have two black children, continuing to the allowed height; minimize by an all-black tree. Exact finite-n ratio and extremal shape require final derivation.

**13.1-8. Red node with one non-NIL child.** A red node's children must be black. If exactly one child were non-NIL, a path through that child would contain at least one more black node than the path through the NIL child, contradicting equal black-height.

## 13.2 Rotations

**13.2-1. RIGHT-ROTATE.** Mirror LEFT-ROTATE: let y=x.left; move y.right to x.left and repair its parent if non-NIL; give y x's parent and update the root/parent child link; set y.right=x and x.parent=y.

**13.2-2. Number of rotations.** Each of the n−1 parent-child edges supports exactly one rotation direction: a left rotation if the child is right, a right rotation if the child is left. Thus n−1 possible single rotations.

**13.2-3. Depth changes under left rotation.** For x with right child y and subtrees α, β, γ: nodes in α keep their depth; nodes in β move up one level; nodes in γ move up one level; x moves down one level and y moves up one level.

**13.2-4. Transform any BST into any other.** At most n−1 right rotations convert a BST into a right-going chain. Convert the target tree to the same chain using at most n−1 right rotations, then reverse that sequence (using left rotations) to obtain the target from the chain. Total O(n) rotations.

**13.2-5. Right-conversion.** Right rotations preserve the inorder sequence and have a directional restriction; not every target tree is reachable from every source by right rotations alone. Example and O(n²) upper-bound proof are pending final audit.

## 13.3 Insertion

**13.3-1. Why insert RED?** Inserting a RED node leaves the black count on every root-to-leaf path unchanged. Inserting BLACK increases the count only on paths through the new node, violating property 5.

**13.3-2. Insert 41, 38, 31, 12, 19, 8.** Standard CLRS fixup trace to be added with each recoloring/rotation and resulting tree after every insertion.

**13.3-3. Black-height labels.** For Figures 13.5 and 13.6, assign each subtree root black-height k; count the black contribution of each displayed node on paths to α, β, γ, δ, ε and verify the transformations preserve each total. Detailed labels pending.

**13.3-4. Sentinel never becomes RED.** The fixup code recolors the parent, uncle, and grandparent of z. The uncle may be the sentinel only in the BLACK-uncle branches, where it is not recolored RED; in case 1 the uncle is RED and therefore cannot be the sentinel. Thus T.nil.color remains BLACK.

**13.3-5. At least one RED node for n>1.** If all internal nodes were BLACK, every root-to-NIL path would have black-height equal to its number of internal nodes. A tree with more than one internal node has leaves at different depths unless it is a perfect tree; in a perfect all-black tree, all leaves do have equal depth, so this argument alone is insufficient. A complete final proof is pending.

**13.3-6. No parent pointers.** During insertion descent, retain the ancestor stack (or a stack of node/direction pairs). After inserting z, simulate fixup using the stack to access parent and grandparent; rotations update the relevant stack entries. The stack has O(lg n) entries in a red-black tree, so time and auxiliary space are O(lg n).

## 13.4 Deletion

**13.4-1. Deleting red y.** Removing or moving a RED y does not change any path's black count. If y is replaced by its child x, x is BLACK (or NIL); no red-red adjacency is introduced. If y is successor moved to z's position, it receives z's color, preserving the black count at the replacement position.

**13.4-2. Root black after fixup.** The loop exits only when x is the root or x is RED. If x is the root, line 44 colors it BLACK; if x is RED, line 44 also colors it BLACK. Thus the root is BLACK.

**13.4-3. Red x and red parent.** The extra black is attached to x. If x is RED, the loop condition fails and line 44 colors x BLACK, absorbing the extra black; its parent remains BLACK under the pre-fixup configuration, restoring property 4.

**13.4-4. Delete 8,12,19,31,38,41.** Start from the tree produced by Exercise 13.3-2 and trace RB-DELETE after each key. Full color/pointer trace pending.

**13.4-5. Sentinel accesses.** Lines that inspect sibling/child colors may read T.nil.color; RB-TRANSPLANT writes T.nil.p; the special assignment x.p=y may write the sentinel parent. In fixup, color assignments to a sibling or sibling child are safe only under the case invariants that rule out recoloring the sentinel RED.

**13.4-6. Black counts in deletion cases.** Use count(RED)=0 and count(BLACK)=1. Include the extra black at x in every path containing x. In each of cases 1–4, compare the sum from the local subtree root to each subtree root α,β,…,ζ before and after recoloring/rotation. Symbolic counts involving c and c′ must be shown case by case in the final audit.

**13.4-7. Parent black at start of case 1.** Case 1 has a RED sibling w. Since w is RED, its parent x.p must be BLACK by property 4. Therefore the color swap in lines 5–6 is valid.

**13.4-8. Insert then immediately delete.** Not necessarily the same tree: insertion fixup may recolor/rotate existing nodes; deleting the inserted node can restore a valid red-black tree with a different shape/coloring. A concrete trace is pending final audit.

**13.4-9. Range enumeration.** Since a and b are keys in the tree, search for a in O(lg n), then repeatedly output the current node and call TREE-SUCCESSOR until key b is output. There are m outputs and O(m) total successor traversal by amortization, giving O(m+lg n). If a and b need not be present, perform a lower-bound search for the smallest key ≥a in O(lg n), then enumerate successors while key≤b; same bound.

## Problems

**13-1. Persistent dynamic sets.** (a) Copy only nodes on the search path and share untouched subtrees. Insert copies the path to the insertion point; delete copies the search path and any successor-splice path. (b) Recursive path-copy insertion returns copied ancestors with one child replaced by the new subtree. (c) O(h) time and O(h) new nodes. (d) Parent pointers make shared children point to one parent only, so changing a copied ancestor's child requires updating the child's parent; that child may be shared with the old version, forcing further copying. In the worst case this propagates across Θ(n) nodes. (e) Use a persistent balanced representation with path copying and no parent pointers; red-black balancing requires carefully persistent rotations/recoloring and O(lg n) copied nodes. Details pending.

**13-2. RB-JOIN.** (a) Maintain tree black-height as a tree-level attribute; during descent, decrement the remaining black-height when passing a BLACK node. Rotations/recolorings change it only in a constant, locally maintainable way. (b) Descend the taller tree's appropriate spine to find a BLACK node y with black-height equal to the shorter tree's black-height. (c) Replace y's position with red x whose left/right children are y and T2 (ordered by the join precondition). (d) Color x RED, then use insertion fixup to restore properties 2 and 4. (e) Swap the trees if necessary and mirror the argument. (f) O(lg n) descent plus O(lg n) fixup. Exact spine direction and pointer details pending.

**13-3. AVL trees.** (a) Minimum nodes satisfy N_h=1+N_{h−1}+N_{h−2}, so N_h grows as Fibonacci and h=O(lg n). (b) If left/right child heights differ by 2, use single or double rotations based on the taller child's outer/inner subtree heights. (c) Insert recursively, update heights on return, and call BALANCE at each ancestor. (d) O(lg n) ancestors are revisited; at most a constant number of rotations per ancestor, hence O(lg n) time and rotations. Full cases and exact height conventions pending.
