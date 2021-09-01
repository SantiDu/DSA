# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        def go_left(node):
            if node:
                stack.append(node)
                go_left(node.left)
        go_left(root)
        l = []
        while stack:
            node = stack.pop()
            l.append(node.val)
            if node.right:
                go_left(node.right)
        return l
