def display(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("---------")

def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(all(board[i] == player for i in line) for line in wins)

board = [" "] * 9
player = "X"

while True:
    display(board)
    pos = int(input(f"Player {player}, enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position. Try again.")
        continue

    board[pos] = player

    if check_winner(board, player):
        display(board)
        print(f"Player {player} wins!")
        break

    if " " not in board:
        display(board)
        print("Match is a draw!")
        break

    player = "O" if player == "X" else "X"