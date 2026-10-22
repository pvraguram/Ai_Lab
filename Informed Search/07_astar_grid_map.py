# ============================================================
# A* SEARCH FOR A GRID MAP (robot path finding)
# 0 = free cell, 1 = obstacle. Moves: up/down/left/right, cost 1
# Heuristic: Manhattan distance to goal (admissible)
# Run: python 07_astar_grid_map.txt
# ============================================================
import heapq

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
]
start, goal = (0, 0), (4, 0)
R, C = len(grid), len(grid[0])

def h(p):
    return abs(p[0] - goal[0]) + abs(p[1] - goal[1])

def astar():
    pq = [(h(start), 0, start, [start])]
    best = {start: 0}
    expanded = 0
    while pq:
        f, g, cur, path = heapq.heappop(pq)
        if g > best[cur]:
            continue
        expanded += 1
        if cur == goal:
            return path, g, expanded
        r, c = cur
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                nxt = (nr, nc)
                if g + 1 < best.get(nxt, float('inf')):
                    best[nxt] = g + 1
                    heapq.heappush(pq, (g + 1 + h(nxt), g + 1, nxt, path + [nxt]))
    return None, None, expanded

path, cost, n = astar()
print("Path :", path)
print("Cost :", cost, "| Nodes expanded:", n, "\n")
for r in range(R):
    row = ""
    for c in range(C):
        if (r, c) == start: row += "S "
        elif (r, c) == goal: row += "G "
        elif grid[r][c] == 1: row += "# "
        elif (r, c) in path: row += "* "
        else: row += ". "
    print(row)
