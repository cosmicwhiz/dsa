import heapq

def shortestPath(grid, k):
    rows = len(grid)
    cols = len(grid[0])

    def isValid(x, y):
        return x >= 0 and y >= 0 and x < rows and y < cols

    def neighbors(x, y):
        w = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        res = []
        for i, j in w:
            if isValid(i, j):
                res.append((i, j))
        return res

    pq = [(0, 0, 0, 0)]
    visited = {}
    wallBreak = {}
    totalWalls = rows*cols

    [visited.setdefault((i, j), 1e+9) for i in range(rows) for j in range(cols)]
    [wallBreak.setdefault((i, j), totalWalls) for i in range(rows) for j in range(cols)]
    while pq:
        u, wb, row, col = heapq.heappop(pq)
        if row == rows-1 and col == cols-1:
            return u
        if visited[(row, col)] <= u and wallBreak[(row, col)] <= wb:
            continue
        visited[(row, col)] = u
        wallBreak[(row, col)] = wb
        for r, c in neighbors(row, col):
            if grid[r][c] == 1:
                if wb < k:
                    heapq.heappush(pq, (u+1, wb+1, r, c))
            else:
                heapq.heappush(pq, (u+1, wb, r, c))
    return -1

grid = [[0,1,0,0,0,1,0,0],
        [0,1,0,1,0,1,0,1],
        [0,0,0,1,0,0,1,0]]
k = 1
res = shortestPath(grid, k)
print(res)