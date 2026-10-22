# ============================================================
# MINIMAX ALGORITHM FOR TIC-TAC-TOE (3x3)
# MAX = X (computer), MIN = O
# Utility: +10 X wins, -10 O wins, 0 draw (depth used to prefer
# faster wins / slower losses)
# Run: python 01_minimax_tic_tac_toe.txt
#   -> choose 1 to watch AI vs AI (always a draw with perfect play)
#   -> choose 2 to play against the AI
# ============================================================

LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),      # rows
         (0, 3, 6), (1, 4, 7), (2, 5, 8),      # columns
         (0, 4, 8), (2, 4, 6)]                 # diagonals
nodes = 0

def winner(b):
    for x, y, z in LINES:
        if b[x] != ' ' and b[x] == b[y] == b[z]:
            return b[x]
    return 'draw' if ' ' not in b else None

def minimax(b, depth, is_max):
    global nodes
    nodes += 1
    w = winner(b)
    if w == 'X': return 10 - depth
    if w == 'O': return depth - 10
    if w == 'draw': return 0
    scores = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X' if is_max else 'O'
            scores.append(minimax(b, depth + 1, not is_max))
            b[i] = ' '
    return max(scores) if is_max else min(scores)

def best_move(b, player):
    best, move = None, None
    for i in range(9):
        if b[i] == ' ':
            b[i] = player
            s = minimax(b, 1, player == 'O')    # next turn belongs to other player
            b[i] = ' '
            if best is None or (player == 'X' and s > best) or (player == 'O' and s < best):
                best, move = s, i
    return move, best

def show(b):
    for r in range(3):
        print(" " + " | ".join(b[3 * r:3 * r + 3]))
        if r < 2: print("---+---+---")
    print()

# ---------- Demo 1: best move from a given position ----------
board = ['X', 'O', 'X',
         ' ', 'O', ' ',
         ' ', ' ', ' ']
print("Given position (X to move):"); show(board)
m, s = best_move(board, 'X')
print(f"Best move for X: cell {m} (row {m // 3 + 1}, col {m % 3 + 1}), minimax value {s}")
print("Nodes evaluated:", nodes, "\n")

choice = input("1 = AI vs AI, 2 = play vs AI : ").strip() or "1"
board = [' '] * 9
turn = 'X'
while winner(board) is None:
    show(board)
    if choice == "2" and turn == 'O':
        while True:
            try:
                i = int(input("Your move (1-9): ")) - 1
                if 0 <= i < 9 and board[i] == ' ':
                    break
            except ValueError:
                pass
            print("Invalid move.")
    else:
        i, _ = best_move(board, turn)
        print(f"{turn} plays cell {i + 1}")
    board[i] = turn
    turn = 'O' if turn == 'X' else 'X'
show(board)
w = winner(board)
print("Result:", "Draw!" if w == 'draw' else w + " wins!")
