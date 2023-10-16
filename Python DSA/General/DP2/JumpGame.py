def jump(nums):
    length = len(nums)
    memo = {}
    def dp(i):
        if i == length-1:
            return True
        elif i >= length or nums[i] == 0:
            return False
        if i in memo:
            return memo[i]
        canJump = False
        for k in range(1, nums[i]+1):
            memo[i]= dp(i+k) or canJump
            if memo[i]:
                break   
        return memo[i]
    return dp(0)

nums = [3,2,2,0,4]
res = jump(nums)
print(res)
