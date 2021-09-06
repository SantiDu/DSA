# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def go(node):
            if node:
                yield str(node.val)
                if node.right is not None and node.left is None:
                    yield "()"
                if node.left:
                    yield "("
                    yield from go(node.left)
                    yield ")"
                if node.right:
                    yield "("
                    yield from go(node.right)
                    yield ")"
        return "".join(go(root))