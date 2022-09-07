
import unittest
from strongPass import Solution

class Test_StrongPass(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(Solution.mergeKLists(Solution,""),5)
        self.assertEqual(Solution.mergeKLists(Solution,"aA1"),3)
        self.assertEqual(Solution.mergeKLists(Solution,"1337C0d3"),0)

if __name__ == '__main__':
    unittest.main()
