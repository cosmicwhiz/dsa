import heapq

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])

    def isValid(i, j):
        return i >= 0 and j >= 0 and i < rows and j < cols

    def neighbors(i, j):
        indices = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
        return [(row, col) for row, col in indices if isValid(row, col)]
    
    freshOranges = 0
    rottenIndices = []
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                rottenIndices.append((row, col))
            elif grid[row][col] == 1:
                freshOranges += 1
    
    queue = []
    for row, col in rottenIndices:
        for nr, nc in neighbors(row, col):
            if grid[nr][nc] == 1:
                queue.append((1, nr, nc))

    visited = set()
    ans = 0
    while queue:
        t, r, c = heapq.heappop(queue)
        if (r, c) not in visited:
            ans = max(t, ans)
            visited.add((r, c))
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    heapq.heappush(queue, (t+1, nr, nc))

    if len(visited) < freshOranges:
        return -1
    return ans


grid = [[0,2]]
res = orangesRotting(grid)
print(res)