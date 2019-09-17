
def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        
        for i in range(0,(len(nums)-3)):
            if i == 0 or nums[i] >= nums[i-1]:
                start = i + 1
                end = len(nums) - 1

                while (start < end):
                    if nums[i] + nums[start] + nums[end] == 0:
                        result.append([nums[i] ,nums[start] ,nums[end]])
                    if nums[i] + nums[start] + nums[end] < 0:
                        curStart = start
                        while(nums[start] == nums[curStart] and start < end ):
                            start += 1
                    else:
                        curEnd = end
                        while(nums[end] == nums[curEnd] and start < end):
                            end -= 1
                            
        print(result)

threeSum([0,0,0])