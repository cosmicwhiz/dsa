def f(i, houses, dp):
    if i < 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    maxAmt = houses[i]
    for j in range(2, i+1):
        amt = f(i-j, houses, dp) + houses[i]
        maxAmt = max(maxAmt, amt)
    dp[i] = maxAmt
    return maxAmt

def rob(nums):
    length = len(nums)
    if length == 1:
        return nums[0]
    dp = [-1]*length
    return max(f(length-1, nums, dp), f(length-2, nums, dp))

def robAdj(nums):
    length = len(nums)
    if length == 1:
        return nums[0]
    dp = [-1]*length
    dp[0] = nums[0]
    dp[1] = nums[1]
    for i in range(2, length):
        take = nums[i] + dp[i-2]
        notTake = dp[i-1]
        dp[i] = max(take, notTake)
    return dp[length-1]

def robOptimized(nums):
    length = len(nums)
    dp = [-1]*length
    def fn(i):
        if i == 0:
            return nums[0]
        elif i < 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        pick = nums[i] + fn(i-2)
        notPick = fn(i-1)
        dp[i] = max(pick, notPick)
        return dp[i]
    return fn(length-1)

nums = [2,7,9,3,1,4,5,2]
res = robAdj(nums)
print(res)