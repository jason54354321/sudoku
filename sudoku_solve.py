
import time

def is_valid(board, row, col, now):
    now = str(now)
    # print(f"trying {now} at: [{row}][{col}]")
    print_board(board)
    for i in range(9):
        if i != col and board[row][i] == now:
            return False
    for i in range(9):
        if i != row and board[i][col] == now:
            return False
    gridRow = row // 3 * 3
    gridCol = col // 3 * 3
    for gRow in range(gridRow, gridRow+3):
        for gCol in range(gridCol, gridCol+3):
            if row != gRow and col != gCol and board[gRow][gCol] == now:
                return False
    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                for n in range(1, 10):
                    print("")
                    board[row][col] = str(n)
                    if is_valid(board, row, col, n):
                        if solve_sudoku(board):
                            return True
                    else:
                        board[row][col] = '.'
                return False
    return True


def print_board(board):
    print("\033c", end="")  # \033c means ANSI escape code, flush the whole screen

    for row in range(9):
        for col in range(9):
            print(f"{board[row][col]}", end="| ")
        print()
    print("--------------------------", end='')
    time.sleep(0.05)



board = [
    ['.', '8', '.', '.', '7', '2', '.', '.', '1'],
    ['.', '5', '.', '.', '3', '1', '6', '4', '9'],
    ['.', '.', '.', '.', '4', '.', '8', '.', '7'],
    ['.', '.', '8', '.', '5', '.', '4', '.', '.'],
    ['.', '4', '.', '.', '.', '.', '2', '.', '8'],
    ['6', '.', '1', '2', '.', '.', '.', '5', '.'],
    ['9', '2', '.', '7', '6', '3', '.', '8', '.'],
    ['.', '7', '.', '.', '1', '.', '.', '6', '2'],
    ['1', '6', '5', '9', '.', '.', '3', '.', '.']
        ]

if solve_sudoku(board):
    print("YEAH!")
    print_board(board)
else:
    print("Cant not solve this sudoku!")
