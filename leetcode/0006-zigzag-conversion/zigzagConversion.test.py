import unittest
from zigzagConversion import Solution

class TestZigZagConvert(unittest.TestCase):

    def test_nums1(self):
        self.assertEqual(Solution.convert(Solution,"1234567890",1), "1234567890", "match strings")
    def test_nums2(self):
        self.assertEqual(Solution.convert(Solution,"1234567890",2), "1357924680", "match strings")
    def test_nums3(self):
        self.assertEqual(Solution.convert(Solution,"1234567890",3), "1592468037", "match strings")
    def test_nums4(self):
        self.assertEqual(Solution.convert(Solution,"0123456789",4), "0615724839", "match strings")
        self.assertEqual(Solution.convert(Solution,"1234567890",4), "1726835940", "match strings")

    # def test_more(self):
    #     self.assertEqual(Solution.convert(Solution,"ama"), ["ama"], "match strings")
    #     self.assertEqual(Solution.convert(Solution,"babaqdbcqcbdqbaba"), ["qdbcqcbdq"], "match strings")

if __name__ == '__main__':
    unittest.main()
