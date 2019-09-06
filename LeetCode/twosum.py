import itertools 

class Solution:
    def __init__(self):
        self.result = []

    def twoSum(self, nums, target):
        # for x, y in list(itertools.combinations(enumerate(nums), 2)):

        #     if x[1]+y[1] == target:
        #         self.result.append(x[0])
        #         self.result.append(y[0])
        doc = {}
        for i in range(len(nums)):
            if target-nums[i] not in doc:
                doc[nums[i]] = i
            else:
                return [ doc[target-nums[i]] , i ]
            print(doc)
        # print(set(self.result))


nums = [2,7,11,2]
# print(Solution().twoSum(nums,9))
Solution().twoSum(nums,9)