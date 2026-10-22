% ============================================================
% PROPOSITIONAL LOGIC - TEST ENTAILMENT USING A SIMPLE KB
% KB |= Q  iff  Q is TRUE in EVERY model (truth assignment)
%               in which KB is TRUE.   (Model checking / truth table)
%
% Formula syntax: atoms p, q, r ...
%   not(F), and(A,B), or(A,B), imp(A,B), iff(A,B)
%
% Example KB:  P -> Q,   Q -> R,   P
% Query:       R      (entailed)      and   not(P) (not entailed)
%
% Run:  swipl 05_propositional_entailment.txt      (or start swipl and type  ?- consult('05_propositional_entailment.txt').)
%       ?- demo.
% ============================================================

% generate every truth assignment for a list of variables
assign([], []).
assign([V|Vs], [V-T|Rest]) :- member(T, [true, false]), assign(Vs, Rest).

% truth value of a formula in a model M
holds(P, M)         :- atom(P), member(P-true, M).
holds(not(F), M)    :- \+ holds(F, M).
holds(and(A,B), M)  :- holds(A, M), holds(B, M).
holds(or(A,B), M)   :- ( holds(A, M) -> true ; holds(B, M) ).
holds(imp(A,B), M)  :- holds(or(not(A), B), M).
holds(iff(A,B), M)  :- holds(imp(A,B), M), holds(imp(B,A), M).

% KB entails Q if there is NO model where KB is true and Q is false
entails(KB, Q, Vars) :-
    \+ ( assign(Vars, M), holds(KB, M), \+ holds(Q, M) ).

tv(F, M, 'T') :- holds(F, M), !.
tv(_, _, 'F').

truth_table(KB, Q, Vars) :-
    write(Vars), write('  KB  Query'), nl,
    forall(assign(Vars, M),
           ( findall(X, member(_-X, M), Vals),
             tv(KB, M, K), tv(Q, M, R),
             write(Vals), write('   '), write(K), write('    '), write(R), nl )).

kb(and(imp(p,q), and(imp(q,r), p))).

demo :-
    kb(KB), Vars = [p,q,r],
    write('KB = (P->Q) ^ (Q->R) ^ P'), nl, nl,
    truth_table(KB, r, Vars), nl,
    ( entails(KB, r, Vars)      -> write('KB |= R      : TRUE')  ; write('KB |= R      : FALSE') ), nl,
    ( entails(KB, q, Vars)      -> write('KB |= Q      : TRUE')  ; write('KB |= Q      : FALSE') ), nl,
    ( entails(KB, not(p), Vars) -> write('KB |= not P  : TRUE')  ; write('KB |= not P  : FALSE') ), nl.

% ---------- QUERIES ----------
% ?- demo.
% ?- kb(K), entails(K, r, [p,q,r]).                 -> true.
% ?- entails(and(imp(p,q), p), q, [p,q]).           -> true.  (Modus Ponens)
% ?- entails(and(imp(p,q), q), p, [p,q]).           -> false. (affirming the consequent)
