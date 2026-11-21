import unittest

from elementary_structures import (
    ArrayDeque, ArrayStack, BinaryNode, CircularQueue, DoublyLinkedList,
    SinglyLinkedQueue, SinglyLinkedStack, preorder_parent_pointers,
    preorder_recursive, preorder_stack, reverse_singly,
)


class TestArrayStack(unittest.TestCase):
    def test_lifo(self):
        s = ArrayStack(3)
        s.push(4); s.push(1); s.push(3)
        self.assertEqual([s.pop(), s.pop(), s.pop()], [3, 1, 4])

    def test_errors(self):
        s = ArrayStack(1)
        s.push(1)
        with self.assertRaises(OverflowError):
            s.push(2)
        s.pop()
        with self.assertRaises(IndexError):
            s.pop()


class TestCircularQueue(unittest.TestCase):
    def test_fifo_and_wraparound(self):
        q = CircularQueue(3)
        for x in (4, 1, 3):
            q.enqueue(x)
        self.assertEqual(q.dequeue(), 4)
        q.enqueue(8)
        self.assertEqual([q.dequeue(), q.dequeue(), q.dequeue()], [1, 3, 8])

    def test_capacity_and_underflow(self):
        q = CircularQueue(1)
        q.enqueue(7)
        with self.assertRaises(OverflowError):
            q.enqueue(8)
        self.assertEqual(q.dequeue(), 7)
        with self.assertRaises(IndexError):
            q.dequeue()


class TestDeque(unittest.TestCase):
    def test_both_ends_and_resize(self):
        d = ArrayDeque()
        d.append(2); d.appendleft(1); d.append(3)
        for x in range(4, 20):
            d.append(x)
        self.assertEqual(d.popleft(), 1)
        self.assertEqual(d.pop(), 19)
        self.assertEqual(list(d), list(range(2, 19)))


class TestLinkedLists(unittest.TestCase):
    def test_singly_stack_queue_reverse(self):
        s = SinglyLinkedStack()
        s.push(1); s.push(2)
        self.assertEqual([s.pop(), s.pop()], [2, 1])
        q = SinglyLinkedQueue()
        q.enqueue(4); q.enqueue(5)
        self.assertEqual([q.dequeue(), q.dequeue()], [4, 5])
        a = SinglyLinkedStack()
        a.push(1); a.push(2); a.push(3)
        head = reverse_singly(a.head)
        vals = []
        while head:
            vals.append(head.value); head = head.next
        self.assertEqual(vals, [1, 2, 3])

    def test_doubly_linked_splice(self):
        d = DoublyLinkedList()
        a = d.prepend(2)
        b = d.prepend(1)
        c = d.insert_after(a, 3)
        self.assertEqual(d.values(), [1, 2, 3])
        self.assertEqual(d.delete(a), 2)
        self.assertEqual(d.values(), [1, 3])
        self.assertIs(d.head, b)
        self.assertIs(d.tail, c)


class TestTreeTraversal(unittest.TestCase):
    def setUp(self):
        self.root = BinaryNode(1)
        self.root.left = BinaryNode(2, parent=self.root)
        self.root.right = BinaryNode(3, parent=self.root)
        self.root.left.left = BinaryNode(4, parent=self.root.left)
        self.root.left.right = BinaryNode(5, parent=self.root.left)
        self.root.right.right = BinaryNode(6, parent=self.root.right)

    def test_three_preorder_methods_agree(self):
        expected = [1, 2, 4, 5, 3, 6]
        self.assertEqual(preorder_recursive(self.root), expected)
        self.assertEqual(preorder_stack(self.root), expected)
        self.assertEqual(preorder_parent_pointers(self.root), expected)

    def test_empty_tree(self):
        self.assertEqual(preorder_parent_pointers(None), [])


if __name__ == "__main__":
    unittest.main()
