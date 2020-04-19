%%%%% Insira aqui os seus predicados.

%% OBS: Criei o predicado list_same_length inspirado nessa thread do Stack overflow:
%% https://stackoverflow.com/questions/13111591/prolog-check-if-two-lists-have-the-same-elements
%% Pois estava tendo problemas, no exercício 2, para checar se os conjuntos eram compatíveis.
%%%%% Use quantos predicados auxiliares julgar necess�rio

%------------------------- Exercício 1 ------------------------------%
lista_para_conjunto(Xs, Cs) :- 
    lista_para_conjunto_helper(Xs, [], Cs).
    
lista_para_conjunto_helper([], Cs, Cs).

lista_para_conjunto_helper([Xs|Xt], H, Cs) :-
    not(member(Xs, H)),
    append(H, [Xs], Res),
    lista_para_conjunto_helper(Xt, Res, Cs).

lista_para_conjunto_helper([Xs|Xt], H, Cs) :-
    member(Xs, H),
    lista_para_conjunto_helper(Xt, H, Cs).

%------------------------- Exercício 2 ------------------------------%

list_same_length([], []).
list_same_length([_|Xs], [_|Ys]) :-
    list_same_length(Xs, Ys).

mesmo_conjunto(Ls, Cs) :-
    list_same_length(Ls, Cs),
    mesmo_conjunto_helper(Ls, Cs).

mesmo_conjunto_helper([], _).
mesmo_conjunto_helper([H|T], Cs) :-
    member(H, Cs),
    mesmo_conjunto_helper(T, Cs).
%------------------------- Exercício 3 ------------------------------%
uniao_conjunto(Cs, Ls, Res) :-
    uniao_conjunto_helper(Cs, Ls, [], Res).

uniao_conjunto_helper([], Ls, Acc, Res) :-
    append(Acc, Ls, NewAcc),
    Res = NewAcc.

uniao_conjunto_helper([Ch|Ct], Ls, Acc, Res) :-
    append(Acc, [Ch], NewAcc),
    uniao_conjunto_helper(Ct, Ls, NewAcc, Res).

%------------------------- Exercício 4 - incompleto. Percebi que tava fazendo o quatro enquanto 
% resolvia 3, então vou deixar o WIP aqui ------------------------------%
inter_conjunto([], Ds, Ds).
inter_conjunto(Cs, [], Cs).

inter_conjunto(Cs, Ds, Res) :-
    inter_conjunto_helper(Cs, Ds, Res). %aqui sim vou descascar os elementos

inter_conjunto_helper([Ch| Ct], [_|Dt], Res) :-
    member(Ch, Dt),
    append(Res, [Ch], NewRes),
    inter_conjunto_helper(Ct, Dt, NewRes).

inter_conjunto_helper([_|Ct], [Dh|Dt], Res) :-
    member(Dh, Ct),
    append(Res, [Dh], NewRes),
    inter_conjunto_helper(Ct, Dt, NewRes).

inter_conjunto_helper([_|Ct], [_|Dt], Res) :- % não achei intersecção entre os elementos atuais,
                                              % segue em frente então.
    inter_conjunto_helper(Ct, Dt, Res).
%%%%%%%% Fim dos predicados adicionados
%%%%%%%% Os testes come�am aqui.
%%%%%%%% Para executar os testes, use a consulta:   ?- run_tests.

%%%%%%%% Mais informacoes sobre testes podem ser encontradas em:
%%%%%%%%    https://www.swi-prolog.org/pldoc/package/plunit.html

:- begin_tests(conjuntos).
test(lista_para_conjunto, all(Xs=[[1,a,3,4]]) ) :-
    lista_para_conjunto([1,a,3,3,a,1,4], Xs).
test(lista_para_conjunto2,fail) :-
    lista_para_conjunto([1,a,3,3,a,1,4], [a,1,3,4]).

test(mesmo_conjunto, set(Xs=[[1,a,3],[1,3,a],[a,1,3],[a,3,1],[3,a,1],[3,1,a]])) :-
    mesmo_conjunto([1,a,3], Xs).
test(uniao_conjunto2,fail) :-
    mesmo_conjunto([1,a,3,4], [1,3,4]).

test(uniao_conjunto, set(Ys==[[1,a,3],[1,3,a],[a,1,3],[a,3,1],[3,a,1],[3,1,a]])) :-
    uniao_conjunto([1,a], [a,3], Xs),
    mesmo_conjunto(Xs,Ys).
test(uniao_conjunto2,fail) :-
    uniao_conjunto([1,a,3,4], [1,2,3,4], [1,1,a,2,3,3,4,4]).

test(inter_conjunto, all(Xs==[[1,3,4]])) :-
    inter_conjunto([1,a,3,4], [1,2,3,4], Xs).
test(inter_conjunto2,fail) :-
    inter_conjunto([1,a,3,4], [1,2,3,4], [1,1,3,3,4,4]).

test(diferenca_conjunto, all(Xs==[[2]])) :-
    diferenca_conjunto([1,2,3], [3,a,1], Xs).
test(diferenca_conjunto2,fail) :-
    diferenca_conjunto([1,3,4], [1,2,3,4], [_|_]).

:- end_tests(conjuntos).
