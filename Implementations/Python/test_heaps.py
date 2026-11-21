import unittest

from heaps import (
    MaxPriorityQueue,
    build_max_heap,
    heapsort,
    left,
    max_heapify,
    parent,
    right,
)


class HeapIndexTests(unittest.TestCase):
    def test_index_helpers(self):
        self.assertEqual(parent(1), 0)
        self.assertEqual(left(0), 1)
        self.assertEqual(right(0), 2)
        with self.assertRaises(ValueError):
            parent(0)


class HeapConstructionTests(unittest.TestCase):
    def test_build_max_heap(self):
        values = [5, 3, 17, 10, 84, 19, 6, 22, 9]
        size = build_max_heap(values)
        self.assertEqual(size, len(values))
        for i in range(1, size):
            self.assertGreaterEqual(values[parent(i)], values[i])
        self.assertEqual(values[0], 84)

    def test_build_empty_and_singleton(self):
        for values in ([], [7]):
            size = build_max_heap(values)
            self.assertEqual(size, len(values))


class HeapifyTests(unittest.TestCase):
    def test_max_heapify_trace(self):
        values = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
        max_heapify(values, len(values), 2)
        self.assertEqual(
            values,
            [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0],
        )

    def test_heapify_leaf_does_nothing(self):
        values = [9, 7, 8, 1, 2]
        before = values.copy()
        max_heapify(values, len(values), 4)
        self.assertEqual(values, before)


class HeapSortTests(unittest.TestCase):
    def test_sort_varied_inputs(self):
        cases = [
            [],
            [1],
            [2, 1],
            [5, 2, 4, 6, 1, 3],
            [3, 41, 52, 26, 38, 57, 9, 49],
            [2, -3, 8, 2, 0, -3],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [7] * 20,
        ]
        for values in cases:
            with self.subTest(values=values):
                expected = sorted(values)
                heapsort(values)
                self.assertEqual(values, expected)


class PriorityQueueTests(unittest.TestCase):
    def test_operations(self):
        q = MaxPriorityQueue([4, 1, 7, 3, 9])
        self.assertEqual(q.maximum(), 9)
        self.assertEqual(q.extract_max(), 9)
        q.insert(12)
        self.assertEqual(q.extract_max(), 12)
        self.assertEqual([q.extract_max() for _ in range(len(q))], [7, 4, 3, 1])

    def test_increase_key(self):
        q = MaxPriorityQueue([10, 8, 9, 2, 5])
        a = q.as_array()
        index = a.index(2)
        q.increase_key(index, 15)
        self.assertEqual(q.maximum(), 15)

    def test_underflow_and_decrease_rejection(self):
        q = MaxPriorityQueue()
        with self.assertRaises(IndexError):
            q.maximum()
        with self.assertRaises(IndexError):
            q.extract_max()
        q = MaxPriorityQueue([5, 3])
        with self.assertRaises(ValueError):
            q.increase_key(1, 1)


if __name__ == "__main__":
    unittest.main()
