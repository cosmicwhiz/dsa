from collections import defaultdict

def threeSum(nums):
    nums.sort()
    length = len(nums)
    res = []
    prev = [float("inf")]

    for i in range(length-1):
        a = nums[i]
        if a == prev:
            continue
        prev = nums[i]
        l, r = i+1, length-1
        n = -a
        while l < r:
            b, c = nums[l], nums[r]
            if b > n:
                l += 1
                continue
            s = b + c
            if s > n:
                r -= 1
            elif s == n:
                res.append([a, b, c])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            else:
                l += 1
    return res


nums = [0,0,0]
res = threeSum(nums)
print(res)