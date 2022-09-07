# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        count=0
        while i < len(nums):
            v = nums[i]
            if v == val:
                nums[i] = nums[j]
                nums[j] = None
                j-=1
            else:
                count+=1
                i+=1
            if i>j:
                break
        # print(count,i)
        return { count: nums }
            

        