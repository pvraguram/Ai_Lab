# ============================================================
# A* SEARCH FOR THE 8-PUZZLE
# Analysis of different heuristics:
#   h1 = Misplaced tiles      (admissible)
#   h2 = Manhattan distance   (admissible, dominates h1)
#   h3 = Euclidean distance   (admissible)
# Run: python 06_astar_8_puzzle_heuristics.txt
# ============================================================
import heapq, math

N = 3
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def misplaced(s):
    return sum(1 for i, t in enumerate(s) if t and t != GOAL[i])

def manhattan(s):
    d = 0
    for i, t in enumerate(s):
        if t:
            g = GOAL.index(t)
            d += abs(i // N - g // N) + abs(i % N - g % N)
    return d

def euclidean(s):
    d = 0
    for i, t in enumerate(s):
        if t:
            g = GOAL.index(t)
            d += math.hypot(i // N - g // N, i % N - g % N)
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
    for i in range(0, 9, 3):
        print("  ", " ".join(str(x) if x else "_" for x in s[i:i + 3]))
    print()

start = (1, 2, 3,
         0, 4, 6,
         7, 5, 8)
start_hard = (8, 1, 3,
              4, 0, 2,
              7, 6, 5)

path, moves, n = astar(start, manhattan)
print("Solving (Manhattan):"); show(start)
for i, s in enumerate(path):
    print("Step", i); show(s)
print("Total moves:", moves)

for name, st in [("EASY start", start), ("HARDER start", start_hard)]:
    print(f"\n===== HEURISTIC COMPARISON : {name} =====")
    print(f"{'Heuristic':<12}{'h(start)':>9}{'Moves':>7}{'Nodes expanded':>16}")
    for hn, h in [("Misplaced", misplaced), ("Euclidean", euclidean), ("Manhattan", manhattan)]:
        p, m, e = astar(st, h)
        print(f"{hn:<12}{h(st):>9.2f}{m:>7}{e:>16}")

print("\nConclusion: all three are admissible -> same optimal moves.")
print("Manhattan >= Misplaced for every state (dominates), so it is more")
print("informed and expands the fewest nodes.")
