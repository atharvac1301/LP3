global n 
n = 4
board = [[0 for i in range(n)] for i in range(n)]
R, C = 1, 2
board[R][C] = 1     # 2 instead of 1, to differentiate pre-placed Queen

def display(board):
    for row in board:
        print(row)
    print("\n")

def isSafe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for k in range(1, row+1):
        if row-k >= 0 and col-k >= 0 and board[row-k][col-k] == 1:
            return False
        if row-k >= 0 and col+k < n and board[row-k][col+k] == 1:
            return False
    return True

def n_queens(board, row):
    if row==n:
        display(board)
        return
    
    for col in range(n):
        if isSafe(board, row, col):
            board[row][col] = 1
            n_queens(board, row+1)
            board[row][col] = 0


def n_queens_constraint():
    
    pass




