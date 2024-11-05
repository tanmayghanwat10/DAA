def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        # All queens are placed successfully
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1

            # Recur for the next row
            if solve_n_queens(board, row + 1, n):
                return True

            # If placing queen in the current position doesn't lead to a solution,
            # backtrack and remove the queen from the current position
            board[row][col] = 0

    # If no placement is possible in the current row, return False
    return False

def print_board(board):
    for row in board:
        print(' '.join('Q' if cell else '.' for cell in row))

# Taking user input for the size of the chessboard
n = int(input("Enter the size of the chessboard (N): "))

# Creating the N-Queens board with the first queen placed
first_queen_column = int(input("Enter the column number for the first queen (0 to N-1): "))
board = [[0] * n for _ in range(n)]
board[0][first_queen_column] = 1

# Solving the N-Queens problem and printing the final board
if solve_n_queens(board, 1, n):
    print("Solution found:")
    print_board(board)
else:
    print("No solution exists.")
