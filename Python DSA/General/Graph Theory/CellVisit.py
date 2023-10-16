import heapq

def minimumTime(grid):
    rows, cols = len(grid), len(grid[0])
    def isValid(i, j):
        return i >= 0 and j >= 0 and i < rows and j < cols

    def neighbors(i, j):
        indices = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
        return [(row, col) for row, col in indices if isValid(row, col)]

    fN = [grid[r][c] for r, c in neighbors(0, 0)]
    if 1 in fN or 0 in fN:
        minHeap = [(0, 0, 0)]
        visited = {}
        [visited.setdefault((r, c), 1e9) for r in range(rows) for c in range(cols)] 
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == rows -1 and c == cols - 1:
                return t
            if visited[(r, c)] <= t:
                continue
            visited[(r, c)] = t
            for nr, nc in neighbors(r, c):
                nt = grid[nr][nc]
                if nt <= t+1:
                    heapq.heappush(minHeap, (t+1, nr, nc))
                elif (nt+t) % 2 != 0:
                    heapq.heappush(minHeap, (nt+2, nr, nc))
                else:
                    heapq.heappush(minHeap, (nt+1, nr, nc))
        return -1
    return -1
    

grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
res = minimumTime(grid)
print(res)