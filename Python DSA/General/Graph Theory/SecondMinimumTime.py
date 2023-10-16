from collections import defaultdict
from heapq import heappush, heappop

def secondMinimum(n, edges, time, change):
    links = defaultdict(list)
    for a, b in edges:
        links[a].append(b)
        links[b].append(a)

    queue = [(0, 1)]
    visited = defaultdict(int)
    while queue:
        t, node = heappop(queue)
        if visited[node] < 2:
            visited[node] += 1
            if node == n and visited[node] == 2:
                return t
            blink = t // change
            if blink % 2:
                t = change*(blink+1)
            for nr in links[node]:
                heappush(queue, (t+time, nr))


edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
n = 5
time = 3
change = 5
res = secondMinimum(n, edges, time, change)
print(res)