
def showGrid():
    intToSymbol = {-1e9: '-', 1e9: '  W'}
    for r in range(rows):
        print('[', end='') 
        for c in range(cols):
            val = grid[r][c]
            if val in intToSymbol: print(intToSymbol[val], end='  ' if c < cols-1 else '')
            else: print(round(val, 2), end='  ' if c < cols-1 else '')
        print(']')

def rewards(grid, rewardPoints, discountRate):
    rows, cols = len(grid), len(grid[0])

    def isNotWall(row, col):
        return grid[row][col] != 1e9

    def isValid(row, col):
        return row >= 0 and col >= 0 and row < rows and col < cols and isNotWall(row, col)
    
    def neighbor(row, col):
        indices = [(row, col-1), (row-1, col), (row, col+1), (row+1, col)]
        return [(r, c) for r, c in indices if isValid(r, c)]

    def bfs(si, sj, sval):
        queue = [(si, sj, sval)]
        
        while queue:
            i, j, val = queue.pop(0)
            if (i, j) in visited and grid[i][j] >= val:
                continue
            visited.add((i, j))
            grid[i][j] = val

            for ni, nj in neighbor(i, j):
                queue.append((ni, nj, rewardPoints + discountRate*val))
    
    nodeCells = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != -1e9 and grid[i][j] != 1e9:
                nodeCells.append((i, j, grid[i][j]))

    visited = set()
    for i, j, val in nodeCells:
        if grid[i][j] <= val:
            bfs(i, j, val)

rows, cols = 6, 6
grid = [[-1e9]*cols for _ in range(rows)]

# Termination states
grid[0][5] = 5
grid[2][0] = 4
grid[-1][-1] = -1

# Walls
wallIndices = [(2, 1), (3, 1), (3, 3), (3, 4), (3, 5)]
for i, j in wallIndices:
    grid[i][j] = 1e9

print('-----------Initial Grid-----------------')
showGrid()
print('\n\n----------------Rewards Grid---------------')
res = rewards(grid, rewardPoints=0, discountRate=0.9)

# Reset the termination states
grid[0][5] = round(5.00, 2)
grid[2][0] = round(4.00, 2)
grid[-1][-1] = round(-1.00, 2)
showGrid()