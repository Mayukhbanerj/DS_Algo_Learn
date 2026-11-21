# Chapter 16 — Amortized Analysis

**Reference:** CLRS Fourth Edition (2022), Sections 16.1–16.4, printed pages 449–470.

Amortized analysis bounds the total cost of every operation sequence in the worst case, then averages that bound over the operations. It is not average-case analysis and uses no probability distribution. An individual operation may be expensive while the sequence has low amortized cost.

## 16.1 Aggregate analysis

For every sequence of n operations, prove a total worst-case cost T(n). Assign each operation amortized cost T(n)/n.

**Stack with PUSH, POP, MULTIPOP.** MULTIPOP(S,k) removes min(s,k) objects from a stack of size s. Each object can be popped only after being pushed. Across n operations on an initially empty stack, there are at most n pushes and at most n successful pops. Total cost is O(n), so amortized cost is O(1).

**Binary counter.** For a k-bit counter starting at zero, bit i flips at most floor(n/2^i) times over n increments. Total flips are bounded by Σ(i=0…k−1) floor(n/2^i) < nΣ(i≥0)1/2^i=2n. A single increment can flip Θ(k) bits, but amortized cost is O(1).

## 16.2 The accounting method

Assign each operation an amortized charge ĉ_i. The invariant is that total credit never becomes negative for any prefix of any legal sequence: Σĉ_i ≥ Σc_i.

**Stack.** Charge PUSH 2, POP 0, MULTIPOP 0. One unit pays for PUSH; one is stored on the pushed object and pays for its eventual pop.

**Binary counter.** Charge 2 per increment. When a bit changes 0→1, one unit pays for the flip and one is stored on that bit. A later 1→0 flip consumes the stored credit.

**Dynamic-table expansion.** Charge 3 per insertion while doubling capacity when full: 1 pays for insertion, 1 is stored on the new item for its next move, and 1 on an old item. By the time the table fills, credits pay for copying.

## 16.3 The potential method

Let D_i be the state after operation i and Φ(D_i) its potential. Define ĉ_i=c_i+Φ(D_i)−Φ(D_(i−1)). Summing telescopes:
Σc_i=Σĉ_i−Φ(D_n)+Φ(D_0).
If Φ(D_i)≥Φ(D_0) for every i, total amortized cost upper-bounds total actual cost. Usually choose Φ(D_0)=0 and Φ≥0.

**Stack.** Φ(S)=number of objects. PUSH has actual cost 1 and ΔΦ=+1, amortized cost 2. POP and MULTIPOP have actual cost equal to objects removed and ΔΦ its negative, amortized cost 0.

**Binary counter.** Φ(A)=number of 1-bits. If an increment resets t trailing 1-bits and sets at most one 0-bit, actual cost ≤t+1 and ΔΦ≤1−t. Amortized cost ≤2.

**Dynamic table expansion.** For num items and size slots, Φ(T)=2(num−size/2). The table is at least half full, so Φ≥0. A nonexpanding insertion costs 1 and raises potential by 2; an expanding insertion costs i when i−1 items are copied and changes potential by 3−i. Both amortized costs are 3.

## 16.4 Dynamic tables: expansion and contraction

A dynamic table maintains contiguous storage, item count num, capacity size, and load factor α=num/size (empty table has α=1 by convention).

**Expansion only.** Double capacity when inserting into a full table. The load factor after expansion is 1/2 or more. Aggregate, accounting and potential analyses show O(1) amortized insertion, despite Θ(n) worst-case copying.

**Expansion and contraction.** Doubling when full and halving immediately below half-full causes oscillation: alternating insertions/deletions can repeatedly copy Θ(n) items. Use hysteresis: double at full, but halve only when deletion makes the table less than 1/4 full. After either resize, load factor returns to 1/2.

Use Φ(T)=2(num−size/2) when α≥1/2, and Φ(T)=size/2−num when α<1/2. Potential is nonnegative and zero immediately after resizing. Between resizes, operations change potential by at most 2; the resize-triggering operation releases enough potential to pay for copying. Amortized costs are constant, so n operations cost O(n). Load factor stays at least 1/4, bounding wasted space by a constant fraction.

## Engineering takeaways

- Worst-case per-operation and amortized costs are different guarantees.
- State the initial state and allowed operation sequences.
- For accounting, prove credit nonnegative for every prefix.
- For potentials, verify initial potential and a lower bound on every reachable state.
- Dynamic arrays need hysteresis to avoid resize thrashing.
- Amortized bounds do not eliminate latency spikes: a resize still causes a real pause.
