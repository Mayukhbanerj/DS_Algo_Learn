# Chapter 3 — Exercises and Problems

Original worked study solutions based on CLRS Fourth Edition, Chapter 3. They are explanations and derivations, not an official solutions manual. The source's assumptions and notation are retained; where an exercise has multiple valid proofs, one clear proof is shown.

## Exercises 3.1 — O-notation, \(\Omega\)-notation, and \(\Theta\)-notation

### 3.1-1 — Lower bound when \(n\) is not a multiple of 3

Let \(m=\lfloor n/3\rfloor\). Put the \(m\) largest elements in the first \(m\) positions. Each of these elements must finish among the final \(m\) positions. Each must move at least \(n-2m+1\) positions to the right in total (the exact endpoint depends on ties/position assignment; the weaker bound of \(n-2m\) is sufficient). In insertion sort, each shift moves one element by one position. Thus the total number of shifts is at least
\[
m(n-2m)=\Omega(n^2),
\]
because \(m=\Theta(n)\) and \(n-2m=\Theta(n)\). Together with the \(O(n^2)\) upper bound, the worst case is \(\Theta(n^2)\). This argument does not require \(3\mid n\).

### 3.1-2 — Selection sort

Selection sort performs \(n-1\) outer iterations. On iteration \(i\), it scans the remaining \(n-i\) elements to find the minimum. The total number of comparisons is
\[
\sum_{i=1}^{n-1}(n-i)=\sum_{j=1}^{n-1}j
=\frac{n(n-1)}2.
\]
This count is independent of the input order. Therefore best-case, worst-case, and every fixed-size input's comparison count are \(\Theta(n^2)\). The algorithm uses \(\Theta(1)\) auxiliary storage.

### 3.1-3 — General fraction \(\alpha\)

Let \(0<\alpha<1\), and suppose the \(\alpha n\) largest values begin in the first \(\alpha n\) positions. They must end in the last \(\alpha n\) positions. The middle region has \((1-2\alpha)n\) positions. To force each selected value to pass through a positive-width middle region, require
\[
0<\alpha<\frac12.
\]
The resulting lower-bound count is proportional to
\[
(\alpha n)((1-2\alpha)n)
=\alpha(1-2\alpha)n^2.
\]
Maximize \(h(\alpha)=\alpha(1-2\alpha)=\alpha-2\alpha^2\). Then
\[
h'(\alpha)=1-4\alpha=0
\quad\Longrightarrow\quad \alpha=\frac14.
\]
Since \(h''(\alpha)=-4<0\), this is the maximum. The maximum coefficient is \(1/8\), giving a lower bound proportional to \(n^2/8\).

## Exercises 3.2 — Formal definitions

### 3.2-1 — Maximum and sum

Assume \(f,g\) are asymptotically nonnegative. For sufficiently large \(n\),
\[
\max(f(n),g(n))\le f(n)+g(n)\le2\max(f(n),g(n)).
\]
Choose \(c_1=1\) and \(c_2=2\), with \(n_0\) large enough that both functions are nonnegative. These inequalities establish
\[
\max(f(n),g(n))=\Theta(f(n)+g(n)).
\]

### 3.2-2 — Why “at least \(O(n^2)\)” is meaningless

\(O(n^2)\) denotes an asymptotic upper-bound set, not a numerical threshold. “At least” asks for a lower bound. The intended statement may be “at least \(\Omega(n^2)\)” or “at most \(O(n^2)\),” depending on the claim. If a tight bound is intended, write \(\Theta(n^2)\).

### 3.2-3 — Exponential comparisons

- \(2^{n+1}=2\cdot2^n\), so \(2^{n+1}=\Theta(2^n)\), and therefore \(O(2^n)\).
- \(2^{2n}=4^n\). Its ratio to \(2^n\) is \(2^n\), which is unbounded. Hence \(2^{2n}\notin O(2^n)\).

### 3.2-4 — Prove Theorem 3.1

We prove both directions.

**Forward direction:** Suppose \(f=\Theta(g)\). By definition, there are positive constants \(c_1,c_2,n_0\) such that
\[
0\le c_1g(n)\le f(n)\le c_2g(n)
\quad(n\ge n_0).
\]
The right inequality proves \(f=O(g)\); the left proves \(f=\Omega(g)\).

**Reverse direction:** Suppose \(f=O(g)\) and \(f=\Omega(g)\). The first relation supplies positive \(c_2,n_2\) such that \(f(n)\le c_2g(n)\) for \(n\ge n_2\). The second supplies positive \(c_1,n_1\) such that \(c_1g(n)\le f(n)\) for \(n\ge n_1\). Choose \(n_0=\max(n_1,n_2)\). Both inequalities then hold for every \(n\ge n_0\), which is exactly \(f=\Theta(g)\).

### 3.2-5 — All-input running time, worst case, and best case

For each input \(x\) of size \(n\), let \(T(x)\) be its running time. Define
\[
T_{\max}(n)=\max_{|x|=n}T(x),\qquad
T_{\min}(n)=\min_{|x|=n}T(x).
\]
If every input has \(T(x)=\Theta(g(n))\), then in particular both extrema are bounded above by \(O(g(n))\) and below by \(\Omega(g(n))\). Hence worst case is \(O(g)\) and best case is \(\Omega(g)\).

Conversely, if \(T_{\max}(n)=O(g(n))\) and \(T_{\min}(n)=\Omega(g(n))\), then every input satisfies
\[
T_{\min}(n)\le T(x)\le T_{\max}(n).
\]
For sufficiently large \(n\), this gives a common positive lower constant and a common positive upper constant, so every input has \(T(x)=\Theta(g(n))\). This equivalence assumes the same input-size domain and the usual finite set of inputs at each size.

### 3.2-6 — \(o(g)\cap\omega(g)\) is empty

Suppose for contradiction that \(f\) belongs to both sets. From \(f=o(g)\), choose \(c=1\): eventually \(f(n)<g(n)\). From \(f=\omega(g)\), also choose \(c=1\): eventually \(g(n)<f(n)\). For all sufficiently large \(n\), both strict inequalities would have to hold simultaneously, which is impossible. Therefore
\[
o(g)\cap\omega(g)=\varnothing.
\]

### 3.2-7 — Two-parameter lower and tight bounds

For asymptotically nonnegative \(f(n,m)\) and \(g(n,m)\), define
\[
\Omega(g(n,m))=
\left\{f:\exists c,n_0,m_0>0,\ 
0\le cg(n,m)\le f(n,m)
\text{ whenever }n\ge n_0\text{ or }m\ge m_0\right\}.
\]
Define
\[
\Theta(g(n,m))=O(g(n,m))\cap\Omega(g(n,m)).
\]
Equivalently, there must be positive \(c_1,c_2,n_0,m_0\) such that
\[
0\le c_1g(n,m)\le f(n,m)\le c_2g(n,m)
\]
under the same joint domain condition. The “or” condition matters: either parameter becoming sufficiently large must activate the bound.

## Exercises 3.3 — Standard notations and common functions

### 3.3-1 — Monotonicity

Suppose \(m\le n\), with \(f\) and \(g\) monotonically increasing.

- Sum: \(f(m)\le f(n)\) and \(g(m)\le g(n)\), so \(f(m)+g(m)\le f(n)+g(n)\).
- Composition: \(g(m)\le g(n)\); since \(f\) is increasing, \(f(g(m))\le f(g(n))\).
- Product, when both functions are also nonnegative: \(0\le f(m)\le f(n)\) and \(0\le g(m)\le g(n)\). Thus \(f(m)g(m)\le f(n)g(n)\).

Therefore all three stated functions are monotonically increasing under the specified assumptions.

### 3.3-2 — Floor/ceiling identity

For integer \(n\) and \(0\le\alpha\le1\), let \(x=\alpha n\). Since \(n-x=(1-\alpha)n\) and \(n\) is an integer,
\[
\lceil n-x\rceil=n-\lfloor x\rfloor.
\]
This follows from the general identity \(\lceil n-x\rceil=n-\lfloor x\rfloor\). Hence
\[
\lfloor\alpha n\rfloor+\lceil(1-\alpha)n\rceil
=\lfloor x\rfloor+n-\lfloor x\rfloor=n.
\]

### 3.3-3 — Perturbing \(n\) by \(o(n)\)

Let \(k\) be a fixed real constant and \(f(n)=n+o(n)\). Then \(f(n)/n\to1\), so \(f(n)=n(1+\epsilon(n))\), where \(\epsilon(n)\to0\). Therefore
\[
f(n)^k=n^k(1+\epsilon(n))^k.
\]
By continuity of \(x^k\) at \(x=1\), \((1+\epsilon(n))^k\to1\). Thus it is bounded above and below by positive constants for sufficiently large \(n\), proving
\[
(n+o(n))^k=\Theta(n^k).
\]
Since \(\lceil n\rceil=\lfloor n\rfloor=n\) for integer \(n\), the corresponding floor/ceiling expressions are also \(\Theta(n^k)\). More generally, if the argument is a real quantity tending to infinity, rounding changes it by less than one and does not change its \(\Theta\)-order.

### 3.3-4 — Four standard facts

**(a) Equation (3.21).** Change of base gives
\[
\log_b a=\frac{\ln a}{\ln b}.
\]
Thus \(a^{\log_b c}=e^{(\ln a)(\ln c)/(\ln b)}\), while \(c^{\log_b a}=e^{(\ln c)(\ln a)/(\ln b)}\). The exponents are equal, so the expressions are equal.

**(b) Factorial bounds.**
- \(n!=o(n^n)\): for example, Stirling gives \(n!\sim\sqrt{2\pi n}(n/e)^n\), whose ratio to \(n^n\) tends to zero.
- \(n!=\omega(2^n)\): Stirling implies \(n!\) grows on the order of \((n/e)^n\sqrt n\); its ratio to \(2^n\) tends to infinity.
- \(\lg(n!)=\Theta(n\lg n)\): upper bound \(n!\le n^n\) gives \(\lg(n!)\le n\lg n\). For the lower bound, at least \(n/2\) factors in \(n!\) are at least \(n/2\), so \(n!\ge(n/2)^{n/2}\). Taking logs gives \(\lg(n!)\ge(n/2)(\lg n-1)=\Omega(n\lg n)\).

**(c) \(\lg(\Theta(n))=\Theta(\lg n)\).** If \(f(n)=\Theta(n)\), then for positive constants \(c_1,c_2\), \(c_1n\le f(n)\le c_2n\) eventually. Taking logs:
\[
\lg n+\lg c_1\le\lg f(n)\le\lg n+\lg c_2.
\]
The additive constants do not change the asymptotic order, so \(\lg f(n)=\Theta(\lg n)\).

### 3.3-5 — Are the factorial functions polynomially bounded?

- \(\lceil\lg n\rceil!\) **is polynomially bounded**. Let \(k=\lceil\lg n\rceil\). Then \(k!\le k^k\), which is not by itself a polynomial bound in \(n\); a sharper argument is needed. By Stirling, \(\lg(k!)=\Theta(k\lg k)=\Theta(\lg n\cdot\lg\lg n)\), so \(k!=n^{\Theta(\lg\lg n)}\), which is superpolynomial. Therefore it is **not** polynomially bounded.
- \(\lceil\lg\lg n\rceil!\) **is polynomially bounded**. Let \(k=\lceil\lg\lg n\rceil\). Then \(\lg(k!)=O(k\lg k)=O(\lg\lg n\cdot\lg\lg\lg n)=o(\lg n)\). Hence \(k!=n^{o(1)}=O(n)\), so it is polynomially bounded.

### 3.3-6 — Compare \(\lg(\lg^* n)\) and \(\lg^*(\lg n)\)

For sufficiently large \(n\), \(\lg^*(\lg n)=\lg^*n-1\), because applying one logarithm first reduces the number of further logarithms needed by exactly one. Meanwhile \(\lg(\lg^*n)\) is the logarithm of the integer \(\lg^*n\). As \(n\to\infty\), \(\lg^*n\to\infty\), and \(\lg^*n-1\) grows faster than \(\lg(\lg^*n)\). Therefore
\[
\lg(\lg^*n)=o(\lg^*(\lg n)).
\]

### 3.3-7 — Golden ratio roots

The golden ratio \(\phi=(1+\sqrt5)/2\) satisfies
\[
\phi^2=\frac{(1+\sqrt5)^2}{4}
=\frac{6+2\sqrt5}{4}
=\frac{3+\sqrt5}{2}
=\frac{1+\sqrt5}{2}+1=\phi+1.
\]
For its conjugate \(\hat\phi=(1-\sqrt5)/2\), the same calculation gives \(\hat\phi^2=\hat\phi+1\). Thus both are roots of \(x^2=x+1\).

### 3.3-8 — Binet's formula by induction

Let
\[
G_i=\frac{\phi^i-\hat\phi^i}{\sqrt5}.
\]
Base cases: \(G_0=0=F_0\), and \(G_1=(\phi-\hat\phi)/\sqrt5=1=F_1\), since \(\phi-\hat\phi=\sqrt5\).

Inductive step: assume \(G_{i-1}=F_{i-1}\) and \(G_{i-2}=F_{i-2}\). Since both roots satisfy \(x^2=x+1\),
\[
\begin{aligned}
G_{i-1}+G_{i-2}
&=\frac{\phi^{i-1}(1+\phi)-\hat\phi^{i-1}(1+\hat\phi)}{\sqrt5}\\
&=\frac{\phi^{i+1}-\hat\phi^{i+1}}{\sqrt5}=G_i.
\end{aligned}
\]
The Fibonacci recurrence gives \(F_i=F_{i-1}+F_{i-2}=G_i\). Hence the formula holds for every \(i\ge0\).

### 3.3-9 — Invert \(k\lg k=\Theta(n)\)

Suppose \(k\lg k=\Theta(n)\). Then for constants \(c_1,c_2>0\),
\[
c_1n\le k\lg k\le c_2n
\]
for sufficiently large inputs. Since \(k\lg k\ge k\) once \(k\ge2\), the upper inequality implies \(k=O(n)\). This alone is too weak. To obtain the sharper relation, use the lower inequality together with \(k=O(n)\), which gives \(\lg k=O(\lg n)\), and therefore
\[
k\ge\frac{c_1n}{O(\lg n)}=\Omega(n/\lg n).
\]
For the reverse bound, if \(k\ge c n/\lg n\), then \(\lg k=\Theta(\lg n)\) for such \(k\), and the product has the required order. More directly, the two-sided relation forces \(\lg k=\Theta(\lg n)\), hence
\[
\boxed{k=\Theta(n/\lg n)}.
\]

## Problems for Chapter 3

### 3-1 — Asymptotic behavior of polynomials

Let \(p(n)=\sum_{i=0}^{d}a_i n^i\), where \(a_d>0\).

For sufficiently large \(n\), the leading term dominates the lower-degree terms. More formally, divide by \(n^d\):
\[
\frac{p(n)}{n^d}=a_d+\sum_{i=0}^{d-1}a_i n^{i-d}\longrightarrow a_d>0.
\]
Thus there are positive constants \(c_1,c_2,n_0\) such that
\(c_1n^d\le p(n)\le c_2n^d\) for \(n\ge n_0\), so \(p(n)=\Theta(n^d)\).

- **(a)** If \(k\ge d\), then \(n^d=O(n^k)\), so \(p(n)=O(n^k)\).
- **(b)** If \(k\le d\), then \(n^d=\Omega(n^k)\), so \(p(n)=\Omega(n^k)\).
- **(c)** If \(k=d\), both bounds hold, so \(p(n)=\Theta(n^k)\).
- **(d)** If \(k>d\), \(p(n)/n^k=\Theta(n^{d-k})\to0\), so \(p(n)=o(n^k)\).
- **(e)** If \(k<d\), \(p(n)/n^k=\Theta(n^{d-k})\to\infty\), so \(p(n)=\omega(n^k)\).

### 3-2 — Relative asymptotic growths

Use the definitions, not just visual inspection. Let \(k\ge1\), \(\alpha>0\), and \(c>1\).

| Pair | \(A\) compared with \(B\) | O | o | \(\Omega\) | \(\omega\) | \(\Theta\) |
|---|---|---:|---:|---:|---:|---:|
| (a) | \(\lg^k n\) vs. \(n^\alpha\) | Yes | Yes | No | No | No |
| (b) | \(n^k\) vs. \(c^n\) | Yes | Yes | No | No | No |
| (c) | \(\sqrt n\) vs. \(n^{\sin n}\) | No | No | No | No | No |
| (d) | \(2^n\) vs. \(2^{n/2}\) | No | No | Yes | Yes | No |
| (e) | \(n^{\lg c}\) vs. \(c^{\lg n}\) | Yes | No | Yes | No | Yes |
| (f) | \(\lg(n!)\) vs. \(\lg(n^n)\) | Yes | No | Yes | No | Yes |

Notes:
- In (a), every fixed polylogarithm is \(o(n^\alpha)\).
- In (b), every fixed polynomial is \(o(c^n)\).
- In (c), \(n^{\sin n}\) oscillates between subpolynomial and quadratic-scale values along subsequences, so it is not asymptotically comparable with \(\sqrt n\).
- In (d), the ratio is \(2^{n/2}\to\infty\).
- In (e), \(c^{\lg n}=n^{\lg c}\) exactly.
- In (f), \(\lg(n!)=\Theta(n\lg n)\), and \(\lg(n^n)=n\lg n\).

### 3-3 — Ordering by asymptotic growth rates

The 30 expressions in the source list, grouped from slowest to fastest, are:

1. \(\{1,\ n^{1/\lg n}\}\), since \(n^{1/\lg n}=2\).
2. \(\lg(\lg^* n)\).
3. \(\{\lg^* n,\ \lg^*(\lg n)\}\). These differ by at most one for sufficiently large \(n\), so they are \(\Theta\)-equivalent.
4. \(2^{\lg^* n}\).
5. \(\ln\ln n\).
6. \(\sqrt{\lg n}\).
7. \(\{\ln n,\ \lg n\}\).
8. \((\lg n)^2\).
9. \(2^{\sqrt{2\lg n}}\).
10. \(\sqrt n=(\sqrt2)^{\lg n}\).
11. \(\{n,\ 2^{\lg n}\}\).
12. \(\{n\lg n,\ \lg(n!)\}\).
13. \(\{n^2,\ 4^{\lg n}\}\).
14. \(n^3\).
15. \((\lg n)!\).
16. \(\{n^{\lg\lg n},\ (\lg n)^{\lg n}\}\), which are equal because \((\lg n)^{\lg n}=n^{\lg\lg n}\).
17. \(n!\).
18. \((n+1)!\).
19. \((3/2)^n\).
20. \(2^n\).
21. \(n\,2^n\).
22. \(e^n\).
23. \(2^{2^n}\).
24. \(2^{2^{n+1}}\).

**Why the key placements hold:**

- Every fixed polylogarithm is smaller than \(2^{\sqrt{2\lg n}}\), because taking logarithms reduces the comparison to \(\sqrt{\lg n}\) versus \(\lg\lg n\).
- \(2^{\sqrt{2\lg n}}=n^{o(1)}\), so it is smaller than every fixed positive power of \(n\).
- \((\lg n)!\) eventually exceeds every fixed polynomial in \(n\), but is \(o(n^{\lg\lg n})\), by Stirling's approximation.
- \(n^{\lg\lg n}\) is superpolynomial but smaller than \(n!\).
- Factorials eventually exceed every fixed-base exponential.
- \(n2^n=o(e^n)\), since \(n(2/e)^n\to0\).
- The final two double exponentials are ordered by their exponents.

**(b) Construct one function incomparable with all 30.** Enumerate the 30 source functions as \(g_1,\ldots,g_{30}\). Define \(f(n)\) by residue classes modulo 60. For \(i=1,\ldots,30\), set
\[
f(n)=g_i(n)/n\quad\text{when }n\equiv 2i-1\pmod{60},
\]
and
\[
f(n)=n\,g_i(n)\quad\text{when }n\equiv 2i\pmod{60}.
\]
(Define any positive value for the finitely many small inputs where a \(g_i\) is not defined.) For each fixed \(i\), there are infinitely many inputs in each of its two residue classes. Along the first class, \(f(n)/g_i(n)=1/n\to0\); along the second, \(f(n)/g_i(n)=n\to\infty\). Thus \(f\notin O(g_i)\) and \(f\notin\Omega(g_i)\) for every \(i\). This gives the required single nonnegative function.

### 3-4 — Asymptotic notation properties

Assume \(f,g\) are asymptotically positive.

- **(a) False.** Let \(f(n)=n\), \(g(n)=n^2\). Then \(f=O(g)\), but \(g\notin O(f)\).
- **(b) False.** Take \(f(n)=n\) and \(g(n)=n^2\). Then the sum is \(\Theta(n^2)\), while the minimum is \(n\), so the sum is not \(\Theta(\min(f,g))\).
- **(c) True under the stated positivity conditions.** If \(f=O(g)\), then eventually \(f\le cg\). Taking logs gives \(\lg f\le\lg c+\lg g\). Since \(\lg g\ge1\), the additive constant is absorbed, so \(\lg f=O(\lg g)\).
- **(d) False.** Let \(f(n)=2n\), \(g(n)=n\). Then \(f=O(g)\), but \(2^{f(n)}=4^n\notin O(2^n)\).
- **(e) False.** Asymptotically positive does not mean eventually at least 1. Let \(f(n)=1/n\). Then \(f(n)^2=1/n^2\), and \(f(n)/f(n)^2=n\to\infty\), so \(f\notin O(f^2)\`.
- **(f) True.** If \(f=O(g)\), transpose symmetry gives \(g=\Omega(f)\).
- **(g) False.** Let \(f(n)=2^n\). Then \(f(n)/f(n/2)=2^{n/2}\), which is unbounded, so \(f(n)\ne\Theta(f(n/2))\).
- **(h) True.** If \(h=o(f)\), then \(h/f\to0\), so \((f+h)/f=1+h/f\to1\). Therefore \(f+h=\Theta(f)\).

### 3-5 — Manipulating asymptotic notation

Assume \(f,g\) are asymptotically positive.

- **(a)** If \(h=\Theta(f)\), then \(\Theta(h)=\Theta(f)\), because each is bounded above and below by constant multiples of the other. Thus \(\Theta(\Theta(f))=\Theta(f)\).
- **(b)** A \(\Theta(f)\) term is already bounded above and below by constants times \(f\). Adding an \(O(f)\) term preserves both bounds, so the result is \(\Theta(f)\).
- **(c)** If \(u=\Theta(f)\) and \(v=\Theta(g)\), then \(u+v=\Theta(f+g)\) by adding the respective upper and lower inequalities.
- **(d)** If \(u=\Theta(f)\), \(v=\Theta(g)\), multiply the positive lower bounds and upper bounds to obtain \(uv=\Theta(fg)\).
- **(e)** Since \(a_1,a_2>0\) are constants and \(k_1,k_2\) are fixed, \((a_1n)^{k_1}=\Theta(n^{k_1})\) and \(\lg^{k_2}(b_1n)=\Theta(\lg^{k_2}n)\) for the stated domain. Multiplying gives \(\Theta(n^{k_1}\lg^{k_2}n)\).
- **(f)** For a finite or convergent sum of nonnegative terms, if each summand is bounded above and below by constant multiples of \(f(k)\), summing preserves those same constant-factor inequalities. Therefore the sum is \(\Theta(\sum_{k\in S}f(k))\), provided the common constants and convergence/domain assumptions are valid.
- **(g)** Let \(S_n=\{1,\ldots,n\}\) and \(f(k)=1/k\). For every \(k\), \(2f(k)=\Theta(f(k))\). But the finite products are
  \[
  \prod_{k=1}^{n}2f(k)=\frac{2^n}{n!},
  \qquad
  \prod_{k=1}^{n}f(k)=\frac1{n!}.
  \]
  Both products converge to zero as \(n\to\infty\), but their ratio is \(2^n\), which is unbounded. Hence the proposed product identity does not necessarily hold.

### 3-6 — Variations on \(O\) and \(\Omega\)

Let \(\Omega_\infty\) denote the alternative definition requiring \(f(n)\ge cg(n)\) for infinitely many integers \(n\).

- **(a)** If \(f=O(g)\), the first alternative holds. Otherwise, for every \(c>0\) and every threshold \(n_0\), some \(n\ge n_0\) violates \(f(n)\le cg(n)\), which means \(f(n)>cg(n)\) for infinitely many \(n\). Thus \(f=\Omega_\infty(g)\). Both can hold.
- **(b)** Define
  \[
  f(n)=\begin{cases}n,&n\text{ even},\\n^2,&n\text{ odd},\end{cases}
  \qquad
  g(n)=\begin{cases}n^2,&n\text{ even},\\n,&n\text{ odd}.\end{cases}
  \]
  Both functions are nonnegative. On even inputs, \(f(n)/g(n)=1/n\to0\), so no eventual positive lower bound \(f=\Omega(g)\) exists. On odd inputs, \(f(n)/g(n)=n\to\infty\), so no eventual upper bound \(f=O(g)\) exists.
- **(c)** Advantage: it gives a broad “infinitely often” lower-bound comparison even for oscillating functions. Disadvantage: it does not guarantee a lower bound for all sufficiently large inputs, so it is weaker for worst-case guarantees.
- **(d)** Replacing \(O\) with \(O'\), where absolute values are bounded, changes the forward direction of Theorem 3.1: \(\Theta(g)\Rightarrow O'(g)\) and \(\Omega(g)\) still hold for nonnegative \(f,g\), but \(O'(g)\) and \(\Omega(g)\) together need not imply \(\Theta(g)\) if \(f\) can be negative or oscillate. For asymptotically nonnegative \(f\), the original equivalence is recovered.
- **(e)** Define \(\widetilde O(g(n))\) by allowing a logarithmic factor: \(f(n)\le c g(n)(\lg n)^k\) eventually for constants \(c,k>0\). Define \(\widetilde\Omega\) by reversing the inequality, and \(\widetilde\Theta=\widetilde O\cap\widetilde\Omega\). The analogue of Theorem 3.1 follows immediately from the intersection definition.

### 3-7 — Iterated functions

For a monotone increasing function \(f\), \(f_c^*(n)\) counts the number of repeated applications needed to reach at most \(c\).

| Part | Function and threshold | Tight result | Reason |
|---|---|---|---|
| (a) | \(f(n)=n-1,\ c=0\) | \(\Theta(n)\) | One decrement per iteration |
| (b) | \(f(n)=\lg n,\ c=1\) | \(\lg^*n\) | This is the definition of log-star |
| (c) | \(f(n)=n/2,\ c=1\) | \(\Theta(\lg n)\) | After \(i\) steps, \(n/2^i\le1\) |
| (d) | \(f(n)=n/2,\ c=2\) | \(\Theta(\lg n)\) | Stop when \(n/2^i\le2\) |
| (e) | \(f(n)=\sqrt n,\ c=2\) | \(\Theta(\lg\lg n)\) | After \(i\) steps, exponent is \(1/2^i\); solve \(n^{1/2^i}\le2\) |
| (f) | \(f(n)=\sqrt n,\ c=1\) | Undefined for \(n>1\) | Repeated square roots approach 1 from above but never reach \(\le1\) in a finite number of steps |
| (g) | \(f(n)=n^{1/3},\ c=2\) | \(\Theta(\lg\lg n)\) | After \(i\) steps, exponent is \(1/3^i\); solve \(n^{1/3^i}\le2\) |

---

## Final chapter checklist

- [ ] State all five asymptotic definitions with the correct quantifiers.
- [ ] Distinguish a bound on the worst case from a bound on every input.
- [ ] Prove a \(\Theta\)-bound using both an upper and lower bound.
- [ ] Explain why some functions are asymptotically incomparable.
- [ ] Derive the polynomial, exponential, logarithmic, factorial, and Fibonacci growth facts.
- [ ] Complete the exact 30-function ranking in Problem 3-3 using the source's printed list.
- [ ] Recheck every proof and every table entry before marking the chapter complete.### 3-6 — Variations on \(O\) and \(\Omega\)

Let \(\Omega_\infty\) denote the alternative definition requiring \(f(n)\ge cg(n)\) for infinitely many integers \(n\).

- **(a)** If \(f=O(g)\), the first alternative holds. If not, then for every \(c>0\) and every threshold \(n_0\), the upper-bound inequality fails for some \(n\ge n_0\). Therefore \(f(n)>cg(n)\) for infinitely many \(n\), which is exactly \(f=\Omega_\infty(g)\). Both relations can hold.
- **(b)** Define, for positive integers \(n\),
  \[
  f(n)=\begin{cases}n,&n\text{ even},\\n^2,&n\text{ odd},\end{cases}
  \qquad
  g(n)=\begin{cases}n^2,&n\text{ even},\\n,&n\text{ odd}.\end{cases}
  \]
  Both are nonnegative. On even inputs \(f/g=1/n\to0\); on odd inputs \(f/g=n\to\infty\). Hence neither \(f=O(g)\) nor \(f=\Omega(g)\).
- **(c)** Advantage: \(\Omega_\infty\) gives a lower-bound comparison on infinitely many inputs, including some oscillating functions that fail an eventual lower bound. Disadvantage: it does not guarantee a lower bound for all sufficiently large inputs, so it is weaker as a worst-case guarantee.
- **(d)** Let \(O'\) mean \(|f(n)|=O(g(n))\). The forward direction of Theorem 3.1 remains true: \(f=\Theta(g)\) implies \(f=O'(g)\) and \(f=\Omega(g)\). The reverse direction also remains true under the theorem's asymptotic-positivity condition: if \(f=\Omega(g)\), then \(f\) is eventually positive, so \(|f|=f\) eventually; combining \(O'(g)\) with \(\Omega(g)\) therefore gives the usual \(\Theta(g)\). Without the positivity condition, the reverse implication can fail.
- **(e)** Define \(\widetilde O(g(n))\) by \(f(n)\le c\,g(n)(\lg n)^k\) eventually for positive constants \(c,k,n_0\). Define \(\widetilde\Omega(g(n))\) by requiring \(f(n)\ge c\,g(n)/(\lg n)^k\) eventually for positive constants \(c,k,n_0\), and define \(\widetilde\Theta=\widetilde O\cap\widetilde\Omega\). The analogue of Theorem 3.1 follows directly from this intersection definition.

### 3-7 — Iterated functions

For a monotone increasing function \(f\), \(f_c^*(n)\) counts the number of repeated applications needed to reach at most \(c\).

| Part | Function and threshold | Tight result | Reason |
|---|---|---|---|
| (a) | \(f(n)=n-1,\ c=0\) | \(\Theta(n)\) | One decrement per iteration |
| (b) | \(f(n)=\lg n,\ c=1\) | \(\lg^*n\) | This is the definition of log-star |
| (c) | \(f(n)=n/2,\ c=1\) | \(\Theta(\lg n)\) | After \(i\) steps, \(n/2^i\le1\) |
| (d) | \(f(n)=n/2,\ c=2\) | \(\Theta(\lg n)\) | Stop when \(n/2^i\le2\) |
| (e) | \(f(n)=\sqrt n,\ c=2\) | \(\Theta(\lg\lg n)\) | After \(i\) steps, exponent is \(1/2^i\); solve \(n^{1/2^i}\le2\) |
| (f) | \(f(n)=\sqrt n,\ c=1\) | Undefined for \(n>1\) | Repeated square roots approach 1 from above but never reach \(\le1\) in a finite number of steps |
| (g) | \(f(n)=n^{1/3},\ c=2\) | \(\Theta(\lg\lg n)\) | After \(i\) steps, exponent is \(1/3^i\); solve \(n^{1/3^i}\le2\) |

---

## Final chapter checklist

- [ ] State all five asymptotic definitions with the correct quantifiers.
- [ ] Distinguish a bound on the worst case from a bound on every input.
- [ ] Prove a \(\Theta\)-bound using both an upper and lower bound.
- [ ] Explain why some functions are asymptotically incomparable.
- [ ] Derive the polynomial, exponential, logarithmic, factorial, and Fibonacci growth facts.
- [ ] Complete the exact 30-function ranking in Problem 3-3 using the source's printed list.
- [ ] Recheck every proof and every table entry before marking the chapter complete.
