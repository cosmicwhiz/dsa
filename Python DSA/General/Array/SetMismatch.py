def setMismatch(nums):
    l = len(nums)
    nums.sort()
    dup = 0
    for i in range(1, l):
        n = nums[i]
        if n == nums[i-1]:
            dup = nums.pop(i)
            break
    for i in range(l-1):
        n = nums[i]
        if n != i+1:
            return [dup, i+1]
    return [dup, l]

nums = [1,1]
res = setMismatch(nums)
print(res)