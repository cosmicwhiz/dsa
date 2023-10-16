from collections import Counter, defaultdict

def validSudoku(board):
    columns = defaultdict(set)
    rows = defaultdict(set)
    for row in range(9):
        for col in range(9):
            val = board[row][col]
            if val.isdigit():
                if val in rows[row] or val in columns[col]:
                    return False
                columns[col].add(val)
                rows[row].add(val)
    
    for rs in range(3):
        for cs in range(3):
            rowStart = rs*3
            colStart = cs*3
            valSet = set()
            for i in range(rowStart, rowStart+3):
                for j in range(colStart, colStart+3):
                    val = board[i][j]
                    if val.isdigit():
                        if val in valSet:
                            return False
                        valSet.add(val)
    return True

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","4"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","1","9"]]
res = validSudoku(board)
print(res)