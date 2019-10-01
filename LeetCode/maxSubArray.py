import math

class Solution:
    def maxSubArray(self, nums):
        maxstartingIndex = -1
        maxEndgingIndex = -1

        maxSoFar = 0
        maxEndinghere = 0
        currstart = 0 
        
        for i in range(len(nums)):
            maxEndinghere += nums[i]

            if maxEndinghere < 0:
                maxEndinghere = 0 
                currstart = i+1
            if maxEndinghere > maxSoFar:
                maxSoFar = maxEndinghere
                maxstartingIndex = currstart
                maxEndgingIndex = i

            # maxEndinghere = max(maxEndinghere+nums[i],nums[i])
            # maxSoFar = max(maxSoFar,maxEndinghere)

        return maxSoFar,maxstartingIndex,maxEndgingIndex
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))