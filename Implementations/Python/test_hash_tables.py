import unittest

from hash_tables import (
    ChainedHashTable, DirectAddressSet, OpenAddressHashTable,
    division_hash, linear_probing_delete, multiplication_hash, universal_hash,
)


class TestDirectAddress(unittest.TestCase):
    def test_bit_set(self):
        s = DirectAddressSet(8)
        self.assertFalse(s.search(3))
        s.insert(3)
        self.assertTrue(s.search(3))
        s.delete(3)
        self.assertFalse(s.search(3))

    def test_bounds(self):
        s = DirectAddressSet(2)
        with self.assertRaises(KeyError):
            s.insert(2)


class TestChaining(unittest.TestCase):
    def test_collisions_update_delete(self):
        h = ChainedHashTable(3, hash_function=lambda key: 0)
        h.insert("a", 1)
        h.insert("b", 2)
        self.assertEqual(h.search("a"), 1)
        self.assertEqual(h.search("b"), 2)
        h.insert("a", 9)
        self.assertEqual(h.search("a"), 9)
        self.assertEqual(h.delete("b"), 2)
        self.assertIsNone(h.search("b"))
        self.assertEqual(len(h), 1)

    def test_no_replace(self):
        h = ChainedHashTable(2)
        h.insert("x", 1)
        with self.assertRaises(KeyError):
            h.insert("x", 2, replace=False)


class TestOpenAddressing(unittest.TestCase):
    def test_linear_collisions_and_tombstone(self):
        h = OpenAddressHashTable(7, hash1=lambda key: 1)
        h.insert("a", 1)
        h.insert("b", 2)
        h.insert("c", 3)
        self.assertEqual(h.search("c"), 3)
        self.assertEqual(h.delete("b"), 2)
        self.assertEqual(h.search("c"), 3)
        h.insert("d", 4)
        self.assertEqual(h.search("d"), 4)

    def test_full_and_duplicate(self):
        h = OpenAddressHashTable(2, hash1=lambda key: 0)
        h.insert(1, "one")
        h.insert(2, "two")
        with self.assertRaises(OverflowError):
            h.insert(3, "three")
        h.insert(1, "ONE")
        self.assertEqual(h.search(1), "ONE")

    def test_double_hash_full_cycle(self):
        h = OpenAddressHashTable(8, hash1=lambda k: 0, hash2=lambda k: 3)
        for k in range(8):
            h.insert(k, k)
        self.assertEqual([h.search(k) for k in range(8)], list(range(8)))

    def test_bad_double_hash_step(self):
        h = OpenAddressHashTable(8, hash1=lambda k: 0, hash2=lambda k: 2)
        with self.assertRaises(ValueError):
            h.insert(1, 1)

    def test_linear_backward_shift_delete(self):
        keys = [74, 43, 93, 18, 82, 38, 92]
        table = [None] * 10
        for key in keys:
            for i in range(10):
                q = (key + i) % 10
                if table[q] is None:
                    table[q] = key
                    break
        q = table.index(43)
        linear_probing_delete(table, q, lambda key: key % 10)
        for key in (74, 93, 18, 82, 38, 92):
            start = key % 10
            found = False
            for i in range(10):
                value = table[(start + i) % 10]
                if value is None:
                    break
                if value == key:
                    found = True
                    break
            self.assertTrue(found, key)
        self.assertNotIn(43, table)


class TestHashFunctions(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(division_hash(100, 12), 4)
        self.assertEqual([multiplication_hash(k, 1000) for k in range(61, 66)],
                         [700, 318, 936, 554, 172])
        self.assertEqual(universal_hash(8, 3, 4, 17, 6), 5)


if __name__ == "__main__":
    unittest.main()
