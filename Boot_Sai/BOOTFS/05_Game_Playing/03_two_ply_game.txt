# ============================================================
# 2-PLY GAME (one move by MAX, one reply by MIN)
# Each root move has opponent replies with utility values.
# MIN picks the smallest value for each move,
# MAX then picks the move with the largest of those minimums.
# Run: python 03_two_ply_game.txt
# ============================================================

game_tree = {
    "Move A": {"Reply A1": 3, "Reply A2": 12, "Reply A3": 8},
    "Move B": {"Reply B1": 2, "Reply B2": 4,  "Reply B3": 6},
    "Move C": {"Reply C1": 14, "Reply C2": 5, "Reply C3": 2},
}

print("Ply 1 = MAX moves, Ply 2 = MIN replies\n")
best_move, best_value = None, float("-inf")
for move, replies in game_tree.items():
    reply = min(replies, key=replies.get)          # MIN's best reply
    value = replies[reply]
    print(f"{move}: replies {replies} -> MIN chooses {reply} = {value}")
    if value > best_value:
        best_move, best_value = move, value

print("\nMAX chooses:", best_move)
print("Minimax value of the game:", best_value)
