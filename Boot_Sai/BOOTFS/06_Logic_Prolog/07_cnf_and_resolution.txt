% ============================================================
% CNF CONVERSION AND RESOLUTION IN PROLOG
%
% CNF steps:
%   1. Eliminate <->  :  A<->B  becomes (A->B) ^ (B->A)
%   2. Eliminate ->   :  A->B   becomes  not A v B
%   3. Move NOT inward (De Morgan, double negation)
%   4. Distribute OR over AND
%
% RESOLUTION (proof by refutation):
%   Add NOT(goal) to the clauses; repeatedly resolve pairs of
%   clauses with complementary literals. If the EMPTY clause []
%   is derived, the KB entails the goal.
%
% Example: KB = { P -> Q,  Q -> R,  P }   Prove R
%
% Run:  swipl 07_cnf_and_resolution.txt      (or start swipl and type  ?- consult('07_cnf_and_resolution.txt').)
%       ?- demo.
% ============================================================

% ------------------- CNF CONVERSION -------------------
nnf(iff(A,B), F)       :- !, nnf(and(imp(A,B), imp(B,A)), F).
nnf(imp(A,B), F)       :- !, nnf(or(not(A), B), F).
nnf(and(A,B), and(X,Y)):- !, nnf(A, X), nnf(B, Y).
nnf(or(A,B),  or(X,Y)) :- !, nnf(A, X), nnf(B, Y).
nnf(not(not(A)), F)    :- !, nnf(A, F).
nnf(not(and(A,B)), F)  :- !, nnf(or(not(A), not(B)), F).
nnf(not(or(A,B)), F)   :- !, nnf(and(not(A), not(B)), F).
nnf(not(imp(A,B)), F)  :- !, nnf(and(A, not(B)), F).
nnf(not(iff(A,B)), F)  :- !, nnf(not(and(imp(A,B), imp(B,A))), F).
nnf(F, F).

dist(and(A,B), and(X,Y)) :- !, dist(A, X), dist(B, Y).
dist(or(A,B), F)         :- !, dist(A, X), dist(B, Y), distr(X, Y, F).
dist(L, L).

distr(and(A,B), C, and(X,Y)) :- !, distr(A, C, X), distr(B, C, Y).
distr(A, and(B,C), and(X,Y)) :- !, distr(A, B, X), distr(A, C, Y).
distr(A, B, or(A,B)).

cnf(F, C) :- nnf(F, N), dist(N, C).

% CNF formula -> list of clauses (each clause = list of literals)
to_clauses(and(A,B), Cs) :- !, to_clauses(A, C1), to_clauses(B, C2), append(C1, C2, Cs).
to_clauses(F, [C])       :- literals(F, L), sort(L, C).
literals(or(A,B), L) :- !, literals(A, L1), literals(B, L2), append(L1, L2, L).
literals(X, [X]).

% ------------------- RESOLUTION -------------------
complement(not(X), X) :- !.
complement(X, not(X)).

tautology(C) :- member(L, C), complement(L, N), member(N, C), !.

resolve(C1, C2, R) :-
    select(L, C1, R1), complement(L, N), select(N, C2, R2),
    append(R1, R2, R3), sort(R3, R).

refute(Cs) :-
    member([], Cs), !,
    write('Empty clause [] derived  =>  GOAL PROVED'), nl.
refute(Cs) :-
    member(C1, Cs), member(C2, Cs),
    resolve(C1, C2, R), \+ tautology(R), \+ member(R, Cs), !,
    write('Resolve '), write(C1), write(' with '), write(C2),
    write('  =>  '), write(R), nl,
    refute([R|Cs]).
refute(_) :-
    write('No new clauses: goal NOT provable'), nl.

prove(KB, Goal) :-
    findall(C, ( member(F, [not(Goal)|KB]),
                 cnf(F, CF), to_clauses(CF, Cl), member(C, Cl) ), Cs0),
    sort(Cs0, Cs),
    write('Clauses (KB + negated goal): '), write(Cs), nl,
    refute(Cs).

demo :-
    write('--- CNF conversion ---'), nl,
    F1 = imp(p, and(q, r)),
    cnf(F1, C1), write(F1), write('  =>  '), write(C1), nl,
    F2 = iff(p, q),
    cnf(F2, C2), write(F2), write('  =>  '), write(C2), nl,
    F3 = not(or(p, and(q, r))),
    cnf(F3, C3), write(F3), write('  =>  '), write(C3), nl, nl,
    write('--- Resolution: KB = {P->Q, Q->R, P}, prove R ---'), nl,
    prove([imp(p,q), imp(q,r), p], r).

% ---------- QUERIES ----------
% ?- demo.
% ?- cnf(imp(p, and(q,r)), C).
%    C = and(or(not(p),q), or(not(p),r)).
% ?- prove([imp(p,q), imp(q,r), p], r).
%    ... Empty clause [] derived => GOAL PROVED
