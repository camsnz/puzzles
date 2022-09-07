import unittest
from findFirst import Solution

_ = None

class Test_FindFirst(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(Solution.strStr(Solution,"sadbutsad", "sad"), 0)

    def test_example2(self):
        self.assertEqual(Solution.strStr(Solution,"leetcode", "leeto"), -1)

if __name__ == '__main__':
    unittest.main()
