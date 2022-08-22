import unittest
from ContainsDuplicate import Leet

containsDuplicate = Leet.containsDuplicateRaw
class TestSum(unittest.TestCase):

    def test_dupe_eg1(self):
        self.assertEqual(containsDuplicate([1, 2, 3, 1]), True, "Should be True")

    def test_dupe_eg2(self):
        self.assertEqual(containsDuplicate([1,2,3,4]), False, "Should be False")

    def test_dupe_eg3(self):
        self.assertEqual(containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True, "Should be True")

    def test_dupe_extra1(self):
        self.assertEqual(containsDuplicate([]), False, "Should be False")


if __name__ == '__main__':
    unittest.main()
