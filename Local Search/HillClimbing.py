import math

def f(x):
    return eval(expr, {"__builtins__": {}}, {"x": x, "math": math})

expr = input("Enter function : ")
choice = input("Find maximum or minimum? (max/min): ").lower()

x = float(input("Enter starting value: "))
step = float(input("Enter step size: "))

while True:
    current = f(x)
    left = x - step
    right = x + step

    if choice == "max":
        if f(left) > current:
            x = left
        elif f(right) > current:
            x = right
        else:
            break

    elif choice == "min":
        if f(left) < current:
            x = left
        elif f(right) < current:
            x = right
        else:
            break

    else:
        print("Invalid choice!")
        break

print("Best x:", x)
print("Function value:", f(x))