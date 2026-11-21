"""Chapter 10 reference implementations.

Python uses 0-based indexing. These implementations make the invariants explicit;
they are educational counterparts to the CLRS array/pointer pseudocode.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")


class ArrayStack(Generic[T]):
    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("capacity must be nonnegative")
        self._items: list[T] = []
        self.capacity = capacity

    def push(self, value: T) -> None:
        if len(self._items) == self.capacity:
            raise OverflowError("stack overflow")
        self._items.append(value)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("stack underflow")
        return self._items.pop()

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)


class CircularQueue(Generic[T]):
    """Fixed-capacity queue using a one-empty-slot circular buffer."""
    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("capacity must be nonnegative")
        self._data: list[Optional[T]] = [None] * (capacity + 1)
        self._head = 0
        self._tail = 0
        self._slots = capacity + 1

    def _next(self, i: int) -> int:
        return (i + 1) % self._slots

    def enqueue(self, value: T) -> None:
        nxt = self._next(self._tail)
        if nxt == self._head:
            raise OverflowError("queue overflow")
        self._data[self._tail] = value
        self._tail = nxt

    def dequeue(self) -> T:
        if self._head == self._tail:
            raise IndexError("queue underflow")
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = self._next(self._head)
        return value  # type: ignore[return-value]

    def __len__(self) -> int:
        return (self._tail - self._head) % self._slots


class ArrayDeque(Generic[T]):
    """Resizable circular deque; each end operation is amortized O(1)."""
    def __init__(self):
        self._data: list[Optional[T]] = [None] * 8
        self._head = 0
        self._size = 0

    def _resize(self) -> None:
        old = self._data
        new: list[Optional[T]] = [None] * (2 * len(old))
        for i in range(self._size):
            new[i] = old[(self._head + i) % len(old)]
        self._data = new
        self._head = 0

    def appendleft(self, value: T) -> None:
        if self._size == len(self._data):
            self._resize()
        self._head = (self._head - 1) % len(self._data)
        self._data[self._head] = value
        self._size += 1

    def append(self, value: T) -> None:
        if self._size == len(self._data):
            self._resize()
        i = (self._head + self._size) % len(self._data)
        self._data[i] = value
        self._size += 1

    def popleft(self) -> T:
        if not self._size:
            raise IndexError("deque is empty")
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % len(self._data)
        self._size -= 1
        return value  # type: ignore[return-value]

    def pop(self) -> T:
        if not self._size:
            raise IndexError("deque is empty")
        i = (self._head + self._size - 1) % len(self._data)
        value = self._data[i]
        self._data[i] = None
        self._size -= 1
        return value  # type: ignore[return-value]

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        for i in range(self._size):
            value = self._data[(self._head + i) % len(self._data)]
            yield value  # type: ignore[misc]


@dataclass
class SinglyNode(Generic[T]):
    value: T
    next: Optional["SinglyNode[T]"] = None


class SinglyLinkedQueue(Generic[T]):
    def __init__(self):
        self.head: Optional[SinglyNode[T]] = None
        self.tail: Optional[SinglyNode[T]] = None

    def enqueue(self, value: T) -> None:
        node = SinglyNode(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self) -> T:
        if self.head is None:
            raise IndexError("queue underflow")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value


class SinglyLinkedStack(Generic[T]):
    def __init__(self):
        self.head: Optional[SinglyNode[T]] = None

    def push(self, value: T) -> None:
        self.head = SinglyNode(value, self.head)

    def pop(self) -> T:
        if self.head is None:
            raise IndexError("stack underflow")
        value = self.head.value
        self.head = self.head.next
        return value


def reverse_singly(head: Optional[SinglyNode[T]]) -> Optional[SinglyNode[T]]:
    prev = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev


@dataclass
class DoublyNode(Generic[T]):
    value: T
    prev: Optional["DoublyNode[T]"] = None
    next: Optional["DoublyNode[T]"] = None


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[DoublyNode[T]] = None
        self.tail: Optional[DoublyNode[T]] = None

    def prepend(self, value: T) -> DoublyNode[T]:
        node = DoublyNode(value, None, self.head)
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node
        return node

    def insert_after(self, where: DoublyNode[T], value: T) -> DoublyNode[T]:
        node = DoublyNode(value, where, where.next)
        if where.next is None:
            self.tail = node
        else:
            where.next.prev = node
        where.next = node
        return node

    def delete(self, node: DoublyNode[T]) -> T:
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        node.prev = node.next = None
        return node.value

    def values(self) -> list[T]:
        out = []
        cur = self.head
        while cur is not None:
            out.append(cur.value)
            cur = cur.next
        return out


@dataclass
class BinaryNode(Generic[T]):
    key: T
    left: Optional["BinaryNode[T]"] = None
    right: Optional["BinaryNode[T]"] = None
    parent: Optional["BinaryNode[T]"] = None


def preorder_recursive(root: Optional[BinaryNode[T]]) -> list[T]:
    out: list[T] = []

    def visit(node: Optional[BinaryNode[T]]) -> None:
        if node is not None:
            out.append(node.key)
            visit(node.left)
            visit(node.right)

    visit(root)
    return out


def preorder_stack(root: Optional[BinaryNode[T]]) -> list[T]:
    if root is None:
        return []
    out: list[T] = []
    stack = [root]
    while stack:
        node = stack.pop()
        out.append(node.key)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return out


def preorder_parent_pointers(root: Optional[BinaryNode[T]]) -> list[T]:
    """Preorder traversal using parent links and O(1) auxiliary space."""
    out: list[T] = []
    previous: Optional[BinaryNode[T]] = None
    current = root
    while current is not None:
        if previous is current.parent:  # entering current
            out.append(current.key)
            if current.left is not None:
                nxt = current.left
            elif current.right is not None:
                nxt = current.right
            else:
                nxt = current.parent
        elif previous is current.left:  # returning from left subtree
            nxt = current.right if current.right is not None else current.parent
        else:  # returning from right subtree
            nxt = current.parent
        previous, current = current, nxt
    return out
