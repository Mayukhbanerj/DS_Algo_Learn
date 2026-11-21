import random
import unittest

from quicksort import (
    bounded_stack_quicksort,
    fuzzy_sort,
    hoare_partition,
    hoare_quicksort,
    partition,
    quicksort,
    randomized_quicksort,
    three_way_partition,
    three_way_quicksort,
)


class QuicksortTests(unittest.TestCase):
    def check_sorters(self, values):
        expected = sorted(values)
        for sorter in (
            quicksort,
            hoare_quicksort,
            bounded_stack_quicksort,
            three_way_quicksort,
        ):
            actual = values.copy()
            sorter(actual)
            self.assertEqual(actual, expected, sorter.__name__)
        actual = values.copy()
        randomized_quicksort(actual, rng=random.Random(7))
        self.assertEqual(actual, expected)

    def test_standard_examples(self):
        self.check_sorters([13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11])
        self.check_sorters([5, 2, 4, 6, 1, 3])
        self.check_sorters([3, 41, 52, 26, 38, 57, 9, 49])

    def test_empty_singleton_and_pair(self):
        for values in ([], [1], [2, 1]):
            self.check_sorters(values)

    def test_sorted_reverse_and_duplicates(self):
        for values in (
            list(range(30)),
            list(range(29, -1, -1)),
            [5] * 50,
            [2, -3, 8, 2, 0, -3] * 5,
        ):
            self.check_sorters(values)

    def test_randomized_arrays(self):
        rng = random.Random(2026)
        for _ in range(500):
            values = [rng.randint(-20, 20) for _ in range(rng.randint(0, 60))]
            self.check_sorters(values)

    def test_lomuto_partition_contract(self):
        a = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
        q = partition(a, 0, len(a) - 1)
        pivot = a[q]
        self.assertTrue(all(x <= pivot for x in a[:q]))
        self.assertTrue(all(x > pivot for x in a[q + 1 :]))
        self.assertEqual(pivot, 11)

    def test_hoare_partition_contract(self):
        a = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
        q = hoare_partition(a, 0, len(a) - 1)
        self.assertLess(q, len(a) - 1)
        self.assertTrue(all(x <= 13 for x in a[: q + 1]))
        self.assertTrue(all(x >= 13 for x in a[q + 1 :]))

    def test_three_way_partition(self):
        a = [3, 5, 3, 2, 3, 8, 3, 1]
        lo, hi = three_way_partition(a, 0, len(a) - 1)
        pivot = a[lo]
        self.assertTrue(all(x < pivot for x in a[:lo]))
        self.assertTrue(all(x == pivot for x in a[lo : hi + 1]))
        self.assertTrue(all(x > pivot for x in a[hi + 1 :]))

    def test_fuzzy_sort_order(self):
        intervals = [(5, 8), (1, 3), (2, 6), (7, 9), (10, 12), (4, 7)]
        result = fuzzy_sort(intervals, random.Random(10))
        # There must be a nondecreasing choice of representative points.
        # A greedy earliest-feasible representative verifies the ordering.
        point = float("-inf")
        for lo, hi in result:
            point = max(point, lo)
            self.assertLessEqual(point, hi)


if __name__ == "__main__":
    unittest.main()
