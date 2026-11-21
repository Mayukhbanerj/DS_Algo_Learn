import unittest
import random
from red_black_tree import RedBlackTree

class TestRedBlackTree(unittest.TestCase):
    def test_empty_and_singleton(self):
        t=RedBlackTree()
        self.assertTrue(t.validate())
        n=t.insert(7)
        self.assertEqual(t.inorder(),[7])
        self.assertTrue(t.validate())
        t.delete(n)
        self.assertEqual(t.inorder(),[])
        self.assertTrue(t.validate())

    def test_clrs_insertion_sequence(self):
        t=RedBlackTree()
        for key in [41,38,31,12,19,8]:
            t.insert(key)
            self.assertTrue(t.validate())
        self.assertEqual(t.inorder(),[8,12,19,31,38,41])

    def test_clrs_deletion_sequence(self):
        tree = RedBlackTree()
        for key in [41, 38, 31, 12, 19, 8]:
            tree.insert(key)
        for key, expected in [
            (8, [12, 19, 31, 38, 41]),
            (12, [19, 31, 38, 41]),
            (19, [31, 38, 41]),
            (31, [38, 41]),
            (38, [41]),
            (41, []),
        ]:
            tree.delete(tree.search(key))
            self.assertEqual(tree.inorder(), expected)
            self.assertTrue(tree.validate())

    def test_queries(self):
        t=RedBlackTree()
        nodes={k:t.insert(k) for k in [15,6,18,3,7,17,20,2,4,13,9]}
        self.assertEqual(t.search(13).key,13)
        self.assertIsNone(t.search(99))
        self.assertEqual(t.minimum().key,2)
        self.assertEqual(t.maximum().key,20)
        self.assertEqual(t.successor(nodes[13]).key,15)
        self.assertIsNone(t.successor(t.maximum()))

    def test_delete_all_orders(self):
        from itertools import permutations
        keys=[0,1,2,3,4]
        for order in permutations(keys):
            t=RedBlackTree()
            handles={k:t.insert(k) for k in order}
            self.assertTrue(t.validate())
            for k in reversed(order):
                t.delete(handles[k])
                self.assertTrue(t.validate())
            self.assertEqual(t.inorder(),[])

    def test_seeded_insert_delete_stress(self):
        rng = random.Random(130)
        for _ in range(200):
            values = [rng.randrange(50) for _ in range(rng.randrange(1, 150))]
            tree = RedBlackTree()
            handles = []
            expected = []
            for value in values:
                handles.append((value, tree.insert(value)))
                expected.append(value)
                self.assertTrue(tree.validate())
                self.assertEqual(tree.inorder(), sorted(expected))
            rng.shuffle(handles)
            for value, node in handles:
                tree.delete(node)
                expected.remove(value)
                self.assertTrue(tree.validate())
                self.assertEqual(tree.inorder(), sorted(expected))

    def test_duplicates(self):
        t=RedBlackTree()
        for k in [4,4,4,3,5,4]:
            t.insert(k)
            self.assertTrue(t.validate())
        self.assertEqual(t.inorder(),[3,4,4,4,4,5])

    def test_delete_mixed(self):
        t=RedBlackTree()
        handles={k:t.insert(k) for k in [20,10,30,25,35,22,27,21,5,15]}
        for k in [20,5,30,22,10,35,15,21,25,27]:
            t.delete(handles[k])
            self.assertTrue(t.validate())
        self.assertEqual(t.inorder(),[])

if __name__=="__main__":
    unittest.main()
