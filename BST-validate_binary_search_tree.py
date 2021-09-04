# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        walk = inorder(root)
        walk2 = inorder(root)
        for _ in walk:
            break
        for a, b in zip(walk, walk2):
            if a <= b:
                return False
        return True