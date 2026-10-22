% Forward Chaining in Prolog

% Facts
fact(a).
fact(b).

% Rules
rule(a, c).
rule(b, d).
rule(c, e).
rule(d, e).

% Forward chaining
forward_chain(Facts, Rules, NewFacts) :-
    apply_rules(Facts, Rules, Derived),
    subtract(Derived, Facts, New),
    (
        New = []
        ->
        NewFacts = Facts
        ;
        append(Facts, New, UpdatedFacts),
        forward_chain(UpdatedFacts, Rules, NewFacts)
    ).

% Apply rules
apply_rules(Facts, Rules, Derived) :-
    findall(Y,
        (
            member(rule(X, Y), Rules),
            member(X, Facts)
        ),
        Derived).