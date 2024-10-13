global n 
n = 4
board = [[0 for i in range(n)] for i in range(n)]
r, c = 1, 2
board[r][c] = 1

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
        return True
    
    if row == r:
        return n_queens(board, row+1)
    
    for col in range(n):
        if col == c:
            continue
      
        if isSafe(board, row, col):
            board[row][col] = 1
            if n_queens(board, row+1):
                return True
            board[row][col] = 0

    return False


if n_queens(board, 0):
    print("Solution: \n")
    display(board)
else:
    print("No Solution")

