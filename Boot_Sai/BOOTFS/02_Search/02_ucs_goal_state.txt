# ============================================================
# UNIFORM COST SEARCH (UCS) TO REACH GOAL STATE
# Expands the node with the LOWEST path cost g(n) first.
# Run: python 02_ucs_goal_state.txt
# ============================================================
import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [start])]          # (cost, node, path)
    best = {start: 0}
    expanded = 0
    while pq:
        cost, node, path = heapq.heappop(pq)
        if cost > best.get(node, float('inf')):
            continue
        expanded += 1
        print(f"Expand {node}  g={cost}")
        if node == goal:
            return path, cost, expanded
        for nb, w in graph[node]:
            nc = cost + w
            if nc < best.get(nb, float('inf')):
                best[nb] = nc
                heapq.heappush(pq, (nc, nb, path + [nb]))
    return None, float('inf'), expanded

graph = {
    'S': [('A', 1), ('B', 5), ('C', 15)],
    'A': [('G', 10)],
    'B': [('G', 5)],
    'C': [('G', 5)],
    'G': []
}

path, cost, n = ucs(graph, 'S', 'G')
print("\nPath :", " -> ".join(path))
print("Cost :", cost)
print("Nodes expanded:", n)
# Note: S->A->G costs 11 but UCS correctly returns S->B->G (cost 10)
