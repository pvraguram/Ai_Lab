% Knowledge Base

% Facts
parent(john, mary).
parent(john, david).
parent(mary, susan).
parent(david, tom).

male(john).
male(david).
male(tom).

female(mary).
female(susan).

% Rules

father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

% Query
?- father(john, mary).