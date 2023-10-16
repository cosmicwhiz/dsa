def allPathsSourceTarget(graph):
    lastNode = len(graph)-1
    paths = []
    def dfs(n, path):
        if n == lastNode:
            paths.append(path.copy())
            return
        for nei in graph[n]:
            path.append(nei)
            dfs(nei, path)
            path.pop()

    dfs(0, [0])
    return paths


graph = [[4,3,1],[3,2,4],[3],[4],[]]
res = allPathsSourceTarget(graph)
print(res)