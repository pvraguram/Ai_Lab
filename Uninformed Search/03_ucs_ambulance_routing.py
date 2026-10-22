# ============================================================
# AMBULANCE ROUTING USING UNIFORM COST SEARCH
# Find the shortest route from the accident spot to the
# NEAREST hospital (multiple goal nodes).
# UCS pops nodes in increasing distance, so the FIRST hospital
# popped from the queue is guaranteed to be the nearest one.
# Run: python 03_ucs_ambulance_routing.txt
# ============================================================
import heapq

# Road network: distances in km
roads = {
    'Accident':   [('Junction1', 4), ('Junction2', 2)],
    'Junction1':  [('Accident', 4), ('HospitalA', 6), ('Junction3', 3)],
    'Junction2':  [('Accident', 2), ('Junction3', 4), ('Junction4', 7)],
    'Junction3':  [('Junction1', 3), ('Junction2', 4), ('HospitalB', 3)],
    'Junction4':  [('Junction2', 7), ('HospitalC', 2)],
    'HospitalA':  [('Junction1', 6)],
    'HospitalB':  [('Junction3', 3)],
    'HospitalC':  [('Junction4', 2)],
}
hospitals = {'HospitalA', 'HospitalB', 'HospitalC'}

def ucs_nearest_hospital(graph, start, goals):
    pq = [(0, start, [start])]
    best = {start: 0}
    while pq:
        dist, node, path = heapq.heappop(pq)
        if dist > best.get(node, float('inf')):
            continue
        if node in goals:                 # first goal popped = nearest
            return node, path, dist
        for nb, d in graph[node]:
            nd = dist + d
            if nd < best.get(nb, float('inf')):
                best[nb] = nd
                heapq.heappush(pq, (nd, nb, path + [nb]))
    return None, None, float('inf')

h, path, dist = ucs_nearest_hospital(roads, 'Accident', hospitals)
print("Nearest hospital :", h)
print("Route            :", " -> ".join(path))
print("Distance (km)    :", dist)
