"""Chapter 14 dynamic-programming algorithms (CLRS-style)."""
from __future__ import annotations
from typing import Sequence, Optional

def rod_cut(prices: Sequence[float], n: Optional[int] = None):
    """Return maximum revenue and first-cut choices; prices[i-1] prices length i."""
    if n is None:
        n = len(prices)
    if n < 0 or n > len(prices):
        raise ValueError("n must be between 0 and len(prices)")
    revenue = [0] * (n + 1)
    first = [0] * (n + 1)
    for length in range(1, n + 1):
        best = float("-inf")
        for piece in range(1, length + 1):
            value = prices[piece - 1] + revenue[length - piece]
            if value > best:
                best = value
                first[length] = piece
        revenue[length] = best
    return revenue[n], first

def rod_cut_memoized(prices: Sequence[float], n: Optional[int] = None):
    """Top-down memoized rod cutting; returns revenue and first-cut choices."""
    if n is None:
        n = len(prices)
    if n < 0 or n > len(prices):
        raise ValueError("n must be between 0 and len(prices)")
    revenue = [None] * (n + 1)
    first = [0] * (n + 1)
    revenue[0] = 0
    def solve(length):
        if revenue[length] is not None:
            return revenue[length]
        best = float("-inf")
        for piece in range(1, length + 1):
            value = prices[piece - 1] + solve(length - piece)
            if value > best:
                best, first[length] = value, piece
        revenue[length] = best
        return best
    return solve(n), first

def reconstruct_cuts(first: Sequence[int], n: int) -> list[int]:
    cuts = []
    while n > 0:
        piece = first[n]
        if piece <= 0 or piece > n:
            raise ValueError("invalid first-cut table")
        cuts.append(piece)
        n -= piece
    return cuts

def matrix_chain_order(dimensions: Sequence[int]):
    """Return minimum scalar cost and split table; dimensions has n+1 entries."""
    n = len(dimensions) - 1
    if n < 1 or any(d <= 0 for d in dimensions):
        raise ValueError("need at least one matrix and positive dimensions")
    m = [[0] * n for _ in range(n)]
    s = [[None] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            best = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if q < best:
                    best, s[i][j] = q, k
            m[i][j] = best
    return m[0][n - 1], s

def matrix_chain_memoized(dimensions: Sequence[int]):
    """Top-down memoized matrix-chain order; returns minimum cost and split table."""
    n = len(dimensions) - 1
    if n < 1 or any(d <= 0 for d in dimensions):
        raise ValueError("need at least one matrix and positive dimensions")
    memo = [[None] * n for _ in range(n)]
    split = [[None] * n for _ in range(n)]
    def solve(i, j):
        if i == j:
            return 0
        if memo[i][j] is not None:
            return memo[i][j]
        best = float("inf")
        for k in range(i, j):
            value = solve(i, k) + solve(k + 1, j) + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
            if value < best:
                best, split[i][j] = value, k
        memo[i][j] = best
        return best
    return solve(0, n - 1), split

def matrix_chain_parenthesization(s) -> str:
    n = len(s)
    def build(i, j):
        if i == j:
            return f"A{i + 1}"
        k = s[i][j]
        return "(" + build(i, k) + build(k + 1, j) + ")"
    return build(0, n - 1)

def lcs(x: Sequence, y: Sequence):
    """Return one LCS and the full length table."""
    m, n = len(x), len(y)
    c = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[None] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "diag"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "up"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "left"
    out = []
    i, j = m, n
    while i > 0 and j > 0:
        if b[i][j] == "diag":
            out.append(x[i - 1]); i -= 1; j -= 1
        elif b[i][j] == "up":
            i -= 1
        else:
            j -= 1
    out.reverse()
    return out, c

def lcs_length_linear_space(x: Sequence, y: Sequence) -> int:
    """LCS length using two rows and O(min(m,n)) auxiliary entries."""
    if len(y) > len(x):
        x, y = y, x
    previous = [0] * (len(y) + 1)
    for a in x:
        current = [0] * (len(y) + 1)
        for j, b in enumerate(y, 1):
            if a == b:
                current[j] = previous[j - 1] + 1
            else:
                current[j] = max(previous[j], current[j - 1])
        previous = current
    return previous[-1]

def optimal_bst(p: Sequence[float], q: Sequence[float]):
    """Return expected cost and root table; p has n entries, q has n+1."""
    n = len(p)
    if len(q) != n + 1:
        raise ValueError("q must contain n+1 dummy-key probabilities")
    if any(v < 0 for v in list(p) + list(q)):
        raise ValueError("probabilities must be nonnegative")
    e = [[0.0] * (n + 1) for _ in range(n + 2)]
    w = [[0.0] * (n + 1) for _ in range(n + 2)]
    root = [[None] * n for _ in range(n)]
    for i in range(n + 1):
        e[i][i] = q[i]
        w[i][i] = q[i]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]
            best = float("inf")
            for r in range(i, j):
                value = e[i][r] + e[r + 1][j] + w[i][j]
                if value < best:
                    best, root[i][j - 1] = value, r
            e[i][j] = best
    return e[0][n], root

def construct_optimal_bst(root):
    """Return a nested tuple; empty intervals are dummy leaves ('d', index)."""
    n = len(root)
    def build(i, j):
        if i > j:
            return ("d", i)
        r = root[i][j]
        return (r + 1, build(i, r - 1), build(r + 1, j))
    return build(0, n - 1)
