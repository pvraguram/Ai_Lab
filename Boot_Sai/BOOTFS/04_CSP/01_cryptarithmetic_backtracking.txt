# ============================================================
# CRYPTARITHMETIC USING CSP: BACKTRACKING + CONSTRAINT SPECIFICATION
# Solves ANY puzzle of the form WORD1 + WORD2 = WORD3:
#   SEND + MORE = MONEY,  SUN + FUN = SWIM,  TWO + TWO = FOUR
#
# CSP FORMULATION
#   Variables  : each distinct letter
#   Domains    : digits 0..9
#   Constraints: 1) all letters take DIFFERENT digits (AllDiff)
#                2) leading letters != 0
#                3) column-wise addition with carries:
#                   col_sum = letter1 + letter2 + carry_in
#                   col_sum % 10 = result letter, carry_out = col_sum // 10
# Backtracking assigns letters column by column (right to left)
# and checks each column as soon as its letters are known (pruning).
# Run: python 01_cryptarithmetic_backtracking.txt
# ============================================================

def solve(w1, w2, w3):
    n = len(w3)
    a, b, r = w1.rjust(n, '0'), w2.rjust(n, '0'), w3       # pad with '0'
    leading = {w1[0], w2[0], w3[0]}
    # variable order: letters in the order they appear right-to-left
    order = []
    for col in range(n - 1, -1, -1):
        for ch in (a[col], b[col], r[col]):
            if ch != '0' and ch not in order:
                order.append(ch)
    assign = {'0': 0}
    used = set()
    steps = [0]

    def val(ch):
        return assign.get(ch)

    def consistent():
        # check every column whose letters are all assigned (right to left)
        carry = 0
        for col in range(n - 1, -1, -1):
            x, y, z = val(a[col]), val(b[col]), val(r[col])
            if x is None or y is None or z is None:
                return True               # cannot check further yet
            s = x + y + carry
            if s % 10 != z:
                return False
            carry = s // 10
        return carry == 0

    def backtrack(i):
        if i == len(order):
            return consistent()
        letter = order[i]
        for d in range(10):
            if d in used or (d == 0 and letter in leading):
                continue
            assign[letter] = d; used.add(d); steps[0] += 1
            if consistent() and backtrack(i + 1):
                return True
            del assign[letter]; used.discard(d)      # BACKTRACK
        return False

    if backtrack(0):
        num = lambda w: int("".join(str(assign[c]) for c in w))
        print(f"{w1} + {w2} = {w3}")
        print("  Mapping:", {k: v for k, v in sorted(assign.items()) if k != '0'})
        print(f"  {num(w1):>6}\n+ {num(w2):>6}\n  ------\n  {num(w3):>6}")
        print("  Assignments tried:", steps[0], "\n")
    else:
        print(f"{w1} + {w2} = {w3}: no solution\n")

solve("SEND", "MORE", "MONEY")
solve("SUN", "FUN", "SWIM")
solve("TWO", "TWO", "FOUR")
