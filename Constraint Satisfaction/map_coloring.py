def is_safe(node, color, colors, graph):
    for neighbour in graph[node]:
        if colors.get(neighbour) == color:
            return False

    return True


def map_coloring(nodes, graph, number_of_colors):
    colors = {}

    def solve(index):
        if index == len(nodes):
            return True

        node = nodes[index]

        for color in range(1, number_of_colors + 1):
            if is_safe(node, color, colors, graph):
                colors[node] = color

                if solve(index + 1):
                    return True

                del colors[node]

        return False

    if solve(0):
        print("\nMap Coloring:")
        for node in nodes:
            print(node, "-> Color", colors[node])
    else:
        print("No solution possible")


n = int(input("Enter number of regions: "))

nodes = []

for i in range(n):
    node = input(f"Enter region {i + 1}: ")
    nodes.append(node)

graph = {}

for node in nodes:
    graph[node] = []

e = int(input("Enter number of adjacent pairs: "))

print("Enter adjacent region pairs:")

for i in range(e):
    a, b = input().split()

    graph[a].append(b)
    graph[b].append(a)

number_of_colors = int(input("Enter number of colors: "))

map_coloring(nodes, graph, number_of_colors)
