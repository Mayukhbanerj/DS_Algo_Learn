import random
import unittest

from linear_sorting import (
    bucket_sort,
    counting_sort,
    counting_sort_in_place,
    radix_sort,
)


class CountingSortTests(unittest.TestCase):
    def test_counting_sort_example(self):
        values = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
        self.assertEqual(counting_sort(values, 6), sorted(values))

    def test_counting_sort_is_stable_for_records(self):
        records = [("a", 2), ("b", 1), ("c", 2), ("d", 0), ("e", 1)]
        result = counting_sort(records, 2, key=lambda record: record[1])
        self.assertEqual(result, [("d", 0), ("b", 1), ("e", 1), ("a", 2), ("c", 2)])

    def test_counting_sort_in_place(self):
        values = [3, 0, 2, 3, 1, 0]
        counting_sort_in_place(values, 3)
        self.assertEqual(values, [0, 0, 1, 2, 3, 3])


class RadixSortTests(unittest.TestCase):
    def test_radix_sort_clrs_example(self):
        values = [329, 457, 657, 839, 436, 720, 355]
        self.assertEqual(radix_sort(values), sorted(values))

    def test_radix_sort_different_bases(self):
        values = [0, 1000, 10, 1, 999, 10, 256, 65535]
        for base in (2, 8, 10, 16, 256):
            self.assertEqual(radix_sort(values, base), sorted(values))

    def test_radix_sort_empty_and_invalid(self):
        self.assertEqual(radix_sort([]), [])
        with self.assertRaises(ValueError):
            radix_sort([-1, 2])


class BucketSortTests(unittest.TestCase):
    def test_bucket_sort_example(self):
        values = [.78, .17, .39, .72, .94, .21, .12, .23, .68, .89]
        self.assertEqual(bucket_sort(values), sorted(values))

    def test_bucket_sort_boundaries_and_duplicates(self):
        values = [0.0, .1, .5, .999999, .5, .0]
        self.assertEqual(bucket_sort(values), sorted(values))

    def test_bucket_sort_invalid(self):
        with self.assertRaises(ValueError):
            bucket_sort([0.2, 1.0])


class RandomizedTests(unittest.TestCase):
    def test_random_inputs(self):
        rng = random.Random(2026)
        for _ in range(300):
            integers = [rng.randrange(0, 10000) for _ in range(rng.randrange(0, 100))]
            self.assertEqual(counting_sort(integers, 9999), sorted(integers))
            self.assertEqual(radix_sort(integers), sorted(integers))
            floats = [rng.random() for _ in range(rng.randrange(0, 100))]
            self.assertEqual(bucket_sort(floats), sorted(floats))


if __name__ == "__main__":
    unittest.main()
