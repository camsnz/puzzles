# https://leetcode.com/problems/pacific-atlantic-water-flow/

import unittest
from pacific import getAdjCoords

class TestPacificAtlantic(unittest.TestCase):

    def test_center(self):
        self.assertEqual(getAdjCoords(1,1,3), [[0,1],[2,1],[1,0],[1,2]], "Should be all NSWE")

    def test_west(self):
        self.assertEqual(getAdjCoords(0,0,3), [[1,0],[0,1]], "Should be SE")
        self.assertEqual(getAdjCoords(0,1,3), [[1,1],[0,0],[0,2]], "Should be NSE")
        self.assertEqual(getAdjCoords(0,2,3), [[1,2],[0,1]], "Should be NW")

    def test_south_east(self):
        self.assertEqual(getAdjCoords(2,2,3), [[1,2],[2,1]], "Should be...")
    # def test_dupe_eg2(self):
    #     self.assertEqual(containsDuplicate([1,2,3,4]), False, "Should be False")

    # def test_dupe_eg3(self):
    #     self.assertEqual(containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True, "Should be True")

    # def test_dupe_extra1(self):
    #     self.assertEqual(containsDuplicate([]), False, "Should be False")


if __name__ == '__main__':
    unittest.main()
