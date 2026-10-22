# ============================================================
# HILL CLIMBING - LOCAL SEARCH (any application)
# Application: maximize f(x) = -(x-7)^2 + 49 for integer x in [0,20]
# Also shows the LOCAL MAXIMUM problem on a bumpy landscape.
# Run: python 01_hill_climbing_any_application.txt
# ============================================================
import random

def hill_climb(f, start, lo, hi):
    current = start
    print(f"  start x={current}, f={f(current)}")
    while True:
        neighbors = [n for n in (current - 1, current + 1) if lo <= n <= hi]
        best = max(neighbors, key=f)
        if f(best) <= f(current):          # no uphill move -> stop
            return current
        current = best
        print(f"  move to x={current}, f={f(current)}")

# 1) Smooth function: hill climbing finds the GLOBAL maximum
f1 = lambda x: -(x - 7) ** 2 + 49
print("Application 1: maximize -(x-7)^2 + 49")
x = hill_climb(f1, 0, 0, 20)
print("Result: x =", x, " f(x) =", f1(x), "\n")

# 2) Bumpy landscape: may get stuck at a LOCAL maximum
values = [1, 3, 6, 4, 2, 5, 9, 12, 8, 3]
f2 = lambda i: values[i]
print("Application 2: landscape", values)
x = hill_climb(f2, 0, 0, len(values) - 1)
print("Stuck at index", x, "value", values[x], "(local maximum)")
print("Global maximum is", max(values), "at index", values.index(max(values)), "\n")

# 3) Random-restart hill climbing fixes it
random.seed(1)
best = None
for r in range(5):
    s = random.randint(0, len(values) - 1)
    print(f"Restart {r + 1}:")
    res = hill_climb(f2, s, 0, len(values) - 1)
    if best is None or values[res] > values[best]:
        best = res
print("Random-restart result: index", best, "value", values[best])
