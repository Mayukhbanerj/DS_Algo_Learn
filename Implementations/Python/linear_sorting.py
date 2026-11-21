"""Linear-time sorting methods from CLRS Chapter 8."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import TypeVar

T = TypeVar("T")


def counting_sort(values: Iterable[T], k: int, key: Callable[[T], int] = lambda x: x) -> list[T]:
    """Stable counting sort for records whose integer keys lie in [0, k]."""
    items = list(values)
    if k < 0:
        raise ValueError("k must be nonnegative")
    counts = [0] * (k + 1)
    for item in items:
        value = key(item)
        if not isinstance(value, int) or not 0 <= value <= k:
            raise ValueError("key outside [0, k]")
        counts[value] += 1
    for i in range(1, k + 1):
        counts[i] += counts[i - 1]
    output: list[T | None] = [None] * len(items)
    for item in reversed(items):
        value = key(item)
        counts[value] -= 1
        output[counts[value]] = item
    return output  # type: ignore[return-value]


def counting_sort_in_place(values: list[int], k: int) -> None:
    """In-place key-only counting sort; not stable for records."""
    if k < 0 or any(not isinstance(x, int) or x < 0 or x > k for x in values):
        raise ValueError("values must be integers in [0, k]")
    counts = [0] * (k + 1)
    for x in values:
        counts[x] += 1
    pos = 0
    for value, count in enumerate(counts):
        for _ in range(count):
            values[pos] = value
            pos += 1


def radix_sort(values: Iterable[int], base: int = 10) -> list[int]:
    """Stable LSD radix sort for nonnegative integers."""
    items = list(values)
    if base < 2:
        raise ValueError("base must be at least 2")
    if any(not isinstance(x, int) or x < 0 for x in items):
        raise ValueError("radix_sort accepts nonnegative integers")
    if not items:
        return items
    exp = 1
    maximum = max(items)
    while maximum // exp > 0:
        counts = [0] * base
        for x in items:
            counts[(x // exp) % base] += 1
        for i in range(1, base):
            counts[i] += counts[i - 1]
        output = [0] * len(items)
        for x in reversed(items):
            digit = (x // exp) % base
            counts[digit] -= 1
            output[counts[digit]] = x
        items = output
        exp *= base
    return items


def bucket_sort(values: Iterable[float]) -> list[float]:
    """Bucket sort for values in [0, 1), using insertion sort per bucket."""
    items = list(values)
    n = len(items)
    if any(not 0.0 <= x < 1.0 for x in items):
        raise ValueError("bucket_sort values must lie in [0, 1)")
    buckets: list[list[float]] = [[] for _ in range(n)]
    for x in items:
        index = min(n - 1, int(n * x))
        buckets[index].append(x)
    result: list[float] = []
    for bucket in buckets:
        for i in range(1, len(bucket)):
            value = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > value:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = value
        result.extend(bucket)
    return result
