import unittest
from reverseInt import Solution

class TestReverseInt(unittest.TestCase):

    def test_reverseEasy(self):
        self.assertEqual(Solution.reverse(Solution, 1), 1, "match strings")
        self.assertEqual(Solution.reverse(Solution, 123), 321, "match strings")
        self.assertEqual(Solution.reverse(Solution, -123), -321, "match strings")

    def test_reverseBig(self):
        self.assertEqual(Solution.reverse(Solution, 2147483648), 0, "match strings")
# 8463847412
# 2147483648

    def test_reverseSmall(self):
        self.assertEqual(Solution.reverse(Solution, -2147483648), 0, "match strings")

if __name__ == '__main__':
    unittest.main()
