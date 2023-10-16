from collections import Counter

def longestConsecutive(nums):
    nums.sort()
    ans, counter = 1, 1
    for i in range(1, len(nums)):
        curr = nums[i]
        prev = nums[i-1]
        if curr - prev == 1:
            counter += 1
        elif curr == prev:
            continue
        else:
            ans = max(ans, counter)
            counter = 1
    return max(ans, counter) if nums else 0

nums = [1,2,0,1]
res = longestConsecutive(nums)
print(res)
    
        