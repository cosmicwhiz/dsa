from collections import Counter

def f(i, nums, dp):
    if i < 0: return [[]]
    if dp[i]: return dp[i]
    notAdd = f(i-1, nums, dp)
    add = []
    for sub in notAdd:
        arr = sub.copy()
        arr.append(nums[i])
        add.append(arr)
    dp[i] = add + notAdd
    return dp[i]

def subsets(nums):
    length = len(nums)
    dp = [[]]*length
    return f(length-1, nums, dp)

nums = [4,4,4,1,4]
res, ctr = [], []
for arr in subsets(nums):
    c = Counter(tuple(arr))
    if c not in ctr:
        ctr.append(c)
        res.append(arr)
print(res)