import random
import unittest

from order_statistics import deterministic_select, min_max, randomized_select


class MinMaxTests(unittest.TestCase):
    def test_odd_and_even(self):
        self.assertEqual(min_max([7, 2, 9, 1, 5]), (1, 9))
        self.assertEqual(min_max([7, 2, 9, 1]), (1, 9))

    def test_singleton(self):
        self.assertEqual(min_max([4]), (4, 4))

    def test_empty_rejected(self):
        with self.assertRaises(ValueError):
            min_max([])


class SelectionTests(unittest.TestCase):
    def test_randomized_select_all_ranks(self):
        values = [31, 4, 18, 7, 22, 1, 15, 9, 2]
        expected = sorted(values)
        for rank, answer in enumerate(expected, 1):
            self.assertEqual(randomized_select(values.copy(), rank, random.Random(rank)), answer)

    def test_deterministic_select_all_ranks(self):
        values = [31, 4, 18, 7, 22, 1, 15, 9, 2]
        expected = sorted(values)
        for rank, answer in enumerate(expected, 1):
            self.assertEqual(deterministic_select(values.copy(), rank), answer)

    def test_duplicates(self):
        values = [5, 1, 5, 2, 5, 3, 2, 1]
        expected = sorted(values)
        for rank, answer in enumerate(expected, 1):
            self.assertEqual(randomized_select(values.copy(), rank, random.Random(rank)), answer)
            self.assertEqual(deterministic_select(values.copy(), rank), answer)

    def test_invalid_rank(self):
        for function in (randomized_select, deterministic_select):
            with self.assertRaises(ValueError):
                function([1, 2, 3], 0)
            with self.assertRaises(ValueError):
                function([1, 2, 3], 4)

    def test_randomized_differential(self):
        rng = random.Random(2026)
        for _ in range(500):
            values = [rng.randrange(-100, 101) for _ in range(rng.randrange(1, 120))]
            expected = sorted(values)
            rank = rng.randrange(1, len(values) + 1)
            self.assertEqual(randomized_select(values.copy(), rank, rng), expected[rank - 1])
            self.assertEqual(deterministic_select(values.copy(), rank), expected[rank - 1])


if __name__ == "__main__":
    unittest.main()
