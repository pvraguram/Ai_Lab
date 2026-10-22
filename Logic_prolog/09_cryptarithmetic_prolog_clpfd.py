% ============================================================
% CRYPTARITHMETIC IN PROLOG (CLP(FD) constraint solver) - optional
% Same puzzles as 04_CSP/01_cryptarithmetic_backtracking.py
% Run:  swipl 09_cryptarithmetic_prolog_clpfd.txt      (or start swipl and type  ?- consult('09_cryptarithmetic_prolog_clpfd.txt').)
% ============================================================
:- use_module(library(clpfd)).

% SEND + MORE = MONEY
send_more_money([S,E,N,D,M,O,R,Y]) :-
    Vars = [S,E,N,D,M,O,R,Y],
    Vars ins 0..9, all_different(Vars),
    S #\= 0, M #\= 0,
              1000*S + 100*E + 10*N + D
            + 1000*M + 100*O + 10*R + E
    #= 10000*M + 1000*O + 100*N + 10*E + Y,
    label(Vars).

% SUN + FUN = SWIM
sun_fun_swim([S,U,N,F,W,I,M]) :-
    Vars = [S,U,N,F,W,I,M],
    Vars ins 0..9, all_different(Vars),
    S #\= 0, F #\= 0,
    100*S + 10*U + N + 100*F + 10*U + N
    #= 1000*S + 100*W + 10*I + M,
    label(Vars).

% TWO + TWO = FOUR
two_two_four([T,W,O,F,U,R]) :-
    Vars = [T,W,O,F,U,R],
    Vars ins 0..9, all_different(Vars),
    T #\= 0, F #\= 0,
    2 * (100*T + 10*W + O) #= 1000*F + 100*O + 10*U + R,
    label(Vars).

% ---------- QUERIES ----------
% ?- send_more_money(L).  -> L = [9,5,6,7,1,0,8,2].
% ?- sun_fun_swim(L).     -> L = [1,2,3,9,0,4,6]  (123 + 923 = 1046)
% ?- two_two_four(L).     -> L = [7,3,4,1,6,8]    (734 + 734 = 1468)
