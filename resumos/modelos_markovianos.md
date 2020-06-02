# Cap 15 - Raciocínio probabilístico temporal

* Previamente, definimos os estados observados como estados enumerados (**agentes determinísticos**) e fórmulas lógicas(**agentes lógicos**). Agora, vamos para uma abordagem na qual avaliamos quão **provável** é um estado. Usarems probabilidade para quantificar a crença num estado.
* Nosso modelo de transição nos dará uma distribuição de probabilidade para nossas variáveis baseados num instante t, dados os estados em instantes passados.

## Tempo e incerteza

### Estados e observações

* Como vamos analisar nossos modelos ao longo do tempo, vamos usar **fatias de tempo** para analisar nosso modelo (ou seja, um instante fixado de tempo). Nesse modelo, algumas variáveis vão ser observáveis enquanto que outras não

  * Ex.: para uma pessoa olhando pela janela, o fenômeno de chuva ou sol é observável, enquanto que a temperatura no mundo la fora não é observável

* O livro utiliza as variáveis *Xt* para denotar fenômenos não observáveis e *Et* para fenômenos não observáveis.

  * e_t = E_t é o valor do fenomeno observado no instante t

* Mais notação: Vamos usar a notação
  $$
  X_{a:b}
  $$
  Para denotar o conjunto de variáves de X_a até X_b (isso vai ajudar na hora de determinar probabilidades conjuntas).

  

### Transição e modelos de sensores

* Como estamos trabalhando com um modelo temporal probabilístico, é razoável modelar a probabilidade de um estado t como
  $$
  P(X_t|X_{0:t-1})
  $$

* O problema é que como T cresce, essa probabilidade cresce exponencialmente em complexidade de ser calculada.

* Isso é resolvido fazendo uma hipótese markoviana: A probabilidade de um estado t depende exclusivamente da probabilidade do estado anterior. Em outras palavras: 

$$
P(X_t|X_{0:t-1}) = P(X_t|X_{t-1})
$$

* Isso é um **modelo de Markov de primeira ordem** (a aridade da ordem do modelo determina quantos estados anteriores podem definir o estado atual).

* Também assumimos que as mudanças nos estados do mundo são dadas por um **processo estacionário**, ou seja, as leis de transição entre dois estados não mudam ao longo do tempo (se repetirmos um experimento n vezes, a transição entre Xt e Xt+1 sempre será a mesma).

* Ok, até agora estavamos olhando para variáveis do mundo não observaveis, estas apresentam um modelo de transição markoviano (no nosso caso, podemos pensar na temperatura como markoviana). Mas e quanto aos **eventos observáveis**? Isto é, como criar um modelo para nossos sensores?

* Podemos dizer muita coisa pelos estados, então uma boa hipótese (chamada de **hipótese markoviana de sensores**) é dizer que a observação de um estado depende exclusivamente do estado associado a ele, isto é:
  $$
  P(E_t|X_{0:t-1}, E_{0:t-1}) = P(E_t|X_t)
  $$
  
* Assim, temos que o nosso **modelo de observação** é 
  $$
  P(E_t|X_t)
  $$

* Essa ordem pode parecer estranha, já que o que é observável é E, e não X. O que essa expressão está nos dizendo basicamente é: imagine que você é um funcionário num hotel, e vê que alguém chega com guarda-chuvas ou não. Dado que está chovendo, qual a probabilidade de alguém chegar com um guarda-chuva? Isso parece estranho, porque o evento observável é a presença do guarda-chuva, então faria mais sentido perguntar "dado que alguém chegou com um guarda chuva, qual a probabilidade de estar chovendo?". Essa pergunta pode ser facilmente respondida utilizando o teorema de bayes, mas o fato mais importante dessa regra é que **a chuva condiciona a presença do guarda-chuva, e não o contrário**. Por isso nosso modelo de observação é assim.

  * Ou seja, **os estados condicionam os sensores**, não o contrário.

* Com isso, dado uma probabilidade de um estado inicial, conseguimos montar uma densidadade de probabilidade para nosso modelo: 
  $$
  P(X_{0:t-1}, E_{0:t-1}) = P(X_0)\prod_{i=1}^{t}P(X_i|X_{i-1})P(E_i|X_i)
  $$

* Ou seja, a probabilidade do modelo num instante t é o produto da probabilidade inicial pelo modelo de transição pelo modelo de observação.

* Só lembrando que 
  $$
  P(X_1, X_2, X_3,..., X_n) = \\P(X_1).P(X_2|X_1).P(X_3|X_2, X_1). P(X_4|X_3, X_2, X_1)...
  $$
  Mas como estamos lidando com uma cadeia de markov de primeira ordem, temos que:
  $$
  P(X_1, X_2, X_3,..., X_n) =\prod_{i=1}^{t}P(X_i|X_{i-1})
  $$
  Então voltando ao nosso caso, que é

$$
P(X_1, X_2, X_3,..., X_n, E_0, E_1, ... ,E_n)
$$

	## Inferencia em modelos temporais

A inferência temporal tem tres estagios

1. Filtragem (estimação de estado): Nesse estado, computamos o estado de crença num estado atual baseado em sensores de instantes anteriores. No nosso exemplo do guarda chuva, seria estimarmos a probabilidade de chover no instante t dado as t observações anteriores de guarda chuva. Isto é:

$$
P(X_t|e_{1:t})
$$

2. Predição. Agora que temos probabilidades para o instante t (digamos que seja o estado atual), queremos predizer o estado daqui a k instantes de tempo. Isto é:

$$
P(X_{t+k}|e_{1:t})
$$

3. 