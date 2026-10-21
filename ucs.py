import heapq

graph = {
    'S': [('A', 2), ('B', 1)],
    'A': [('G', 9)],
    'B': [('G', 2)],
    'G': []
}

def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        pq,
                        (cost + weight, neighbor, path + [neighbor])
                    )

    return None, float('inf')

print(ucs(graph, 'S', 'G'))