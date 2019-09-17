import heapq

def find2ndLargest(nums):
    fmax = -float('inf')
    smax = -float('inf')
    for i in nums:
        if i > fmax: 
            smax = fmax
            fmax = i
        elif i > smax and fmax != i:
            smax = i
        

    print(smax)
    

find2ndLargest([-1,10,10,8,2,4,5,5,6,7,8,8,9])