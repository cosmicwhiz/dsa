def maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])
    
    def isValid(i, j):
        return i >= 0 and j >= 0 and i < rows and j < cols

    def neighbors(i, j):
        indices = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
        return [(row, col) for row, col in indices if isValid(row, col)]

    def bfs(i, j):
        queue = [(i, j)]
        visited = set()
        area = 0
        while queue:
            r, c = queue.pop(0)
            if (r, c) not in visited:
                visited.add((r, c))
                area += 1
                grid[r][c] = 2
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] == 1:
                        queue.append((nr, nc))
        return area

    ans = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                print("Checking")
                ans = max(ans, bfs(row, col))
    return ans


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]
res = maxAreaOfIsland(grid)
print(res)
