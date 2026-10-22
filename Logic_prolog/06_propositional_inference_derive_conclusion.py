% ============================================================
% DERIVE A CONCLUSION SENTENCE USING PROPOSITIONAL LOGIC INFERENCE
%
% Sentences:
%   R : It is raining.
%   W : The ground is wet.
%   C : The match is cancelled.
%   H : Students stay in the hostel.
%
% Knowledge base:
%   1. R                (It is raining)
%   2. R -> W           (If it rains, the ground is wet)
%   3. W -> C           (If the ground is wet, the match is cancelled)
%   4. C -> H           (If the match is cancelled, students stay in)
%
% Inference rule: MODUS PONENS   (P, P -> Q  |-  Q)
%   From 1,2 : W
%   From W,3 : C
%   From C,4 : H        <- derived conclusion
%
% Run:  swipl 06_propositional_inference_derive_conclusion.txt      (or start swipl and type  ?- consult('06_propositional_inference_derive_conclusion.txt').)
%       ?- derive_all.
% ============================================================
:- dynamic fact/1.

fact(raining).

implies(raining, ground_wet).
implies(ground_wet, match_cancelled).
implies(match_cancelled, stay_in_hostel).

% apply Modus Ponens until nothing new can be derived
derive_all :-
    fact(P), implies(P, Q), \+ fact(Q), !,
    assertz(fact(Q)),
    write('Modus Ponens: '), write(P), write(' , '),
    write(P), write(' -> '), write(Q), write('  |-  '), write(Q), nl,
    derive_all.
derive_all :-
    write('Derived facts: '),
    findall(F, fact(F), L), write(L), nl.

% Same KB in plain Prolog rules (backward chaining)
raining.
ground_wet      :- raining.
match_cancelled :- ground_wet.
stay_in_hostel  :- match_cancelled.

% ---------- QUERIES ----------
% ?- derive_all.
%   Modus Ponens: raining , raining -> ground_wet  |-  ground_wet
%   Modus Ponens: ground_wet , ground_wet -> match_cancelled  |-  match_cancelled
%   Modus Ponens: match_cancelled , match_cancelled -> stay_in_hostel  |-  stay_in_hostel
% ?- stay_in_hostel.     -> true.
