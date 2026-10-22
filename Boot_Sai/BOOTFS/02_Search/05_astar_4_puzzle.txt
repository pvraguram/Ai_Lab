# ============================================================
# A* SEARCH FOR THE 4-PUZZLE (2x2 board, tiles 1-3 + blank)
# Also analyzes different heuristic values.
# f(n) = g(n) + h(n)
# Run: python 05_astar_4_puzzle.txt
# ============================================================
import heapq

N = 2
GOAL = (1, 2,
        3, 0)          # 0 = blank

def h_zero(s):          # h = 0  -> A* becomes UCS
    return 0

def h_misplaced(s):     # number of tiles not in goal position
    return sum(1 for i, t in enumerate(s) if t != 0 and t != GOAL[i])

def h_manhattan(s):     # sum of row+col distance of every tile
    d = 0
    for i, t in enumerate(s):
        if t:
            g = GOAL.index(t)
            d += abs(i // N - g // N) + abs(i % N - g % N)
    return d

def neighbors(s):
    z = s.index(0)
    r, c = divmod(z, N)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            l = list(s)
            k = nr * N + nc
            l[z], l[k] = l[k], l[z]
            yield tuple(l)

def astar(start, h):
    pq = [(h(start), 0, start, [start])]
    best = {start: 0}
    expanded = 0
    while pq:
        f, g, s, path = heapq.heappop(pq)
        if g > best[s]:
            continue
        expanded += 1
        if s == GOAL:
            return path, g, expanded
        for nb in neighbors(s):
            if g + 1 < best.get(nb, float('inf')):
                best[nb] = g + 1
                heapq.heappush(pq, (g + 1 + h(nb), g + 1, nb, path + [nb]))
    return None, None, expanded

def show(s):
    for i in range(0, N * N, N):
        print("  ", " ".join(str(x) if x else "_" for x in s[i:i + N]))
    print()

start = (0, 3,
         2, 1)

path, moves, n = astar(start, h_manhattan)
print("Start state:"); show(start)
print("Solution with Manhattan heuristic:", moves, "moves\n")
for step, s in enumerate(path):
    print("Step", step); show(s)

print("===== HEURISTIC ANALYSIS =====")
print(f"{'Heuristic':<12}{'h(start)':>9}{'Moves':>7}{'Expanded':>10}")
for name, h in [("h=0 (UCS)", h_zero), ("Misplaced", h_misplaced), ("Manhattan", h_manhattan)]:
    p, m, e = astar(start, h)
    print(f"{name:<12}{h(start):>9}{m:>7}{e:>10}")
print("\nAll admissible heuristics give the same optimal number of moves.")
print("Manhattan gives the largest (most accurate) h value, so it is the")
print("most informed. The 2x2 puzzle has only 12 reachable states, so the")
print("node counts are equal here; on the 8-puzzle the difference is large.")
