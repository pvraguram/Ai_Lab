# ============================================================
# A* SEARCH vs UNIFORM COST SEARCH (comparison)
# UCS : f(n) = g(n)            (uninformed)
# A*  : f(n) = g(n) + h(n)     (informed, h = straight-line distance)
# Both are optimal; A* expands fewer nodes.
# Run: python 09_astar_vs_ucs.txt
# ============================================================
import heapq

# Romania map (classic textbook example)
graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
    'Rimnicu': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101)],
}
# straight-line distance to Bucharest (admissible)
sld = {'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Timisoara': 329,
       'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160, 'Rimnicu': 193,
       'Fagaras': 176, 'Pitesti': 100, 'Bucharest': 0}

def search(start, goal, h):
    pq = [(h(start), 0, start, [start])]
    best = {start: 0}
    order = []
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g > best[node]:
            continue
        order.append(node)
        if node == goal:
            return path, g, order
        for nb, w in graph[node]:
            if g + w < best.get(nb, float('inf')):
                best[nb] = g + w
                heapq.heappush(pq, (g + w + h(nb), g + w, nb, path + [nb]))

ucs = lambda n: 0
astar = lambda n: sld[n]

for name, h in [("UCS", ucs), ("A*", astar)]:
    path, cost, order = search('Arad', 'Bucharest', h)
    print(f"===== {name} =====")
    print("Expansion order:", ", ".join(order))
    print("Path :", " -> ".join(path))
    print("Cost :", cost, "| Nodes expanded:", len(order), "\n")

print("Both find the same optimal path (cost 418).")
print("A* expands fewer nodes because h(n) guides it toward the goal.")
