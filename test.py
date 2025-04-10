# test.py
import unittest
from algorithms import *

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.unsorted = [5, 3, 8, 6, 2, 7, 4, 1]
        self.sorted = sorted(self.unsorted)

    def test_linear_search(self):
        self.assertEqual(linear_search(self.unsorted, 6), 3)
        self.assertEqual(linear_search(self.unsorted, 10), -1)

    def test_binary_search(self):
        self.assertEqual(binary_search(self.sorted, 6), self.sorted.index(6))
        self.assertEqual(binary_search(self.sorted, 10), -1)

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.unsorted.copy()), self.sorted)

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.unsorted.copy()), self.sorted)

    def test_quick_sort(self):
        self.assertEqual(quick_sort(self.unsorted.copy()), self.sorted)

    def test_heap_sort(self):
        self.assertEqual(heap_sort(self.unsorted.copy()), self.sorted)

if __name__ == '__main__':
    unittest.main()
