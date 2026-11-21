"""Chapter 15 greedy algorithms."""
from __future__ import annotations
from bisect import bisect_right
import heapq
import itertools
from typing import Sequence

def activity_selection(activities: Sequence[tuple[float, float]]) -> list[int]:
    """Return original indices of a maximum compatible activity set."""
    order = sorted(range(len(activities)), key=lambda i: (activities[i][1], activities[i][0], i))
    chosen = []
    last_finish = float("-inf")
    for i in order:
        start, finish = activities[i]
        if start >= last_finish:
            chosen.append(i)
            last_finish = finish
    return chosen

def interval_partitioning(activities: Sequence[tuple[float, float]]):
    """Return (hall_count, hall_id_by_original_activity_index)."""
    order = sorted(range(len(activities)), key=lambda i: (activities[i][0], activities[i][1], i))
    halls = []  # (finish time, hall id)
    assignment = [None] * len(activities)
    count = 0
    for i in order:
        start, finish = activities[i]
        if halls and halls[0][0] <= start:
            _, hall = heapq.heappop(halls)
        else:
            hall = count
            count += 1
        assignment[i] = hall
        heapq.heappush(halls, (finish, hall))
    return count, assignment

def weighted_activity_selection(activities: Sequence[tuple[float, float, float]]):
    """Return (maximum value, selected original indices)."""
    order = sorted(range(len(activities)), key=lambda i: (activities[i][1], activities[i][0], i))
    starts = [activities[i][0] for i in order]
    finishes = [activities[i][1] for i in order]
    values = [activities[i][2] for i in order]
    pred = [bisect_right(finishes, starts[j], 0, j) - 1 for j in range(len(order))]
    dp = [0] * (len(order) + 1)
    take = [False] * len(order)
    for j in range(1, len(order) + 1):
        include = values[j - 1] + dp[pred[j - 1] + 1]
        exclude = dp[j - 1]
        if include > exclude:
            dp[j] = include
            take[j - 1] = True
        else:
            dp[j] = exclude
    chosen = []
    j = len(order) - 1
    while j >= 0:
        include = values[j] + dp[pred[j] + 1]
        if include > dp[j]:
            chosen.append(order[j])
            j = pred[j]
        else:
            j -= 1
    chosen.reverse()
    return dp[-1], chosen

def fractional_knapsack(items: Sequence[tuple[float, float]], capacity: float):
    """Items are (value, weight); return (value, [(index, fraction), ...])."""
    if capacity < 0 or any(weight <= 0 for _, weight in items):
        raise ValueError("capacity must be nonnegative and weights positive")
    order = sorted(range(len(items)), key=lambda i: items[i][0] / items[i][1], reverse=True)
    remaining = capacity
    total = 0.0
    selected = []
    for i in order:
        value, weight = items[i]
        if remaining <= 0:
            break
        fraction = min(1.0, remaining / weight)
        if fraction > 0:
            selected.append((i, fraction))
            total += fraction * value
            remaining -= fraction * weight
    return total, selected

def zero_one_knapsack(items: Sequence[tuple[int, int]], capacity: int):
    """Items are (value, integer weight); return (max value, chosen indices)."""
    if capacity < 0 or any(weight < 0 for _, weight in items):
        raise ValueError("capacity and weights must be nonnegative")
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i, (value, weight) in enumerate(items, 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weight <= w:
                dp[i][w] = max(dp[i][w], value + dp[i - 1][w - weight])
    chosen = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i - 1)
            w -= items[i - 1][1]
    chosen.reverse()
    return dp[n][capacity], chosen

def huffman_codes(frequencies: dict[str, float]):
    """Return (code_by_symbol, tree); tree leaves are strings, internals are pairs."""
    if not frequencies:
        return {}, None
    if any(freq < 0 for freq in frequencies.values()):
        raise ValueError("frequencies must be nonnegative")
    counter = itertools.count()
    heap = [(freq, next(counter), symbol) for symbol, freq in frequencies.items()]
    heapq.heapify(heap)
    if len(heap) == 1:
        symbol = heap[0][2]
        return {symbol: "0"}, symbol
    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, next(counter), (left, right)))
    tree = heap[0][2]
    codes = {}
    def walk(node, prefix):
        if isinstance(node, str):
            codes[node] = prefix
        else:
            walk(node[0], prefix + "0")
            walk(node[1], prefix + "1")
    walk(tree, "")
    return codes, tree

def huffman_cost(frequencies: dict[str, float], codes: dict[str, str]) -> float:
    return sum(frequencies[symbol] * len(code) for symbol, code in codes.items())

def farthest_in_future(requests: Sequence[str], capacity: int):
    """Return (miss_count, trace); direct O(nk) offline optimal cache simulation."""
    if capacity < 0:
        raise ValueError("capacity must be nonnegative")
    cache = set()
    misses = 0
    trace = []
    for i, block in enumerate(requests):
        if block in cache:
            trace.append(("hit", block, None))
            continue
        misses += 1
        evicted = None
        if capacity > 0:
            if len(cache) == capacity:
                next_use = {}
                for resident in cache:
                    try:
                        next_use[resident] = requests.index(resident, i + 1)
                    except ValueError:
                        next_use[resident] = float("inf")
                evicted = max(cache, key=lambda resident: next_use[resident])
                cache.remove(evicted)
            cache.add(block)
        trace.append(("miss", block, evicted))
    return misses, trace

def coin_change_greedy(amount: int, denominations: Sequence[int]) -> list[int]:
    if amount < 0 or any(d <= 0 for d in denominations):
        raise ValueError("amount must be nonnegative and denominations positive")
    result = []
    for coin in sorted(denominations, reverse=True):
        count, amount = divmod(amount, coin)
        result.extend([coin] * count)
    if amount:
        raise ValueError("amount cannot be represented")
    return result

def coin_change_dp(amount: int, denominations: Sequence[int]):
    if amount < 0 or any(d <= 0 for d in denominations):
        raise ValueError("amount must be nonnegative and denominations positive")
    best = [float("inf")] * (amount + 1)
    choice = [None] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in denominations:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
                choice[value] = coin
    if best[amount] == float("inf"):
        raise ValueError("amount cannot be represented")
    coins = []
    while amount:
        coin = choice[amount]
        coins.append(coin)
        amount -= coin
    return best[-1], coins

def shortest_processing_time(processing: Sequence[float]):
    """Return job order and average completion time (all jobs available, nonpreemptive)."""
    order = sorted(range(len(processing)), key=lambda i: (processing[i], i))
    elapsed = 0
    completion_sum = 0
    for i in order:
        elapsed += processing[i]
        completion_sum += elapsed
    return order, completion_sum / len(order) if order else 0.0

def srpt_schedule(jobs: Sequence[tuple[float, float]]):
    """Jobs are (release_time, processing_time); return completion times by input index."""
    order = sorted(range(len(jobs)), key=lambda i: (jobs[i][0], i))
    completion = [None] * len(jobs)
    heap = []
    time = 0.0
    pos = 0
    current = None
    while pos < len(order) or heap or current is not None:
        if current is None and not heap and pos < len(order):
            time = max(time, jobs[order[pos]][0])
        while pos < len(order) and jobs[order[pos]][0] <= time:
            idx = order[pos]
            heapq.heappush(heap, (jobs[idx][1], idx))
            pos += 1
        if current is None and heap:
            rem, idx = heapq.heappop(heap)
            current = [rem, idx]
        if current is None:
            continue
        next_release = jobs[order[pos]][0] if pos < len(order) else float("inf")
        run = min(current[0], next_release - time)
        if run == float("inf"):
            run = current[0]
        time += run
        current[0] -= run
        while pos < len(order) and jobs[order[pos]][0] <= time:
            idx = order[pos]
            heapq.heappush(heap, (jobs[idx][1], idx))
            pos += 1
        if current[0] <= 0:
            completion[current[1]] = time
            current = None
        elif heap and heap[0][0] < current[0]:
            heapq.heappush(heap, (current[0], current[1]))
            current = None
    return completion
