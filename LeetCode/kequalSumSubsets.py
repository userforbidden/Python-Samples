def canPartitionKsubsets(nums,k):
    target, rem = divmod(sum(nums), k)
    if rem: return False

    def search(groups):
        if not nums: return True
        v = nums.pop()
        for i, group in enumerate(groups):
            if group + v <= target:
                groups[i] += v
                if search(groups): return True
                groups[i] -= v
            if not group: break
        nums.append(v)
        return False

    nums.sort()
    if nums[-1] > target: return False
    while nums and nums[-1] == target:
        nums.pop()
        k -= 1

    return search([0] * k)
    



print(canPartitionKsubsets([4, 3, 2, 3, 5, 2, 1,0,4],4))