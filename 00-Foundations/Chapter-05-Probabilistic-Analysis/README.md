# Chapter 5 — Probabilistic Analysis and Randomized Algorithms

**Reference:** CLRS, *Introduction to Algorithms*, Fourth Edition (2022), Chapter 5.  
**Scope:** The hiring problem, indicator random variables, randomized algorithms, random permutations, birthday paradox, balls and bins, streaks, and online hiring.

These are original study notes aligned to the source chapter, not a reproduction of the textbook.

## Learning objectives

- Distinguish worst-case analysis, average-case analysis, and expected running time.
- Model a random input as a probability distribution over possible inputs.
- Use indicator random variables and linearity of expectation, even when indicators are dependent.
- Analyze the hiring problem's worst-case and average-case costs.
- Explain how randomization moves control from the input to the algorithm.
- Prove that an in-place permutation algorithm produces a uniform random permutation.
- Apply indicator variables to birthday matches, occupancy, inversions, and other counting problems.
- Analyze the expected longest coin-flip streak and the online hiring strategy.

---

## 5.1 The hiring problem

An employment agency presents \(n\) candidates in sequence. Interview each candidate, and hire the candidate if they are better than the best candidate seen so far. Interviewing costs \(c_i\); hiring costs \(c_h\), with \(c_h\) much larger.

The algorithm always interviews all \(n\) candidates. If it hires \(m\) people, total cost is
\[
C(n)=c_i n+c_hm.
\]
The analysis therefore focuses on the number \(m\) of hires.

### Worst case

If candidates arrive in strictly increasing order of quality, every candidate is a new record and is hired. Thus \(m=n\), and total cost is \(\Theta(c_i n+c_hn)\), usually written \(O(c_hn)\) when hiring dominates.

### Probabilistic analysis

A probabilistic analysis makes an assumption about the input distribution. For the hiring problem, assume all \(n!\) possible rank permutations are equally likely. This is a **uniform random permutation**.

The algorithm's average-case cost is the expected cost over that input distribution. This is not the same as an expected running time of a randomized algorithm: in the latter, the algorithm itself makes random choices.

### Randomized algorithms

If the input distribution is unknown or adversarial, randomize the algorithm. A randomized algorithm's behavior depends on both the input and random-number-generator outcomes.

Assume \(\text{RANDOM}(a,b)\) returns an independent, uniformly random integer in \([a,b]\). Randomizing the candidate order before running HIRE-ASSISTANT makes the order uniform regardless of how the input list was originally arranged.

---

## 5.2 Indicator random variables

For an event \(A\), its indicator variable is
\[
I\{A\}=
\begin{cases}
1,&A\text{ occurs},\\
0,&A\text{ does not occur}.
\end{cases}
\]
Its expected value is exactly the event's probability:
\[
\boxed{E[I\{A\}]=\Pr(A)}.
\]

### Linearity of expectation

For random variables \(X_1,\ldots,X_n\),
\[
\boxed{E\left[\sum_{i=1}^{n}X_i\right]
=\sum_{i=1}^{n}E[X_i]}.
\]
This identity holds whether or not the variables are independent. Independence is needed for many product/variance rules, but not for linearity of expectation.

If \(X\) counts how many events \(A_i\) occur, write
\[
X=\sum_i I\{A_i\},
\quad\text{so}\quad
E[X]=\sum_i\Pr(A_i).
\]
This often avoids computing the full probability distribution of \(X\).

### Hiring problem with indicators

Let \(X_i=1\) if candidate \(i\) is hired and 0 otherwise. Then
\[
X=\sum_{i=1}^{n}X_i.
\]
In a uniform random permutation, candidate \(i\) is hired exactly when they are the best among the first \(i\) candidates. Each of those \(i\) candidates is equally likely to be the best, so
\[
\Pr(X_i=1)=E[X_i]=1/i.
\]
Therefore
\[
E[X]=\sum_{i=1}^{n}\frac1i=H_n=\ln n+O(1).
\]
The expected hiring cost is \(c_hH_n=\Theta(c_h\ln n)\), much smaller than the worst-case \(c_hn\).

### Key distinction

- Worst-case cost: maximum over inputs of a fixed size.
- Average-case cost: expectation over a specified input distribution.
- Expected cost of a randomized algorithm: expectation over its random choices, for a fixed input (or over both input and random choices if stated).

---

## 5.3 Randomized algorithms

### Randomized hiring

The procedure first uniformly permutes the candidate list and then runs HIRE-ASSISTANT. Its expected number of hires is \(H_n\), regardless of the original input order. The random permutation costs \(\Theta(n)\), so the full algorithm still runs in linear time if permutation is included; the expected expensive hiring cost is logarithmic.

### Uniform random permutation

A uniform random permutation assigns probability \(1/n!\) to every permutation.

The in-place procedure RANDOMLY-PERMUTE is:

    for i = 1 to n:
        swap A[i] with A[RANDOM(i, n)]

At iteration \(i\), the algorithm chooses the element for position \(i\) uniformly from the still-unfixed suffix \(A[i:n]\). After the iteration, position \(i\) is never changed again.

A loop-invariant proof tracks the probability of every possible prefix permutation:
- Before iteration \(i\), each possible \((i-1)\)-permutation occupies the first \(i-1\) positions with probability \((n-i+1)!/n!\).
- Conditional on such a prefix, the next required element is selected with probability \(1/(n-i+1)\).
- Thus each possible \(i\)-permutation has probability \((n-i)!/n!\).
- At termination \(i=n+1\), each full permutation has probability \(1/n!\).

Therefore RANDOMLY-PERMUTE produces a uniform random permutation in \(\Theta(n)\) time and \(O(1)\) extra space (beyond the array).

**Important:** It is not enough to show that every element has probability \(1/n\) of occupying every position. Those marginal probabilities do not guarantee that all \(n!\) permutations are equally likely.

### Pseudorandomness

A practical generator is usually deterministic but produces values that behave statistically like random values for the intended application. The mathematical analysis assumes independent uniform random choices; implementation quality and seed management are separate engineering concerns.

---

## 5.4 Probabilistic analysis and further uses of indicator variables

### Birthday paradox

Assume \(n\) possible birthdays, uniformly distributed and mutually independent. For \(k\) people, the probability that all birthdays are distinct is
\[
\Pr(B_k)=\prod_{i=0}^{k-1}\left(1-\frac{i}{n}\right).
\]
Hence
\[
\Pr(\text{at least one match})=1-\prod_{i=0}^{k-1}\left(1-\frac{i}{n}\right).
\]
Using \(1-x\le e^{-x}\),
\[
\Pr(B_k)\le e^{-k(k-1)/(2n)}.
\]
A match becomes likely when \(k=\Theta(\sqrt n)\), not \(\Theta(n)\). For (n=365), the exact product gives a 50% collision probability at 23 people.

An indicator-variable approximation counts matching pairs. For each pair \(i<j\), let \(X_{ij}=1\) if their birthdays match. Then \(E[X_{ij}]=1/n\), and the number of matching pairs is
\[
X=\sum_{i<j}X_{ij},\qquad
E[X]=\binom{k}{2}\frac1n.
\]
The expected number of matching pairs reaches 1 when \(k=\Theta(\sqrt n)\). This expectation is not itself the exact probability of a match, but it gives the same asymptotic threshold.

### Balls and bins

Throw \(n\) independent balls uniformly into \(b\) bins.

- Expected balls in a fixed bin: \(n/b\).
- Expected tosses until a fixed bin gets its first ball: \(b\).
- Expected tosses until every bin is nonempty (coupon collector):
  \[
  bH_b=b\ln b+O(b).
  \]

For the coupon collector, divide tosses into stages. Stage \(i\) ends when the \(i\)-th new bin is hit. When \(i-1\) bins are occupied, the next toss hits a new bin with probability \((b-i+1)/b\), so the expected stage length is \(b/(b-i+1)\). Summing gives \(bH_b\).

### Longest streak of heads

Flip a fair coin \(n\) times. A particular run of \(k\) consecutive positions is all heads with probability \(2^{-k}\). A union bound over at most \(n\) starting positions gives
\[
\Pr(\text{some run of length }k)\le n2^{-k}.
\]
Choosing \(k=2\lg n\) makes this probability at most \(1/n\), which yields an \(O(\lg n)\) upper bound on the longest streak.

For a lower bound, partition the flips into disjoint blocks of length about \(\frac12\lg n\). Each block is all heads with probability about \(n^{-1/2}\). There are \(\Theta(n/\lg n)\) independent blocks, so the probability that none is all heads becomes very small. Thus the expected longest streak is
\[
\boxed{\Theta(\lg n)}.
\]
Indicator variables for streaks of length \(k\) give an alternative expectation-based argument.

### Online hiring (secretary problem)

You must reject or hire each candidate immediately and hire exactly once. A strategy is:
1. Interview and reject the first \(k\) candidates, remembering their best score.
2. Hire the first later candidate whose score exceeds every score seen so far.
3. If no such candidate appears, hire the last candidate.

Let \(S\) be the event that the strategy hires the overall best candidate. If the best candidate is in position \(i>k\), success requires that the best among the first \(i-1\) candidates lie in the first \(k\) positions. This occurs with probability \(k/(i-1)\), while the overall best is in position \(i\) with probability \(1/n\). Therefore
\[
\Pr(S)=\frac{k}{n}\sum_{i=k+1}^{n}\frac1{i-1}
=\frac{k}{n}\sum_{j=k}^{n-1}\frac1j.
\]
Integral bounds approximate this by
\[
\Pr(S)\approx\frac{k}{n}\ln\frac nk.
\]
Maximizing \(x\ln(1/x)\) gives \(x=1/e\), so choose \(k\approx n/e\). The success probability is at least approximately \(1/e\) (and the source's lower-bound analysis establishes at least \(1/e\) with this choice).

---

## Engineering perspective

- An average-case claim is incomplete until the input distribution is stated.
- Randomizing an input can protect an algorithm from adversarial ordering, but adds permutation cost.
- Indicator variables turn counting problems into sums of event probabilities.
- Linearity of expectation does not require independence.
- Marginally uniform positions do not imply a uniform random permutation.
- Pseudorandom generators are engineering approximations to the independent-uniform model.
- Expected cost and worst-case guarantees answer different questions; do not substitute one for the other.

## Revision sheet

- \(E[I\{A\}]=\Pr(A)\).
- \(E[\sum X_i]=\sum E[X_i]\), even for dependent variables.
- Expected hires in random order: \(H_n=\ln n+O(1)\).
- RANDOMLY-PERMUTE yields every permutation with probability \(1/n!\).
- Birthday collision threshold: \(\Theta(\sqrt n)\).
- Coupon collector: \(bH_b=\Theta(b\lg b)\).
- Longest fair-coin head streak: \(\Theta(\lg n)\).
- Online hiring strategy: reject about \(n/e\), then accept the first record; success probability about \(1/e\).

## Chapter notes

The chapter notes point to advanced probability texts and randomized-algorithm surveys, including work by Fisher and Yates and Durstenfeld on random permutations. They also connect the hiring problem to the secretary problem and later online-selection research.

## Coverage audit

- [x] Section 5.1: hiring problem, worst case, probabilistic analysis, randomized algorithms
- [x] Section 5.2: indicators, linearity of expectation, hiring analysis
- [x] Section 5.3: randomized hiring, uniform permutations, loop-invariant proof
- [x] Section 5.4: birthday paradox, balls and bins, streaks, online hiring
- [x] Exercises 5.1-1 through 5.4-8 — companion file
- [x] Problems 5-1 and 5-2 — companion file

**Status:** Chapter 5 notes drafted; companion solutions and three-way audit remain before completion.
