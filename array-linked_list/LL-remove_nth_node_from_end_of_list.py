# leetcode, rt 98%, mu 48%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1 = ptr2 = head
        previous = None
        for i in range(n):
            try:
                ptr2 = ptr2.next
            except AttributeError:
                return head
        while ptr2:
            if previous is None:
                previous = head
            else:
                previous = previous.next
            ptr1, ptr2 = ptr1.next, ptr2.next
        if previous is None:
            return ptr1.next
        else:
            previous.next = ptr1.next
            return head