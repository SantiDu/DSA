# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        
        def go(root):
            stack = [root]
            left_to_right = True
            while stack:
                yield [node.val for node in stack]
                stack2 = []
                left_to_right = not left_to_right
                for _ in range(len(stack)):
                    node = stack.pop()
                    if left_to_right:
                        if node.left:
                            stack2.append(node.left)
                        if node.right:
                            stack2.append(node.right)
                    else:
                        if node.right:
                            stack2.append(node.right)
                        if node.left:
                            stack2.append(node.left)
                stack = stack2
        return [level for level in go(root)]