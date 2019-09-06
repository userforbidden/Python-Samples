import heapq

def find2ndLargest(nums):
    lnums = nums
    heapq.heapify(lnums)
    print(heapq.nlargest(2,lnums)[1])
    

find2ndLargest([2,4,5,5,6,7,8,8,9])