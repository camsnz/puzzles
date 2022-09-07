import unittest
from integerToRoman import Solution

class TestIntegerToRoman(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(Solution.intToRoman(Solution,58),"LVIII",58)
        self.assertEqual(Solution.intToRoman(Solution,1994),"MCMXCIV",1994)

    def test_reversed(self):
        self.assertEqual(Solution.intToRoman(Solution,1),"I",1)
        self.assertEqual(Solution.intToRoman(Solution,2),"II",2)
        self.assertEqual(Solution.intToRoman(Solution,3),"III",3)
        self.assertEqual(Solution.intToRoman(Solution,4),"IV",4)
        self.assertEqual(Solution.intToRoman(Solution,6),"VI",6)
        self.assertEqual(Solution.intToRoman(Solution,7),"VII",7)
        self.assertEqual(Solution.intToRoman(Solution,8),"VIII",8)
        self.assertEqual(Solution.intToRoman(Solution,9),"IX",9)
        self.assertEqual(Solution.intToRoman(Solution,10),"X",10)
        self.assertEqual(Solution.intToRoman(Solution,11),"XI",11)
        self.assertEqual(Solution.intToRoman(Solution,12),"XII",12)
        self.assertEqual(Solution.intToRoman(Solution,13),"XIII",13)
        self.assertEqual(Solution.intToRoman(Solution,14),"XIV",14)
        self.assertEqual(Solution.intToRoman(Solution,15),"XV",15)
        self.assertEqual(Solution.intToRoman(Solution,16),"XVI",16)
        self.assertEqual(Solution.intToRoman(Solution,17),"XVII",17)
        self.assertEqual(Solution.intToRoman(Solution,18),"XVIII",18)


if __name__ == '__main__':
    unittest.main()
