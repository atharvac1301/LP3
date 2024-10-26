def solve(row, n, board, column, left_diagonal, right_diagonal, result):
    if row == n:
        # Add current board to result list
        result.append([row[:] for row in board])
        return
    
    for col in range(n):
        # Skip this row if it already has a queen (marked as 2)
        if any(cell == 2 for cell in board[row]):
            solve(row + 1, n, board, column, left_diagonal, right_diagonal, result)
            return
            
        # Check if queen can be placed
        if (board[row][col] != 2 and  # Not a pre-placed queen position
            not column[col] and 
            not left_diagonal[row + col] and 
            not right_diagonal[n + col - row - 1]):
            
            # Place the queen and update status
            board[row][col] = 1
            column[col] = 1
            left_diagonal[row + col] = 1
            right_diagonal[n + col - row - 1] = 1
            
            # Move to next row
            solve(row + 1, n, board, column, left_diagonal, right_diagonal, result)
            
            # Backtrack: remove the queen and update status
            # Don't remove if it's a pre-placed queen (marked as 2)
            if board[row][col] != 2:
                board[row][col] = 0
                column[col] = 0
                left_diagonal[row + col] = 0
                right_diagonal[n + col - row - 1] = 0

def solve_n_queen_with_constraint(n, pre_placed_row, pre_placed_col):
    # Validate input
    if not (0 <= pre_placed_row < n and 0 <= pre_placed_col < n):
        raise ValueError("Pre-placed queen position is outside the board")
        
    # Initialize board and mark pre-placed queen
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[pre_placed_row][pre_placed_col] = 2  # Use 2 to mark pre-placed queen
    
    # Initialize tracking arrays
    column = [0] * n
    left_diagonal = [0] * (2 * n - 1)
    right_diagonal = [0] * (2 * n - 1)
    
    # Mark the pre-placed queen's attacking squares
    column[pre_placed_col] = 1
    left_diagonal[pre_placed_row + pre_placed_col] = 1
    right_diagonal[n + pre_placed_col - pre_placed_row - 1] = 1
    
    # Initialize result list
    result = []
    
    # Start solving from row 0
    solve(0, n, board, column, left_diagonal, right_diagonal, result)
    return result

def display_board(board):
    """Helper function to display the board with different symbols for placed and pre-placed queens"""
    symbols = {0: '.', 1: 'Q', 2: 'P'}  # P for pre-placed queen
    for row in board:
        print(" ".join(symbols[cell] for cell in row))
    print()

def main():
    # Get input from user
    n = int(input("Enter the size of the board: "))
    row = int(input(f"Enter the row (0-{n-1}) of pre-placed queen: "))
    col = int(input(f"Enter the column (0-{n-1}) of pre-placed queen: "))
    
    try:
        # Find solutions
        solutions = solve_n_queen_with_constraint(n, row, col)
        
        # Display results
        if not solutions:
            print(f"\nNo solutions exist for {n}x{n} board with a queen pre-placed at position ({row}, {col})")
        else:
            print(f"\nFound {len(solutions)} solution(s) for {n}x{n} board with a queen pre-placed at position ({row}, {col}):")
            print("\nLegend: P = Pre-placed queen, Q = Placed queen, . = Empty square\n")
            for i, solution in enumerate(solutions, 1):
                print(f"Solution {i}:")
                display_board(solution)
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()