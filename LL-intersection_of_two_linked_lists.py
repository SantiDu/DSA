# leetcode, rt 76%, mu 35%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not (headA and headB):
            return None
        def get_tail_len(head):
            n = 1
            while head.next:
                n += 1
                head = head.next
            return head, n
        tailA, nA = get_tail_len(headA)
        tailB, nB = get_tail_len(headB)
        def walk(head, n):
            while n:
                head = head.next
                n -= 1
            return head
        if tailA is tailB:
            if nA < nB:
                diff = nB - nA
                headB = walk(headB, diff)
                remaining_steps = nA
            elif nA > nB:
                diff = nA - nB
                headA = walk(headA, diff)
                remaining_steps = nB
            else:
                remaining_steps = nA
            for i in range(remaining_steps):
                if headA is headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
        else:
            return None