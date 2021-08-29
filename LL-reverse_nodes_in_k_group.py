# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # move ptr2 to tail
        ptr2 = head
        for i in range(k - 1):
            if ptr2:
                ptr2 = ptr2.next
            else:
                return head
        # preserve beginning
        beginning = ptr2
        # reverse, move ptr2 at the same time
        def reverse(head, ptr2):
            k2 = 0 # n of ptr2 moved
            tail, head_nxt_group = head, ptr2.next
            previous = None
            for i in range(k):
                # exchange link direction
                next_ = head.next
                head.next = previous
                previous, head = head, next_
                # move ptr2
                if ptr2:
                    ptr2 = ptr2.next
                    k2 += 1
            if ptr2:
                go_further = True
                tail.next = ptr2
            else:
                if k2 > 0:
                    go_further = False
                    tail.next = head_nxt_group
                else:
                    go_further = True
                    tail.next = ptr2
            return head_nxt_group, ptr2, go_further
        # run
        go_further = True
        while go_further:
            head, ptr2, go_further = reverse(head, ptr2)            
        return beginning
