# ============================================================
# WATER JUG PROBLEM FORMULATED AS A CSP
# Jug A = 4 L, Jug B = 3 L, Goal: exactly 2 L in Jug A
#
# CSP FORMULATION
#   Variables  : S0, S1, ..., Sk   (state of the jugs after each step)
#   Domains    : Si = (a, b) with 0 <= a <= 4, 0 <= b <= 3
#   Constraints:
#     C1 (initial)    : S0 = (0, 0)
#     C2 (capacity)   : 0 <= a <= 4 and 0 <= b <= 3
#     C3 (transition) : S(i+1) must be reachable from Si by ONE legal
#                       action (fill, empty, pour A->B, pour B->A)
#     C4 (no repeat)  : all states are different (AllDiff)
#     C5 (goal)       : Sk has a = 2
# Solved with backtracking, trying k = 1, 2, 3 ... (shortest first)
# Run: python 03_water_jug_csp.txt
# ============================================================
CAP_A, CAP_B, GOAL = 4, 3, 2

domain = [(a, b) for a in range(CAP_A + 1) for b in range(CAP_B + 1)]   # C2

def transition_ok(s, t):                                            # C3
    a, b = s
    p_ab = min(a, CAP_B - b)
    p_ba = min(b, CAP_A - a)
    legal = {
        (CAP_A, b): "Fill A",      (a, CAP_B): "Fill B",
        (0, b): "Empty A",         (a, 0): "Empty B",
        (a - p_ab, b + p_ab): "Pour A->B",
        (a + p_ba, b - p_ba): "Pour B->A",
    }
    return legal.get(t) if t != s else None

def backtrack(assignment, k):
    if len(assignment) == k + 1:
        return assignment if assignment[-1][0] == GOAL else None       # C5
    prev = assignment[-1]
    for value in domain:
        if value in assignment:                                         # C4
            continue
        if transition_ok(prev, value) is None:                          # C3
            continue
        result = backtrack(assignment + [value], k)
        if result:
            return result
    return None

for k in range(1, 15):
    sol = backtrack([(0, 0)], k)                                        # C1
    if sol:
        print(f"Solution with k = {k} steps (all constraints satisfied):")
        print(f"  S0 = {sol[0]}  (initial)")
        for i in range(1, len(sol)):
            print(f"  S{i} = {sol[i]}  <- {transition_ok(sol[i - 1], sol[i])}")
        print(f"\nGoal constraint: Jug A = {sol[-1][0]} L  ✓")
        break
