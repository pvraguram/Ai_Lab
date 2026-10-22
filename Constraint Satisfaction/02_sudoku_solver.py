# Run: python 02_sudoku_solver.txt
# CSP: variables = 81 cells, domain = 1..9,
# constraints = no repeat in row, column, 3x3 box. Solved by backtracking.
# ============================================
# SUDOKU USING CSP + BACKTRACKING
# ============================================

N = 9

# 0 means empty cell

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# ============================================
# DISPLAY BOARD
# ============================================

def print_board():
    for row in board:
        print(row)


# ============================================
# FIND EMPTY CELL
# ============================================

def find_empty():
    for row in range(N):
        for col in range(N):
            if board[row][col] == 0:
                return row, col

    return None


# ============================================
# CHECK CONSTRAINTS
# ============================================

def is_valid(row, col, num):

    # Check row
    for j in range(N):
        if board[row][j] == num:
            return False

    # Check column
    for i in range(N):
        if board[i][col] == num:
            return False

    # Check 3 x 3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):

            if board[i][j] == num:
                return False

    return True


# ============================================
# BACKTRACKING SEARCH
# ============================================

def solve():

    empty = find_empty()

    # No empty cell -> solution found
    if empty is None:
        return True

    row, col = empty

    # Try values 1 to 9
    for num in range(1, 10):

        # Check CSP constraints
        if is_valid(row, col, num):

            # Assign value
            board[row][col] = num

            # Recursively solve
            if solve():
                return True

            # Backtrack
            board[row][col] = 0

    return False


# ============================================
# MAIN
# ============================================

print("Original Sudoku:")
print_board()

if solve():

    print("\nSolved Sudoku:")
    print_board()

else:

    print("No solution exists.")