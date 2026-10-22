% ============================================
% WUMPUS WORLD - PROPOSITIONAL REASONING
% ============================================

% --------------------------------------------
% FACTS
% --------------------------------------------

% Cell (1,1) is safe
safe(1,1).

% There is a pit at (3,1)
pit(3,1).

% Wumpus is at (4,1)
wumpus(4,1).

% Gold is at (2,3)
gold(2,3).


% --------------------------------------------
% BREEZE RULE
% --------------------------------------------

% A cell is breezy if an adjacent cell
% contains a pit.

breeze(X,Y) :-
    adjacent(X,Y,A,B),
    pit(A,B).


% --------------------------------------------
% STENCH RULE
% --------------------------------------------

% A cell has stench if an adjacent cell
% contains the Wumpus.

stench(X,Y) :-
    adjacent(X,Y,A,B),
    wumpus(A,B).


% --------------------------------------------
% ADJACENT CELLS
% --------------------------------------------

adjacent(X,Y,A,Y) :-
    A is X + 1.

adjacent(X,Y,A,Y) :-
    A is X - 1.

adjacent(X,Y,X,B) :-
    B is Y + 1.

adjacent(X,Y,X,B) :-
    B is Y - 1.


% --------------------------------------------
% SAFE CELL
% --------------------------------------------

safe_cell(X,Y) :-
    \+ pit(X,Y),
    \+ wumpus(X,Y).