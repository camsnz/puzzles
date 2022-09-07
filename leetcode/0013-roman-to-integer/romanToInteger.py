# https://leetcode.com/problems/roman-to-integer/

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

romans = dict()
romans['I'] = 1
romans['V'] = 5
romans['X'] = 10
romans['L'] = 50
romans['C'] = 100
romans['D'] = 500
romans['M'] = 1000
# order = ['I','V','X','L','C','D','M']

class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        mter = iter(s)
        for i, c in enumerate(mter):
            # c = s[i]
            nextC = ''
            if (i+1 < len(s)):
                nextC = s[i+1]

            # orderIdx = order.index(c)
            if(
                (c == 'I' and nextC in ['V','X']) or
                (c == 'X' and nextC in ['L','C']) or
                (c == 'C' and nextC in ['D','M'])
            ):
                count += romans[nextC] - romans[c]
                # i=i+2
                mter.__next__()
                # yield i+2
            else:
                count += romans[c]
            # print(f"{i} {c} {count}")
            # yield i+1
        return count

print(Solution.romanToInt(Solution, "I"))
print(Solution.romanToInt(Solution, "II"))
print(Solution.romanToInt(Solution, "III"))
print(Solution.romanToInt(Solution, "IV"))
print(Solution.romanToInt(Solution, "VI"))
print(Solution.romanToInt(Solution, "VII"))
print(Solution.romanToInt(Solution, "VIII"))
print(Solution.romanToInt(Solution, "IX"))
print(Solution.romanToInt(Solution, "X"))
print(Solution.romanToInt(Solution, "XI"))
print(Solution.romanToInt(Solution, "XII"))
print(Solution.romanToInt(Solution, "XIII"))
print(Solution.romanToInt(Solution, "XIV"))
print(Solution.romanToInt(Solution, "XV"))
print(Solution.romanToInt(Solution, "XVI"))
print(Solution.romanToInt(Solution, "XVII"))
print(Solution.romanToInt(Solution, "XVIII"))

