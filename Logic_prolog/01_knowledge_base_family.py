% ============================================================
% KNOWLEDGE BASE USING PROLOG (facts, rules, queries)
% Run:  swipl 01_knowledge_base_family.txt      (or start swipl and type  ?- consult('01_knowledge_base_family.txt').)
%       then type the queries shown at the bottom
% ============================================================

% ---------- FACTS ----------
parent(john, mary).
parent(john, tom).
parent(mary, ann).
parent(mary, raj).
parent(tom, bob).

male(john).  male(tom).  male(bob).  male(raj).
female(mary). female(ann).

% ---------- RULES ----------
father(X, Y)      :- parent(X, Y), male(X).
mother(X, Y)      :- parent(X, Y), female(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y)     :- parent(P, X), parent(P, Y), X \= Y.
brother(X, Y)     :- sibling(X, Y), male(X).
sister(X, Y)      :- sibling(X, Y), female(X).
uncle(U, X)       :- parent(P, X), brother(U, P).
cousin(X, Y)      :- parent(A, X), parent(B, Y), sibling(A, B).

% Recursive rule
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% ---------- QUERIES ----------
% ?- father(john, mary).        -> true.
% ?- mother(M, ann).            -> M = mary.
% ?- grandparent(john, G).      -> G = ann ; G = raj ; G = bob.
% ?- sibling(ann, S).           -> S = raj.
% ?- uncle(U, ann).             -> U = tom.
% ?- cousin(bob, C).            -> C = ann ; C = raj.
% ?- ancestor(john, D).         -> D = mary ; tom ; ann ; raj ; bob.
