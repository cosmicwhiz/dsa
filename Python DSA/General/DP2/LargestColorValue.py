from collections import defaultdict


def largestPathValue(colors, edges):
    totalNodes = len(colors)
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
    print(graph)
    visited = set()
    memo = {}
    def dp(n):
        visited.add(n)
        if not graph[n]: return [{colors[n]: 1}]
        if n in memo: return memo[n]
        c = colors[n]
        paths = []
        for n1 in graph[n]:
            if n1 == n: continue
            pathVal = dp(n1)
            for path in pathVal:
                if c not in path:
                    path[c] = 1
                else: path[c] += 1
                paths.append(path)
                print((n, n1),path)
        memo[n] = paths
        return paths

    ans = -1
    for n in range(totalNodes):
        if n not in visited:
            paths = dp(n)
            print(paths)
            for path in paths:
                ans = max(ans, max(path.values()))
    return ans
        
colors = "hhqhuqhqff"
edges = [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]
res = largestPathValue(colors, edges)
print(res)