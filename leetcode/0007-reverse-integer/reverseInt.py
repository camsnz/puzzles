# https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

import itertools

class Solution:
    def reverse(self, x: int) -> int:
        s = f"{x}"
        leng = len(s)
        ult = leng-1

        nsa =[]
        for i in range(leng):
            nsa.append(s[ult - i])
        if s[0] == "-":
            ns = "-" + "".join(nsa[0:ult])
        else:
            ns = "".join(nsa)
        
        max = f"{((2**31)-1)}"
        min = f"{((-2**31))}"

        if(ns[0] == "-"):
            print("n>", min, ns)
            if(len(ns) > len(min)):
                return 0
            elif(len(ns) == len(min)):
                for i in range(1,leng):
                    if(int(ns[i]) > int(min[i])):
                        return 0
                    if(int(ns[i]) < int(min[i])):
                        break
        else:
            if(len(ns) > len(max)):
                return 0
            elif(len(ns) == len(max)):
                for i in range(leng):
                    if(int(ns[i]) > int(max[i])):
                        return 0

        return int(ns)
