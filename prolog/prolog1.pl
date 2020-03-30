pai(abraao, isac). %fato
pai(isac, jaco). %fato
pai(isac, esau). %fato
pai(jaco, jose).
pai(esau, assis).

mae(sara, isac).
mae(rebeca, jaco).
mae(rebeca, esau).
mae(raquel, jose).

progenitor(X,Y) :- pai(X,Y). %predicato (função)
progenitor(X,Y) :- mae(X,Y). %predicado (função)

irmao(X, Y) :-
 	progenitor(Z, X),
 	progenitor(Z, Y),
 	X @< Y. %lexicograficamente menor

avo(X, Y) :-
    progenitor(X, Z),
    progenitor(Z, Y).

tio(X, Y) :- %ta meio errado.
    progenitor(H, Y),
    irmao(X, H).

primo(X,Y) :-
	progenitor(Z,X),
    progenitor(H, Y),
    irmao(Z, H).

ancestral(X, Y) :- progenitor(X, Y). %clausula de parada
ancestral(X,Y) :-
    progenitor(X, Z),
 ancestral(Z, Y).

% Exercicios:
% 1) Incluir avós no predicado (avo) - done
% 2) Implementar primo(X,Y), tio(X,Y) e tio_avo(X,Y)
% 3) Implementar ancestrais_masculinos, não deve fornecer sara como resposta
% 4) Implementar mesma geração: irmãos, primos_irmãos, primos de n-ésimo grau - Todo mundo no 
% mesmo nivel da arvore. (Tentar fazer de forma recursiva.)