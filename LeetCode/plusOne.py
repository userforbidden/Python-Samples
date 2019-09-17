#recursive 
def plusOne(nums,k):
    if not nums:
        return [1]

    elif nums[-1] == 9:
        q,r = divmod((nums[-1] + k),10)
        return plusOne(nums[:-1],q) + [r]
    
    nums[-1] = nums[-1] + 1

    return nums

intarr = [2,1,4,7,4,8,3,6,4,9,9]
intarr2 = [9,9,9,9,9,9,9,9,9,9]
k = 55
# Simple approach
strarr = int(''.join(map(str,intarr2))) + k
print(list(map(int,list(str(strarr)))))

print(plusOne(intarr2,k))