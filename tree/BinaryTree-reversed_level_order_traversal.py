# leetcode, rt 62%, mu 85%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        
        levels = [[root]]
        
        while l := levels[-1]:
            next_level = []
            for node in l:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            levels.append(next_level)
        
        return [[node.val for node in l] for l in levels[:-1].__reversed__()]