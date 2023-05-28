# leetcode, rt 75%, mu 73%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        is_1st = True
        while l1 or l2:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            val = val1 + val2 + carry
            if is_1st:
                head = head2 = ListNode(val % 10)
                is_1st = False
            else:
                head2.next = ListNode(val % 10)
                head2 = head2.next
            carry = val // 10
        if carry:
            head2.next = ListNode(carry)
        return head