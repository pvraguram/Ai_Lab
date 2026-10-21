import heapq

graph = {
    'S': ['A', 'B'],
    'A': ['G'],
    'B': ['G'],
    'G': []
}

h = {
    'S': 4,
    'A': 3,
    'B': 1,
    'G': 0
}

def greedy_bfs(graph, start, goal):
    pq = [(h[start], start, [start])]
    visited = set()

    while pq:
        _, node, path = heapq.heappop(pq)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        pq, (h[neighbor], neighbor, path + [neighbor])
                    )

    return None

print(greedy_bfs(graph, 'S', 'G'))