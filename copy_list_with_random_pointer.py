"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList2(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        head2 = head3 = head
        while head:
            head.next = Node(head.val, head.next)
            head = head.next.next
        while head2 and head2.next:
            if head2.random is None:
                head2.next.random = None
            else:
                head2.next.random = head2.random.next
            head2 = head2.next.next
        beginning = head3 = head3.next
        while head3 and head3.next:
            head3.next = head3.next.next
            head3 = head3.next
        return beginning

    def copyRandomList2(self, head: 'Node') -> 'Node':
        htable = {}
        # first traverse:
        #   copy the linked list,
        #   fill in two dicts.
        count = 0
        previous, ptr, head2 = None, head, None
        while head:
            current_cp = Node(head.val)
            if count == 0:
                head2 = ptr2 = current_cp
            if previous:
                previous.next = current_cp
            htable[head] = current_cp
            previous, head = current_cp, head.next
            count += 1
        # second traverse:
        #   copy the random pointer
        while ptr:                
            if ptr.random is None:
                ptr2.random = None
            else:
                ptr2.random = htable[ptr.random]
            ptr, ptr2 = ptr.next, ptr2.next
        return head2