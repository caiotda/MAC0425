# Aula 1 - introdução

***

### Na última aula

* IA: Estudo e desenvolvimento de entidades **Autonomas** capazes de **perceber** o ambiente e **agir** de maneira **satisfatória**

  * Tem uma formalização matematica pra isso, mas sei la.

  * Percepções: P

  * Ações: A

  * Agente: 

  * $$
    f: P^* \implies A
    $$

  * Conjunto de estados do mndo: S

  * Função de desempenho g: S* X A* -> ] -inf, inf [

    * Ou seja, pega todos estados do mundo, pega todas ações e faz algo.

  * O agente inteligente é o f que otimiza G

***

## Tópicos abordados

* Explicaçõa dos diversos tópicos da IA

***

## Tópicos de IA

* Busca
* Representação de conhecimento
* Raciocínio Lógico
* Planejamento
* RAciocínio probabilístico
* Aprendizagem automática
  * " Aprender" soluções a partir de exemplos
  * Aprendizagem supervisionada
    * Exemplos são rotulados
  * Por reforço
    * Exemplos são recompensados por ações
    * Planejamento sem modelo
* Aspectos metodológicos éticos e filosóficos

**Todos esses tópicos estão dentro do "guarda chuva" da IA**.

## HIstorico

* 1956: Primeira conferência de IA.
* 1957: Primeiro neurônio de uma rede neural (Perceptron);
* 1958: Provador de teoremas.

Propósito da IA antiga: Criar um General Problem Solver (GPS): Tomamos todo o espaço de solução possível, e navegamos por ele.

***

# Resolução de problemas por busca em grafo

* Capítulos 3, 4 e 5 do livro

  ***

  ## Introdução 

* Ex: Slider puzzle

  * Dado um slider com estado inicial, como chegar no estado final no qual ele está resolvido?
  * Para cada estado, avaliamos todos possíveis estados seguintes.
    * Isso pode gerar um problema de explosão combinatória.

* Representação como busca em grafo

  * Solução especializada para cada problema
  * Conhecimento hard coded
  * Heurística não genérica para selcionar ações
  * Modelo de mundo imutável

* Planejamento clássico

* Planejamento

  * Principal desafio: Desenhar algoritmos e heuristicas eificientes agnósticas ao domínio
  * Inúmeras variantes
    * Planejamento não determinístico
    * Planejamento probabilístico
    * Planejamento multiagentes

* Representação de conhecimetno

  * Ontologia: Descrição formal de um domínio de conhecimento
    * Tipos entidades e propriedades
    * RElações entre entidades
  * Desafios:
    * Especificar/minerar ontologia
    * Gerencias/atualizar/associar bases
    * inferência
  * Web semântica
    * Tornar conteúdo da web manipulável por computadores.

* Raciocínio probabilístico

  * Informações originais são combinadas à crenã original para produzir nova crença