def numIslands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def isValid(x, y):
        return x >= 0 and y >= 0 and x < rows and y < cols

    def neighbors(x, y):
        w = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        res = []
        for i, j in w:
            if isValid(i, j) and (i, j) not in visited:
                res.append((i, j))
        return res

    def bfs(i, j):
        queue = [(i, j)]
        visited.add((i, j))
        while queue:
            x, y = queue.pop(0)
            for row, col in neighbors(x, y):
                if grid[row][col] == "1":
                    queue.append((row, col))
                    visited.add((row, col))

    totalIslands = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                if grid[i][j] == "1":
                    bfs(i, j)
                    totalIslands += 1
    return totalIslands

def numberOfIslands(grid):
    rows, cols = len(grid), len(grid[0])
    
    def isValid(i, j):
        return i >= 0 and j >= 0 and i < rows and j < cols

    def neighbors(i, j):
        indices = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
        return [(row, col) for row, col in indices if isValid(row, col)]

    def bfs(i, j):
        queue = [(i, j)]
        visited = set()
        while queue:
            r, c = queue.pop(0)
            if (r, c) not in visited:
                visited.add((r, c))
                grid[r][c] = "2"
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] == "1":
                        queue.append((nr, nc))

    ans = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                bfs(row, col)
                ans += 1
    return ans

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

res = numberOfIslands(grid)
print(res)