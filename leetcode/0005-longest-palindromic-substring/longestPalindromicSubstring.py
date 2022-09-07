# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

def isPalindrome(s: str) -> bool:
    j = len(s)
    for i in range(len(s)):
        j=j-1
        if(i >= j):
            # print("isPal",s)
            return True
        if(s[i] != s[j]):
            return False
    return None


def rev(s:str,n:int)->InterruptedError:
    return len(s)-(n+1)

# aba

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pals = []
        for i in range(len(s)):
            for j in range(len(s)):
                b = rev(s,j)

                pal = s[i:b+1]
                if(isPalindrome(pal)):
                    if(len(pals) == 0):
                        pals.append(pal)
                    elif(len(pals[0]) < len(pal)):
                        pals.clear()
                        pals.append(pal)
                    elif(len(pals[0]) == len(pal)):
                        pals.append(pal)
                    break

                # print(f"a {a}, b {b}, pal {[pal]}")
                # if(b <= a+1):
                #     print("b<=a:",i,rev(s,j),pal)
                #     if(len(pals) == 0):
                #         print("new",pal)
                #         pals.append(pal)
                #     elif(len(pals[0]) == j-i):
                #         print("equal",pal)
                #         pals.append(pal)
                #     elif(len(pals[0]) < j-i):
                #         print("greater",pal)
                #         pals.clear()
                #         pals.append(pal)
                #     break
                
        return pals

# match ends, increase each until fault or equal idx's