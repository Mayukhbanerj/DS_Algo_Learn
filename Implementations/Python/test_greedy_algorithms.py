import unittest
from greedy_algorithms import (
    activity_selection, interval_partitioning, weighted_activity_selection,
    fractional_knapsack, zero_one_knapsack, huffman_codes, huffman_cost,
    farthest_in_future, coin_change_greedy, coin_change_dp,
    shortest_processing_time, srpt_schedule,
)

class TestGreedyAlgorithms(unittest.TestCase):
    def test_activity_selection(self):
        acts=[(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
        chosen=activity_selection(acts)
        self.assertEqual(len(chosen),4)
        selected=sorted((acts[i] for i in chosen),key=lambda x:x[0])
        self.assertTrue(all(selected[i][1]<=selected[i+1][0] for i in range(len(selected)-1)))

    def test_interval_partitioning(self):
        acts=[(0,3),(1,4),(3,5),(2,7),(5,8)]
        halls,assignment=interval_partitioning(acts)
        self.assertEqual(halls,3)
        for i in range(len(acts)):
            for j in range(i):
                if assignment[i]==assignment[j]:
                    self.assertTrue(acts[i][1]<=acts[j][0] or acts[j][1]<=acts[i][0])

    def test_weighted_activity(self):
        acts=[(1,3,5),(2,5,6),(4,6,5),(6,7,4),(5,8,11),(7,9,2)]
        value,chosen=weighted_activity_selection(acts)
        self.assertEqual(value,17)
        ordered=sorted((acts[i] for i in chosen),key=lambda a:a[0])
        self.assertTrue(all(ordered[i][1]<=ordered[i+1][0] for i in range(len(ordered)-1)))

    def test_fractional_knapsack(self):
        value,selected=fractional_knapsack([(60,10),(100,20),(120,30)],50)
        self.assertAlmostEqual(value,240)
        self.assertAlmostEqual(sum([(10 if i==0 else 20 if i==1 else 30)*f for i,f in selected]),50)

    def test_zero_one_knapsack(self):
        value,chosen=zero_one_knapsack([(60,10),(100,20),(120,30)],50)
        self.assertEqual(value,220)
        self.assertEqual(set(chosen),{1,2})

    def test_huffman(self):
        freq={"a":45,"b":13,"c":12,"d":16,"e":9,"f":5}
        codes,tree=huffman_codes(freq)
        self.assertEqual(huffman_cost(freq,codes),224)
        for x in codes:
            for y in codes:
                if x!=y:self.assertFalse(codes[y].startswith(codes[x]))
        self.assertIsNotNone(tree)

    def test_farthest_in_future(self):
        misses,trace=farthest_in_future(["A","B","C","A","B"],2)
        self.assertEqual(misses,4)
        self.assertEqual(trace[2][2],"B")

    def test_coin_change(self):
        self.assertEqual(len(coin_change_greedy(87,[25,10,5,1])),5)
        self.assertEqual(coin_change_dp(6,[1,3,4]),(2,[3,3]))

    def test_scheduling(self):
        order,avg=shortest_processing_time([3,5])
        self.assertEqual(order,[0,1])
        self.assertEqual(avg,5.5)
        completion=srpt_schedule([(0,6),(1,2)])
        self.assertEqual(completion,[8,3])

if __name__=="__main__":unittest.main()
