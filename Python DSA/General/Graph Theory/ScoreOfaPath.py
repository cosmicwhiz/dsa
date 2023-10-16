from collections import defaultdict


def minScore(n, roads):
    graph = defaultdict(list)
    for a, b, d in roads:
        graph[a].append((d, b))
        graph[b].append((d, a))
    
    visited = set()
    q = [1]
    ans = 1e9
    while q:
        node = q.pop(0)
        if node not in visited:
            visited.add(node)
            for d, n in graph[node]:
                ans = min(ans, d)
                q.append(n)
    return ans


n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]
res = minScore(n, roads)
print(res)