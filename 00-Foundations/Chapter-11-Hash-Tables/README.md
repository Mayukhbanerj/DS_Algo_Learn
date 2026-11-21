# Chapter 11 — Hash Tables

**Reference:** CLRS, Fourth Edition (2022), printed pages 273–311.

Hash tables implement dictionaries by mapping a key universe into a compact array. Direct addressing allocates one slot per possible key; hashing reduces space by mapping a large universe to m slots and resolving collisions.

## 11.1 Direct-address tables

For U={0,…,m−1}, T[k] points to the record with key k or is NIL. SEARCH returns T[k]; INSERT sets T[x.key]=x; DELETE sets T[x.key]=NIL. Each operation is Θ(1) worst case, but space is Θ(m), independent of the number n of stored records. The technique is useful only when the universe is small.

A bit vector represents a set with distinct keys and no satellite data: bit k is 1 iff k is present. Membership, insertion and deletion are Θ(1); space is m bits.

## 11.2 Hash tables

A hash function h:U→{0,…,m−1} maps keys to slots. Different keys can map to the same slot: a collision. The function is deterministic for a given key and selected function. A random-looking hash function can reduce collisions but cannot eliminate them when |U|>m.

### Independent uniform hashing
The ideal model chooses each key's slot independently and uniformly from m slots, then returns the same slot for repeated evaluations of that key. It is a theoretical abstraction, not directly implementable.

### Chaining
Each slot points to a linked list of all records hashing to that slot. INSERT prepends in Θ(1) worst case (assuming no duplicate key). SEARCH takes time proportional to the chain length. DELETE by node pointer is Θ(1) with doubly linked chains; singly linked deletion may need to find the predecessor. Exercise 11.2-4 shows a special circular-singly-linked representation that deletes in Θ(1) by copying the successor record into the supplied node and unlinking the successor; this changes physical record placement.

The load factor is α=n/m, the average chain length; α may exceed 1. Worst-case search is Θ(n), when all keys collide.

Under independent uniform hashing:
- Unsuccessful search examines an expected α elements, hence Θ(1+α) expected time.
- Successful search for a uniformly selected stored element, with head insertion, examines an expected 1+(n−1)/(2m) elements, hence Θ(1+α).

For successful search, let x_i be the i-th inserted element. A later-inserted x_i appears before x_j in their chain when i>j and they collide. Indicator variables for the searched element and each later insertion yield expected preceding elements (n−1)/(2m); linearity of expectation suffices.

If n=O(m), α=O(1), so searches are expected O(1). This is not a worst-case guarantee.

For Exercise 11.2-4, bucket chains can instead be circular singly linked lists. A bucket points to any node in the cycle. To delete node x, copy its successor's record into x and unlink that successor; handle a singleton by clearing the bucket. This preserves O(1) deletion with one element and one link per occupied slot, provided clients do not rely on stable physical node addresses.

## 11.3 Hash functions

A good hash function is efficient and distributes keys approximately uniformly and independently. A fixed function cannot guarantee this for arbitrary adversarial keys. Random hashing chooses a function at runtime independently of the data.

### Static hashing
Division: h(k)=k mod m. A prime m not close to a power of 2 may avoid common patterns, but no fixed m guarantees good behavior for all inputs.

Multiplication: h(k)=floor(m·frac(kA)), 0<A<1. For m=2^ℓ and w-bit keys, multiply-shift computes the low w bits of ka and extracts their ℓ most significant bits. A randomized odd multiplier is a useful variant, but a fixed multiplier alone has no universal guarantee.

### Universal hashing
A finite family H is universal if, for every distinct k1,k2, Pr[h(k1)=h(k2)]≤1/m when h is chosen uniformly from H. Probability is over the selected function, not an assumed input distribution. Universal hashing protects expected performance against adversarially chosen keys.

With chaining and n=O(m) insertions, any sequence of s INSERT, SEARCH and DELETE operations has expected total Θ(s), under the theorem's assumptions.

Related properties:
- Uniform: each key maps to each slot with probability 1/m.
- Universal: each distinct pair collides with probability at most 1/m.
- ε-universal: each distinct pair collides with probability at most ε.
- d-independent: any d distinct keys have jointly uniform hash values.

Independent uniform hashing is universal, but universality does not imply uniformity or higher-order independence.

### Number-theoretic universal family
Choose prime p larger than the key universe, and choose a uniformly random a∈Zp* and b∈Zp. Define h_ab(k)=((ak+b) mod p) mod m. For two distinct keys, their residues before the final modulo-m reduction are a uniformly distributed ordered pair of distinct residues. For each first residue, at most (p−1)/m other residues share its class modulo m. Collision probability is therefore at most 1/m.

A randomized multiply-shift family with odd multipliers is another practical option; CLRS gives it a 2/m collision bound.

### Long inputs
For a radix-128 string, process characters with a running remainder r←(128r+c) mod m. This computes the full integer's remainder without constructing the giant integer. Cryptographic hashes such as SHA-256 handle arbitrary byte strings and yield fixed-length outputs; salting creates a family. A cryptographic hash is not the same formal guarantee as a universal family.

## 11.4 Open addressing

Every record occupies the table itself. A key k has a probe sequence <h(k,0),…,h(k,m−1)> that must be a permutation of all m slots. The load factor α=n/m≤1.

INSERT probes until NIL. SEARCH follows the same sequence and may stop at NIL, since the key would have been inserted there if it were later in its probe sequence. Deletion cannot simply write NIL: that may break another key's probe path. A DELETED marker lets SEARCH continue through tombstones and lets INSERT reuse them, but tombstones affect search cost.

### Independent uniform permutation hashing
The ideal model chooses each key's probe sequence as an independent uniform permutation. For α<1 and no deletions, expected unsuccessful-search probes are at most 1/(1−α). Let X be the number of probes. Given j−1 occupied probes, the chance the next is occupied is (n−j+1)/(m−j+1)≤α. Thus Pr[X≥i]≤α^(i−1), and the tail-sum identity plus the geometric series gives E[X]≤1/(1−α).

Insertion has the same expected bound because it probes for the first empty slot. For a uniformly selected stored key, successful-search probes are bounded by (1/α) ln(1/(1−α)), by averaging the insertion-time bound over the n insertion positions and bounding the harmonic sum by an integral.

### Double hashing
h(k,i)=(h1(k)+i·h2(k)) mod m. The step h2(k) must be relatively prime to m to visit every slot. Sufficient designs: m prime with 1≤h2(k)<m, or m a power of 2 with h2(k) odd. If gcd(h2(k),m)=d>1, only m/d slots are visited.

### Linear probing
Linear probing is h(k,i)=(h1(k)+i) mod m. It creates primary clustering: occupied runs tend to grow. In the RAM model this increases probes; on hierarchical-memory machines sequential probes improve cache locality.

## 11.5 Practical considerations

The RAM model treats all probes as equal cost. Real machines have registers, caches and main memory with different latencies. A sequential scan within a cache block can outperform a few scattered memory accesses, so linear probing can be practical despite clustering.

### Deletion in linear probing
For a key at slot q, mark q empty and scan forward until the next empty slot. For a scanned key k' at q', move it into the current hole q exactly when g(k',q)<g(k',q'), where g(k,q)=(q−h1(k)) mod m. This means q occurred earlier in k'’s probe sequence than q'; leaving q empty would make k' unreachable. After moving k', the new hole is q'. This backward-shift deletion is specific to linear probing.

### 5-independent hashing and wee hashing
CLRS states that if h1 is 5-independent and α≤2/3, linear probing supports expected constant-time search, insertion and deletion.

The wee hash illustration defines f_a(k)=swap((2k²+ak) mod 2^w), where swap exchanges the two w/2-bit halves of a word and a is odd. Iterate r rounds. For short t-bit keys, the construction uses an odd parameter a+2^t and an offset b before reducing modulo m. For long inputs, split the bit string into w-bit words and repeatedly apply the round function to each word plus the current state. CLRS presents this as an illustrative cryptographically inspired family, not a security-reviewed replacement for a cryptographic hash.

## Engineering checklist
- Use direct addressing only for genuinely small universes.
- Choose collision resolution based on deletion needs, memory layout and load factor.
- Keep hashing deterministic for a fixed key and seed.
- Use a per-process random seed when adversarial keys are possible.
- Resize chained tables as α grows; resize open-addressed tables before α approaches 1.
- Test collisions, wraparound, full/empty states, duplicates, tombstones and deletion reachability.
- Expected O(1) is not worst-case O(1).
- For untrusted input, use a reviewed keyed hash rather than assuming modulo hashing is secure.
