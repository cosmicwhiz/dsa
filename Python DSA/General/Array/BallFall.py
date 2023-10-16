def findBall(grid):
    res = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(cols):
        cr = 0
        col = i
        while True:
            if cr >= rows:
                res.append(col)
                break
            val = grid[cr][col]
            acVal = col + val
            if acVal < 0 or acVal >= cols or grid[cr][acVal] != val:
                res.append(-1)
                break
            else:
                cr += 1
                col = acVal
    return res


grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
res = findBall(grid)
print(res)