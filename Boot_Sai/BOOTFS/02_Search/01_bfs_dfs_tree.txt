# ============================================================
# BFS AND DFS FOR A GIVEN TREE / GRAPH
# Run: python 01_bfs_dfs_tree.txt
# ============================================================
from collections import deque

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

# ---------- BFS : level by level (FIFO queue) ----------
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    order = []
    while queue:
        node, path = queue.popleft()
        order.append(node)
        if node == goal:
            return order, path
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                queue.append((nb, path + [nb]))
    return order, None

# ---------- DFS : go deep first (LIFO stack) ----------
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    order = []
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        if node == goal:
            return order, path
        for nb in reversed(graph[node]):      # keep left-to-right order
            if nb not in visited:
                stack.append((nb, path + [nb]))
    return order, None

start, goal = 'A', 'G'
o, p = bfs(tree, start, goal)
print("BFS visit order:", " ".join(o))
print("BFS path       :", " -> ".join(p))
o, p = dfs(tree, start, goal)
print("DFS visit order:", " ".join(o))
print("DFS path       :", " -> ".join(p))
