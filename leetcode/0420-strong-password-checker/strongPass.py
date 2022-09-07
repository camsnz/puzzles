# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

# It has at least 6 characters and at most 20 characters.
# It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        

        shortBy = 6 - len(password)
        hasUpper = password