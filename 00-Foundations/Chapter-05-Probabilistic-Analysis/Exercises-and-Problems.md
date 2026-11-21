# Chapter 5 — Exercises and Problems

Original worked study solutions based on CLRS Fourth Edition, Chapter 5. These are explanations and derivations, not an official solutions manual. Probability assumptions are stated where they affect the answer.

## Exercises 5.1 — The hiring problem

### 5.1-1 — A total order on candidate ranks

If every pair of candidates can be compared and the better candidate can always be identified, the comparison relation is complete. Assuming the comparisons are consistent (transitive) and candidates have distinct ranks, they define a total order. Each candidate can therefore be assigned a unique rank from 1 through \(n\).

### 5.1-2 — Implement RANDOM(a,b) using only RANDOM(0,1)

Let \(m=b-a+1\). If \(m=1\), return \(a\). Otherwise let \(r=\lceil\lg m\rceil\). Generate \(r\) independent fair bits and interpret them as an integer \(x\in[0,2^r-1]\). If \(x<m\), return \(a+x\); otherwise repeat.

Each value in \([0,m-1]\) is equally likely conditional on acceptance, so the output is uniform. The acceptance probability is \(m/2^r>1/2\), so the expected number of trials is \(2^r/m<2\). Each trial uses \(r\) random bits; expected time is
\[
\Theta(\lg m)=\Theta(\lg(b-a+1)).
\]

### 5.1-3 — Remove bias from a biased coin

Call BIASED-RANDOM twice. If the results are \(01\), return 0; if they are \(10\), return 1; if they are \(00\) or \(11\), repeat.

The probability of \(01\) is \((1-p)p\), and the probability of \(10\) is \(p(1-p)\). Conditional on the two results differing, each outcome is therefore equally likely. A pair is accepted with probability \(2p(1-p)\). The expected number of pairs is \(1/[2p(1-p)]\), so the expected number of calls to BIASED-RANDOM is
\[
\boxed{\frac1{p(1-p)}}.
\]

## Exercises 5.2 — Indicator random variables

### 5.2-1 — Exactly one hire and exactly n hires

The first candidate is always hired. Exactly one hire occurs iff the first candidate is the best of all \(n\), probability \(1/n\). Exactly \(n\) hires occur iff the ranks arrive in strictly increasing order, which is one of \(n!\) equally likely permutations:
\[
\Pr(X=1)=1/n,\qquad \Pr(X=n)=1/n!.
\]

### 5.2-2 — Exactly two hires

Let \(j\) be the position of the globally best candidate. It must be the second record, so \(j\ge2\). Among the first \(j-1\) candidates, the first must be the best; otherwise an additional hire would occur. Choose the \(j-1\) candidates in \(\binom{n-1}{j-1}\) ways, put their maximum first, arrange the other \(j-2\) arbitrarily, put the global maximum at \(j\), and arrange the remaining \(n-j\) candidates arbitrarily. The count for this \(j\) is
\[
\binom{n-1}{j-1}(j-2)!(n-j)!=\frac{(n-1)!}{j-1}.
\]
Summing over \(j=2,\ldots,n\) gives \((n-1)!H_{n-1}\) permutations. Thus
\[
\boxed{\Pr(X=2)=\frac{H_{n-1}}n}.
\]

### 5.2-3 — Expected sum of n dice

Let \(D_i\) be the value of die \(i\). Each fair six-sided die has expectation
\[
E[D_i]=(1+2+3+4+5+6)/6=7/2.
\]
By linearity of expectation,
\[
E\left[\sum_{i=1}^nD_i\right]=\sum_{i=1}^nE[D_i]=\boxed{7n/2}.
\]

### 5.2-4 — Linearity without independence

- Two independent fair dice: each expectation is \(3.5\), so the sum has expectation \(7\).
- Roll the first die and set the second equal to it: the sum is twice the first die, so expectation \(2(3.5)=7\).
- Roll the first die and set the second to \(7\) minus the first: the sum is always \(7\).

All three expectations are 7. The last two pairs are dependent, demonstrating that linearity does not require independence.

### 5.2-5 — Hat-check problem

Let \(X_i=1\) if customer \(i\) receives their own hat, and 0 otherwise. A uniform random permutation returns customer \(i\)'s hat with probability \(1/n\). The number of correct returns is \(X=\sum_iX_i\). Therefore
\[
E[X]=\sum_{i=1}^nE[X_i]=n(1/n)=\boxed1.
\]

### 5.2-6 — Expected number of inversions

For each pair \(i<j\), let \(X_{ij}=1\) if \(A[i]>A[j]\). In a uniform random permutation of distinct values, either ordering is equally likely, so \(E[X_{ij}]=1/2\). There are \(\binom n2\) pairs. Hence
\[
E[\text{inversions}]
=\binom n2\frac12
=\boxed{\frac{n(n-1)}4}.
\]

## Exercises 5.3 — Randomized algorithms

### 5.3-1 — A nonempty-prefix loop invariant

First swap \(A[1]\) with \(A[\text{RANDOM}(1,n)]\), then for \(i=2,\ldots,n\), swap \(A[i]\) with \(A[\text{RANDOM}(i,n)]\).

Before the first loop iteration (\(i=2\)), \(A[1]\) is a uniformly random 1-permutation: every element has probability \(1/n\) of occupying it. The same induction as the standard RANDOMLY-PERMUTE proof shows that before iteration \(i\), every \((i-1)\)-permutation appears in the prefix with probability \((n-i+1)!/n!\). The final full permutation is uniform.

### 5.3-2 — PERMUTE-WITHOUT-IDENTITY

The procedure never leaves \(A[1]\) unchanged: it swaps position 1 with a position strictly greater than 1, and later iterations do not touch position 1. Thus it never outputs the identity. But it does not generate all nonidentity permutations. For \(n=3\), it has only \((n-1)!=2\) possible random-choice sequences, whereas there are \(3!-1=5\) nonidentity permutations. It therefore cannot be uniform over all nonidentity permutations.

### 5.3-3 — PERMUTE-WITH-ALL is not uniform

For \(n=3\), the algorithm makes \(3^3=27\) equally likely random choices. Enumerating the choices shows that the identity permutation occurs 4 times, while the cyclic permutation \(\langle2,3,1\rangle\) occurs 5 times. Their probabilities are \(4/27\) and \(5/27\), not the uniform value \(1/6\). Hence the algorithm is not uniform.

### 5.3-4 — PERMUTE-BY-CYCLE

A random offset creates a cyclic rotation of the input. Each element has probability \(1/n\) of landing in any fixed position, but only \(n\) cyclic rotations are possible, out of \(n!\) permutations. For \(n>2\), most permutations have probability zero, so the output is not uniform.

### 5.3-5 — RANDOM-SAMPLE

After iteration \(k\), the set \(S\) has size \(t=k-(n-m)\) and is a uniform \(t\)-subset of \(\{1,\ldots,k\}\). The claim holds initially for the empty set. Assume it holds before the next iteration.

For a target \((t+1)\)-subset \(R\subseteq\{1,\ldots,k\}\):
- If \(k\in R\), the previous set must be \(R\setminus\{k\}\). Any of its \(t\) elements, or \(k\) itself, selected by RANDOM(1,k) leads to the new set \(R\): \(t+1\) choices.
- If \(k\notin R\), the previous set must be \(R\setminus\{i\}\) for one of the \(t+1\) elements \(i\in R\), and the random choice must be that \(i\).

In either case, the probability is
\[
\frac{t+1}{k\binom{k-1}{t}}=\frac1{\binom{k}{t+1}}.
\]
Thus every \((t+1)\)-subset is equally likely. At termination \(t=m,k=n\), so the algorithm returns a uniform random \(m\)-subset using exactly \(m\) random-number calls.

## Exercises 5.4 — Probabilistic analysis and further uses

Assume 365 equally likely birthdays and independence unless otherwise stated.

### 5.4-1 — Match with your birthday; two July 4 birthdays

For \(k\) people including you, the probability nobody else shares your birthday is \((364/365)^{k-1}\). We need
\[
1-(364/365)^{k-1}\ge1/2.
\]
The smallest integer is \(\boxed{k=254}\).

The probability that at most one of \(k\) people has a July 4 birthday is
\[
(364/365)^k+\frac{k}{365}(364/365)^{k-1}.
\]
The smallest \(k\) for which the complementary probability is greater than \(1/2\) is \(\boxed{613}\).

### 5.4-2 — 99% birthday-match probability

The probability of no shared birthday is
\[
P_k=\prod_{i=0}^{k-1}\left(1-\frac{i}{365}\right).
\]
The smallest \(k\) for which \(1-P_k\ge0.99\) is \(k=57\). For 57 people, the expected number of matching pairs is
\[
\binom{57}{2}\frac1{365}=\frac{1596}{365}\approx\boxed{4.373}.
\]

### 5.4-3 — Expected tosses until a bin gets two balls

With \(b\) bins, the probability that the first \(j\) tosses all land in distinct bins is
\[
\frac{b(b-1)\cdots(b-j+1)}{b^j}.
\]
If \(T\) is the first toss on which a collision occurs, the tail-sum formula gives
\[
\boxed{E[T]=\sum_{j=0}^{b}\frac{b!}{(b-j)!\,b^j}}.
\]
For large \(b\), the birthday-paradox approximation gives \(E[T]\sim\sqrt{\pi b/2}\).

### 5.4-4 — Pairwise versus mutual independence

Pairwise independence is not sufficient for the birthday-paradox analysis. For a prime \(q\), choose independent uniform \(a,b\in\mathbb Z_q\), and define three birthdays
\[
X_1=a+b,\quad X_2=2a+b,\quad X_3=3a+b\pmod q.
\]
Every pair is independent and uniform because the corresponding two linear equations determine \(a,b\) uniquely. But if \(a=0\), all three birthdays match; if \(a\ne0\), the three values are distinct for \(q>2\). Thus the probability of a match is \(1/q\), unlike the mutually independent value \(3/q-2/q^2\). Pairwise independence does not determine the joint collision probability.

### 5.4-5 — Three people with the same birthday

Let \(X\) count triples of people who all share a birthday. Each particular triple matches with probability \(1/365^2\), so
\[
E[X]=\binom{k}{3}\frac1{365^2}.
\]
The indicator-based threshold \(E[X]\ge1\) first occurs at \(\boxed{k=94}\). This is an expected-count criterion for a likely triple, not an exact 50% probability threshold.

### 5.4-6 — Probability a k-string is a k-permutation

A length-\(k\) string over \(n\) symbols has \(n^k\) equally likely possibilities. The number with no repeated symbols is \(n!/(n-k)!\). Therefore
\[
\Pr(\text{k-string is a k-permutation})
=\frac{n!}{(n-k)!\,n^k}
=\prod_{i=0}^{k-1}\left(1-\frac{i}{n}\right).
\]
This is exactly the probability of no birthday collision among \(k\) people with \(n\) equally likely birthdays.

### 5.4-7 — Empty bins and singleton bins

Let \(I_i\) indicate that bin \(i\) is empty. Then \(E[I_i]=(1-1/n)^n\), so the expected number of empty bins is
\[
\boxed{n(1-1/n)^n\approx n/e}.
\]
Let \(J_i\) indicate that bin \(i\) contains exactly one ball. Then
\[
E[J_i]=n\frac1n(1-1/n)^{n-1}=(1-1/n)^{n-1}.
\]
The expected number of singleton bins is
\[
\boxed{n(1-1/n)^{n-1}\approx n/e}.
\]

### 5.4-8 — A long streak with high probability

Let \(k=\lfloor\lg n-2\lg\lg n\rfloor\), and partition the first \(n\) flips into \(m=\lfloor n/k\rfloor\) disjoint blocks of length \(k\). Each block is all heads with probability \(2^{-k}\). The events for disjoint blocks are independent, so
\[
\Pr(\text{no block is all heads})=(1-2^{-k})^m
\le e^{-m2^{-k}}.
\]
Since \(2^{-k}\) is on the order of \((\lg n)^2/n\) and \(m\) is on the order of \(n/\lg n\), the exponent \(m2^{-k}\) is at least \(\ln n\) for sufficiently large \(n\). Thus the failure probability is at most \(1/n\), and a streak of length at least \(\lg n-2\lg\lg n-O(1)\) occurs with probability at least \(1-1/n\).

## Problems for Chapter 5

### 5-1 — Probabilistic counting

The counter state \(i\) represents \(n_i\). Let \(\Delta_i=n_{i+1}-n_i\). On an increment, the represented value rises by \(\Delta_i\) with probability \(1/\Delta_i\), and otherwise stays unchanged. Conditional on the current state,
\[
E[\text{new represented value}\mid i]
=\frac1{\Delta_i}n_{i+1}
+\left(1-\frac1{\Delta_i}\right)n_i
=n_i+1.
\]
Taking expectations and applying induction, after \(n\) increments the expected represented count is exactly \(n\).

For \(n_i=100i\), each increment advances the counter by 100 with probability \(1/100\). Ignoring the stated negligible overflow probability, after \(n\) operations the represented count is \(100Y\), where \(Y\sim\operatorname{Binomial}(n,1/100)\). Hence
\[
\operatorname{Var}(100Y)
=100^2n(1/100)(99/100)
=\boxed{99n}.
\]

### 5-2 — Searching an unsorted array

**(a) Randomized search pseudocode**

    RANDOM-SEARCH(A, n, x)
        seen[1:n] = false
        count = 0
        while count < n:
            i = RANDOM(1, n)
            if not seen[i]:
                seen[i] = true
                count += 1
                if A[i] == x:
                    return i
        return NIL

**(b)** If exactly one position contains \(x\), each independent draw hits it with probability \(1/n\). The first hit time is geometric with expectation \(n\). The algorithm cannot exhaust all positions before hitting the target, so the expected number of draws is \(n\).

**(c)** If \(k\ge1\) positions contain \(x\), each draw hits one with probability \(k/n\). Expected draws to the first hit: \(\boxed{n/k}\).

**(d)** If \(k=0\), the algorithm must see every index. This is the coupon collector, with expected draws \(nH_n=\Theta(n\lg n)\).

**(e)** Deterministic linear search with one matching position uniformly located has average cost \((n+1)/2\), and worst-case cost \(n\).

**(f)** With \(k\ge1\) matching positions uniformly distributed, the expected first matching position is the minimum of a uniformly chosen \(k\)-subset:
\[
E[\text{checks}]=\frac{n+1}{k+1}.
\]
The worst case puts all \(k\) matches at the end, so the first match is at \(n-k+1\).

**(g)** If no position matches, deterministic search checks all \(n\) entries in both average and worst cases.

**(h)** SCRAMBLE-SEARCH first spends \(\Theta(n)\) time to permute, then performs linear search. Its worst-case time is \(\Theta(n)\) for every \(k\). Its expected time is also \(\Theta(n)\) overall because the shuffle alone costs \(\Theta(n)\); for \(k\ge1\), the expected scan after shuffling is \((n+1)/(k+1)\).

**(i)** Deterministic linear search is generally preferable: it has no randomization overhead, is \(\Theta(n)\) worst case, and for \(k\ge1\) its expected number of checks is \((n+1)/(k+1)\), slightly better than random search's \(n/k\). When \(k=0\), it avoids the coupon-collector overhead of random search. SCRAMBLE-SEARCH adds a full permutation cost without improving the asymptotic total.

---

## Final Chapter 5 checklist

- [ ] Distinguish input randomness from algorithmic randomness.
- [ ] Derive expected hiring cost with indicators.
- [ ] Prove uniformity of RANDOMLY-PERMUTE and RANDOM-SAMPLE.
- [ ] Use linearity of expectation without assuming independence.
- [ ] Solve birthday, balls-and-bins, streak, and online-hiring questions.
- [ ] Compare the three searching algorithms in Problem 5-2.
