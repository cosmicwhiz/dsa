import heapq

def minStoneSum(piles, k):
    totalStones = sum(piles)
    for i in range(len(piles)):
        piles[i] = -piles[i]
    heapq.heapify(piles)
    count = 0
    stonesRemoved = 0
    while count < k:
        s = -heapq.heappop(piles)
        rm = s // 2
        stonesRemoved += rm
        heapq.heappush(piles, rm-s)
        count += 1
    return totalStones - stonesRemoved

piles = [10000]
k = 10000
res = minStoneSum(piles, k)
print(res)