import random


def minFallingPathSum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    memo = {}
    def fallPath(i, j):
        if i >= rows:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        curVal = matrix[i][j]
        if j == 0:
            memo[(i, j)] = curVal + min(fallPath(i+1, j),
                            fallPath(i+1, j+1))
        elif j == rows-1:
            memo[(i, j)] = curVal + min(fallPath(i+1, j-1),
                            fallPath(i+1, j))
        else:
            memo[(i, j)] = curVal + min(fallPath(i+1, j-1),
                            fallPath(i+1, j),
                            fallPath(i+1, j+1))
        return memo[(i, j)]
        
    res = float("inf")
    for j in range(cols):
        res = min(res, fallPath(0, j))
    return res


nums = []
rows, cols = 50, 50
for k in range(320):
    length = rows*cols
    for i in range(1, rows*cols+1):
        nums.append(i)
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            index = random.randint(0, length-1)
            row.append(nums[index])
            nums.pop(index)
            length -= 1
        matrix.append(row)
    # for row in matrix:
    #     print(row)
    res = minFallingPathSum(matrix)
    print(res)