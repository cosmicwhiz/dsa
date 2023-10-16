import heapq
import collections
import sys

def networkTimeDelay(times, n, k):
    neighbours = collections.defaultdict(list)
    for u, v, w in times:
        neighbours[u].append((w, v))
    
    minHeap = [(0, k)]
    visited = set()
    minTime = 0

    while minHeap:
        curT, src = heapq.heappop(minHeap)
        if src in visited:
            continue
        minTime = max(minTime, curT)
        visited.add(src)
        for t, dst in neighbours[src]:
            if dst not in visited:
                heapq.heappush(minHeap, [curT+t, dst])
    
    if len(visited) == n:
        return minTime
    return -1


times = [[1,2,1],[2,3,2],[1,3,2]]
n = 3
k = 1
res = networkTimeDelay(times, n, k)
print(res)