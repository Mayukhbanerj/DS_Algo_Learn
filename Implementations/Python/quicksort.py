"""Quicksort implementations for CLRS Chapter 7 (0-based indexing)."""

from __future__ import annotations

import random
from typing import MutableSequence, TypeVar

T = TypeVar("T")


def partition(a: MutableSequence[T], p: int, r: int) -> int:
    """Lomuto partition; pivot is a[r], low side uses <= pivot."""
    pivot = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quicksort(a: MutableSequence[T], p: int = 0, r: int | None = None) -> None:
    """Deterministic in-place quicksort; worst-case O(n^2) recursion depth."""
    if r is None:
        r = len(a) - 1
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


def randomized_partition(
    a: MutableSequence[T], p: int, r: int, rng: random.Random | None = None
) -> int:
    """Uniformly select a pivot, then use Lomuto partition."""
    rng = rng or random
    i = rng.randint(p, r)
    a[i], a[r] = a[r], a[i]
    return partition(a, p, r)


def randomized_quicksort(
    a: MutableSequence[T],
    p: int = 0,
    r: int | None = None,
    rng: random.Random | None = None,
) -> None:
    if r is None:
        r = len(a) - 1
    rng = rng or random
    if p < r:
        q = randomized_partition(a, p, r, rng)
        randomized_quicksort(a, p, q - 1, rng)
        randomized_quicksort(a, q + 1, r, rng)


def three_way_partition(a: MutableSequence[T], p: int, r: int) -> tuple[int, int]:
    """Return inclusive equal-key interval [lt, gt]."""
    pivot = a[r]
    lt, i, gt = p, p, r
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


def three_way_quicksort(a: MutableSequence[T], p: int = 0, r: int | None = None) -> None:
    if r is None:
        r = len(a) - 1
    if p < r:
        lt, gt = three_way_partition(a, p, r)
        three_way_quicksort(a, p, lt - 1)
        three_way_quicksort(a, gt + 1, r)


def hoare_partition(a: MutableSequence[T], p: int, r: int) -> int:
    """Hoare partition with first element as pivot; returns split boundary."""
    pivot = a[p]
    i, j = p - 1, r + 1
    while True:
        j -= 1
        while a[j] > pivot:
            j -= 1
        i += 1
        while a[i] < pivot:
            i += 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]


def hoare_quicksort(a: MutableSequence[T], p: int = 0, r: int | None = None) -> None:
    if r is None:
        r = len(a) - 1
    if p < r:
        q = hoare_partition(a, p, r)
        hoare_quicksort(a, p, q)
        hoare_quicksort(a, q + 1, r)


def bounded_stack_quicksort(
    a: MutableSequence[T], p: int = 0, r: int | None = None
) -> None:
    """Recurse on the smaller side and iterate over the larger side."""
    if r is None:
        r = len(a) - 1
    while p < r:
        q = partition(a, p, r)
        if q - p < r - q:
            bounded_stack_quicksort(a, p, q - 1)
            p = q + 1
        else:
            bounded_stack_quicksort(a, q + 1, r)
            r = q - 1


def fuzzy_sort(intervals: list[tuple[float, float]], rng=None) -> list[tuple[float, float]]:
    """Randomized fuzzy sort. Returns intervals in compatible left-to-right order."""
    rng = rng or random.Random()
    if len(intervals) <= 1:
        return intervals[:]
    pivot = intervals[rng.randrange(len(intervals))]
    lo, hi = pivot
    left, middle, right = [], [], []
    for interval in intervals:
        a, b = interval
        if b < lo:
            left.append(interval)
        elif a > hi:
            right.append(interval)
        else:
            lo = max(lo, a)
            hi = min(hi, b)
            middle.append(interval)
    # Reclassify against the final common intersection; initial overlaps may
    # cease to overlap as the intersection tightens.
    left, middle, right = [], [], []
    for interval in intervals:
        a, b = interval
        if b < lo:
            left.append(interval)
        elif a > hi:
            right.append(interval)
        else:
            middle.append(interval)
    return fuzzy_sort(left, rng) + middle + fuzzy_sort(right, rng)
