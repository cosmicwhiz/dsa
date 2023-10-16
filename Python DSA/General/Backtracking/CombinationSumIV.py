def combinationSum(nums, target):
    def backtrack(start, arr, s, length):
        if s == target:
            res[0] += 1
            return
        elif s > target:
            return
        
        for i in range(start, length):
            arr.append(nums[i])
            backtrack(start, arr, s+nums[i], length)
            arr.pop()
    
    res = [0]
    backtrack(0, [], 0, len(nums))
    return res[0]


nums = [1,2,3,6,5,9,7]
target = 40
ans = combinationSum(nums, target)
print(ans)