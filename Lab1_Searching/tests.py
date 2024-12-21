import unittest
from linear_search import *
from binary_search import *

class TestSearch(unittest.TestCase):
    def test_linear_found(self):
        input_array = [9, 8, 6, 1, 3, 7, 4]
        input_key = 6
        expected = 2
        result = linear_search(array=input_array, key=input_key)
        self.assertEqual(result, expected)
    
    def test_linear_not_found(self):
        input_array = [9, 8, 6, 1, 3, 7, 4]
        input_key = 5
        expected = -1
        result = linear_search(array=input_array, key=input_key)
        self.assertEqual(result, expected)

    def test_binary_found(self):
        input_array = [1, 2, 3, 4, 5, 6, 7, 8]
        input_key = 6
        expected = 5
        result = binary_search(array=input_array, key=input_key)
        self.assertEqual(result, expected)

    def test_binary_not_found(self):
        input_array = [1, 2, 3, 4, 5, 6, 7, 8]
        input_key = 9
        expected = -1
        result = binary_search(array=input_array, key=input_key)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()