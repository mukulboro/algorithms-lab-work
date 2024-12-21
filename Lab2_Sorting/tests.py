import unittest
from merge_sort import merge_sort
from quick_sort import quicksort

class TestSorting(unittest.TestCase):
    def setUp(self):
        self.input = [9, 8, 6, 1, 3, 7, 4]
        self.expected = [1, 3, 4, 6, 7, 8, 9]
        return super().setUp()
    
    def test_merge_sort(self):
        merge_sort(A=self.input,
                            p=0,
                            r=len(self.input)-1)
        self.assertEqual(self.input, self.expected)

    def test_quick_sort(self):
        quicksort(A=self.input,
                            p=0,
                            r=len(self.input)-1)
        self.assertEqual(self.input, self.expected)

if __name__ == "__main__":
    unittest.main()
    