global n
n=4

def display(board):
    for row in board:
        print(row)
    print("\n")


def isSafe(board, row, col):
    '''
    2 represents pre-placed queen. 1 represents normal queen.
    Top, Bottom, Diagonal{Top-Left, Top-Right, Bottom-Left, Bottom-Right}
    '''
    # Check entire column
    for i in range(n):
        if board[i][col] in (1, 2):
            return False
    
    # Check the entire row
    for j in range(n):                                      
        if board[row][j] in (1, 2):
            return False
    
    # Check top-left and top-right diagonal
    for k in range(1, row+1):
        if row-k >=0 and col-k >=0 and board[row-k][col-k]:
            return False
        if row-k >=0 and col+k < n and board[row-k][col+k]:
            return False
        
    # Check bottom-left and bottom-right diagonal
    for k in range(1, n-row-1):
        if row+k < n and col-k >=0 and board[row+k][col-k]:
            return False
        if row+k < n and col+k < n and board[row+k][col+k]:
            return False
            
    return True


def n_queens_preplaced(board, row, preplaced_row):
    if row==n:
        display(board)
        return

    if row==preplaced_row:
        n_queens_preplaced(board, row+1, preplaced_row)
    
    for col in range(n):
        if isSafe(board, row, col):
            board[row][col] = 1
            n_queens_preplaced(board, row+1, preplaced_row)
            board[row][col] = 0
    

def solve_n_queens_preplaced(preplaced_row, preplaced_col):
    board = [[0 for i in range(n)] for i in range(n)]
    
    # Place the pre-placed queen
    board[preplaced_row][preplaced_col] = 2
    
    found = n_queens_preplaced(board, 0, preplaced_row)
    '''
    if not found:
        print(f"No solution exists for R={preplaced_row}, C={preplaced_col}")
    return found
    '''

R, C = 0, 2
solve_n_queens_preplaced(R, C)