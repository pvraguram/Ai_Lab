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

    for line in wins:
        if all(board[i] == player for i in line):
            return True
    return False

board = [" "] * 9
players = ["X", "O", "Y"]
turn = 0

while True:
    display(board)
    player = players[turn % 3]

    try:
        pos = int(input(f"Player {player}, enter position (1-9): ")) - 1
    except ValueError:
        print("Enter a valid number.")
        continue

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

    turn += 1