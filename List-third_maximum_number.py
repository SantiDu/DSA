from math import inf

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -inf
        for i in nums:
            if i > max1:
                max1, max2, max3 = i, max1, max2
            elif max2 < i < max1:
                max2, max3 = i, max2
            elif max3 < i < max2:
                max3 = i
        if max3 == -inf:
            return max1
        else:
            return max3