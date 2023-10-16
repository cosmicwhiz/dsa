import heapq

def swimInWater(grid):
    rows = len(grid)
    cols = rows

    times = {}
    [times.setdefault((r, c), 0) for r in range(rows) for c in range(cols)]
    # print(times)

    def isValid(row, col):
        return row >= 0 and col >= 0 and row < rows and col < cols

    def neighbours(row, col):
        indices = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        return [(r, c) for r, c in indices if isValid(r, c)]

    def bfs():
        pq = [(grid[0][0], 0, 0)]
        visited = set()
        while pq:
            e, row, col = heapq.heappop(pq)
            if (row, col) not in visited:
                visited.add((row, col))
                for r, c in neighbours(row, col):
                    if (r, c) not in visited:
                        ne = grid[r][c]
                        if ne <= e:
                            times[(r, c)] = e
                        else:
                            times[(r, c)] = ne
                        heapq.heappush(pq, (times[(r, c)], r, c))
    bfs()
    return times[(rows-1, cols-1)]


grid = [[0, 2], [1, 3]]
res = swimInWater(grid)
print(res)
