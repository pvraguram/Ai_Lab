# ============================================================
# WATER JUG PROBLEM USING BFS AND DFS
# Jug1 = 4 L, Jug2 = 3 L, Goal = exactly 2 L in Jug1
# State = (jug1, jug2)
# Rules: fill, empty, pour one into the other
# Run: python 10_water_jug_bfs_dfs.txt
# ============================================================
from collections import deque

CAP1, CAP2, TARGET = 4, 3, 2

def successors(state):
    a, b = state
    p12 = min(a, CAP2 - b)       # pour jug1 -> jug2
    p21 = min(b, CAP1 - a)       # pour jug2 -> jug1
    return [
        ((CAP1, b), "Fill Jug1"),
        ((a, CAP2), "Fill Jug2"),
        ((0, b),    "Empty Jug1"),
        ((a, 0),    "Empty Jug2"),
        ((a - p12, b + p12), "Pour Jug1 -> Jug2"),
        ((a + p21, b - p21), "Pour Jug2 -> Jug1"),
    ]

def is_goal(s):
    return s[0] == TARGET

def bfs(start=(0, 0)):
    q = deque([(start, [(start, "Start")])])
    seen = {start}
    while q:
        s, path = q.popleft()
        if is_goal(s):
            return path
        for nxt, act in successors(s):
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, path + [(nxt, act)]))

def dfs(start=(0, 0)):
    stack = [(start, [(start, "Start")])]
    seen = set()
    while stack:
        s, path = stack.pop()
        if s in seen:
            continue
        seen.add(s)
        if is_goal(s):
            return path
        for nxt, act in reversed(successors(s)):
            if nxt not in seen:
                stack.append((nxt, path + [(nxt, act)]))

def show(name, path):
    print(f"===== {name} ({len(path) - 1} steps) =====")
    for s, act in path:
        print(f"  {act:<20} -> {s}")
    print()

show("BFS", bfs())
show("DFS", dfs())
print("BFS gives the shortest solution; DFS finds A solution but")
print("it may be longer, since it explores one branch deeply first.")
