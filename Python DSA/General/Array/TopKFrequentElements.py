from collections import Counter

def topKFrequent(nums, k):
    return [k for k, v in sorted(Counter(nums).items(), key=lambda p: -p[1])[:k]]

nums = [3,4,1,4,2,2,2]
k = 2
res = topKFrequent(nums, k)
print(res)