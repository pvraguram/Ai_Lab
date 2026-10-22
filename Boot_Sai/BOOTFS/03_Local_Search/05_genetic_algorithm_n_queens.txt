# ============================================================
# GENETIC ALGORITHM FOR N-QUEENS (N = 6)
# Shows chromosome encoding, crossover and mutation.
#
# CHROMOSOME ENCODING:
#   A list of N genes; gene i = column (0..N-1) of the queen in row i.
#   e.g. [1, 3, 5, 0, 2, 4] -> row0 col1, row1 col3, ...
# FITNESS = number of NON-attacking pairs (max = N*(N-1)/2 = 15)
# SELECTION = tournament selection
# CROSSOVER = single-point crossover
# MUTATION  = change one random gene to a random column
# Run: python 05_genetic_algorithm_n_queens.txt
# ============================================================
import random

N = 6
POP_SIZE = 50
MUTATION_RATE = 0.2
MAX_GEN = 200
MAX_FIT = N * (N - 1) // 2

def fitness(ch):
    attacks = sum(1 for i in range(N) for j in range(i + 1, N)
                  if ch[i] == ch[j] or abs(ch[i] - ch[j]) == j - i)
    return MAX_FIT - attacks

def random_chromosome():
    return [random.randrange(N) for _ in range(N)]

def tournament(pop, k=3):
    return max(random.sample(pop, k), key=fitness)

def crossover(p1, p2, verbose=False):
    point = random.randint(1, N - 1)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    if verbose:
        print(f"  Crossover at point {point}:")
        print(f"    Parent1 {p1} | Parent2 {p2}")
        print(f"    Child1  {c1} | Child2  {c2}")
    return c1, c2

def mutate(ch, verbose=False):
    if random.random() < MUTATION_RATE:
        i = random.randrange(N)
        old = ch[i]
        ch[i] = random.randrange(N)
        if verbose:
            print(f"  Mutation: gene {i} changed {old} -> {ch[i]}  => {ch}")
    return ch

def show(ch):
    for r in range(N):
        print("   " + " ".join("Q" if ch[r] == c else "." for c in range(N)))

def run_ga(show_ops):
    population = [random_chromosome() for _ in range(POP_SIZE)]
    for gen in range(MAX_GEN):
        population.sort(key=fitness, reverse=True)
        best = population[0]
        if gen % 20 == 0 or fitness(best) == MAX_FIT:
            print(f"Generation {gen}: best {best} fitness {fitness(best)}/{MAX_FIT}")
        if fitness(best) == MAX_FIT:
            return best
        new_pop = population[:2]                       # elitism: keep best 2
        first = True
        while len(new_pop) < POP_SIZE:
            p1, p2 = tournament(population), tournament(population)
            verbose = show_ops and first and gen < 2   # print operators early
            c1, c2 = crossover(p1, p2, verbose)
            c1, c2 = mutate(c1, verbose), mutate(c2, verbose)
            new_pop += [c1, c2]
            first = False
        population = new_pop[:POP_SIZE]
    return population[0]

# ---------- encoding example ----------
example = random_chromosome()
print("CHROMOSOME ENCODING EXAMPLE:", example,
      "fitness =", fitness(example), "/", MAX_FIT)
show(example)

print("\nOPERATOR DEMO:")
pa, pb = random_chromosome(), random_chromosome()
ca, cb = crossover(pa, pb, verbose=True)
i = random.randrange(N)
before = ca[:]
ca[i] = (ca[i] + 1 + random.randrange(N - 1)) % N    # guaranteed change
print(f"  Mutation: {before} -> gene {i} changed {before[i]} -> {ca[i]} => {ca}\n")

# ---------- run (restart if population gets stuck) ----------
run = 1
while True:
    print(f"=== GA run {run} ===")
    best = run_ga(show_ops=(run == 1))
    if fitness(best) == MAX_FIT:
        break
    print("Stuck in local optimum -> restarting with a new population\n")
    run += 1

print("\nSOLUTION:", best, "fitness", fitness(best), "/", MAX_FIT)
show(best)
