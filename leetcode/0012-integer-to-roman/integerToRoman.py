# https://leetcode.com/problems/integer-to-roman/

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

from curses.has_key import has_key
import itertools
from typing import List


romansToInt = dict()
romansToInt['I'] = 1
romansToInt['V'] = 5
romansToInt['X'] = 10
romansToInt['L'] = 50
romansToInt['C'] = 100
romansToInt['D'] = 500
romansToInt['M'] = 1000

romPre = dict()
# romPre['I'] = 'I'
romPre['V'] = 'I'
romPre['X'] = 'I'
romPre['L'] = 'X'
romPre['C'] = 'X'
romPre['D'] = 'C'
romPre['M'] = 'C'

intsToRoman = dict()
intsToRoman[1] = 'I'
intsToRoman[5] = 'V'
intsToRoman[10] = 'X'
intsToRoman[50] = 'L'
intsToRoman[100] = 'C'
intsToRoman[500] = 'D'
intsToRoman[1000] = 'M'

order = ['I','V','X','L','C','D','M']
romansHighToLow = order[::-1]

# print(romansHighToLow)
# print(order)
# print(ints)
# print(romans)

class Solution:
    def intToRoman(self, num: int) -> int:
        chars = []
        for r in range(len(romansHighToLow)):
            rom = romansHighToLow[r]
            dec = romansToInt[rom]
            fac = num // dec
            rem = num%dec
            # print(f"num: {num} rom: {rom} dec: {dec} fac: {fac} rem: {rem}")
            if num >= dec:
                for i in range(fac):
                    chars.append(rom)
                num = num - (dec * fac) # rem lol
            
            if rom in romPre.keys():
                aRom = romPre[rom]
                aDec = romansToInt[aRom]
                if(num >= dec-aDec):
                    chars.append(aRom)
                    chars.append(rom)
                    num = num - (dec-aDec)
        return "".join(chars)

