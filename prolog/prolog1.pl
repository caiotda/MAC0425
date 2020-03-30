pai(joaquim, valeria).
pai(joaquim, reginaldo).
pai(joaquim, ricardo).
pai(joaquim, rogerio).

pai(lidio, caio).
pai(lidio, pamela).

pai(reginaldo, guilherme).
pai(reginaldo, carla).
pai(reginaldo, lucas).

pai(rogerio, duda).
pai(rogerio, ana).

mae(maria, valeria).
mae(maria, reginaldo).
mae(maria, ricardo).
mae(maria, rogerio).

pai(claudio, maria).
pai(claudio, ventania).


mae(valeria, caio).
mae(valeria, pamela).

casado(valeria, lidio).
irmao(maria, rosa).
irmao(rosa, maria).


progenitor(X,Y) :- pai(X,Y). %predicato (função)
progenitor(X,Y) :- mae(X,Y). %predicado (função)


irmao(X, Y) :-
 	progenitor(Z, X),
 	progenitor(Z, Y),
	X \= Y.


tio(X,Y):-
    progenitor(Z, Y),
    irmao(X, Z).
tio(X,Y):-
    progenitor(Z, Y),
    irmao(Z, W),
    casado(W, X).

tio_avo(X,Y):-
    progenitor(Z, Y),
    tio(X, Z).

avo(X, Y) :-
    progenitor(X, Z),
    progenitor(Z, Y).

primo(X,Y) :-
    progenitor(Z, X),
    progenitor(P, Y),
    irmao(Z, P).


ancestral(X, Y) :- progenitor(X, Y). %clausula de parada
ancestral(X,Y) :-
    progenitor(X, Z),
 ancestral(Z, Y).

ancestrais_masculinos(X, Y) :- pai(X, Y).
ancestrais_masculinos(X, Y) :-
    pai(Z, Y),
    ancestrais_masculinos(X, Z).

% Exercicios:
% 1) Incluir avós no predicado (avo) - done
% 2) Implementar primo(X,Y), tio(X,Y) e tio_avo(X,Y) - done
% 3) Implementar ancestrais_masculinos, não deve fornecer sara como resposta - done
% 4) Implementar mesma geração: irmãos, primos_irmãos, primos de n-ésimo grau - Todo mundo no 
% mesmo nivel da arvore. (Tentar fazer de forma recursiva.)