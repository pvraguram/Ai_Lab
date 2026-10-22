import heapq

def heuristic(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)

    return distance

def solve(start, goal):
    queue = [(heuristic(start, goal), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while queue:
        f, g, state = heapq.heappop(queue)

        if g != cost[state]:
            continue

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]

            for state in reversed(path):
                for i in range(0, 9, 3):
                    print(state[i:i + 3])
                print()

            print("Minimum moves:", len(path) - 1)
            return

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_pos = nr * 3 + nc
                new_state = list(state)
                new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
                new_state = tuple(new_state)

                new_g = g + 1

                if new_g < cost.get(new_state, float("inf")):
                    cost[new_state] = new_g
                    parent[new_state] = state
                    new_f = new_g + heuristic(new_state, goal)
                    heapq.heappush(queue, (new_f, new_g, new_state))

    print("No solution found.")

start = tuple(map(int, input("Enter initial state (0 for blank): ").split()))
goal = tuple(map(int, input("Enter goal state (0 for blank): ").split()))

if len(start) != 9 or len(goal) != 9 or set(start) != set(range(9)) or set(goal) != set(range(9)):
    print("Invalid puzzle. Enter each number from 0 to 8 exactly once.")
else:
    solve(start, goal)
