# Chapter 11 — Exercises and Problems

Original study solutions based on CLRS Fourth Edition. Indices are zero-based unless stated otherwise.

## 11.1 Direct-address tables

**11.1-1. Maximum.** Scan T from m−1 down to 0; return the first non-NIL slot. If none exists, return NIL. Worst-case Θ(m), O(1) extra space.

**11.1-2. Bit vector.** Maintain B[k]=1 iff k is present. SEARCH reads B[k]; INSERT sets it; DELETE clears it. All Θ(1), storage m bits.

**11.1-3. Duplicate keys.** Let each slot point to a doubly linked list of records with that key. Insert at head; search returns a matching record/list; delete by node pointer unlinks in Θ(1). If search must return every duplicate, output size imposes its own cost.

**11.1-4. Huge table without initialization.** Use T[0…m−1], a compact array A of stored keys, and count s. T[k] stores the index i of k in A; validate an uninitialized entry by checking A[T[k]]=k. INSERT appends k to A and sets T[k]=s. DELETE swaps A[s−1] into k's position, repairs that moved key's T entry, and decrements s. Only O(n) entries are touched; initialization Θ(1), operations Θ(1). A back-index/round-trip validation is essential because T initially contains garbage.

## 11.2 Hash tables

**11.2-1. Expected colliding pairs.** For each unordered key pair define an indicator equal to 1 if it collides. Its expectation is 1/m. By linearity, E[C]=binom(n,2)/m=n(n−1)/(2m).

**11.2-2. Chaining trace.** With m=9 and h(k)=k mod 9, insert 5,28,19,15,20,33,12,17,10. Remainders are 5,1,1,6,2,6,3,8,1. With head insertion the final chains are: slot 1: 10→19→28; slot 2: 20; slot 3: 12; slot 5: 5; slot 6: 33→15; slot 8: 17; all other slots empty.

**11.2-3. Sorted chains.** Search can stop once a key exceeds the target. Successful and unsuccessful expected search remain Θ(1+α) asymptotically under uniform hashing, though comparisons may improve. INSERT must find the sorted position, costing Θ(chain length); DELETE by node pointer remains Θ(1) in a doubly linked chain.

**11.2-4. Free list.** A singly linked free list suffices: allocate by popping its head and deallocate by pushing at its head, both Θ(1). The subtlety is the exercise's slot-layout restriction: bucket deletion is given an object pointer and must remain Θ(1), while a singly linked bucket list ordinarily cannot delete an arbitrary node in Θ(1). The implementation must therefore account explicitly for the predecessor/successor information without exceeding the stated per-slot storage. I am leaving the representation detail flagged for final audit rather than claiming that a simple singly linked bucket list satisfies the requirement.

**11.2-5. Large collision class.** There are m hash values. If every class had at most n−1 keys, |U|≤m(n−1). Thus |U|>m(n−1) implies some class contains at least n keys. Choosing n of them yields a chain with Θ(n) worst-case search.

**11.2-6. Uniform random stored key.** Let L be the longest chain. Repeatedly choose a slot uniformly and a position uniformly from 1…L; accept if that position exists in the chosen chain. Each stored key has equal acceptance probability 1/(mL), so conditional on acceptance it is uniform. Acceptance probability is n/(mL)=α/L; expected trials L/α, each O(1), giving O(L/α)=O(L(1+1/α)). Empty table is handled separately.

## 11.3 Hash functions

**11.3-1. Long-string list search.** Compute the query hash once. Compare stored hash values first; compare full strings only when hashes match. Hash equality is only a filter, not proof of string equality.

**11.3-2. Division for radix-128 string.** Maintain remainder r and process each character c by r←(128r+c) mod m. This is the full radix number modulo m and uses O(1) extra words.

**11.3-3. Permutation collision.** Since 2^p≡1 mod (2^p−1), each radix digit has the same positional weight modulo the modulus. The hash is the sum of digits modulo 2^p−1, invariant under character permutations. This is undesirable for anagram-sensitive dictionaries or compiler identifiers.

**11.3-4. Multiplication method.** For A=(√5−1)/2 and m=1000, h(k)=floor(1000·frac(kA)). Values for 61,62,63,64,65 are 700,318,936,554,172.

**11.3-5. Lower bound on ε.** Count ordered distinct key pairs across output buckets. For each h, each bucket containing s keys contributes s(s−1) colliding ordered pairs. Convexity makes this total at least |U|(|U|−1)(1/|Q|−1/|U|), so averaging over the |U|(|U|−1) ordered pairs gives ε≥1/|Q|−1/|U|.

**11.3-6. Polynomial family.** For distinct d-tuples x,y, P(b)=Σ(x_j−y_j)b^j is a nonzero polynomial over Z_p of degree at most d−1. It has at most d−1 roots. Uniform b therefore gives collision probability at most (d−1)/p.

## 11.4 Open addressing

**11.4-1. Insertions.** For keys 10,22,31,4,15,28,17,88,59 in m=11, linear probing yields slots [10,0,9,4,5,6,7,1,8], final table by slot 0…10: [22,88,NIL,NIL,4,15,28,17,59,31,10]. CLRS uses h1(k)=k (not k mod 11, which is equivalent in the first probe) and h2(k)=1+(k mod 10). Double hashing yields slots [10,0,9,4,5,6,3,7,2], final table [22,NIL,59,17,4,15,28,88,NIL,31,10].

**11.4-2. Tombstones.** DELETE writes DELETED. SEARCH continues past DELETED but stops at NIL. INSERT remembers the first DELETED, continues until NIL to rule out an existing duplicate, then inserts at the remembered tombstone; if no NIL remains, reuse the tombstone or report full.

**11.4-3. Bounds.** At α=3/4, unsuccessful/insertion bound is 4 and successful bound is (4/3)ln4≈1.848. At α=7/8, the bounds are 8 and (8/7)ln8≈2.376.

**11.4-4. Full table.** Averaging insertion-time bounds when n=m gives (1/m)Σ_{i=0}^{m−1}m/(m−i)=H_m.

**11.4-5. Double-hash cycle.** The least positive d satisfying d·h2(k)≡0 mod m is m/gcd(m,h2(k)). Thus the sequence visits m/gcd(m,h2(k)) distinct slots; gcd 1 is necessary and sufficient for all m slots.

**11.4-6. Equal bounds.** Solve 1/(1−α)=2·(1/α)ln(1/(1−α)), equivalently α=2(1−α)ln(1/(1−α)). The nonzero solution is approximately α=0.715. This equates the stated upper bounds, not necessarily exact expectations.

## 11.5 Practical considerations

**11.5-1. One-to-one f_a.** If f_a(x)=f_a(y), the half-word swap is invertible, so 2x²+ax≡2y²+ay (mod 2^w). Factor (x−y)(2(x+y)+a)≡0. Since a is odd, the second factor is odd and invertible modulo 2^w. Hence x≡y. Every iterate is therefore one-to-one.

**11.5-2. Random oracle.** A random oracle assigns independent uniform outputs to distinct inputs. For any five distinct inputs and any specified output 5-tuple, probability is m^−5; it is 5-independent.

**11.5-3. Bit propagation.** One round has the stated dependency from input bit k_i to ga output bits b_j only for j≥i. Swapping halves maps output position j to j−w/2 (for upper-half j) or j+w/2 (for lower-half j). A flip in the most significant input bit k_(w−1) can therefore affect only output bit w/2−1 after round 1. In round 2, that changed bit can affect all b_j with j≥w/2−1; after swapping, output bits 0,…,w/2−1 and w−1 may change. In particular bit 0 may now change. In round 3, a change in input bit 0 may affect every b_j, and hence every output bit after swapping. Thus the least r that permits a flip in any chosen input bit to affect any output bit is r=3.

## Problems

**11-1. Longest probe.** At insertion i, at most n≤m/2 slots are occupied. The probability the first p probes are all occupied is at most 2^−p. Setting p=2 lg n gives O(1/n²); a union bound over n insertions gives Pr[X>2 lg n]=O(1/n). Tail-sum splitting at 2 lg n gives E[X]=O(lg n).

**11-2. Static searchable set.** (a) Sort the keys in place and binary search: O(lg n) worst-case with no asymptotic extra storage. (b) Unsuccessful open-address search bound 1/(1−α) should be O(lg n), requiring m−n=Ω(n/lg n) extra slots.

**11-3. Maximum chain.** For a fixed slot, occupancy is Binomial(n,1/n), so Q_k=binom(n,k)(1/n)^k(1−1/n)^(n−k). Union bound gives Pr[M≥k]≤n·Pr[one slot occupancy≥k]. Using binom(n,k)≤n^k/k! and Stirling, Q_k≤(e/k)^k. For k≥k0 with k0=c lg n/lg lg n and sufficiently large c, this is at most n^−3. Also Q_(k+1)/Q_k=((n−k)/(k+1))·(1/(n−1))≤1/(k+1), so the binomial upper tail from k0 is at most a constant multiple of Q_k0. A union bound over n slots gives Pr[M≥k0]=O(n^−2). Since M≤n, E[M]≤k0+nPr[M≥k0]=O(lg n/lg lg n).

**11-4. Hashing and authentication.** (a) 2-independence gives each specified pair of outputs probability 1/m²; summing over m equal slots gives collision probability 1/m, hence universality. (b) The linear family without additive b is universal but not 2-independent: the all-zero tuple always maps to zero. (c) Adding random b makes any pair of distinct inputs map to any specified output pair with probability 1/p²: choose a coordinate i where x_i≠y_i; after fixing other a_j, the two equations uniquely determine a_i and b. Thus 2-independent. (d) A forged different message/tag pair is accepted only on a collision under the secret random function; probability at most 1/p, regardless of computation, under the stated one-tag setting. Adaptive multiple-message authentication requires additional analysis.
