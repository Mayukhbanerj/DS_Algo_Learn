"""Binary max-heap and heapsort (0-based Python indexing)."""

from __future__ import annotations


def parent(i: int) -> int:
    if i <= 0:
        raise ValueError("the root has no parent")
    return (i - 1) // 2


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def max_heapify(a: list[int], heap_size: int, i: int) -> None:
    """Restore the max-heap property below i; child subtrees must be heaps."""
    while True:
        largest = i
        l, r = left(i), right(i)
        if l < heap_size and a[l] > a[largest]:
            largest = l
        if r < heap_size and a[r] > a[largest]:
            largest = r
        if largest == i:
            return
        a[i], a[largest] = a[largest], a[i]
        i = largest


def build_max_heap(a: list[int]) -> int:
    """Build a max-heap in place and return its active size."""
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(a, n, i)
    return n


def heapsort(a: list[int]) -> None:
    """Sort a in ascending order in place, using O(1) auxiliary space."""
    heap_size = build_max_heap(a)
    for end in range(len(a) - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        heap_size -= 1
        max_heapify(a, heap_size, 0)


class MaxPriorityQueue:
    """Array-backed max-priority queue for comparable numeric keys."""

    def __init__(self, values=()):
        self._a = list(values)
        build_max_heap(self._a)

    def __len__(self):
        return len(self._a)

    def maximum(self):
        if not self._a:
            raise IndexError("heap underflow")
        return self._a[0]

    def extract_max(self):
        if not self._a:
            raise IndexError("heap underflow")
        result = self._a[0]
        last = self._a.pop()
        if self._a:
            self._a[0] = last
            max_heapify(self._a, len(self._a), 0)
        return result

    def insert(self, key):
        self._a.append(float("-inf"))
        self.increase_key(len(self._a) - 1, key)

    def increase_key(self, i: int, key) -> None:
        if key < self._a[i]:
            raise ValueError("new key is smaller than current key")
        self._a[i] = key
        while i > 0 and self._a[parent(i)] < self._a[i]:
            p = parent(i)
            self._a[i], self._a[p] = self._a[p], self._a[i]
            i = p

    def as_array(self):
        return self._a.copy()
