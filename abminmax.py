def alpha_beta(depth, node, maximizing, values, alpha, beta):
    if depth == 3:
        return values[node]

    if maximizing:
        best = float('-inf')

        for i in range(2):
            value = alpha_beta(
                depth + 1, node * 2 + i, False,
                values, alpha, beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = alpha_beta(
                depth + 1, node * 2 + i, True,
                values, alpha, beta
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alpha_beta(
    0, 0, True, values,
    float('-inf'), float('inf')
)

print("Optimal value:", result)