import unittest
from mostWater import Solution

class TestMostWater(unittest.TestCase):

    def test_eg1(self):
        self.assertEqual(Solution.maxArea(Solution,[1,8,6,2,5,4,8,3,7]),49,"eg1",)

    def test_eg2(self):
        self.assertEqual(Solution.maxArea(Solution,[1,1]),1,"eg2",)
            
    def test_eg3(self):
        self.assertEqual(Solution.maxArea(Solution,[1,8,6,2,5,4,8,3,2]),40,"eg3",)

if __name__ == '__main__':
    unittest.main()
