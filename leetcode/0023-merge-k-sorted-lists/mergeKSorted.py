# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

MIN_INT = ((2**31)-1)

class Solution:
    def mergeKLists(self, lists: List[Optional[List]]) -> Optional[List]:
        idx = [0]*len(lists)
        slice = {}
        lengths = []

        # init slice
        for i in range(len(lists)):
            lengths.append(len(lists[i]))
            if(lengths[i] > 0):
                slice[i] = lists[i][idx[i]]

        result = []
        while(sum(lengths) > 0):
            mn = min(slice.values())
            for i in range(len(slice.keys())):
                v = slice[i]
                if v != MIN_INT and mn == v:
                    result.append(v)
                    idx[i] += 1
                    lengths[i] -= 1
                    if lengths[i] > 0:
                        slice[i] = lists[i][idx[i]]
                    else:
                        slice[i] = MIN_INT
                    break
                
        return result



        