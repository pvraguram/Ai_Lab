# ============================================================
# A* WITH AN OVERESTIMATED HEURISTIC -> SUBOPTIMAL SOLUTION
#
# A heuristic is ADMISSIBLE if h(n) <= true cost to goal h*(n).
# A* is optimal only when h is admissible.
# If h overestimates, A* may skip the cheapest path.
#
# Graph:      S --1--> A --3--> G      (S-A-G total = 4, OPTIMAL)
#             S --2--> B --3--> G      (S-B-G total = 5)
#
# True costs to goal: h*(S)=4, h*(A)=3, h*(B)=3, h*(G)=0
# Run: python 08_astar_overestimated_heuristic.txt
# ============================================================
import heapq

graph = {
    'S': [('A', 1), ('B', 2)],
    'A': [('G', 3)],
    'B': [('G', 3)],
    'G': []
}

h_admissible    = {'S': 4, 'A': 3,  'B': 3, 'G': 0}   # h <= h*
h_overestimated = {'S': 4, 'A': 10, 'B': 1, 'G': 0}   # h(A)=10 > h*(A)=3

def astar(start, goal, h):
    pq = [(h[start], 0, start, [start])]
    closed = set()
    while pq:
        f, g, node, path = heapq.heappop(pq)
        print(f"   expand {node}: g={g}, h={h[node]}, f={f}")
        if node == goal:
            return path, g
        if node in closed:
            continue
        closed.add(node)
        for nb, w in graph[node]:
            if nb not in closed:
                heapq.heappush(pq, (g + w + h[nb], g + w, nb, path + [nb]))
    return None, None

print("1) ADMISSIBLE heuristic", h_admissible)
p1, c1 = astar('S', 'G', h_admissible)
print("   Path:", " -> ".join(p1), "| Cost:", c1, "\n")

print("2) OVERESTIMATED heuristic", h_overestimated)
p2, c2 = astar('S', 'G', h_overestimated)
print("   Path:", " -> ".join(p2), "| Cost:", c2, "\n")

print("===== PROOF =====")
for n in h_overestimated:
    true = {'S': 4, 'A': 3, 'B': 3, 'G': 0}[n]
    flag = "OVERESTIMATES" if h_overestimated[n] > true else "ok"
    print(f"  h({n}) = {h_overestimated[n]:>2}   true h*({n}) = {true}   {flag}")
print(f"\nOptimal cost = {c1}, cost with overestimated h = {c2}")
print("Since", c2, ">", c1, "the solution is SUBOPTIMAL.")
print("Reason: f(A) = 1 + 10 = 11 looked worse than f(G via B) = 5,")
print("so A* reached G through B and stopped before trying A.")
