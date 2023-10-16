import heapq
import collections

def findCheapestPrice(t, flights, src, dst, k):
    neighbours = collections.defaultdict(list)
    for i, j, p in flights:
        neighbours[i].append((p, j))
    minHeap = [(0, -1, src)]
    vis = {}
    [vis.setdefault(i, 1e+9) for i in range(t)]
    while minHeap:
        p, stops, s = heapq.heappop(minHeap)
        if s == dst:
            return p
        if vis[s] <= stops:
            continue
        vis[s] = stops
        for neip, nei in neighbours[s]:
            if stops < k:
                heapq.heappush(minHeap, (neip+p, stops+1, nei))
    return -1

flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]

print(findCheapestPrice(11, flights, 0, 2, 4))
