import unittest
from dynamic_programming import (
    rod_cut, rod_cut_memoized, reconstruct_cuts, matrix_chain_order, matrix_chain_memoized,
    matrix_chain_parenthesization, lcs, lcs_length_linear_space,
    optimal_bst, construct_optimal_bst,
)

class TestDynamicProgramming(unittest.TestCase):
    def test_rod_cutting(self):
        prices=[1,5,8,9,10,17,17,20,24,30]
        revenue,first=rod_cut(prices,4)
        self.assertEqual(revenue,10)
        self.assertEqual(rod_cut_memoized(prices,4)[0],10)
        self.assertEqual(sum(reconstruct_cuts(first,4)),4)
        self.assertEqual(sum(prices[x-1] for x in reconstruct_cuts(first,4)),10)

    def test_rod_cutting_zero_and_validation(self):
        self.assertEqual(rod_cut([],0)[0],0)
        with self.assertRaises(ValueError):rod_cut([1],2)

    def test_matrix_chain_clrs(self):
        cost,s=matrix_chain_order([30,35,15,5,10,20,25])
        self.assertEqual(cost,15125)
        self.assertEqual(matrix_chain_memoized([30,35,15,5,10,20,25])[0],15125)
        self.assertEqual(matrix_chain_parenthesization(s),"((A1(A2A3))((A4A5)A6))")

    def test_matrix_chain_single(self):
        cost,s=matrix_chain_order([7,11])
        self.assertEqual(cost,0)
        self.assertEqual(matrix_chain_parenthesization(s),"A1")

    def test_lcs(self):
        result,c=lcs("ABCBDAB","BDCABA")
        self.assertEqual(len(result),4)
        self.assertTrue(is_subsequence(result,"ABCBDAB"))
        self.assertTrue(is_subsequence(result,"BDCABA"))
        self.assertEqual(lcs_length_linear_space("ABCBDAB","BDCABA"),4)

    def test_lcs_empty_and_space(self):
        self.assertEqual(lcs("","ABC")[0],[])
        self.assertEqual(lcs_length_linear_space("","ABC"),0)

    def test_optimal_bst_clrs(self):
        p=[.15,.10,.05,.10,.20]
        q=[.05,.10,.05,.05,.05,.10]
        cost,root=optimal_bst(p,q)
        self.assertAlmostEqual(cost,2.75)
        self.assertEqual(root[0][4],1)
        self.assertIsNotNone(construct_optimal_bst(root))

def is_subsequence(s, text):
    it=iter(text)
    return all(any(ch==x for x in it) for ch in s)

if __name__=="__main__":unittest.main()
