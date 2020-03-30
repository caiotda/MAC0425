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

% EXERCICIO PRA PROXIMA AULA: implementar uma função que concatena duas listas.
% concat(l1, l2, resultado) - concatena l1 com l2 e armazena em resultado. FAzer de forma recursiva.