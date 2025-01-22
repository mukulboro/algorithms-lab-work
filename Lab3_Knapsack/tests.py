import unittest
from knapsack import Knapsack
from fractional_knapsack import FractionalKnapsack
import math

class KnapSackTest(unittest.TestCase):
    def test_01_bruteforce(self):
        tst_items = (1, 2, 3, 4, 5)
        tst_weights = (3, 6, 7, 9, 2)
        tst_capacity = 15

        expected_profit = 10
        expected_config = ('1', '0', '0', '1', '1')

        k = Knapsack(items=tst_items,
                     weights=tst_weights,
                     capacity=tst_capacity)
        result_max_profit, result_config = k.brute_force()
        self.assertEqual(expected_profit, result_max_profit)
        self.assertEqual(expected_config, result_config)

    def test_01_dynamic(self):
        tst_items = (1, 2, 3, 4, 5)
        tst_weights = (3, 6, 7, 9, 2)
        tst_capacity = 15

        expected_profit = 10
        expected_config = ('0', '1', '1', '0', '1')

        k = Knapsack(items=tst_items,
                     weights=tst_weights,
                     capacity=tst_capacity)
        result_max_profit, result_config = k.dynamic()
        self.assertEqual(expected_profit, result_max_profit)
        self.assertEqual(expected_config, result_config)

    def test_fractional_bruteforce(self):
        tst_items = (10, 5, 15, 7, 6)
        tst_weights = (2, 3, 5, 7, 1)
        tst_capacity = 10

        expected_profit = 35.0
        
        k = FractionalKnapsack(items=tst_items,
                              weights=tst_weights,
                              capacity=tst_capacity)
        result_max_profit, _ = k.brute_force()
        self.assertEqual(expected_profit, math.ceil(result_max_profit))

    def test_fractional_greedy(self):
        tst_items = (10, 5, 15, 7, 6)
        tst_weights = (2, 3, 5, 7, 1)
        tst_capacity = 10

        expected_profit = 35.0
        
        k = FractionalKnapsack(items=tst_items,
                              weights=tst_weights,
                              capacity=tst_capacity)
        result_max_profit, _ = k.greedy()
        self.assertEqual(expected_profit, math.ceil(result_max_profit))

if __name__ == "__main__":
    unittest.main()