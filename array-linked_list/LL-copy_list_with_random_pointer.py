# leetcode, rt 87%, mu 44%

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
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