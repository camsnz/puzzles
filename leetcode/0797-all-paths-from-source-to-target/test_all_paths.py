import unittest
from all_paths import Solution as Sol

class AllPathsTest(unittest.TestCase):
    sol = Sol()

    def test_filter_out(self):
        """
        Various: deletes, misses, empties, start and end of lists.
        """
        self.assertEqual(self.sol.filterOut([], [2]), [])
        self.assertEqual(self.sol.filterOut([1,2,3], []), [1,2,3])
        self.assertEqual(self.sol.filterOut([1,2,3], [1,2,3]), [])
        self.assertEqual(self.sol.filterOut([1,2,3], [1]), [2,3])
        self.assertEqual(self.sol.filterOut([1,2,3], [2]), [1,3])
        self.assertEqual(self.sol.filterOut([1,2,3], [3]), [1,2])

    def test_visit__empty_cases(self):
        """
        Empty scenarios, empty results
        """
        self.assertEqual(self.sol.allPathsSourceTarget([]), [])

    def test_visit__bad_data_nullish(self):
        """
        Bad data, empty nodes, empty results
        """
        self.assertEqual(self.sol.allPathsSourceTarget(graph=[[]]), [])
        self.assertEqual(self.sol.allPathsSourceTarget(graph=[[],[]]), [])

    def test_visit__bad_data_no_path(self):
        """
        Bad data, no paths, empty results
        """
        self.assertEqual(self.sol.allPathsSourceTarget([[2],[2],[1],[]]), [])

    def test_visit__bad_data_dead_ends(self):
        """
        Bad data, dead ends, clean results
        """
        self.assertEqual(self.sol.allPathsSourceTarget([[1,3],[2],[],[4],[]]), [[0,3,4]])
        self.assertEqual(self.sol.allPathsSourceTarget([[1,3],[2],[],[]]), [[0,3]])
        self.assertEqual(self.sol.allPathsSourceTarget([[2],[],[3],[]]), [[0,2,3]])

    def test_visit__bad_data_cycles(self):
        """
        Bad data, dead ends, clean results
        """
        self.assertEqual(self.sol.allPathsSourceTarget([[1],[2],[1,3],[4],[]]), [[0,1,2,3,4]])
        self.assertEqual(self.sol.allPathsSourceTarget([[1],[2,3],[3],[2,4],[5],[]]), [[0,1,2,3,4,5], [0,1,3,4,5]])

if __name__ == '__main__':
    unittest.main()
