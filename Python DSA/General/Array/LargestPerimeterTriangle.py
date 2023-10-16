import random

def largestPerimeter(nums):
    nums.sort(key=lambda k: -k)
    print(nums)
    target = nums[0]
    for i in range(1, len(nums)-1):
        pairSum = nums[i] + nums[i+1]
        if pairSum > target:
            return pairSum+target
        target = nums[i]
    return 0

nums = [3, 6, 2, 3]
print(largestPerimeter(nums))
