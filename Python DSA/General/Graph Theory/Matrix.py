import heapq

def updateMatrix(mat):
    rows, cols = len(mat), len(mat[0])

    def isValid(r, c):
        return r >= 0 and c >= 0 and r < rows and c < cols

    def neighbor(r, c):
        indices = [(r, c-1), (r-1, c), (r, c+1), (r+1, c)]
        return [(i, j) for i, j in indices if isValid(i, j)]
    
    def bfs(i, j):
        q = [(0, i, j)]
        visited = set()
        while q:
            d, r, c = heapq.heappop(q)
            if (r, c) not in visited:
                visited.add((r, c))
                if mat[r][c] == 0:
                    return d
                for nr, nc in neighbor(r, c):
                    heapq.heappush(q, (d+1, nr, nc))

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] != 0:
                mat[i][j] = bfs(i, j)
    
    return mat

mat = [[0,0,1,1],[0,1,1,1],[1,1,1,0]]
for row in mat:
    print(row)
res = updateMatrix(mat)
print(res)