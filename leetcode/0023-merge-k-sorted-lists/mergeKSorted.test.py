
import unittest
from mergeKSorted import Solution

class Test_Merge_K_Sorted(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(Solution.mergeKLists(Solution,[[1,4,5],[1,3,4],[2,6]]),[1,1,2,3,4,4,5,6])
        self.assertEqual(Solution.mergeKLists(Solution,[]),[])
        self.assertEqual(Solution.mergeKLists(Solution,[[]]),[])

if __name__ == '__main__':
    unittest.main()
