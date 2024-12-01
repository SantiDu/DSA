# leetcode, rt 52%, mu 18%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return None
        
        s = 0
        stack = []
        
        def go_left(node):
            while node:
                stack.append(node)
                node = node.left

        go_left(root)
    
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                s += node.val
            elif node.val > high:
                return s
            go_left(node.right)

        return s