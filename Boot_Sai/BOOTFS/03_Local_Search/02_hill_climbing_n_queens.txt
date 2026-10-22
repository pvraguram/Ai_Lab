# ============================================================
# N-QUEENS USING HILL CLIMBING (steepest ascent + random restart)
# State: board[row] = column of the queen in that row
# Objective: minimise h = number of attacking queen pairs
# Run: python 02_hill_climbing_n_queens.txt
# ============================================================
import random

N = 8

def conflicts(board):
    h = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                h += 1
    return h

def best_neighbor(board):
    best, best_h = board, conflicts(board)
    for row in range(N):
        for col in range(N):
            if col != board[row]:
                nb = board[:]
                nb[row] = col
                h = conflicts(nb)
                if h < best_h:
                    best, best_h = nb, h
    return best, best_h

def hill_climbing():
    board = [random.randrange(N) for _ in range(N)]
    h = conflicts(board)
    steps = 0
    while True:
        nb, nh = best_neighbor(board)
        if nh >= h:                # no improvement -> local minimum
            return board, h, steps
        board, h = nb, nh
        steps += 1

def show(board):
    for r in range(N):
        print(" ".join("Q" if board[r] == c else "." for c in range(N)))

restarts = 0
while True:
    board, h, steps = hill_climbing()
    print(f"Attempt {restarts + 1}: stopped after {steps} steps with h = {h}")
    if h == 0:
        break
    restarts += 1

print(f"\nSolution found after {restarts} restart(s): {board}")
print("Conflicts:", conflicts(board))
show(board)
