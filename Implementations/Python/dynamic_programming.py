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

def lcs_memoized(x: Sequence, y: Sequence) -> int:
    """Top-down memoized LCS length in O(mn) time."""
    m, n = len(x), len(y)
    memo = [[None] * (n + 1) for _ in range(m + 1)]
    def solve(i, j):
        if i == 0 or j == 0:
            return 0
        if memo[i][j] is not None:
            return memo[i][j]
        if x[i - 1] == y[j - 1]:
            value = solve(i - 1, j - 1) + 1
        else:
            value = max(solve(i - 1, j), solve(i, j - 1))
        memo[i][j] = value
        return value
    return solve(m, n)

def lis_quadratic(values: Sequence):
    """Return one strictly increasing subsequence in O(n^2) time."""
    n = len(values)
    if n == 0:
        return []
    length = [1] * n
    previous = [None] * n
    for i in range(n):
        for j in range(i):
            if values[j] < values[i] and length[j] + 1 > length[i]:
                length[i] = length[j] + 1
                previous[i] = j
    end = max(range(n), key=length.__getitem__)
    out = []
    while end is not None:
        out.append(values[end])
        end = previous[end]
    return out[::-1]

def lis_nlogn(values: Sequence):
    """Return one strictly increasing subsequence in O(n log n) time."""
    from bisect import bisect_left
    tails = []
    tail_indices = []
    previous = [None] * len(values)
    for i, value in enumerate(values):
        pos = bisect_left(tails, value)
        if pos == len(tails):
            tails.append(value)
            tail_indices.append(i)
        else:
            tails[pos] = value
            tail_indices[pos] = i
        if pos > 0:
            previous[i] = tail_indices[pos - 1]
    if not tails:
        return []
    idx = tail_indices[-1]
    out = []
    while idx is not None:
        out.append(values[idx])
        idx = previous[idx]
    return out[::-1]

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

def edit_distance(x: Sequence, y: Sequence, costs: dict[str, float]):
    """Return minimum cost and an optimal sequence of copy/replace/delete/insert/twiddle/kill operations."""
    required = {"copy", "replace", "delete", "insert", "twiddle", "kill"}
    if not required.issubset(costs):
        raise ValueError("costs must define copy, replace, delete, insert, twiddle, and kill")
    m, n = len(x), len(y)
    dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
    parent = [[None] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + costs["delete"]
        parent[i][0] = (i - 1, 0, "delete")
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + costs["insert"]
        parent[0][j] = (0, j - 1, "insert")
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            candidates = []
            if x[i - 1] == y[j - 1]:
                candidates.append((dp[i - 1][j - 1] + costs["copy"], i - 1, j - 1, "copy"))
            else:
                candidates.append((dp[i - 1][j - 1] + costs["replace"], i - 1, j - 1, "replace"))
            candidates.append((dp[i - 1][j] + costs["delete"], i - 1, j, "delete"))
            candidates.append((dp[i][j - 1] + costs["insert"], i, j - 1, "insert"))
            if i >= 2 and j >= 2 and x[i - 2] == y[j - 1] and x[i - 1] == y[j - 2]:
                candidates.append((dp[i - 2][j - 2] + costs["twiddle"], i - 2, j - 2, "twiddle"))
            value, pi, pj, operation = min(candidates, key=lambda item: item[0])
            dp[i][j] = value
            parent[i][j] = (pi, pj, operation)
    # Kill is allowed only as the final operation, after all target characters exist.
    end_i = m
    best = dp[m][n]
    if dp[m][n] > min(dp[i][n] + costs["kill"] for i in range(m + 1)):
        best = min(dp[i][n] + costs["kill"] for i in range(m + 1))
        end_i = min(i for i in range(m + 1) if dp[i][n] + costs["kill"] == best)
    operations = []
    i, j = end_i, n
    while i or j:
        pi, pj, operation = parent[i][j]
        operations.append(operation)
        i, j = pi, pj
    operations.reverse()
    if end_i < m:
        operations.append("kill")
    return best, operations

def longest_palindromic_subsequence(text: Sequence):
    """Return one longest palindromic subsequence in O(n^2) time and space."""
    n = len(text)
    if n == 0:
        return []
    length = [[0] * n for _ in range(n)]
    choice = [[None] * n for _ in range(n)]
    for i in range(n):
        length[i][i] = 1
    for span in range(2, n + 1):
        for i in range(n - span + 1):
            j = i + span - 1
            if text[i] == text[j]:
                length[i][j] = 2 + (length[i + 1][j - 1] if span > 2 else 0)
                choice[i][j] = "both"
            elif length[i + 1][j] >= length[i][j - 1]:
                length[i][j] = length[i + 1][j]
                choice[i][j] = "left"
            else:
                length[i][j] = length[i][j - 1]
                choice[i][j] = "right"
    left, right = [], []
    i, j = 0, n - 1
    while i <= j:
        if i == j:
            left.append(text[i])
            break
        if choice[i][j] == "both":
            left.append(text[i]); right.append(text[j])
            i += 1; j -= 1
        elif choice[i][j] == "left":
            i += 1
        else:
            j -= 1
    return left + right[::-1]

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
