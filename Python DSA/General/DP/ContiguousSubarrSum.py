def checkSubarraySum(nums, k):
    subArrSum = {}
    length = len(nums)

    def dp(i):
        if i >= length-1:
            return False, {nums[i]}
        n = nums[i]
        sums = {n}
        found, sumsArr = dp(i+1)
        if found:
            return True, sums
        for s in sumsArr:
            newSum = n + s
            if newSum % k == 0:
                return True, sums
            sums.add(n+s)
        print(i, sums)
        return found, sums
        
    res = dp(0)[0]
    return res

nums = [23,2,6,4,7]
k = 10
res = checkSubarraySum(nums, k)
print(res)

# found = False
# sums = {n}
# for k in range(i+1, length):
#     found, sumsArr = dp(k)
#     if found:
#         return found, sums
#     for s in sumsArr:
#         curSum = n + s
#         if curSum % k == 0:
#             return True, sums
#         sums.add(curSum)
# subArrSum[i] = sums
# return found, sums