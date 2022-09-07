# https://leetcode.com/problems/remove-element/

from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenH = len(haystack)
        lenN = len(needle)
        sk = lenN-1 # init ahead
        while(sk < lenH):
            n = lenN-1
            h = sk
            while(n>=0):
                if(needle[n] == haystack[h]):
                    if(n==0):
                        return h
                    n-=1
                    h-=1
                else:
                    sk+=1
                    break
        return -1
        

