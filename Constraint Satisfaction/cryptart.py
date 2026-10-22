from itertools import permutations

words = input("Enter words: ").upper().split()
result = input("Enter result: ").upper()
letters = set("".join(words) + result)

if len(letters) > 10:
    print("No solution")
    exit()

leading = {w[0] for w in words + [result]}


def value(word, d):
    return int("".join(str(d[x]) for x in word))


for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))
    if any(d[x] == 0 for x in leading):
        continue
    if sum(value(w, d) for w in words) == value(result, d):
        print("\nSolution:")
        for x in sorted(d):
            print(x, "=", d[x])
        print("\nEquation:")
        print(" + ".join(str(value(w, d)) for w in words),
              "=", value(result, d))
        break
else:
    print("No solution")