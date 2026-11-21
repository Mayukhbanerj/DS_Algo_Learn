# Chapter 15 — Exercises and Problems

Original study solutions based on CLRS Fourth Edition, Sections 15.1–15.4.

## 15.1 Activity selection

**15.1-1. Dynamic programming.** Add sentinel activities a_0 and a_(n+1), with f_0=0 and s_(n+1)=∞. For i<j, let c[i,j] be the maximum number of mutually compatible activities strictly between a_i and a_j. Then c[i,j]=max_{i<k<j, f_i≤s_k, f_k≤s_j}(1+c[i,k]+c[k,j]), with empty maximum 0. Store the maximizing k. There are O(n²) states and O(n) candidate k values per state: O(n³) time and O(n²) space. Reconstruct recursively from the stored k values. The sorted greedy algorithm is Θ(n), asymptotically faster.

**15.1-2. Latest start.** Sort by nonincreasing start time. Choose the compatible activity with largest start time, then recurse on activities finishing no later than its start. In an optimal solution, let a be the last-starting selected activity. The greedy activity g starts at least as late as a; replacing a by g preserves compatibility with every earlier selected activity and cannot reduce cardinality. The remaining prefix is the same problem, so induction proves optimality.

**15.1-3. Bad greedy rules.**
- Least duration: choose C=[3,5) before A=[0,4) and B=[4,8). C conflicts with both, while A and B are compatible; greedy gets 1, optimum gets 2.
- Earliest start: choose A=[0,10) before B=[1,2), C=[2,3), D=[3,4). Greedy gets 1, optimum gets 3.
- Fewest overlaps: with activities in this order, A=[6,10), B=[18,23), C=[11,21), D=[11,22), E=[0,6), F=[4,8), G=[9,13), H=[1,4), I=[2,3), the initial overlap degrees are 2,2,3,3,3,2,3,2,2. Breaking the minimum-degree tie in favor of A selects A, then B, then E (3 activities). But H,F,G,B are mutually compatible (4 activities). Thus this tie-breaking rule is not guaranteed optimal.

**15.1-4. Minimum lecture halls.** Sort by start time. Maintain a min-heap of (current finish time, hall id). For each activity, reuse the hall with minimum finish if that finish≤the activity's start; otherwise create a hall. Update the selected hall's finish. If a new hall is opened, all existing halls are occupied at that activity's start, so the number of halls used is a lower bound on any schedule. Hence the algorithm is optimal. O(n lg n) time.

**15.1-5. Weighted activities.** Sort by finish time and compute p(j), the rightmost compatible predecessor. OPT[0]=0; OPT[j]=max(v_j+OPT[p(j)],OPT[j−1]). Store the choice and backtrack. O(n lg n) preprocessing and O(n) DP time, O(n) space.

## 15.2 Greedy strategy

**15.2-1. Fractional knapsack proof.** Suppose a feasible solution takes some weight from item j while a higher-density item i is not full. Move ε weight from j to i. Value changes by ε(v_i/w_i−v_j/w_j)>0, contradicting optimality. Therefore some optimum fills items in nonincreasing density order.

**15.2-2. 0-1 knapsack DP.** Let K[i,w] be maximum value using the first i items and capacity w. K[i,w]=K[i−1,w] if w_i>w; otherwise max(K[i−1,w],v_i+K[i−1,w−w_i]). Base K[0,w]=0. Store choices for reconstruction. O(nW) time and O(nW) space (O(W) value space if only the optimum value is needed).

**15.2-3. Weight/value orders agree oppositely.** Sort so w_1≤…≤w_n and v_1≥…≥v_n. Any chosen item j with an unchosen i<j can be replaced by i: weight does not increase and value does not decrease. Thus an optimum is a prefix. Choose the largest k with Σ_(i=1…k)w_i≤W. Any k+1 items weigh at least the first k+1, so no solution can use more than k items; among k-item sets the prefix has maximum value. O(n) after sorting.

**15.2-4. Water stops.** With two liters allowing m miles, from the current location choose the farthest refill station reachable within m miles; repeat, unless the destination itself is reachable. If no station is reachable before the destination, the route is infeasible. Exchange: the first stop of any feasible plan is no farther than the greedy stop, so replacing it with the greedy stop leaves at least as much remaining range for all later stops. O(n) after sorting locations.

**15.2-5. Unit intervals.** Sort points. Take the leftmost uncovered point x and place [x,x+1]; discard all points ≤x+1 and repeat. Any interval covering x can be shifted right to [x,x+1] without losing any point to its right, so the greedy choice is safe. O(n lg n) including sorting.

**15.2-6. Fractional knapsack in O(n).** Use deterministic linear-time selection to find a median density. Partition items into higher- and lower-density groups and sum the weight of the higher group. If it exceeds W, recurse only on that group. Otherwise take all higher-density items and recurse on the lower group with residual capacity, taking a fraction of the pivot-density group if the threshold falls there. Each iteration processes O(n) items and recurses on at most half, so T(n)=T(n/2)+O(n)=O(n).

**15.2-7. Maximize product.** The payoff is Π a_i^(b_i). Taking logarithms gives Σ b_i ln(a_i). Sort A and B in the same nondecreasing order and pair corresponding elements. For a_i≤a_j and b_i≤b_j, aligned pairing is at least crossed pairing because (b_j−b_i)(ln a_j−ln a_i)≥0. Repeatedly uncrossing proves optimality. O(n lg n) to sort; O(n) pairing after sorting.

## 15.3 Huffman codes

**15.3-1. Equal-frequency condition.** We have x.freq≤y.freq and a.freq≤b.freq, with x,y the two smallest and a,b sibling leaves of maximum depth. If x.freq=b.freq, then x≤y≤a≤b=x forces all four frequencies to be equal.

**15.3-2. Optimal trees are full.** If an internal node has only one child, contract that node and connect its child directly to the parent. Every leaf below it becomes one level shallower, strictly reducing cost because all frequencies are positive. Therefore a non-full tree cannot be optimal.

**15.3-3. Fibonacci frequencies.** For a:1,b:1,c:2,d:3,e:5,f:8,g:13,h:21, one Huffman code is a=1111110, b=1111111, c=111110, d=11110, e=1110, f=110, g=10, h=0. The tree is a chain of merges: the two 1-frequency leaves are deepest siblings, then c joins their parent, then d joins that subtree, and so on. For the first n Fibonacci frequencies, the two smallest symbols have code length n−1, the next has length n−2, …, and the largest has length 1 (left/right bit choices may vary).

**15.3-4. Sum of merge costs.** Each internal node contributes the sum of frequencies of all leaves in its subtree. A leaf c is counted once for each internal ancestor, exactly d_T(c) times. Thus Σ_internal freq(subtree)=Σ_c c.freq·d_T(c)=B(T).

**15.3-5. Encoding a code tree.** A full binary tree with n leaves has 2n−1 total nodes. Encode its shape with a preorder bit per node (1 for leaf, 0 for internal), using 2n−1 bits. Then store the character label at each leaf in traversal order, using n⌈lg n⌉ bits. Total 2n−1+n⌈lg n⌉ bits.

**15.3-6. Ternary Huffman.** For a full ternary tree, every internal node has three children. If n is not congruent to 1 modulo 2, add one zero-frequency dummy leaf so that the leaf count is 1 mod 2. Repeatedly extract the three least-frequency trees and merge them under a new parent with summed frequency. The exchange and contraction arguments from binary Huffman apply with three siblings; hence the code is optimal.

**15.3-7. Nearly equal frequencies.** Let every frequency lie in [m,2m). Initially all 256 leaves have weights in this range. Any pair merge has weight in [2m,4m), strictly larger than every unmerged leaf, so Huffman pairs all original leaves before merging any pair-node. The 128 pair weights lie in [2m,4m); their pairwise merges lie in [4m,8m), larger than all unmerged pair weights. Repeating, each level is perfectly paired before the next level is merged. The resulting tree is perfect with depth 8, so Huffman uses an 8-bit code and gives no improvement over fixed-length coding.

**15.3-8. No universal shorter lossless encoding.** There are 2^n binary files of length n, but only 1+2+…+2^(n−1)=2^n−1 binary strings shorter than n bits. An injective encoding of every n-bit file into a shorter string is impossible by the pigeonhole principle.

## 15.4 Offline caching

**15.4-1. Furthest-in-future manager.** On each request, report HIT if present. On a miss with free capacity, insert the requested block. On a full-cache miss, compute the next request index for every cached block (∞ if never used again), evict the block with the largest next-use index, and insert the requested block. A direct scan costs O(k) per miss, O(nk) overall.

**15.4-2. LRU is not optimal.** Let cache capacity be 2 and requests be A,B,C,A,B. LRU misses on all five requests: after C it evicts A, then misses A and evicts B, then misses B. Furthest-in-future evicts B when C arrives (B is needed after A), hits on A, and misses on B: four misses.

**15.4-3. Why y may change.** In the exchange proof, after the first differing eviction, a later request can cause the original solution to evict some common block w rather than the original x. The two caches then differ by y versus w, not necessarily y versus x. Requiring the same x throughout breaks the induction in property 1 at precisely this step.

**15.4-4. Multiple prefetches — source-model caveat.** Under the literal miss definition in §15.4 (a miss occurs only when the requested block is absent), free prefetching makes the claim false: with cache capacity 2 and requests A,B, a policy can load both A and B on the miss for A, then hit on B, for 1 miss. Any policy that loads at most one block per request, starting empty, must miss on both A and B, for 2 misses. The exercise's claim becomes true if every prefetched block transfer is charged as a miss/transfer; then deferring a prefetch until its first request does not increase transfer count. The section's stated demand-miss objective does not explicitly charge prefetches, so I am flagging this wording/assumption discrepancy rather than asserting an unsupported proof.

## Problems

**15-1. Coin changing.**
(a) For quarters, dimes, nickels, pennies, repeatedly take the largest coin not exceeding the remaining amount. Exchange argument: an optimal solution never uses 5 pennies (replace by nickel), 2 nickels (replace by dime), 3 dimes (replace by quarter plus nickel), or 2 dimes plus a nickel (replace by quarter). Thus the greedy representation is optimal.
(b) For denominations 1,c,c²,…,c^k, any c coins of value c^i can be replaced by one coin c^(i+1). Hence an optimum uses at most c−1 coins of each denomination below the largest; these are exactly the greedy digits.
(c) Denominations {1,3,4}, amount 6: greedy 4+1+1 uses 3 coins, while 3+3 uses 2.
(d) Let DP[0]=0 and DP[x]=1+min_{d≤x}(DP[x−d]) over denominations d. Store the minimizing coin. O(nk) time and O(n) space.

**15-2. Scheduling to minimize average completion time.**
(a) Sort tasks by nondecreasing processing time (shortest processing time first). For adjacent tasks i,j with p_i>p_j, swapping them reduces the sum of completion times by p_i−p_j. Repeatedly removing inversions yields an optimal SPT order. O(n lg n).
(b) With release times and preemption, use shortest remaining processing time (SRPT): at every time run the released unfinished task with least remaining processing time, preempting when a new task arrives with less remaining time. An exchange argument shows that any schedule that runs a longer-remaining task while a shorter-remaining released task waits can be locally improved by swapping a small time slice; repeated exchanges yield SRPT. A min-heap keyed by remaining time supports O(n lg n) event handling.
