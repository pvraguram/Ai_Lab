# Minimax Algorithm

def minimax(board, depth, is_maximizing):
    # Check terminal states
    if board == ["X", "X", "X"]:
        return 10 - depth

    if board == ["O", "O", "O"]:
        return depth - 10

    # If no empty position
    if "_" not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(len(board)):
            if board[i] == "_":
                board[i] = "X"

                score = minimax(board, depth + 1, False)

                board[i] = "_"

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(len(board)):
            if board[i] == "_":
                board[i] = "O"

                score = minimax(board, depth + 1, True)

                board[i] = "_"

                best_score = min(best_score, score)

        return best_score


board = ["X", "O", "_"]

print("Best score:", minimax(board, 0, True))