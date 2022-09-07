# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        leng = len(s)
        if (leng <= 1):
            return True
        if s[0] == s[leng-1]:
            return self.isPalindrome(self, int(s[1:leng-1]))


# def isPalindrome(s: str) -> bool:
#     j = len(s)
#     for i in range(len(s)):
#         j=j-1
#         if(i >= j):
#             # print("isPal",s)
#             return True
#         if(s[i] != s[j]):
#             return False
#     return None
