import unittest
from regexMatch import Solution

class TestRegexMatch(unittest.TestCase):

    def test_eg1(self):
        self.assertEqual(Solution.isMatch(Solution,"aa","a"),False,)

    def test_eg2(self):
        self.assertEqual(Solution.isMatch(Solution,"aa","a*"),True,)

    def test_eg3(self):
        self.assertEqual(Solution.isMatch(Solution,"ab",".*"),True,)

    def test_eg4(self):
        self.assertEqual(Solution.isMatch(Solution,"abaaaq1xnnnnn","aba*q.*m*"),True,)


if __name__ == '__main__':
    unittest.main()
