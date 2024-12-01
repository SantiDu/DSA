# leetcode, rt 95%, mu 87%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        
        queue = deque()
        queue.append(root)
        queue.append(None)
        
        levels = [[root.val]]
        l = []
        
        while len(queue) != 1:
            node = queue.popleft()
            if node is None:
                levels.append(l)
                l = []
                queue.append(None)
            else:
                if node.left:
                    queue.append(node.left)
                    l.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    l.append(node.right.val)
        return levels