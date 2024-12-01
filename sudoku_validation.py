def is_valid(board, row, col):
    now = board[row][col]
    for i in range(9):
        # row
        if now == board[row][i]:
            if col == i: continue
            return False
        # col
        if now == board[i][col]:
            if row == i: continue
            return False
    # Grid
    bigRow = row // 3 * 3
    bigCol = col // 3 * 3
    for r in range(bigRow, bigRow + 3):
        for c in range(bigCol, bigCol + 3):
            if now == board[r][c]:
                if row == r and col == c: continue
                return False
    return True


def helper(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] != '.':
                if not is_valid(board, row, col):
                    return False

    return True


board = [
        ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
        ]

print(helper(board))
