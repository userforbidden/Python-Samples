import math

class Solution:
    def maxSubArray(self, nums):
        maxSoFar = nums[0]
        maxEndinghere = nums[0]
        for i in range(len(nums)):
            maxEndinghere = max(maxEndinghere+nums[i],nums[i])
            maxSoFar = max(maxSoFar,maxEndinghere)

        return maxSoFar
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))