
from collections import defaultdict


meetings = [[10,8,6],[9,5,11],[0,5,18],[4,5,13],[11,6,17],[0,11,10],[10,11,7],[5,8,3],[7,6,16],[3,6,10],[3,11,1],[8,3,2],[5,0,7],[3,8,20],[11,0,20],[8,3,4],[1,9,4],[10,7,11],[8,10,18]]

adj = defaultdict(list)

for x, y, time in meetings:
    adj[x].append([y, time])
    adj[y].append([x, time])
print(adj)

visited = [False] * 12

def dfs(queue, t):
    u = queue.pop(0)
    if not visited[u]:
        visited[u] = True
    for v, w in adj[u]:
        if not visited[v] and w >= t:
            queue.append(v)
            dfs(queue, w)
dfs([9], 0)
dfs([0], 0)
print([i for i,v in enumerate(visited) if v == True])