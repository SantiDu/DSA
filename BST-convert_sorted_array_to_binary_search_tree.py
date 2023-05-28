# leetcode, rt 9%, mu 60%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createNode(nums):
            if nums:
                i = len(nums) // 2
                tn = TreeNode(nums[i])
                tn.left = createNode(nums[:i])
                tn.right = createNode(nums[i+1:])
                return tn
            else:
                return None
        return createNode(nums)
