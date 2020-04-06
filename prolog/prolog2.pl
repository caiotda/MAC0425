% Prolog segue a logica de primeira ordem

% Constantes: identificadores. Começam com letra minúscula (ou aspas); abraao, bla, ble, caio, 'Avô'
% Símbolos funcionais: identificadores com argumentos - pai(arg1, arg2).
    % numero de argumentos = aridade do simbolo

% predicados id(arg1, ... argn) -> 
    % aridade tbm é a quantidade de argumentos
% Diferença entre predicado e simbolo funcional : simbolo funcional é a definição do predicado,
% é o que a linguagem parseia. A identidade logica de um functor é o predicado.

% Ex.:  pai(pai(X), X) :- ...: uso não recomendado.
% Variáveis : Começam com letra maiúsucla ou _: X, _valor, _. A variável _ é uma variável especial
% Numeric: 1, 2, ..., -0.43.

% termos atomicos: átomos, variáveis, numeric.
% termos complexos: funcional (arg1, ..., argn).

% Mecanismo básico do prolog: unificação.
% ?- X = c. :exemplo de unificação.
% f(X, g(Y,Z)) = f(c, g(X,Y)).
% ?-  X = c, g(Y,Z) = g(X,Y).     []
% ?-  g(Y,Z) = g(c, Y).           [X = c] - apliquei a substituição X = c naquele termo.
% ?- Y = c, Z = Y.                [X = c]
% ?- Z = c.                       [X = c, Y = c]
% true.                           [X = c, Y = c, Z = c] - Substituição resposta

pai(abraao, isaac) :- true.
pai(isaac, jaco). %duas sintaxes pra escrever fatos
pai(abraao, maria).

mae(maria, epaminondas).

avo(X,Y) :- % Se X é avô de Y, então vale que X tem um filho Z que é pai de Y.
    pai(X,Z), % apesar da virgula representar um "e" - e nele não importa a ordem - , pro prolog 
    pai(Z,Y). % importa a ordem sim. Isso muda a ordem da resposta.
avo(X,Y) :-
    pai(X, Z),
    mae(Z, Y).

% cut
% A lista é uma estrutura de dados recursiva na qual sempre temos uma lista vazia ao fim (base da 
% recursao)

% Cut: Operador para "fatiar" um elemento da lista. No lado esquerdo fica o elemento selecionado,
% no lado direito, o resto da lista

% ?- [a,b,c] = [HEAD | rest].
% HEAD = a, rest = [b,c]
% ?- [b, c] = [cabeça | cauda].
% cabeça = b, c = [cauda]
% ?- [c] = [H | T].
% H = c, T = [].


%operador member

% descasca a lista e retorna os membros de uma lista, um por um.

membro(X ,[X | _] ).
membro(X ,[_|Ys]):-
    membro(X, Ys).


concat([], Ys, Ys).
concat([X1| Xs], Ys, [X1| Zs]) :-
    concat(Xs, Ys, Zs).

prefixo([], _).
prefixo([X | Xs], [X| Ys]) :-
    prefixo(Xs, Ys).

sufixo(L1, L1).
sufixo(X, [_|Ys]):-
    sufixo(X, Ys).

inverte([], Aux, Aux).
inverte([X|Xs], Aux, Ys) :-
    inverte([Xs], [X | Aux], Ys).

tamanho([], 0).
tamanho([_| Xs], N):-
    tamanho(Xs, M),
    M is N + 1.

contem_inteiro([X | _]) :- integer(X).
contem_inteiro([_| Xs]) :- contem_inteiro(Xs).

lista_de_inteiros([]).
lista_de_inteiros([X| Xs]) :- integer(X), lista_de_inteiros(Xs).

isVowel(V):- member(V, ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']).
lista_de_vogais([El]) :- isVowel(El).
lista_de_vogais([X| Xs]) :- isVowel(X), lista_de_vogais(Xs).

%n-esimo elemento da lista
n_elemento(0, [X| _],  X).
n_elemento(N, [_| Xs], X):- M is N-1, n_elemento(M, Xs, X).

% Implementação ineficiente: crescimento absurdo da pilha
fatorial(0, 1).
fatorial(1, 1).
fatorial(N, F):- N> 0, M is N-1, fatorial(M, Helper),!, F is Helper * N. %não faço ideia do que o cut faz, mas me fez sentido ele ser usado aqui.

fat(N, F) :- fatAUX(N, 1, F).
fatAUX(0, F, F).
fatAUX(N, Acc, F) :-
    N > 0,
    Acc1 is Acc * N,
    M is N - 1,
    fatAUX(M, Acc1, F).
% Falta fazer o mesma_geracao.

% implementar fibonacci (com recursão de cauda, usar 4 argumentos : N, fib(n-1), fib(n-2), result)

% fazer um somador de lista. O mesmo com produtoria (somar todos elementos da lista, mesmo com prod)