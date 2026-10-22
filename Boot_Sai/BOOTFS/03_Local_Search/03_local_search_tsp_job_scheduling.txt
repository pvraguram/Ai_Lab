# ============================================================
# LOCAL SEARCH (HILL CLIMBING) FOR
#   A) TRAVELLING SALESMAN PROBLEM (TSP)
#   B) JOB SCHEDULING (minimise makespan on 2 machines)
# Run: python 03_local_search_tsp_job_scheduling.txt
# ============================================================
import random
random.seed(7)

# ------------------------------------------------------------
# A) TSP - state = order of cities, neighbor = swap two cities
# ------------------------------------------------------------
cities = ['A', 'B', 'C', 'D', 'E']
dist = [
    [0, 12, 10, 19, 8],
    [12, 0, 3, 7, 2],
    [10, 3, 0, 6, 20],
    [19, 7, 6, 0, 4],
    [8, 2, 20, 4, 0],
]

def tour_cost(t):
    return sum(dist[t[i]][t[(i + 1) % len(t)]] for i in range(len(t)))

def tsp_hill_climb():
    tour = list(range(len(cities)))
    random.shuffle(tour)
    cost = tour_cost(tour)
    print("Initial tour:", " -> ".join(cities[i] for i in tour), "| cost", cost)
    while True:
        best, best_cost = None, cost
        for i in range(len(tour)):
            for j in range(i + 1, len(tour)):
                nb = tour[:]
                nb[i], nb[j] = nb[j], nb[i]
                c = tour_cost(nb)
                if c < best_cost:
                    best, best_cost = nb, c
        if best is None:
            return tour, cost
        tour, cost = best, best_cost
        print("Improved    :", " -> ".join(cities[i] for i in tour), "| cost", cost)

print("===== A) TSP =====")
best_t, best_c = None, float('inf')
for r in range(5):                          # random restarts
    t, c = tsp_hill_climb()
    if c < best_c:
        best_t, best_c = t, c
    print()
route = [cities[i] for i in best_t] + [cities[best_t[0]]]
print("Best tour:", " -> ".join(route), "| cost", best_c, "\n")

# ------------------------------------------------------------
# B) JOB SCHEDULING - assign each job to machine 0 or 1
#    Objective: minimise makespan (finish time of busiest machine)
#    Neighbor: move one job to the other machine
# ------------------------------------------------------------
jobs = {'J1': 7, 'J2': 3, 'J3': 5, 'J4': 4, 'J5': 6, 'J6': 2}
names = list(jobs)

def makespan(assign):
    load = [0, 0]
    for j, m in zip(names, assign):
        load[m] += jobs[j]
    return max(load), load

assign = [0] * len(names)                  # start: everything on machine 0
cost, load = makespan(assign)
print("===== B) JOB SCHEDULING =====")
print("Initial:", assign, "loads", load, "makespan", cost)
while True:
    best, best_cost = None, cost
    for i in range(len(names)):
        nb = assign[:]
        nb[i] = 1 - nb[i]
        c, _ = makespan(nb)
        if c < best_cost:
            best, best_cost = nb, c
    if best is None:
        break
    assign, cost = best, best_cost
    print("Improved:", assign, "loads", makespan(assign)[1], "makespan", cost)

print("\nFinal schedule:")
for m in (0, 1):
    print(f"  Machine {m + 1}:", [j for j, a in zip(names, assign) if a == m])
print("Makespan:", cost, "(total work 27, so 14 is the best possible)")
