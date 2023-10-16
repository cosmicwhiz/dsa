# import heapq

# class MedianFinder:

#     def __init__(self):
#         self.nums = []
#         self.length = 0

#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.nums, num)
#         self.length += 1

#     def findMedian(self) -> float:
#         if self.length:
#             temp = self.nums.copy()
#             start = 0
#             i = self.length // 2
#             if self.length % 2 == 0:
#                 while start < i-1:
#                     heapq.heappop(temp)
#                     start += 1
#                 a = heapq.heappop(temp)
#                 b = heapq.heappop(temp)
#                 return (a+b) / 2
#             while start < i:
#                 heapq.heappop(temp)
#                 start += 1
#             return heapq.heappop(temp)
    
# mf = MedianFinder()
# for i in range(-1, -6, -1):
#     mf.addNum(i)
#     print(mf.nums)
#     med = mf.findMedian()
#     print(med)
import math

def minEatingSpeed(piles, h):
    def canEatSafely(rate):
        return sum([math.ceil(p / rate) for p in piles]) <= h

    lower, upper = 1, max(piles)
    while lower < upper:
        rate = (upper+lower) // 2
        if canEatSafely(rate):
            upper = rate
        else:
            lower = rate + 1
    return lower

piles = [440]
h = 439
res = minEatingSpeed(piles, h)
print(res)
piles = [540]
h = 539
res = minEatingSpeed(piles, h)
print(res)