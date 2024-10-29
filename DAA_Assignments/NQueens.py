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


n_queens(board, 0)



'''
Dump:

def isSafe(board, row, col):
    # Check this row on left side
    for j in range(col):
        if board[row][j] == 1 or board[row][j] == 2:
            return False
    
    # Check this column on upper and lower side
    for i in range(n):
        if board[i][col] == 1 or board[i][col] == 2:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1 or board[i][j] == 2:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1 or board[i][j] == 2:
            return False
            
    # Check lower left diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1 or board[i][j] == 2:
            return False
            
    # Check lower right diagonal
    for i, j in zip(range(row, n), range(col, n)):
        if board[i][j] == 1 or board[i][j] == 2:
            return False
            
    return True

-------------------------------------------------------
    
def n_queens_preplaced(board, row, preplaced_row):
    if row == n:
        display(board)
        return True
    
    if row == preplaced_row:
        return n_queens_preplaced(board, row + 1, preplaced_row)
    
    for col in range(n):
        if isSafe(board, row, col):
            board[row][col] = 1
            if n_queens_preplaced(board, row + 1, preplaced_row):
                return True
            board[row][col] = 0
    
    return False

'''


