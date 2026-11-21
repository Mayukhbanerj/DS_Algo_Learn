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

**16.3-2. Exercise 16.1-3.** Let Φ(i)=2(i−2^floor(lg i)) for i≥1, and Φ(0)=0. Between powers of two the potential rises by 2 per operation; at a power of two it drops by Θ(i), paying for the expensive operation. Actual cost plus potential change is O(1) amortized, so total cost O(n).

**16.3-3. Min-heap.** Choose Φ(H)=c n lg n for n≥1 and Φ(empty)=0, with c sufficiently large. INSERT increases potential by O(lg n), matching its O(lg n) actual cost. EXTRACT-MIN reduces potential by Θ(lg n), paying for the O(lg n) heap repair; choose c to dominate the implementation constant. Φ is nonnegative and requires no bound on maximum heap size.

**16.3-4. Stack initial/final sizes.** Let P be pushes and R successful pops. R=P+s_0−s_n. Primitive push/pop cost is P+R=2P+s_0−s_n. Add constant per-call overhead if counting API calls rather than primitive operations.

**16.3-5. Queue with two stacks.** ENQUEUE pushes onto input stack. DEQUEUE pops output; if output is empty, transfer all input items to output, then pop. Each item is pushed once onto input, transferred once, and popped once. A sequence costs O(m), amortized O(1) per queue operation.

**16.3-6. DELETE-LARGER-HALF.** Use linear-time selection to partition around the median, then discard the largest ceil(|S|/2) elements. Each deletion removes at least half the current elements, so the total sizes of the sets partitioned over all deletion operations form a geometric series, O(total inserted items). Store survivors in an array; output in O(|S|). Total sequence cost O(m).

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
(c) DELETE: find the key, remove it, then redistribute/rebuild lower-level sorted arrays to restore the binary-size invariant. The exact amortized bound depends on the redistribution strategy; this draft flags the missing implementation detail rather than claiming a bound without a complete strategy.

**16-3. Amortized weight-balanced trees.**
(a) Inorder-traverse the subtree into a sorted array, then recursively choose middle elements as roots. Θ(m) time and O(m) auxiliary space.
(b) At each node, either child has size at most α times its parent. A root-to-leaf path therefore has O(log_(1/α)n)=O(lg n) height.
(c) Φ is a positive constant times a sum of nonnegative absolute imbalances, so Φ≥0. A 1/2-balanced tree has equal child sizes at every node, so Φ=0.
(d) If a subtree of size m is not α-balanced, one child has size >αm. Its imbalance exceeds (2α−1)m. Rebuilding makes the subtree perfectly balanced and removes that potential. Choose c≥1/(2α−1), up to the unit rebuilding-cost constant, to pay Θ(m).
(e) Search/update changes sizes along O(lg n) path; ordinary work and potential changes are O(lg n). A triggered rebuild is paid by the potential drop from (d). Amortized insertion/deletion is O(lg n).

**16-4. Red-black restructuring.**
(a) A black-height-Θ(lg n) tree can be arranged so insertion fixup Case 1 propagates recoloring up the tree; similarly a deletion-fixup Case 2 chain can propagate upward. Each yields Θ(lg n) color changes.
(b) INSERT-FIXUP Case 1 is nonterminating; Cases 2 and 3 terminate. DELETE-FIXUP Case 1 transforms to another case; Case 2 moves x upward and is nonterminating; Cases 3 and 4 terminate.
(c) INSERT-FIXUP Case 1 recolors red parent and uncle black and grandparent red; the number of red nodes decreases by 1.
(d) Ordinary insertion adds a red node (+1 potential). Nonterminating Case 1 decreases potential by 1 and uses O(1) structural modifications; terminating cases use O(1) structural modifications and change potential by O(1).
(e) Each nonterminating iteration spends one unit of red-node potential, and the initial increase is one, so structural modifications per insertion are O(1) amortized.
(f) Under w(x), each nonterminating insertion-fixup case reduces total potential by at least 1; amortized structural modifications are O(1).
(g) The corresponding local analysis for deletion-fixup shows every nonterminating case decreases Φ by at least 1; amortized structural modifications are O(1).
(h) Each insert/delete contributes O(1) initial/final potential change, while nonterminating iterations are paid by unit potential decreases and terminating cases cost O(1). Since Φ starts at 0 and is nonnegative, m updates cause O(m) total structural modifications.
