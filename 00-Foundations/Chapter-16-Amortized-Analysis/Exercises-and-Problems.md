# Chapter 16 — Exercises and Problems

Original solutions aligned to CLRS Fourth Edition, Sections 16.1–16.4.

## 16.1 Aggregate analysis

**16.1-1. MULTIPUSH.** Yes. Each pushed object can be popped at most once. Across n operations, at most n objects are pushed and at most n successful pops occur. MULTIPUSH adds work proportional to objects it inserts; total cost is O(n), hence amortized O(1).

**16.1-2. DECREMENT.** Alternate between 0 and 2^k−1 by decrementing from 0 modulo 2^k and incrementing back. Each operation flips all k bits, so n operations can cost Θ(nk).

**16.1-3. Powers of two.** Costs are 1 except at i=2^j, where cost is 2^j. Total cost ≤n+Σ(j=0…floor(lg n))2^j<3n. Amortized cost O(1).

## 16.2 Accounting method

**16.2-1. Periodic stack backup.** Assume the stack has at most k items and a backup copies the current stack after every k stack operations. Charge each PUSH and POP an amortized cost of 2: one unit pays for the operation, and one unit is saved in a global backup account. During any block of k operations, at most k credits accumulate; the backup copies at most k items, so those credits pay its cost. The account is nonnegative, and n operations plus all backups cost O(n).

**16.2-2. Exercise 16.1-3 by accounting.** Charge every operation 3. Ordinary operations cost 1 and deposit 2 credits. An operation at i=2^j costs 2^j; the accumulated account is sufficient because the total actual cost through any prefix n is at most n+Σ_(2^j≤n)2^j<3n. Thus the account never becomes negative and the amortized cost is 3.

**16.2-3. INCREMENT and RESET.** Keep a pointer h to the highest-order 1-bit (h=−1 when the counter is zero). INCREMENT performs the usual carry, updating h when a new highest 1-bit is set. RESET examines and clears only A[0…h], then sets h=−1. Use potential Φ(x)=x+popcount(x), where x is the counter's integer value. For an increment that resets t trailing ones and sets one zero, actual cost is at most t+1, while ΔΦ=1+(1−t)=2−t; amortized cost is at most 3. RESET costs at most h+1≤k; it changes x to 0 and popcount(x) to 0, so ΔΦ=−x−popcount(x). Since a nonzero k-bit value with highest set bit h satisfies x≥2^h≥h+1, the amortized reset cost is nonpositive. Starting from zero, Φ is nonnegative, so any sequence of n INCREMENT/RESET operations costs O(n).

## 16.3 Potential method

**16.3-1. Shifted potential.** Define Φ'(D)=Φ(D)−Φ(D_0). Then Φ'(D_0)=0, Φ'(D)≥0, and every potential difference is unchanged, so amortized costs are identical.

**16.3-2. Exercise 16.1-3.** Let C(i) be the actual cost of the first i operations and define Φ(i)=3i−C(i), with Φ(0)=0. Since C(i)=i+Σ_(2^j≤i) (2^j−1) <3i, Φ(i)≥0. The amortized cost of operation i is c_i+Φ(i)−Φ(i−1)=3 exactly. Thus every prefix has nonnegative credit and total actual cost is at most 3n.

**16.3-3. Min-heap.** Choose Φ(H)=c n lg n for n≥1 and Φ(empty)=0, with c sufficiently large. INSERT increases potential by O(lg n), matching its O(lg n) actual cost. EXTRACT-MIN reduces potential by Θ(lg n), paying for the O(lg n) heap repair; choose c to dominate the implementation constant. Φ is nonnegative and requires no bound on maximum heap size.

**16.3-4. Stack initial/final sizes.** Let P be pushes and R successful pops. R=P+s_0−s_n. Primitive push/pop cost is P+R=2P+s_0−s_n. Add constant per-call overhead if counting API calls rather than primitive operations.

**16.3-5. Queue with two stacks.** ENQUEUE pushes onto input stack. DEQUEUE pops output; if output is empty, transfer all input items to output, then pop. Each item is pushed once onto input, transferred once, and popped once. A sequence costs O(m), amortized O(1) per queue operation.

**16.3-6. DELETE-LARGER-HALF.** Use linear-time selection to partition around the median, then discard the largest ceil(|S|/2) elements. Let n_j be the multiset size immediately before deletion j, and let a_j be the number of INSERTs since the preceding deletion (take the initial size as 0). Since each deletion leaves at most half its input, n_(j+1)≤n_j/2+a_(j+1). Summing this recurrence gives Σ_j n_j≤2Σ_j a_j plus the initial-size term. Thus the total linear-time selection/partition work over all deletions is O(total INSERTs), and INSERT itself is O(1). Store survivors in an array; output in O(|S|). Total sequence cost is O(m).

## 16.4 Dynamic tables

**16.4-1. First insertion.** Initially num=size=0 and Φ=0. Allocate one slot and insert. Actual cost is 1; afterward α=1 and Φ=2(1−1/2)=1. Amortized cost is 2.

**16.4-2. Open addressing.** Keep α below a fixed threshold α_max<1 so expected probe counts remain bounded under uniform hashing. When threshold is reached, rebuild into a larger table. Rebuild costs Θ(n), but occurs only after Θ(n) further insertions, giving O(1) expected amortized insertion. A particular insertion can still cost Θ(n) due to probing or resizing.

**16.4-3. Accounting.** Charge a constant per insertion/deletion and save credits for future copying. With expansion at full and contraction below 1/4, each resize returns load factor to 1/2. It takes Θ(size) operations to reach the next threshold, accumulating Θ(size) credit to pay for Θ(size) copying.

**16.4-4. Contract by 2/3 below 1/3.** At the trigger, num≈size/3. After contraction, new size is 2size/3 and load factor is approximately 1/2. The potential |2num−size| is Θ(size) before contraction, enough to pay Θ(size) copying, and O(1) afterward (ignoring integer rounding). Away from resize, one insertion/deletion changes potential by at most 2. Amortized cost is O(1).

## Problems

**16-1. Binary reflected Gray code.**
(a) The bit that flips when moving from index i−1 to i is the position of the least significant 1-bit in i, equivalently ctz(i).
(b) Compute G(i)=i xor (i>>1) for i=0…2^k−1. Consecutive Gray codes differ in exactly one bit, including wraparound. Each output takes O(1), total Θ(2^k).

**16-2. Making binary search dynamic.**
(a) SEARCH binary-searches every nonempty sorted array A_i. There are O(lg n) arrays, each of size at most n, so O(lg² n) worst-case.
(b) INSERT treats the key as a singleton run. If A_0 is full, merge its contents with the run and carry the sorted result to A_1, continuing like binary addition. Worst-case O(n); each level-i array is rewritten only once per 2^i insertions, so O(n lg n) total merge work and O(lg n) amortized insertion.
(c) DELETE: find the key, remove it, then redistribute/rebuild lower-level sorted arrays to restore the binary-size invariant. After removing x from A_i, its remaining 2^i−1 keys are already sorted. Partition this sorted sequence into i consecutive sorted arrays of sizes 1,2,4,…,2^(i−1), thereby restoring the binary representation of n−1. This costs Θ(2^i) in the worst case, hence O(n). SEARCH remains O(lg² n). INSERT remains O(n) worst case; its O(lg n) amortized bound from part (b) applies only when the operation sequence contains INSERT and SEARCH. For mixed INSERT/DELETE sequences, the stated split-based implementation has O(n) worst-case cost per update and therefore O(n) amortized cost per update as a valid upper bound. This is not a tight amortized characterization: an alternating deletion of a large run and insertion can make both operations Θ(n). The problem does not require an O(lg n) amortized deletion bound.

**16-3. Amortized weight-balanced trees.**
(a) Inorder-traverse the subtree into a sorted array, then recursively choose middle elements as roots. Θ(m) time and O(m) auxiliary space.
(b) At each node, either child has size at most α times its parent. A root-to-leaf path therefore has O(log_(1/α)n)=O(lg n) height.
(c) Φ is a positive constant times a sum of nonnegative absolute imbalances, so Φ≥0. A 1/2-balanced tree has equal child sizes at every node, so Φ=0.
(d) If a subtree of size m is not α-balanced, one child has size >αm. Its imbalance exceeds (2α−1)m. Rebuilding makes the subtree perfectly balanced and removes that potential. Choose c≥1/(2α−1), up to the unit rebuilding-cost constant, to pay Θ(m).
(e) Search/update changes sizes along O(lg n) path; ordinary work and potential changes are O(lg n). A triggered rebuild is paid by the potential drop from (d). Amortized insertion/deletion is O(lg n).

**16-4. Red-black restructuring.**
(a) For insertion, take a perfect tree whose levels alternate BLACK and RED, with a BLACK root and a RED bottom internal level. Insert a new RED key as a child of a bottom-level RED node, choosing the side so its uncle is also RED. Insertion-fixup Case 1 recolors the parent and uncle BLACK and the grandparent RED, moving the violation up two levels. The same alternating pattern repeats at each higher level, for Θ(h)=Θ(lg n) recolorings; choose the insertion position/side so the propagation reaches the root. For deletion, start with a perfect all-BLACK tree and delete a BLACK leaf. Its sibling is BLACK with two BLACK children, so deletion-fixup Case 2 colors the sibling RED and moves the extra black to the parent. The same configuration repeats up the ancestor chain, causing Θ(h)=Θ(lg n) recolorings. Both examples have n=Θ(2^h), hence h=Θ(lg n).
(b) INSERT-FIXUP Case 1 is nonterminating because it can repeat at the grandparent; Cases 2 and 3 terminate after a constant number of additional steps (Case 2 immediately becomes Case 3). DELETE-FIXUP Case 2 is nonterminating because it moves x up one level and can repeat. Cases 1, 3, and 4 are terminating in the sense of the hint: Case 1 converts to one of Cases 2–4, Case 3 converts to Case 4, and Case 4 exits; each requires only O(1) additional work.
(c) INSERT-FIXUP Case 1 recolors red parent and uncle black and grandparent red; the number of red nodes decreases by 1.
(d) Lines 13–16 of RB-INSERT add one red node (+1 potential) and perform no rotations. Every nonterminating Case 1 decreases the red-node potential by 1 and makes no rotation. The terminating Case 2/3 sequence performs at most two rotations and changes potential by O(1). Thus the total amortized structural modifications are O(1).
(e) Each nonterminating iteration spends one unit of red-node potential, and the initial increase is one, so structural modifications per insertion are O(1) amortized.
(f) **INSERT-FIXUP.** The only nonterminating case is Case 1. Let P be the red parent, U its red uncle, and G their black grandparent; the newly inserted red node is a child of P. Before recoloring, w(P)=0 (P is red), w(U)=0 (U is red), and w(G)=2 (G is black with two red children). Their total is 2. After Case 1, P and U are black and G is red. P has exactly one red child (the inserted node), so w(P)=0; U has no red children, so w(U)=1; and w(G)=0. The total becomes 1, hence ΔΦ=−1. All other nodes retain their w-values. The loop can repeat only through Case 1, so each repetition releases one unit of potential; the terminating Cases 2–3 perform at most two rotations and O(1) recolorings. The insertion itself changes the potential by O(1). Thus the amortized structural modifications per insertion-fixup are O(1).

(g) **DELETE-FIXUP.** Figure 13.7 shows that only Case 2 repeats. Let B=x:p and D=x's sibling. At entry, D is black with two black children, so w(D)=1. Write c for B's color. If c=RED, then w(B)=0; after Case 2, B remains red and D becomes red, so both weights are 0 and the potential drops by 1. If c=BLACK, then before Case 2, B has no red children and w(B)=1; after D is recolored red, B is black with exactly one red child, so w(B)=0, while w(D)=0. The affected total therefore falls from 2 to 0. In either case ΔΦ≤−1. No other node's w-value changes. Case 2 is the only repeating case; Cases 1 and 3 each lead to a following case after O(1) work, and Case 4 exits after O(1) work and at most three rotations. Thus each repetition is paid by a unit potential decrease, and the nonrepeating work is constant: amortized structural modifications per deletion-fixup are O(1).
(h) Each insert/delete contributes O(1) initial/final potential change, while nonterminating iterations are paid by unit potential decreases and terminating cases cost O(1). Since Φ starts at 0 and is nonnegative, m updates cause O(m) total structural modifications.
