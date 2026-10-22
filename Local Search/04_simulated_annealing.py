# ============================================================
# SIMULATED ANNEALING TO REACH THE GOAL STATE (8-Queens)
# Goal state: board with 0 attacking pairs.
# Accept worse moves with probability e^(-delta/T); T slowly cools.
# Run: python 04_simulated_annealing.txt
# ============================================================
import random, math

N = 8

def conflicts(b):
    return sum(1 for i in range(N) for j in range(i + 1, N)
               if b[i] == b[j] or abs(b[i] - b[j]) == j - i)

def simulated_annealing(T=10.0, cooling=0.995, T_min=0.001):
    current = [random.randrange(N) for _ in range(N)]
    cost = conflicts(current)
    it = 0
    while T > T_min and cost > 0:
        nb = current[:]
        nb[random.randrange(N)] = random.randrange(N)   # random neighbor
        delta = conflicts(nb) - cost
        if delta < 0 or random.random() < math.exp(-delta / T):
            current, cost = nb, cost + delta            # accept
        T *= cooling                                    # cool down
        it += 1
        if it % 300 == 0:
            print(f"  iter {it:5d}  T={T:7.4f}  conflicts={cost}")
    return current, cost, it

attempt = 1
while True:
    print(f"Run {attempt}:")
    board, cost, it = simulated_annealing()
    print(f"  finished after {it} iterations, conflicts = {cost}\n")
    if cost == 0:
        break
    attempt += 1

print("GOAL STATE REACHED:", board)
for r in range(N):
    print(" ".join("Q" if board[r] == c else "." for c in range(N)))
