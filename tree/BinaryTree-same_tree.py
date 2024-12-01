# leetcode, rt 96%, mu 31%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import zip_longest
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def walk(node):
            if node:
                yield node.val
                if node.left:
                    yield from walk(node.left)
                else:
                    yield None
                if node.right:
                    yield from walk(node.right)
                else:
                    yield None
            else:
                yield None
        for a, b in zip_longest(walk(p), walk(q)):
            if a is None and b is None:
                continue
            elif a == 0 and b == 0:
                continue
            elif not (a and b and a == b):
                return False
        return True