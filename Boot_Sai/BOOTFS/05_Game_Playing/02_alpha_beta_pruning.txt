# ============================================================
# ALPHA-BETA PRUNING  (+ comparison with plain MINIMAX)
# alpha = best value MAX can guarantee so far
# beta  = best value MIN can guarantee so far
# Prune a branch when alpha >= beta.
# Part 1: textbook game tree (shows which leaves are pruned)
# Part 2: Tic-Tac-Toe, number of nodes evaluated Minimax vs Alpha-Beta
# Run: python 02_alpha_beta_pruning.txt
# ============================================================
import math

# ---------------- PART 1 : GAME TREE ----------------
#                 MAX
#        /         |         \
#      MIN        MIN        MIN
#     / | \      / | \      / | \
#    3 12  8    2  4  6   14  5  2
tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]

def ab_tree():
    alpha, beta_root = -math.inf, math.inf
    best_val = -math.inf
    for i, child in enumerate(tree):
        beta = math.inf
        print(f"MIN node {chr(66 + i)} (alpha = {alpha}):")
        for j, leaf in enumerate(child):
            print(f"   evaluate leaf {leaf}")
            beta = min(beta, leaf)
            if beta <= alpha:
                pruned = child[j + 1:]
                if pruned:
                    print(f"   beta={beta} <= alpha={alpha} -> PRUNE {pruned}")
                break
        print(f"   value of {chr(66 + i)} = {beta}")
        best_val = max(best_val, beta)
        alpha = max(alpha, best_val)
    return best_val

print("===== PART 1: GAME TREE =====")
v = ab_tree()
print("Minimax value of root (MAX):", v, "\n")

# ---------------- PART 2 : TIC-TAC-TOE ----------------
LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
count = {'mm': 0, 'ab': 0}

def winner(b):
    for x, y, z in LINES:
        if b[x] != ' ' and b[x] == b[y] == b[z]:
            return b[x]
    return 'draw' if ' ' not in b else None

def utility(w, depth):
    return {'X': 10 - depth, 'O': depth - 10, 'draw': 0}[w]

def minimax(b, depth, is_max):
    count['mm'] += 1
    w = winner(b)
    if w: return utility(w, depth)
    best = -math.inf if is_max else math.inf
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X' if is_max else 'O'
            s = minimax(b, depth + 1, not is_max)
            b[i] = ' '
            best = max(best, s) if is_max else min(best, s)
    return best

def alphabeta(b, depth, alpha, beta, is_max):
    count['ab'] += 1
    w = winner(b)
    if w: return utility(w, depth)
    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                best = max(best, alphabeta(b, depth + 1, alpha, beta, False))
                b[i] = ' '
                alpha = max(alpha, best)
                if alpha >= beta:
                    break                     # beta cut-off
        return best
    best = math.inf
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            best = min(best, alphabeta(b, depth + 1, alpha, beta, True))
            b[i] = ' '
            beta = min(beta, best)
            if alpha >= beta:
                break                         # alpha cut-off
    return best

def best_move_ab(b):
    best, move = -math.inf, None
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X'
            s = alphabeta(b, 1, -math.inf, math.inf, False)
            b[i] = ' '
            if s > best:
                best, move = s, i
    return move, best

print("===== PART 2: TIC-TAC-TOE =====")
board = ['X', 'O', 'X',
         ' ', 'O', ' ',
         ' ', ' ', ' ']
m, s = best_move_ab(board)
print("Position:", board)
print(f"Best move for X (alpha-beta): cell {m}, value {s}\n")

empty = [' '] * 9
v1 = minimax(empty[:], 0, True)
v2 = alphabeta(empty[:], 0, -math.inf, math.inf, True)
print("Empty board - full game search:")
print(f"  Minimax    : value {v1}, nodes evaluated = {count['mm']}")
print(f"  Alpha-Beta : value {v2}, nodes evaluated = {count['ab']}")
print(f"  Same answer, {100 * (1 - count['ab'] / count['mm']):.1f}% fewer nodes with pruning.")
