"""Order-statistic algorithms for CLRS Chapter 9."""

from __future__ import annotations

import random
from collections.abc import MutableSequence
from typing import TypeVar

T = TypeVar("T")


def min_max(values: list[T]) -> tuple[T, T]:
    """Return (minimum, maximum) using at most 3*floor(n/2) comparisons."""
    if not values:
        raise ValueError("min_max requires at least one value")
    n = len(values)
    if n % 2:
        minimum = maximum = values[0]
        start = 1
    else:
        if values[0] < values[1]:
            minimum, maximum = values[0], values[1]
        else:
            minimum, maximum = values[1], values[0]
        start = 2
    for i in range(start, n, 2):
        a, b = values[i], values[i + 1]
        if a < b:
            small, large = a, b
        else:
            small, large = b, a
        if small < minimum:
            minimum = small
        if large > maximum:
            maximum = large
    return minimum, maximum


def _partition3(a: MutableSequence[T], lo: int, hi: int, pivot: T) -> tuple[int, int]:
    """Partition a[lo:hi+1] into < pivot, == pivot, > pivot."""
    lt, i, gt = lo, lo, hi
    while i <= gt:
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    return lt, gt


def randomized_select(a: MutableSequence[T], i: int, rng: random.Random | None = None) -> T:
    """Return the 1-based ith smallest value; mutates a; expected O(n)."""
    if not 1 <= i <= len(a):
        raise ValueError("rank i must be in [1, len(a)]")
    generator = rng if rng is not None else random
    lo, hi = 0, len(a) - 1
    target = i - 1
    while lo <= hi:
        pivot = a[generator.randrange(lo, hi + 1)]
        lt, gt = _partition3(a, lo, hi, pivot)
        if target < lt:
            hi = lt - 1
        elif target > gt:
            lo = gt + 1
        else:
            return a[target]
    raise RuntimeError("unreachable selection state")


def _median_of_medians(values: list[T]) -> T:
    """Choose a deterministic pivot with the median-of-five guarantee."""
    if len(values) <= 5:
        return sorted(values)[(len(values) - 1) // 2]
    medians: list[T] = []
    for start in range(0, len(values), 5):
        group = sorted(values[start:start + 5])
        medians.append(group[(len(group) - 1) // 2])
    return _median_of_medians(medians)


def deterministic_select(a: MutableSequence[T], i: int) -> T:
    """Return the 1-based ith smallest value; mutates a; worst-case O(n).

    Uses groups of five and a three-way partition, so duplicate keys are safe.
    """
    if not 1 <= i <= len(a):
        raise ValueError("rank i must be in [1, len(a)]")
    lo, hi = 0, len(a) - 1
    target = i - 1
    while True:
        if lo == hi:
            return a[lo]
        pivot = _median_of_medians(list(a[lo:hi + 1]))
        lt, gt = _partition3(a, lo, hi, pivot)
        if target < lt:
            hi = lt - 1
        elif target > gt:
            lo = gt + 1
        else:
            return a[target]
