# https://leetcode.com/problems/zigzag-conversion/

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"

# 1234567890
# 
# 
# 
# 1   5   9
# 2 4 6 8 0
# 3   7
#> 1592468037

# 0 2 4 6
# 1 3 5 7

# 1     7
# 2   6 8
# 3 5   9
# 4     0
#> 17 268 359 40

# 0     6
# 1   5 7
# 2 4   8
# 3     9
#> 0615724839

# rows: 4. (numRows-1)*2 = 6
# mod:4->2: 
# mod:5->1: 6-5
# 


# 4:
#   row = 4+1
#   row = 4 - (4 - 4) - 1


import itertools
# import numpy as np

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for x in range(numRows)]
        for i in range(len(s)):
            row = 0
            if(numRows == 1):
                rows[row].append(s[i])
                print(f"i:{i}, row:{row},si:{s[i]}")
                continue

            mod=i%((numRows-1)*2)
            # row = i % numRows
            if(mod < numRows):
                row = mod
                rows[row].append(s[i])
                print(f"i:{i}, row:{row},si:{s[i]}")
                continue

            rem = (numRows-1)*2
            row = rem - mod
            rows[row].append(s[i])
            print(f"i:{i}, row:{row},si:{s[i]}")

        print(rows)
        chars = itertools.chain.from_iterable(rows)
        return "".join(chars)