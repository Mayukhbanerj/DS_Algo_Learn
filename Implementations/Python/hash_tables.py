"""Chapter 11 educational hash-table implementations."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, Optional, TypeVar, Callable

K = TypeVar("K")
V = TypeVar("V")


class DirectAddressSet:
    def __init__(self, universe_size: int):
        if universe_size < 0:
            raise ValueError("universe_size must be nonnegative")
        self._bits = bytearray(universe_size)

    def _check(self, key: int) -> None:
        if not isinstance(key, int) or not 0 <= key < len(self._bits):
            raise KeyError(key)

    def search(self, key: int) -> bool:
        self._check(key)
        return bool(self._bits[key])

    def insert(self, key: int) -> None:
        self._check(key)
        self._bits[key] = 1

    def delete(self, key: int) -> None:
        self._check(key)
        self._bits[key] = 0


@dataclass
class _ChainNode(Generic[K, V]):
    key: K
    value: V
    prev: Optional["_ChainNode[K, V]"] = None
    next: Optional["_ChainNode[K, V]"] = None


class ChainedHashTable(Generic[K, V]):
    """Separate chaining with doubly linked buckets and a caller-supplied hash."""
    def __init__(self, capacity: int, hash_function: Callable[[K], int] = hash):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._buckets: list[Optional[_ChainNode[K, V]]] = [None] * capacity
        self._hash = hash_function
        self._size = 0

    def _slot(self, key: K) -> int:
        return self._hash(key) % len(self._buckets)

    def __len__(self) -> int:
        return self._size

    def search(self, key: K) -> Optional[V]:
        node = self._buckets[self._slot(key)]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def insert(self, key: K, value: V, *, replace: bool = True) -> None:
        slot = self._slot(key)
        node = self._buckets[slot]
        while node is not None:
            if node.key == key:
                if not replace:
                    raise KeyError(f"duplicate key: {key!r}")
                node.value = value
                return
            node = node.next
        head = self._buckets[slot]
        new_node = _ChainNode(key, value, None, head)
        if head is not None:
            head.prev = new_node
        self._buckets[slot] = new_node
        self._size += 1

    def delete(self, key: K) -> V:
        slot = self._slot(key)
        node = self._buckets[slot]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            raise KeyError(key)
        if node.prev is None:
            self._buckets[slot] = node.next
        else:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        self._size -= 1
        return node.value

    @property
    def load_factor(self) -> float:
        return self._size / len(self._buckets)

    def items(self) -> Iterator[tuple[K, V]]:
        for head in self._buckets:
            node = head
            while node is not None:
                yield node.key, node.value
                node = node.next


_DELETED = object()


class OpenAddressHashTable(Generic[K, V]):
    """Open addressing with linear or double hashing and tombstone deletion."""
    def __init__(
        self,
        capacity: int,
        hash1: Callable[[K], int] = hash,
        hash2: Optional[Callable[[K], int]] = None,
    ):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._table: list[object] = [None] * capacity
        self._hash1 = hash1
        self._hash2 = hash2
        self._size = 0
        self._deleted = 0

    def __len__(self) -> int:
        return self._size

    @property
    def load_factor(self) -> float:
        return self._size / len(self._table)

    def _step(self, key: K) -> int:
        m = len(self._table)
        if self._hash2 is None:
            return 1
        step = self._hash2(key) % m
        if step == 0:
            raise ValueError("double-hash step must be nonzero modulo capacity")
        # Reject incomplete probe cycles instead of silently missing slots.
        import math
        if math.gcd(step, m) != 1:
            raise ValueError("double-hash step must be relatively prime to capacity")
        return step

    def _probes(self, key: K):
        m = len(self._table)
        start = self._hash1(key) % m
        step = self._step(key)
        for i in range(m):
            yield (start + i * step) % m

    def search(self, key: K) -> Optional[V]:
        for q in self._probes(key):
            item = self._table[q]
            if item is None:
                return None
            if item is not _DELETED and item[0] == key:
                return item[1]
        return None

    def insert(self, key: K, value: V, *, replace: bool = True) -> int:
        first_deleted = None
        for q in self._probes(key):
            item = self._table[q]
            if item is None:
                target = first_deleted if first_deleted is not None else q
                if first_deleted is not None:
                    self._deleted -= 1
                self._table[target] = (key, value)
                self._size += 1
                return target
            if item is _DELETED:
                if first_deleted is None:
                    first_deleted = q
            elif item[0] == key:
                if not replace:
                    raise KeyError(f"duplicate key: {key!r}")
                self._table[q] = (key, value)
                return q
        if first_deleted is not None:
            self._table[first_deleted] = (key, value)
            self._deleted -= 1
            self._size += 1
            return first_deleted
        raise OverflowError("hash table is full")

    def delete(self, key: K) -> V:
        for q in self._probes(key):
            item = self._table[q]
            if item is None:
                break
            if item is not _DELETED and item[0] == key:
                self._table[q] = _DELETED
                self._size -= 1
                self._deleted += 1
                return item[1]
        raise KeyError(key)


def division_hash(key: int, capacity: int) -> int:
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    return key % capacity


def multiplication_hash(key: int, capacity: int, A: float = (5**0.5 - 1) / 2) -> int:
    if capacity <= 0 or not 0 < A < 1:
        raise ValueError("capacity must be positive and 0 < A < 1")
    return int(capacity * ((key * A) % 1.0))


def universal_hash(key: int, a: int, b: int, prime: int, capacity: int) -> int:
    if prime <= 1 or not 1 <= a < prime or not 0 <= b < prime:
        raise ValueError("require prime > 1, 1 <= a < prime, and 0 <= b < prime")
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    return ((a * key + b) % prime) % capacity


def linear_probing_delete(table: list[Optional[K]], q: int, hash1: Callable[[K], int]) -> None:
    """Delete slot q from a linear-probing table by backward-shifting keys.

    The table stores keys directly and uses None for an empty slot. This
    operation is not valid for arbitrary double-hashing probe sequences.
    """
    m = len(table)
    if not 0 <= q < m or table[q] is None:
        raise KeyError(q)
    table[q] = None
    hole = q
    scan = (q + 1) % m
    while table[scan] is not None:
        key = table[scan]
        if (hole - hash1(key)) % m < (scan - hash1(key)) % m:
            table[hole] = key
            table[scan] = None
            hole = scan
        scan = (scan + 1) % m
