% ============================================================
% FIRST ORDER LOGIC IN PROLOG
%
% English statements:
%   a) John likes all kinds of food.
%   b) Apple and vegetables are food.
%   c) Anything anyone eats and is not killed by is food.
%   d) Anil eats peanuts and is still alive.
%   e) Harry eats everything that Anil eats.
%   f) Anyone who is alive is not killed.
% PROVE: John likes peanuts.
%
% FOL:
%   a) forall x  food(x) -> likes(John, x)
%   b) food(Apple) ^ food(Vegetables)
%   c) forall x,y  eats(y, x) ^ not killed(y) -> food(x)
%   d) eats(Anil, Peanuts) ^ alive(Anil)
%   e) forall x  eats(Anil, x) -> eats(Harry, x)
%   f) forall x  alive(x) -> not killed(x)
%
% Run:  swipl 03_first_order_logic.txt      (or start swipl and type  ?- consult('03_first_order_logic.txt').)
% ============================================================

food(apple).
food(vegetables).
food(X) :- eats(Y, X), not_killed(Y).

eats(anil, peanuts).
eats(harry, X) :- eats(anil, X).

alive(anil).
not_killed(X) :- alive(X).

likes(john, X) :- food(X).

% ---------- QUERIES ----------
% ?- likes(john, peanuts).   -> true.
% ?- likes(john, X).         -> X = apple ; X = vegetables ; X = peanuts.
% ?- eats(harry, X).         -> X = peanuts.
% ?- food(peanuts).          -> true.
