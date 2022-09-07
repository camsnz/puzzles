import unittest
from longestPalindromicSubstring import Solution

class TestLongestPalindromeSubstring(unittest.TestCase):

    def test_samples(self):
        self.assertEqual(Solution.longestPalindrome(Solution,"babad"), ["bab","aba"], "match strings")
        self.assertEqual(Solution.longestPalindrome(Solution,"cbbd"), ["bb"], "match strings")

    def test_more(self):
        self.assertEqual(Solution.longestPalindrome(Solution,"ama"), ["ama"], "match strings")
        self.assertEqual(Solution.longestPalindrome(Solution,"babaqdbcqcbdqbaba"), ["qdbcqcbdq"], "match strings")
        # qdbcqcbdq
        # qdbcqcbq

if __name__ == '__main__':
    unittest.main()
