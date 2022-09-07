# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def make(self, *vals:int):
        head = ListNode()
        tail = head
        for i, v in enumerate(vals):
            tail.next = ListNode(v)
            tail = tail.next
        return head.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if(list1.val > list2.val):
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        head.next = None
        tail = head

        while(list1 != None and list2 != None):
            if(list1.val > list2.val):
                # tmp = list2.next
                tail.next = list2
                tail = tail.next
                list2 = list2.next
                tail.next = None
            else:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
                tail.next = None
        
        return head
        

ln = ListNode()
# l2 = ListNode()
l1 = ln.make(1,2,4)
l2 = ln.make(1,3,4)

def printList(list:ListNode):
    while(list != None):
        print(list.val)
        list = list.next

printList( Solution.mergeTwoLists(Solution, l1, l2) )