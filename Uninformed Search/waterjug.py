from collections import deque


def water_jug(jug1, jug2, target):
    start = (0, 0)
    queue = deque([start])
    visited = {start}
    parent = {start: (None, "Start")}

    while queue:
        current = queue.popleft()
        x, y = current

        if x == target or y == target:
            path = []
            while current is not None:
                previous, operation = parent[current]
                path.append((current, operation))
                current = previous
            path.reverse()
            return path

        states = [
            ((jug1, y), "Fill Jug 1"),
            ((x, jug2), "Fill Jug 2"),
            ((0, y), "Empty Jug 1"),
            ((x, 0), "Empty Jug 2"),
        ]

        amount = min(x, jug2 - y)
        states.append(
            ((x - amount, y + amount), "Pour Jug 1 -> Jug 2")
        )

        amount = min(y, jug1 - x)
        states.append(
            ((x + amount, y - amount), "Pour Jug 2 -> Jug 1")
        )

        for state, operation in states:
            if state not in visited:
                visited.add(state)
                parent[state] = (current, operation)
                queue.append(state)

    return None


jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

if target > max(jug1, jug2):
    print("\nTarget cannot be measured.")
else:
    solution = water_jug(jug1, jug2, target)
    if solution:
        for step, (state, operation) in enumerate(solution):
            x, y = state
            print(f"Step {step}: ({x}, {y}) -> {operation}")
        print("\nGoal reached!")
    else:
        print("\nNo solution exists.")