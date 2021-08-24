# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = 1
        tail = head
        while next_ := tail.next:
            tail = next_
            n += 1
        k %= n
        if k == 0:
            return head
        head2 = head
        steps = n - k
        for i in range(steps - 1):
            head = head.next
        beginning = head.next
        head.next = None
        tail.next = head2
        return beginning
        