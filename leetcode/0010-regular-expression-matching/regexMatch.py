# https://leetcode.com/problems/regular-expression-matching/

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

from typing import List
# import numpy as np

def isCharMatch(c:str,p:str) -> bool:
    return (c == p or p == ".")

class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        lenP = len(pattern)
        lenS = len(string)
        si=0
        pi=0
        while(pi < lenP and si < lenS):
            c = string[si]
            p = pattern[pi]
            if(pi+1 < lenP and pattern[pi+1] == "*"):
                q = "*"
            else:
                q = ""

            if(isCharMatch(c, p)):
                si+=1
                if(q != "*"):
                    pi+=1
            elif(q == "*" and not isCharMatch(c, p)):
                pi+=2
            else:
                return False
            
        return (si == lenS)
