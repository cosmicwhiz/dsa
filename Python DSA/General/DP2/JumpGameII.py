def jump(nums):
    length = len(nums)
    memo = [-1]*length
    def dp(i):
        if i >= length:
            return 0
        elif i == length - 1:
            return 1
        elif nums[i] == 0:
            return 0
        futherJumps = set()
        for k in range(nums[i], 0, -1):
            futherJumps.add(dp(i+k))
    return nums 


nums = [2,3,1,1,4]
res = jump(nums)
print(res)