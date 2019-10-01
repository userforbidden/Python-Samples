import heapq

def find2ndLargest(nums):

    #initialize the two pointers fmax and smax to -inf 

    fmax = -float('inf')
    smax = -float('inf')
    
    #iterate through the list of given numbers
    for i in nums:
        #check if current number is greater than fmax
        # if yes update smax as fmax and update fmax as the current number
        if i > fmax: 
            smax = fmax
            fmax = i
        #else check if the number is greater than smax also check if fmax is not equal to current number
        elif i > smax and fmax != i:
            smax = i
        

    print(smax)

#Time Complexity for this program is O(n) because it passes through all the numbers and n-1 comparisions 
#Space complexity there is no additional Space taken so it is Constant Time 

find2ndLargest([-1,10,10,8,2,4,5,5,6,7,8,8,9])