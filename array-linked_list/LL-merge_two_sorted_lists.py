# leetcode, rt 48%, mu 86%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:   
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l2
        previous = None
        while l1:
            if l2 and l2.val <= l1.val:
                temp = l2.next
                l2.next = l1
                if previous:
                    previous.next = l2
                previous, l2 = l2, temp
            else:
                if previous is None:
                    head = l1
                previous, l1 = l1, l1.next
        if previous:
            previous.next = l2
        return head