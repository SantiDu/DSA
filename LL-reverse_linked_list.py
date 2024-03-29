# leetcode, rt 65%, mu 77%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        while head:
            next_ = head.next
            head.next = previous
            previous, head = head, next_
        return previous