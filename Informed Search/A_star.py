import heapq

graph = {
    'S': [('A', 2), ('B', 1)],
    'A': [('G', 9)],
    'B': [('G', 2)],
    'G': []
}

h = {
    'S': 4,
    'A': 3,
    'B': 1,
    'G': 0
}

def a_star(graph, start, goal):
    pq = [(h[start], 0, start, [start])]
    best_cost = {start: 0}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if g != best_cost.get(node):
            continue

        if node == goal:
            return path, g

        for neighbor, weight in graph[node]:
            new_g = g + weight

            if new_g < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_g
                new_f = new_g + h[neighbor]

                heapq.heappush(
                    pq, (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, float('inf')

print(a_star(graph, 'S', 'G'))