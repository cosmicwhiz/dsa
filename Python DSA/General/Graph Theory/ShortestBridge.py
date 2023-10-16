import heapq
import random

class IslandMaker:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
    
    def isValid(self, row, col):
        return row >= 0 and col >= 0 and row < self.rows and col < self.cols

    def neighbours(self, row, col):
        indices = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        return [(r, c) for r, c in indices if self.isValid(r, c)]

    def getGrid(self):
        grid = []
        for i in range(self.rows):
            row = [0]*self.cols
            grid.append(row)

        availableCells = []
        for i in range(self.rows):
            for j in range(self.cols):
                availableCells.append((i, j))

        visited = set()
        prevSize = 0
        for islands in range(2):
            i, j = random.choice(availableCells)
            q = [(i, j)]
            size = random.randint(1, (self.rows*self.cols)//20)
            while q and len(visited) < size+prevSize:
                # index = random.randint(0, len(q)-1)
                row, col = q.pop()

                # pop the selected cell from both queue and available cells
                # q.pop(q.index((row, col)))
                availableCells.pop(availableCells.index((row, col)))

                grid[row][col] = 1
                visited.add((row, col))
                for r, c in self.neighbours(row, col):
                    if (r, c) not in visited and (r, c) not in q:
                            q.append((r, c))
            prevSize = size
        
        
        return grid


def shortestBridge(grid):    
    rows = len(grid)
    cols = rows
    
    def findLand():
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return (i, j)
    
    def isValid(row, col):
        return row >= 0 and col >= 0 and row < rows and col < cols

    def neighbours(row, col):
        indices = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        return [(r, c) for r, c in indices if isValid(r, c)]

    shoreZeroes = set()

    visited = set()
    def bfs():
        queue = [findLand()]
        while queue:
            row, col = queue.pop()
            visited.add((row, col))
            for r, c in neighbours(row, col):
                if grid[r][c] == 1:
                    if (r, c) not in visited:
                        queue.append((r, c))
                else:
                    shoreZeroes.add((r, c))
    
    bfs()
    newShoreZeroes = set()
    for row, col in shoreZeroes:
        count = 0
        for r, c in neighbours(row, col):
            if (r, c) in visited and grid[r][c] == 1:
                count += 1
        limit = 0
        if row == 0:
            limit += 1
        if col == 0:
            limit += 1
        if count < 4 - limit:
            newShoreZeroes.add((row, col))
    dist = {}
    [dist.setdefault((i, j), 1e+9) for i in range(rows) for j in range(cols)]
    zeroesFlipped = 1e+9

    while newShoreZeroes:
        i, j = newShoreZeroes.pop()
        pq = [(1, i, j)]
        visZeroes = set()
        while pq:
            w, row, col = heapq.heappop(pq)
            if grid[row][col] == 1:
                zeroesFlipped = min(zeroesFlipped, w-1)
                break
            if dist[(row, col)] <= w:
                continue
            dist[(row, col)] = w
            if (row, col) not in visZeroes:
                visZeroes.add((row, col))
                for r, c in neighbours(row, col):
                    if (r, c) not in visZeroes and (r, c) not in visited:
                        if (r, c) in newShoreZeroes:
                            heapq.heappush(pq, (1, r, c))
                        else:
                            heapq.heappush(pq, (w+1, r, c))
    if zeroesFlipped != 1e+9:
        return zeroesFlipped
    
grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,1,1,1,0,0,1,0,0],[1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,0],[1,0,1,1,1,1,1,1,1,0],[1,1,0,1,1,1,1,1,1,1]]
for row in grid:
    print(row)
res = shortestBridge(grid)
print(res)