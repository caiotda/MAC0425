# Aula 02 - Busca Cega

***

* Quando a IA surgiu nos anos 50, a crença era que existiria um GPS (general problem solver), que busca, pelo espaço de todas soluções, uma solução pro nosso problema.

* Isso nos traz uma necessidade de afunilamento: nem todas soluções são relevantes, então como **achar um espaço de busca relevante**?

* Ex.: Ir da estação Praça da árvore à trianon

  * Conhecido: mapa da linha, localização.
  * Ações: ir pra estação adjacente.
  * Solução: sequência de ações (praça da arvore -> santa cruz -> vila mariana -> ana rosa -> paraiso -> brigadeiro -> trianon)
  * Custo da solução: Número de estações visitadas.

  

  ### Abstração

  * Busca em grafo
    * nós - estados
    * arcos - ações
  * Problema computacional: **encontrar um caminho menos custoso de um nó inicial a um nó meta**.

*  Ex: Torre de Hanói

  * Estado inicial: n discos empilados na agulha 1, ordenado por tamanho
  * Meta: n discos empilhados na agulha 2, ordenado por tamanho
  * Ações: move disco de uma agulha para outra, respeitando ordem por tamanhos
  * custo: número de ações

  ### Abstração

  * Estado: configuração dos discos
  * Ação: mover disco i para agulha j.

  ## Problema de busca

  * Dados
    * Conjunto de estados S e de ações A
    * Funções de ações aplicaveis num estado A(s) -> S' c S
    * Modelo de transição T(s,a) -> s'
    * Função de custo g(a1,...,an) -> ] -inf, inf [
    * Estado inicial s0 E S e conjunto de estados metas Mc S
  * Objetivo :  Encontrar sequencia de ações que levam do estado inicial ao estado meta com o menor custo possível

  ## Representação

  * Problema pode ser formalizado de diversas formas
  * Tamanho do espaço de estados pode mudar significativamente dependendo da representação
  * Adequação de representação depnde da busca
  * Alternativas comuns
    * configurações "completas"
    * configurações "parciais"
  * Ex: problema das N-rainhas
    * Podemos representar num grafo, e cada nó sendo uma repsentação possivel. Partimos de uma represetação inicial na qual todas rainhas estão na mesma linha e, para cada estado, analisamos todo cenario possivel de movimento (e se eu mover só a rainha1? E se só mover a rainha2? ...).
    * O estado meta é nenhuma rainha poder se atacar.
    * O problema dessa representação é que ela apresenta estados inválidos (o estado inicial por ex)
    * Também é uma representação superexponencial: temos n^n estados.
    * Outra representação: parto de um tabuleiro vazio e vou incrementando rainhas adicionadas. E coloco rainhas de forma que não se atacam
      * Dessa forma, cada estado é válido, mas incompleto.
      * Reduzimos o número de estados

  ## Busca no espaço de estados

  * Algoritmo visita estados buscando encontrar estado meta
    * algoritmo parte do estado inicial
    * a cada iteração visita estado um ou mais estado sucessor de algum estado já visitado.
      * Pode visitar vários e eleger um como o sucessor.
  * **Busca cega**
    * Usa apenas conhecimentos sobre a especificação do problema (Seria o espaço de estados)
  * **Busca heuristica**
    * Possui informações além do espaço de problemas
      * Ex: "tenta sempre pegar uma saida a direita" - num labirinto
      * Ou no sudoku: tenta expandir ao maximo antes de chutar
  * **Busca local**
    * Guarda pouca informação sobre o mundo. Não armazena informações sobre o caminho
    * Redes neurais fazem uma busca local 

  ## Arvore de busca e espaço de estados

  * Nós do espaço de estados são abstraçoes do mundo
    * cada estado é um nó
  * Nós da arvore de busca correspondem a planos parciais
    * Um estado pode corresponder a multiplos nós

  ## Fator de ramificação

  * Número de nós filhos gerados.

  ## Proxima aula: busca cega

  

  