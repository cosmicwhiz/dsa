def modifyBoard(board):
    rows, cols = len(board), len(board[0])

    def isValid(i, j):
        return i >= 0 and j >= 0 and i < rows and j < cols

    def neighbors(i, j):
        indices = [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
        return [(row, col) for row, col in indices if isValid(row, col)]

    def bfs(i, j):
        queue = [(i, j)]
        visited = set()
        canBeSurrounded = True
        while queue:
            r, c = queue.pop(0)
            if (r, c) not in visited:
                visited.add((r, c))
                adjacent = neighbors(r, c)
                if len(adjacent) < 4:
                    canBeSurrounded = False
                for nr, nc in adjacent:
                    if board[nr][nc] == "O":
                        queue.append((nr, nc))
        if canBeSurrounded:
            for r, c in visited:
                board[r][c] = "X"
        else:
            for r, c in visited:
                board[r][c] = "-"

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "O":
                bfs(row, col)

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "-":
                board[row][col] = "O"

    return board


board = [
    ["X","X","X","X"],
    ["X","O","O","O"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]

res = modifyBoard(board)
print(res)