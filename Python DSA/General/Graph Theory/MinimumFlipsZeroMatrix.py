import heapq


def isValid(i, j, r, c):
        return i >= 0 and j >= 0 and i < r and j < c

def neighbours(i, j, r, c):
    indices = [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]
    return [(x, y) for x, y in indices if isValid(x, y, r, c)]


def flip(i, j, m, r, c):
    t = []
    for row in m:
        t.append(row.copy())
    t[i][j] = abs(t[i][j]-1)
    for x, y in neighbours(i, j, r, c):
        t[x][y] = abs(t[x][y]-1)
    return t
    
def minFlips(mat):
    r, c = len(mat), len(mat[0])
    q = [(0, mat)]
    visited = set()
    count = 0
    # maxFlips = 0
    while q:
        f, m = heapq.heappop(q)
        if sum(map(sum, m)) == 0:
            return f
        tupleMat = tuple(map(tuple, m))
        if tupleMat in visited:
            # maxFlips = max(f, maxFlips)
            continue
        count += 1
        visited.add(tupleMat)
        for i in range(r):
            for j in range(c):
                newMat = flip(i, j, m, r, c)
                heapq.heappush(q, (f+1, newMat))
                
    return -1


def getMatrices(m, n):
    indices = [(i, j) for i in range(m) for j in range(n)]
    combinations = []
    def dp(c, arr):
        for i in range(len(arr)):
            temp = c.copy()
            temp.append(arr[i])
            combinations.append(temp)
            dp(temp, arr[i+1:])
    
    dp([], indices)
    matrices = []
    for c in combinations:
        mat = [[0]*n for i in range(m)]
        for i, j in c:
            mat[i][j] = 1
        matrices.append(mat)
    return matrices

matrices = getMatrices(2, 4)
validMatrices = []
for m in matrices:
    res = minFlips(m)
    if res != -1:
        validMatrices.append([m, res])
for i,m in enumerate(validMatrices):
    print(i+1,m)
