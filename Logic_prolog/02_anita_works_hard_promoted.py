% ============================================================
% GIVEN KNOWLEDGE BASE:
%   If a person works hard, they succeed.
%   If they succeed, they get promoted.
%   Anita works hard.
% PROVE: Anita gets promoted.
%
% FOL:
%   WorksHard(Anita)
%   forall x  WorksHard(x) -> Succeeds(x)
%   forall x  Succeeds(x)  -> Promoted(x)
%
% Proof (Modus Ponens twice):
%   WorksHard(Anita), WorksHard(Anita) -> Succeeds(Anita)  => Succeeds(Anita)
%   Succeeds(Anita),  Succeeds(Anita)  -> Promoted(Anita)  => Promoted(Anita)
%
% Run:  swipl 02_anita_works_hard_promoted.txt      (or start swipl and type  ?- consult('02_anita_works_hard_promoted.txt').)
% ============================================================

works_hard(anita).

succeeds(X) :- works_hard(X).
promoted(X) :- succeeds(X).

% ---------- QUERIES ----------
% ?- promoted(anita).    -> true.
% ?- succeeds(anita).    -> true.
% ?- promoted(Who).      -> Who = anita.
% ?- trace, promoted(anita).   (shows the backward-chaining proof steps)
