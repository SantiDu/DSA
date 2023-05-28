# leetcode, rt 61%, mu 8%

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
from itertools import zip_longest

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def go(root):
            queue = deque([root])
            while queue:
                queue.append(None)
                for _ in range(len(queue)):
                    node = queue.popleft()
                    yield node
                    if node:
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
        walk = go(root)
        walk2 = go(root)
        for _ in walk2:
            break
        for a, b in zip_longest(walk, walk2):
            if a:
                a.next = b
        return root