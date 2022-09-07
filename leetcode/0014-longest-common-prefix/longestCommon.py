# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return 0
        first = strs[0]
        maxx = len(first)
        for i, s in enumerate(strs, 1):
            j=0
            while((j < max(len(first), len(s))) and s[j] == first[j]):
                j+=1
            if(j < maxx):
                maxx = j
        
        return first[0:maxx]


print(Solution.longestCommonPrefix(Solution, ["test","tester","tessa"]))
