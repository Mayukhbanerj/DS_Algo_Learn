import unittest
from itertools import permutations
from binary_search_tree import BinarySearchTree

class TestBST(unittest.TestCase):
    def build(self,keys):
        t=BinarySearchTree()
        nodes=[t.insert(k) for k in keys]
        return t,nodes

    def test_empty_and_singleton(self):
        t=BinarySearchTree()
        self.assertEqual(t.inorder(),[])
        self.assertEqual(t.height(),-1)
        n=t.insert(7)
        self.assertEqual(t.inorder(),[7])
        self.assertEqual(t.height(),0)
        t.delete(n)
        self.assertEqual(t.inorder(),[])
        self.assertTrue(t.validate())

    def test_walks(self):
        t,_=self.build([6,5,7,2,5,8])
        self.assertEqual(t.inorder(),[2,5,5,6,7,8])
        self.assertEqual(t.preorder(),[6,5,2,5,7,8])
        self.assertEqual(t.postorder(),[2,5,5,8,7,6])

    def test_queries(self):
        t,nodes=self.build([15,6,18,3,7,17,20,2,4,13,9])
        self.assertEqual(t.search(13).key,13)
        self.assertIsNone(t.search(99))
        self.assertEqual(t.minimum().key,2)
        self.assertEqual(t.maximum().key,20)
        x=t.search(13)
        self.assertEqual(t.successor(x).key,15)
        self.assertEqual(t.predecessor(x).key,9)
        self.assertIsNone(t.predecessor(t.minimum()))
        self.assertIsNone(t.successor(t.maximum()))

    def test_delete_leaf_one_child_two_child(self):
        t,_=self.build([15,6,18,3,7,17,20,2,4,13,9])
        t.delete(t.search(2))
        self.assertTrue(t.validate())
        t.delete(t.search(13))
        self.assertTrue(t.validate())
        t.delete(t.search(6))
        self.assertTrue(t.validate())
        self.assertEqual(t.inorder(),[3,4,7,9,15,17,18,20])

    def test_delete_successor_direct_right_child(self):
        t,_=self.build([10,5,15,18])
        z=t.search(10); successor=t.successor(z)
        t.delete(z)
        self.assertIs(t.search(12),successor)
        self.assertEqual(t.inorder(),[5,15,18])
        self.assertTrue(t.validate())

    def test_delete_successor_deeper(self):
        t,_=self.build([20,10,30,25,35,22,27,21])
        z=t.search(20); successor=t.successor(z)
        t.delete(z)
        self.assertIs(t.search(21),successor)
        self.assertEqual(t.inorder(),[10,21,22,25,27,30,35])
        self.assertTrue(t.validate())

    def test_duplicates_right_on_insert(self):
        t,_=self.build([4,4,4,3,5])
        self.assertEqual(t.inorder(),[3,4,4,4,5])
        self.assertEqual(t.height(),2)
        self.assertTrue(t.validate())

    def test_all_small_insertion_orders_and_deletion_orders(self):
        keys = [0, 1, 2, 3, 4]
        for order in permutations(keys):
            t = BinarySearchTree()
            handles = {key: t.insert(key) for key in order}
            self.assertTrue(t.validate())
            self.assertEqual(t.inorder(), keys)
            for key in reversed(order):
                t.delete(handles[key])
                self.assertTrue(t.validate())
                remaining = sorted(k for k in keys if k not in order[order.index(key):])
                self.assertEqual(t.inorder(), remaining)

    def test_successor_predecessor_all_nodes(self):
        t,_=self.build([8,4,12,2,6,10,14,5,7,9,11])
        ordered=t.inorder()
        nodes=[]
        for k in ordered:
            nodes.append(t.search(k))
        for i,node in enumerate(nodes):
            self.assertEqual(t.predecessor(node).key if i else None, ordered[i-1] if i else None)
            self.assertEqual(t.successor(node).key if i+1<len(nodes) else None, ordered[i+1] if i+1<len(nodes) else None)

if __name__=="__main__":unittest.main()
