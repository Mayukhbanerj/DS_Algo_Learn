import unittest

from insertion_sort import insertion_sort
from merge_sort import merge_sort


class SortingTests(unittest.TestCase):
    def test_insertion_sort_example(self):
        values = [5, 2, 4, 6, 1, 3]
        self.assertEqual(insertion_sort(values), [1, 2, 3, 4, 5, 6])

    def test_merge_sort_example(self):
        values = [3, 41, 52, 26, 38, 57, 9, 49]
        self.assertEqual(merge_sort(values), [3, 9, 26, 38, 41, 49, 52, 57])

    def test_empty_and_singleton(self):
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(insertion_sort([7]), [7])
        self.assertEqual(merge_sort([7]), [7])

    def test_duplicates_and_negative_values(self):
        expected = [-3, -3, 0, 2, 2, 8]
        self.assertEqual(insertion_sort([2, -3, 8, 2, 0, -3]), expected)
        self.assertEqual(merge_sort([2, -3, 8, 2, 0, -3]), expected)

    def test_already_sorted_and_reverse_sorted(self):
        self.assertEqual(insertion_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
