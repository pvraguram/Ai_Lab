import random

n = int(input("Population size: "))
l = int(input("Chromosome length: "))
g = int(input("Generations: "))
mr = float(input("Mutation rate: "))
expr = input("Fitness function f(x): ")

pop = [
    list(map(int, input(f"Chromosome {i+1}: ").split()))
    for i in range(n)
]


def fit(c):
    x = int(''.join(map(str, c)), 2)
    return eval(expr, {"__builtins__": {}}, {"x": x})


for gen in range(g):
    f = [fit(c) for c in pop]

    print(f"\nGeneration {gen+1}")

    for c, v in zip(pop, f):
        print(''.join(map(str, c)), "->", v)

    new = [pop[f.index(max(f))].copy()]

    while len(new) < n:
        total = sum(f)

        def select():
            r = random.uniform(0, total)
            s = 0

            for c, v in zip(pop, f):
                s += v
                if s >= r:
                    return c.copy()

            return pop[-1].copy()

        p1, p2 = select(), select()

        point = random.randint(1, l - 1)

        c1 = p1[:point] + p2[point:]
        c2 = p2[:point] + p1[point:]

        for c in (c1, c2):
            for i in range(l):
                if random.random() < mr:
                    c[i] ^= 1

        new += [c1, c2][:n - len(new)]

    pop = new


f = [fit(c) for c in pop]
i = f.index(max(f))

print("\nBest chromosome:", ''.join(map(str, pop[i])))
print("x =", int(''.join(map(str, pop[i])), 2))
print("Fitness =", f[i])
