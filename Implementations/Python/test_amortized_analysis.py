import unittest
from amortized_analysis import Stack, BinaryCounter, DynamicArray, gray_code, DynamicSortedArrays

class TestAmortizedAnalysis(unittest.TestCase):
    def test_stack(self):
        s=Stack()
        s.multipush([1,2,3,4])
        self.assertEqual(s.multipop(3),[4,3,2])
        self.assertEqual(s.pop(),1)
        with self.assertRaises(IndexError):s.pop()
    def test_multipush_and_validation(self):
        s=Stack();s.multipush([1,2]);self.assertEqual(len(s),2)
        with self.assertRaises(ValueError):s.multipop(-1)
    def test_counter_wraparound(self):
        c=BinaryCounter(3)
        self.assertEqual([c.increment() for _ in range(9)],[1,2,3,4,5,6,7,0,1])
        self.assertEqual(c.decrement(),0)
    def test_counter_reset_pointer(self):
        c=BinaryCounter(8)
        for _ in range(31): c.increment()
        self.assertEqual(c.high,4)
        self.assertEqual(c.reset(),5)
        self.assertEqual(c.value,0)
        self.assertEqual(c.high,-1)
        self.assertEqual(c.reset(),0)
    def test_dynamic_array_expand_contract(self):
        a=DynamicArray()
        costs=[a.insert(i) for i in range(9)]
        self.assertEqual(a.values(),list(range(9)))
        self.assertLessEqual(sum(costs),3*9)
        while a.values():a.delete_at(len(a.values())-1)
        self.assertEqual(a.capacity,0)
    def test_dynamic_array_no_resize_thrashing(self):
        a=DynamicArray()
        for i in range(16):a.insert(i)
        before=a.copies
        a.delete_at(0)
        self.assertEqual(a.copies,before)
    def test_gray_code(self):
        for k in range(1,7):
            seq=gray_code(k)
            self.assertEqual(len(seq),2**k)
            for i in range(len(seq)):
                self.assertEqual((seq[i]^seq[(i+1)%len(seq)]).bit_count(),1)
    def test_dynamic_sorted_arrays(self):
        d=DynamicSortedArrays()
        values=[7,2,9,1,4,8,3,6,5]
        for v in values:d.insert(v)
        self.assertEqual(d.all_values(),sorted(values))
        for v in values:self.assertIsNotNone(d.search(v))
        self.assertIsNone(d.search(10))

if __name__=="__main__":unittest.main()
