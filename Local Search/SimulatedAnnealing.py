import random
import math

def f(x):
    return eval(expr, {"x": x, "math": math})

expr = input("Enter function : ")
choice = input("Find maximum or minimum? (max/min): ").lower()

x = float(input("Enter starting value: "))
T = 100
best = x

while T > 0.1:
    next_x = x + random.uniform(-1, 1)

    delta = f(next_x) - f(x)

    if choice == "min":
        delta = -delta

    if delta > 0 or random.random() < math.exp(delta / T):
        x = next_x

    if choice == "max" and f(x) > f(best):
        best = x
    elif choice == "min" and f(x) < f(best):
        best = x

    T *= 0.95

print("Best x:", best)
print("Function value:", f(best))