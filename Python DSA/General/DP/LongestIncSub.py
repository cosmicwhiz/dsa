import random
import sys

sys.setrecursionlimit(10000)
def lengthOfLISSol(nums):
    lis = [1]*len(nums)
    i = len(nums) - 2
    while i >= 0:
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                lis[i] = max(lis[i], 1 + lis[j])
        i -= 1
    return max(lis)

def lengthOfLIS(nums):
    totalNums = len(nums)-1
    lis = {}
    [lis.setdefault(i, 1) for i in range(totalNums+1)]

    def dp(index):
        if index == totalNums:
            lis[index] = 1
            return [(lis[index], nums[index])]

        val = nums[index]
        subArr = dp(index+1)
        for l, n in subArr:
            if val < n:
                lis[index] = l + 1
                break
        else:
            lis[index] = 1
        subArr.append((lis[index], val))
        return sorted(subArr, key=lambda p: (-p[0], p[1]))
        
    res = dp(0)
    return res[0][0]

totalTests = 1000
testsPassed = 0
for test in range(totalTests):
    totalNums = random.randint(50, 100)
    nums = []
    for i in range(totalNums):
        num = random.randint(-10, 10)
        nums.append(num)
    print(nums)
    if lengthOfLISSol(nums) == lengthOfLIS(nums):
        testsPassed += 1
    else:
        break

print(f'Tests Passed: {testsPassed}/{totalTests}')
