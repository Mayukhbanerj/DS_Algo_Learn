# Chapter 4 — Exercises and Problems

Original worked study solutions based on CLRS Fourth Edition, Chapter 4. These are explanations and derivations, not an official solutions manual. Assume algorithmic constant-time base cases unless stated otherwise.

## Exercises 4.1 — Multiplying square matrices

### 4.1-1 — Non-power-of-two dimensions

Pad each matrix with zero rows and columns to the next power-of-two dimension \(m=2^{\lceil\lg n\rceil}\). Since \(n\le m<2n\), recursive multiplication costs \(\Theta(m^3)=\Theta(n^3)\). Discard the extra rows and columns. The recurrence in padded dimension is \(T(m)=8T(m/2)+\Theta(1)=\Theta(m^3)\).

### 4.1-2 — Rectangular products

Partition into \(n\times n\) blocks.

- \(kn\times n\) multiplied by \(n\times kn\): the result has \(k^2\) blocks, each one \(n\times n\) product. Cost \(\Theta(k^2n^3)\).
- \(n\times kn\) multiplied by \(kn\times n\): the result is one \(n\times n\) block, the sum of \(k\) products. Cost \(\Theta(kn^3)\).

The second is asymptotically faster by a factor of \(k\).

### 4.1-3 — Copying submatrices

Copying input/output blocks adds \(\Theta(n^2)\) work per call:
\[
T(n)=8T(n/2)+\Theta(n^2)=\Theta(n^3).
\]
The leaves still dominate.

### 4.1-4 — Recursive matrix addition

Indented pseudocode:

    MATRIX-ADD-RECURSIVE(A, B, C, n)
        if n == 1: C[1,1] = A[1,1] + B[1,1]; return
        partition A, B, C into four n/2 by n/2 blocks
        recursively add corresponding 11, 12, 21, 22 blocks

With index calculations, \(T(n)=4T(n/2)+\Theta(1)=\Theta(n^2)\). If partitioning copies all entries, \(T(n)=4T(n/2)+\Theta(n^2)=\Theta(n^2\lg n)\).

## Exercises 4.2 — Strassen's algorithm

### 4.2-1 — Multiply the two \(2\times2\) matrices

\[
A=\begin{bmatrix}1&3\\7&5\end{bmatrix},\quad
B=\begin{bmatrix}6&8\\4&2\end{bmatrix}.
\]
The ten sums/differences are
\[
(S_1,\ldots,S_{10})=(6,4,12,-2,6,8,-2,6,-6,14).
\]
The seven products are
\[
(P_1,\ldots,P_7)=(6,8,72,-10,48,-12,-84).
\]
Combining:
\[
\begin{aligned}
C_{11}&=48-10-8-12=18,\\
C_{12}&=6+8=14,\\
C_{21}&=72-10=62,\\
C_{22}&=48+6-72+84=66.
\end{aligned}
\]
Thus \(AB=\begin{bmatrix}18&14\\62&66\end{bmatrix}\).

### 4.2-2 — Strassen pseudocode

    STRASSEN(A, B, C, n)
        if n == 1: C[1,1] += A[1,1] * B[1,1]; return
        partition A, B, C into 11, 12, 21, 22 blocks
        S1=B12-B22       S2=A11+A12
        S3=A21+A22       S4=B21-B11
        S5=A11+A22       S6=B11+B22
        S7=A12-A22       S8=B21+B22
        S9=A11-A21       S10=B11+B12
        P1=A11*S1        P2=S2*B22
        P3=S3*B11        P4=A22*S4
        P5=S5*S6         P6=S7*S8
        P7=S9*S10
        C11 += P5+P4-P2+P6
        C12 += P1+P2
        C21 += P3+P4
        C22 += P5+P1-P3-P7

There are seven recursive products and \(\Theta(n^2)\) nonrecursive work, so \(T(n)=7T(n/2)+\Theta(n^2)=\Theta(n^{\lg7})\).

### 4.2-3 — Largest number of \(3\times3\) multiplications

If a \(3\times3\) multiplication uses \(k\) multiplications, the recurrence is \(T(n)=kT(n/3)+\Theta(n^2)\), with exponent \(\log_3 k\). To beat Strassen require \(\log_3 k<\lg7\), or \(k<3^{\lg7}\approx21.8\). The largest integer is \(k=21\), giving \(\Theta(n^{\log_3 21})\approx\Theta(n^{2.771})\).

### 4.2-4 — Pan's algorithms

| Dimension | Multiplications | Exponent |
|---:|---:|---:|
| 68 | 132,464 | 2.7951285 |
| 70 | 143,640 | 2.7951227 |
| 72 | 155,424 | 2.7951474 |

The \(70\times70\) method has the smallest exponent, narrowly. All three beat Strassen's \(\lg7\approx2.807355\).

### 4.2-5 — Complex multiplication with three real multiplications

Compute \(p_1=ac\), \(p_2=bd\), \(p_3=(a+b)(c+d)\). Then real part \(=p_1-p_2\) and imaginary part \(=p_3-p_1-p_2\).

### 4.2-6 — Use matrix squaring to multiply two matrices

Square
\[
M=\begin{bmatrix}A&B\\0&0\end{bmatrix}.
\]
Then \(M^2=\begin{bmatrix}A^2&AB\\0&0\end{bmatrix}\). Extract \(AB\). Squaring a \(2n\times2n\) matrix costs \(\Theta((2n)^\alpha)=\Theta(n^\alpha)\).

## Exercises 4.3 — The substitution method

### 4.3-1 — Prove the specified bounds

- **(a)** \(T(n)=T(n-1)+n\): repeated substitution gives \(T(n)=T(n_0)+\sum_{i=n_0+1}^{n}i=O(n^2)\).
- **(b)** \(T(n)=T(n/2)+\Theta(1)\): \(\Theta(\lg n)\) levels each cost constant, so \(O(\lg n)\).
- **(c)** \(T(n)=2T(n/2)+n\): guess \(T(n)\le cn\lg n\). The step gives \(cn\lg(n/2)+n=cn\lg n-cn+n\le cn\lg n\) for \(c\ge1\). The recursion tree gives the matching lower bound, so \(\Theta(n\lg n)\).
- **(d)** \(T(n)=2T(n/2+17)+n\): let \(S(m)=T(m-34)\). The recursive argument becomes \(m/2\), and the driving term is \(\Theta(m)\), so \(S(m)=O(m\lg m)\), hence \(T(n)=O(n\lg n)\).
- **(e)** \(T(n)=2T(n/3)+\Theta(n)\): the driving term dominates \(n^{\log_3 2}\), and \(2(n/3)=(2/3)n\); case 3 gives \(\Theta(n)\).
- **(f)** \(T(n)=4T(n/2)+\Theta(n)\): watershed \(n^2\), so \(\Theta(n^2)\).

### 4.3-2 — Strengthen the induction for \(4T(n/2)+n\)

The guess \(T(n)\le cn^2\) gives \(cn^2+n\), which does not close. Use \(T(n)\le cn^2-dn\):
\[
4(c(n/2)^2-d(n/2))+n=cn^2-2dn+n\le cn^2-dn
\]
when \(d\ge1\). Choose constants to cover base cases. The recursion tree gives \(\Omega(n^2)\), so the solution is \(\Theta(n^2)\).

### 4.3-3 — Strengthen the induction for \(2T(n-1)+1\)

The guess \(c2^n\) gives \(c2^n+1\). Use \(T(n)\le c2^n-d\):
\[
2(c2^{n-1}-d)+1=c2^n-2d+1\le c2^n-d
\]
for \(d\ge1\). Choose constants for the base cases; \(T(n)=O(2^n)\).

## Exercises 4.4 — The recursion-tree method

### 4.4-1 — Guess and verify upper bounds

| Recurrence | Tight bound |
|---|---|
| (a) \(T(n)=T(n/2)+n^3\) | \(\Theta(n^3)\) |
| (b) \(T(n)=4T(n/3)+n\) | \(\Theta(n^{\log_3 4})\) |
| (c) \(T(n)=4T(n/2)+n\) | \(\Theta(n^2)\) |
| (d) \(T(n)=3T(n-1)+1\) | \(\Theta(3^n)\) |

### 4.4-2 — Lower bound for the number of leaves

For \(L(n)=L(n/3)+L(2n/3)\), inductively assume \(L(x)\ge cx\). Then \(L(n)\ge c(n/3)+c(2n/3)=cn\). Choose \(c\) for the base cases. Together with the chapter's \(O(n)\) upper bound, \(L(n)=\Theta(n)\).

### 4.4-3 — Lower bound for the unbalanced recurrence

For \(T(n)=T(n/3)+T(2n/3)+\Theta(n)\), at least \(\Theta(\lg n)\) top levels have all subproblems above the base threshold. At each such level, the subproblem sizes sum to \(n\), so the level costs \(\Theta(n)\). Hence \(T(n)=\Omega(n\lg n)\); the recursion-tree upper bound is \(O(n\lg n)\), giving \(\Theta(n\lg n)\).

### 4.4-4 — Split by a constant fraction

For \(T(n)=T(\alpha n)+T((1-\alpha)n)+\Theta(n)\), \(0<\alpha<1\), each level's subproblem sizes sum to \(n\). Both fractions are fixed below 1, so the height is \(\Theta(\lg n)\). Thus \(T(n)=\Theta(n\lg n)\).

## Exercises 4.5 — The master method

### 4.5-1

Here \(a=2,b=4\), so \(p=\log_4 2=1/2\).

- **(a)** \(f=1\): case 1, \(\Theta(\sqrt n)\).
- **(b)** \(f=\sqrt n\): case 2, \(k=0\), \(\Theta(\sqrt n\lg n)\).
- **(c)** \(f=\sqrt n\lg^2n\): case 2, \(k=2\), \(\Theta(\sqrt n\lg^3n)\).
- **(d)** \(f=n\): case 3, \(\Theta(n)\).
- **(e)** \(f=n^2\): case 3, \(\Theta(n^2)\).

### 4.5-2 — Caesar's matrix algorithm

\(T(n)=aT(n/4)+\Theta(n^2)\), exponent \(\log_4a\). To beat Strassen require \(\log_4a<\lg7\), so \(a<49\). Largest integer: \(\boxed{48}\).

### 4.5-3 — Binary search

For \(T(n)=T(n/2)+\Theta(1)\), \(a=1,b=2,p=0\). Case 2 with \(k=0\) gives \(\Theta(\lg n)\).

### 4.5-4 — Why regularity fails for \(f(n)=\lg n\)

\[
\frac{f(n/2)}{f(n)}=\frac{\lg n-1}{\lg n}\to1.
\]
No constant \(c<1\) bounds this ratio eventually. Also \(\lg n\notin\Omega(n^\epsilon)\) for every \(\epsilon>0\), so case 3's polynomial-separation condition fails.

### 4.5-5 — Step-function driving term

Let \(f(n)=2^{\lceil\lg n\rceil}\). Choose \(a=1,b=3/2\), so \(p=\log_{3/2}1=0\). Since \(n\le f(n)<2n\), \(f(n)=\Omega(n)\), satisfying case 3's growth condition with \(\epsilon=1\). For infinitely many intervals \((3/2)2^k<n<2^{k+1}\), both \(n\) and \(n/b\) lie in the same dyadic interval, so \(f(n/b)=f(n)\). Since \(a=1\), the ratio \(af(n/b)/f(n)=1\) along those inputs; no constant \(c<1\) can satisfy regularity.

## Exercises 4.6 — Continuous master theorem

### 4.6-1 — Lower bound on a sum

For \(k\ge0\),
\[
\sum_{j=0}^{\lfloor\lg_b n\rfloor}(\lg_b n-j)^k
=\Theta((\lg_b n)^{k+1}).
\]
The upper bound follows from \(\sum_{r=1}^{m+1}r^k=O(m^{k+1})\). For the lower bound, keep the first \(\lfloor m/2\rfloor\) terms, each at least \((m/2)^k\), where \(m=\lg_b n\).

### 4.6-2 — Regularity implies polynomial separation

If \(af(n/b)\le cf(n)\) with \(c<1\), iteration gives \(a^j f(n/b^j)\le c^j f(n)\). Choose \(j=\lfloor\lg_b(n/n_0)\rfloor\), so \(n/b^j\) lies in a fixed positive interval. Polynomial growth bounds that remaining factor below by a positive constant. Therefore
\[
f(n)=\Omega((a/c)^j)
=\Omega(n^{\log_b(a/c)})
=\Omega(n^{\log_ba+\epsilon}),
\quad \epsilon=\log_b(1/c)>0.
\]

### 4.6-3 — Driving function \(n^p/\lg n\)

Let \(p=\log_ba\). The internal-node sum is
\[
\Theta\!\left(n^p\sum_{j=0}^{\lfloor\lg_b n\rfloor}
\frac1{\lg(n/b^j)}\right)
=\Theta\!\left(n^p\sum_{r=1}^{\Theta(\lg n)}\frac1r\right)
=\Theta(n^p\lg\lg n).
\]
The leaf term is smaller, so \(T(n)=\Theta(n^p\lg\lg n)\).

## Exercises 4.7 — Akra–Bazzi recurrences

### 4.7-1 — Scaling the driving function

If \(T(n)=\sum_i a_iT(n/b_i)+f(n)\), define \(T'(n)=cT(n)\) and scale its base conditions by \(c>0\). Then \(T'(n)=cf(n)+\sum_i a_iT'(n/b_i)\). Thus multiplying the driving function by a positive constant does not change its asymptotic order.

### 4.7-2 — Polynomial growth examples

For \(f(n)=n^2\), \(f(\lambda n)/f(n)=\lambda^2\), bounded by a constant depending on fixed \(\lambda\). For \(f(n)=2^n\), the ratio is \(2^{(\lambda-1)n}\), unbounded for any fixed \(\lambda>1\); it fails.

### 4.7-3 — Eventual nonnegativity

Set \(\lambda=1\) in \(f(n)/d\le f(\lambda n)\le df(n)\). Then \(f(n)/d\le f(n)\), which rules out negative values for all sufficiently large \(n\). Thus \(f\) is eventually nonnegative (and positive if it is not eventually zero).

### 4.7-4 — Fixed-scale invariance without polynomial growth

Choose a non-linear additive function \(A:\mathbb R\to\mathbb R\), satisfying \(A(x+y)=A(x)+A(y)\) and unbounded on every interval (a Hamel-basis construction). Let \(f(n)=\exp(A(\ln n))\). For each fixed \(\lambda>0\),
\[
f(\lambda n)=\exp(A(\ln\lambda))f(n),
\]
so each fixed scaling changes \(f\) by a constant factor. But no single constant works uniformly for all \(\lambda\) in a nontrivial interval, so the polynomial-growth condition fails.

### 4.7-5 — Akra–Bazzi solutions

- **(a)** \(p=1\), since \(1/2+1/3+1/6=1\). The integral is \(\int_1^n(\lg u)/u\,du=\Theta(\lg^2n)\). Result: \(\Theta(n\lg^2n)\).
- **(b)** \(p\) solves \(3/3^p+8/4^p=1\), numerically \(p\approx1.85674<2\). The integral is \(\int_1^n u^{1-p}/\lg u\,du=\Theta(n^{2-p}/\lg n)\). Result: \(\Theta(n^2/\lg n)\).
- **(c)** \(p=0\), since \(2/3+1/3=1\). Integral \(\int_1^n(\lg u)/u\,du=\Theta(\lg^2n)\). Result: \(\Theta(\lg^2n)\).
- **(d)** \(p=-1\), since \((1/3)3^{-p}=1\). Integral \(\int_1^n du/u=\Theta(\lg n)\). Result: \(\Theta((\lg n)/n)\).
- **(e)** \(p=3\), since \(3(1/3)^3+3(2/3)^3=1\). The integral \(\int_1^n u^2/u^4\,du\) is bounded. Result: \(\Theta(n^3)\).

### 4.7-6 — Akra–Bazzi implies the continuous master theorem

For \(T(n)=aT(n/b)+f(n)\), the Akra–Bazzi exponent solves \(a/b^p=1\), so \(p=\log_ba\). Its integral formula is
\[
T(n)=\Theta\!\left(n^p\left(1+\int_1^n\frac{f(u)}{u^{p+1}}\,du\right)\right).
\]
If \(f=O(n^{p-\epsilon})\), the integral is bounded, giving \(\Theta(n^p)\). If \(f=\Theta(n^p\lg^kn)\), the integral is \(\Theta(\lg^{k+1}n)\), giving \(\Theta(n^p\lg^{k+1}n)\). If \(f=\Omega(n^{p+\epsilon})\) and regularity holds, the result is \(\Theta(f(n))\). These are the three continuous-master cases.

---

## Problems for Chapter 4

### 4-1 — Recurrence examples

| Part | Recurrence | Tight solution | Reason |
|---|---|---|---|
| (a) | \(2T(n/2)+n^3\) | \(\Theta(n^3)\) | Case 3 |
| (b) | \(T(8n/11)+n\) | \(\Theta(n)\) | Geometric sum |
| (c) | \(16T(n/4)+n^2\) | \(\Theta(n^2\lg n)\) | Case 2 |
| (d) | \(4T(n/2)+n^2\lg n\) | \(\Theta(n^2\lg^2n)\) | Case 2, \(k=1\) |
| (e) | \(8T(n/3)+n^2\) | \(\Theta(n^2)\) | Case 3; regularity ratio \(8/9\) |
| (f) | \(7T(n/2)+n^2\lg n\) | \(\Theta(n^{\lg7})\) | Case 1 |
| (g) | \(2T(n/4)+\sqrt n\) | \(\Theta(\sqrt n\lg n)\) | Case 2 |
| (h) | \(T(n-2)+n^2\) | \(\Theta(n^3)\) | Sum quadratic costs |

### 4-2 — Parameter-passing costs

Let \(N\) be the original array/matrix size and \(n\) the active subproblem size.

| Algorithm | Pointer | Copy full \(N\)-object | Copy active subrange |
|---|---|---|---|
| Binary search | \(T=T(n/2)+\Theta(1)=\Theta(\lg n)\) | \(T=T(n/2)+\Theta(N)=\Theta(N\lg n)\) | \(T=T(n/2)+\Theta(n)=\Theta(n)\) |
| Merge sort | \(T=2T(n/2)+\Theta(n)=\Theta(n\lg n)\) | \(T=2T(n/2)+\Theta(N+n)=\Theta(Nn)\) | \(T=2T(n/2)+\Theta(n)=\Theta(n\lg n)\) |
| Recursive matrix multiply | \(T=8T(n/2)+\Theta(1)=\Theta(n^3)\) | \(T=8T(n/2)+\Theta(N^2)=\Theta(N^2n^3)\) | \(T=8T(n/2)+\Theta(n^2)=\Theta(n^3)\) |

The full-copy strategy pays for copying the original object at every recursive call. Copying only the active subrange makes the per-level copy cost proportional to the amount of data actually being processed.

### 4-3 — Solving recurrences with a change of variables

For \(T(n)=2T(\sqrt n)+\Theta(\lg n)\), set \(m=\lg n\), \(S(m)=T(2^m)\). Then \(S(m)=2S(m/2)+\Theta(m)=\Theta(m\lg m)\), so \(T(n)=\Theta(\lg n\lg\lg n)\).

For **(e)** \(T(n)=2T(\sqrt n)+\Theta(1)\), the transformed recurrence is \(S(m)=2S(m/2)+\Theta(1)=\Theta(m)\), hence \(\Theta(\lg n)\).

For **(f)** \(T(n)=3T(\sqrt[3]n)+\Theta(n)\), \(S(m)=3S(m/3)+\Theta(2^m)\); the driving term dominates, so \(T(n)=\Theta(n)\).

### 4-4 — More recurrence examples

| Part | Recurrence | Tight solution |
|---|---|---|
| (a) | \(5T(n/3)+n\lg n\) | \(\Theta(n^{\log_3 5})\) |
| (b) | \(3T(n/3)+n/\lg n\) | \(\Theta(n\lg\lg n)\) |
| (c) | \(8T(n/2)+n^3\sqrt n\) | \(\Theta(n^{7/2})\) |
| (d) | \(2T(n/2-2)+n/2\) | \(\Theta(n\lg n)\) |
| (e) | \(2T(n/2)+n/\lg n\) | \(\Theta(n\lg\lg n)\) |
| (f) | \(T(n/2)+T(n/4)+T(n/8)+n\) | \(\Theta(n)\) |
| (g) | \(T(n-1)+1/n\) | \(\Theta(\lg n)\) |
| (h) | \(T(n-1)+\lg n\) | \(\Theta(n\lg n)\) |
| (i) | \(T(n-2)+1/\lg n\) | \(\Theta(n/\lg n)\) |
| (j) | \(\sqrt n\,T(\sqrt n)+n\) | \(\Theta(n\lg\lg n)\) |

For (f), \(p\) solves \(2^{-p}+4^{-p}+8^{-p}=1\), with \(p\approx0.87915<1\), so the \(n\) driving term dominates. For (j), divide by \(n\): \(U(n)=T(n)/n\) satisfies \(U(n)=U(\sqrt n)+1\), requiring \(\Theta(\lg\lg n)\) iterations.

### 4-5 — Fibonacci numbers and generating functions

Let \(F(z)=\sum_{i\ge0}F_i z^i\).

- **(a)** The Fibonacci recurrence and \(F_0=0,F_1=1\) give \(F(z)=z+zF(z)+z^2F(z)\).
- **(b)** Solve:
  \[
  F(z)=\frac{z}{1-z-z^2}
  =\frac{z}{(1-\phi z)(1-\hat\phi z)}
  =\frac1{\sqrt5}\left(\frac1{1-\phi z}-\frac1{1-\hat\phi z}\right).
  \]
- **(c)** Expand both geometric series to get \(F(z)=\frac1{\sqrt5}\sum_{i\ge0}(\phi^i-\hat\phi^i)z^i\).
- **(d)** Coefficient comparison gives Binet's formula. Since \(|\hat\phi|<1\), \(F_i\) is the nearest integer to \(\phi^i/\sqrt5\).
- **(e)** Prove \(F_{i+2}\ge\phi^i\) by induction. Base cases \(i=0,1\) hold. For the step, \(F_{i+2}=F_{i+1}+F_i\ge\phi^{i-1}+\phi^{i-2}=\phi^i\).

### 4-6 — Chip testing

**(a)** It is enough to show an ambiguous instance with \(n\) even and exactly \(n/2\) good chips. Pair each good chip with one bad chip. In each pair, the good chip truthfully reports that its partner is bad; the bad chip can report the same answer. The test therefore reports only “at least one is bad,” and does not reveal which chip is bad. The bad chips can coordinate this behavior across all pairs. The same observed outcomes are consistent with swapping which member of each pair is good, so no strategy can always identify the good set when at least half may be bad.

**(b)** Pair chips and test both directions. Keep one chip only when both report the other is good; otherwise discard both. A good-good pair contributes one good chip. A mixed pair cannot be retained because its good chip reports the other bad. A bad-bad pair may be retained if both lie, but contributes one bad chip. If there are \(x\) good-good pairs, \(y\) mixed pairs, and \(z\) bad-bad pairs, strict original majority gives \(2x+y>y+2z\), hence \(x>z\). The retained set still has a strict good majority and at most \(\lceil n/2\rceil\) chips.

**(c)** Repeat recursively. The number of tests satisfies \(Q(n)\le\lfloor n/2\rfloor+Q(\lceil n/2\rceil)=\Theta(n)\). The final chip is good because the reduced set retains a strict good majority.

**(d)** Test the known-good chip against each other chip. The good chip reports accurately, identifying all good chips in an additional \(\Theta(n)\) tests.

### 4-7 — Monge arrays

A matrix is Monge if \(A[i,j]+A[k,l]\le A[i,l]+A[k,j]\) for all \(i<k,j<l\).

- **(a)** The global inequality implies the adjacent one. Conversely, rearrange the adjacent inequality to \(A[i,j]-A[i,j+1]\le A[i+1,j]-A[i+1,j+1]\). Sum over adjacent columns and rows to obtain the global inequality.
- **(b)** The only violated adjacent inequality in the supplied array is \(23+7>22+6\) in the first two rows and columns 2–3. Change \(22\) to \(24\). All adjacent inequalities then hold, so the matrix is Monge.
- **(c)** Let \(p=f(i)\) and \(q=f(k)\) for \(i<k\). Suppose \(p>q\). Since \(p\) is the leftmost minimum in row \(i\), \(A[i,p]<A[i,q]\). Since \(q\) is a minimum in row \(k\), \(A[k,q]\le A[k,p]\). Therefore \(A[i,q]+A[k,p]>A[i,p]+A[k,q]\), contradicting the Monge inequality applied to columns \(q<p\). Hence \(f(i)\le f(k)\), and the leftmost-minimum indices are nondecreasing.
- **(d)** Find minima in even rows recursively. By part (c), the minimum of an odd row lies between the minima of its neighboring even rows. Scan only that interval. The intervals have total length \(O(n+m)\) because the endpoints move monotonically.
- **(e)** \(T(m,n)=T(\lceil m/2\rceil,n)+O(m+n)\). The \(m\)-terms sum geometrically to \(O(m)\); the \(n\)-term is paid over \(O(\lg m)\) levels. Thus \(T(m,n)=O(m+n\lg m)\).

## Final Chapter 4 checklist

- [ ] Derive the eight-product and seven-product recurrences.
- [ ] Reproduce Strassen's \(S_i,P_i\) equations.
- [ ] Prove recurrence bounds with explicit constants.
- [ ] Sum recursion-tree levels and leaves.
- [ ] State the master theorem cases and verify regularity.
- [ ] Derive the continuous-master sum.
- [ ] Apply Akra–Bazzi to unequal subproblem sizes.
- [ ] Work parameter-passing, Fibonacci, chip-testing, and Monge-array problems independently.
