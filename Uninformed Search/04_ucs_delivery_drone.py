# ============================================================
# DELIVERY DRONE NAVIGATION - UCS FOR MINIMUM BATTERY USAGE
# Graph: nodes = waypoints, edge weight = battery % used
# (depends on distance, wind, altitude change).
# UCS always expands the cheapest path first, so the first time
# it pops the destination, that path has MINIMUM battery usage.
# We compare with BFS (fewest hops) to show the difference.
# Run: python 04_ucs_delivery_drone.txt
# ============================================================
import heapq
from collections import deque

battery = {
    'Warehouse': [('P1', 8), ('P2', 3)],
    'P1':        [('Customer', 4)],            # 2 hops, 12% total
    'P2':        [('P3', 2)],
    'P3':        [('P4', 2)],
    'P4':        [('Customer', 2)],            # 4 hops, 9% total
    'Customer':  []
}

def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    best = {start: 0}
    while pq:
        cost, node, path = heapq.heappop(pq)
        print(f"  pop {node:10s} battery used so far = {cost}%")
        if node == goal:
            return path, cost
        if cost > best.get(node, float('inf')):
            continue
        for nb, w in graph[node]:
            if cost + w < best.get(nb, float('inf')):
                best[nb] = cost + w
                heapq.heappush(pq, (cost + w, nb, path + [nb]))
    return None, None

def bfs(graph, start, goal):
    q = deque([[start]])
    seen = {start}
    while q:
        path = q.popleft()
        if path[-1] == goal:
            return path
        for nb, _ in graph[path[-1]]:
            if nb not in seen:
                seen.add(nb)
                q.append(path + [nb])

def path_cost(graph, path):
    return sum(dict(graph[a])[b] for a, b in zip(path, path[1:]))

print("UCS trace:")
p, c = ucs(battery, 'Warehouse', 'Customer')
print("\nUCS route :", " -> ".join(p), f"| battery = {c}%")
b = bfs(battery, 'Warehouse', 'Customer')
print("BFS route :", " -> ".join(b), f"| battery = {path_cost(battery, b)}%")
print("\nUCS uses less battery even though it takes more hops,")
print("because it orders the frontier by cumulative cost g(n).")
