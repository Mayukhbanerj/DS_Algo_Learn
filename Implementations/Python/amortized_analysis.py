"""Chapter 16 amortized-analysis examples and dynamic-table implementation."""
from __future__ import annotations

class Stack:
    def __init__(self):
        self.items = []
    def push(self, value):
        self.items.append(value)
    def pop(self):
        if not self.items:
            raise IndexError("pop from empty stack")
        return self.items.pop()
    def multipop(self, k):
        if k < 0:
            raise ValueError("k must be nonnegative")
        count = min(k, len(self.items))
        result = self.items[-count:][::-1] if count else []
        if count:
            del self.items[-count:]
        return result
    def multipush(self, values):
        self.items.extend(values)
    def __len__(self):
        return len(self.items)

class BinaryCounter:
    def __init__(self, width: int, value: int = 0):
        if width <= 0 or value < 0 or value >= 1 << width:
            raise ValueError("invalid width or initial value")
        self.width = width
        self.value = value
        self.high = value.bit_length() - 1
    def increment(self):
        self.value = (self.value + 1) % (1 << self.width)
        self.high = self.value.bit_length() - 1
        return self.value
    def decrement(self):
        self.value = (self.value - 1) % (1 << self.width)
        self.high = self.value.bit_length() - 1
        return self.value
    def reset(self):
        examined = self.high + 1
        self.value = 0
        self.high = -1
        return examined
    def bits(self):
        return [(self.value >> i) & 1 for i in range(self.width)]

class DynamicArray:
    """Array model with doubling and quarter-full halving; reports copied-item costs."""
    def __init__(self):
        self.data = []
        self.capacity = 0
        self.copies = 0
    @property
    def load_factor(self):
        return len(self.data) / self.capacity if self.capacity else 1.0
    def insert(self, value):
        cost = 1
        if self.capacity == 0:
            self.capacity = 1
            self.data = []
        elif len(self.data) == self.capacity:
            new_capacity = 2 * self.capacity
            new = list(self.data)
            cost += len(self.data)
            self.copies += len(self.data)
            self.data = new
            self.capacity = new_capacity
        self.data.append(value)
        return cost
    def delete_at(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("invalid index")
        value = self.data.pop(index)
        cost = 1
        if not self.data:
            self.data = []
            self.capacity = 0
        elif self.capacity > 1 and len(self.data) < self.capacity / 4:
            new_capacity = max(1, self.capacity // 2)
            new = list(self.data)
            cost += len(self.data)
            self.copies += len(self.data)
            self.data = new
            self.capacity = new_capacity
        return value, cost
    def values(self):
        return list(self.data)

def gray_code(width: int) -> list[int]:
    if width < 0:
        raise ValueError("width must be nonnegative")
    return [i ^ (i >> 1) for i in range(1 << width)]

class DynamicSortedArrays:
    """Insertion/search structure with power-of-two sorted runs."""
    def __init__(self):
        self.levels = []
        self.size = 0
    def search(self, key):
        from bisect import bisect_left
        for level, arr in enumerate(self.levels):
            if arr is not None:
                i = bisect_left(arr, key)
                if i < len(arr) and arr[i] == key:
                    return level, i
        return None
    def insert(self, key):
        from heapq import merge
        carry = [key]
        level = 0
        while True:
            if level == len(self.levels):
                self.levels.append(carry)
                break
            if self.levels[level] is None:
                self.levels[level] = carry
                break
            carry = list(merge(self.levels[level], carry))
            self.levels[level] = None
            level += 1
        self.size += 1
    def all_values(self):
        return sorted(x for arr in self.levels if arr is not None for x in arr)
