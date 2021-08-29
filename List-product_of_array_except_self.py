class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]
        for i in nums[:-1]:
            product.append(product[-1] * i)
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= right
            right *= nums[i]
        return product