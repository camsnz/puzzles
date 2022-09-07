import unittest
from removeElement import Solution

_ = None

class Test_RemoveElement(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(Solution.removeElement(Solution,[3,2,2,3],3), {2:[2,2,_,_]}, "example1")
        self.assertEqual(Solution.removeElement(Solution,[0,1,2,2,3,0,4,2],2), {5:[0,1,4,0,3,_,_,_]}, "example2")

if __name__ == '__main__':
    unittest.main()
