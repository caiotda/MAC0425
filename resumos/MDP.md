# Capítulo 17 - Tomando decisões complexas

## Problemas sequenciais de decisão

* Como estamos num ambiente não determinístico, a tomada de decisões é complicada:

  * Imagine que estamos num grid world 4x4, e que o ambiente é totalmente observável (isto é, o agente sabe de todas posições do mundo dele). O objetivo do agente é ir do ponto A ao ponto B. Num mundo determinístico a solução é trivial. Mas como estamos num mundo não determinístico, cada ação tem uma probabilidade de falhar, ou não apresentar o resultado esperado
  * Digamos que o agente tem 80% de sucesso em andar na direção desejada. Mas possui 20% de chance de desviar para a direita ou para a esquerda por acidente.

* Por isso, nosso modelo de transição vai ser probabilistico e as transições são markovianas. Assim, sempre que atrelarmos uma ação com um estado inicial e final, vamos usar probabilidades, ou seja:
  $$
  P(s'|s, a)
  $$

* Não iremos apensar usar probabilidades para pesar decisões, mas também usar funções de **utilidade**, fornecendo recompensas ao gente

  * Ex.: o que é melhor? Chegar no aeroporto com antecedência de 5 dias e chance de eprder seu voo de 0.1% ou chegar 4 horas antes com chande de perder o voo de 5%? A teoria utilitarista serve como contrapeso à probabilidade

* Assim, vamos associar uma recompensa R(s) a cada estado s. Pode ser positiva ou negativa

  * Essa recompensa é aditiva: a utilidade de um caminho é a soma das recompensas recebidas

* Um problema sequencial para um mundo totalmente observável e estocástico com um modelo de transição markoviano e recompensas aditivas é um **Processo de decisão Markoviano** (Markov decision process) também conhecido como MDP.

  * Um MDP consiste de um conjunto de estados, ações ( ACTIONS(s) ), um modelo de transição P(s'|s, a) e uma função de recompensa R(s)

* Nesse caso, uma solução não pode mais ser uma sequência de ações, dado o não determinismo do nosso mundo. Para tanto, diremos que uma solução é uma **política** pi. A política deve fornecer uma ação ao agente, para qualquer estado. Denotaremos a ação recomendada no estado s pela política pi como: 
  $$
  \pi(s)
  $$

* Medimos a qualidade de uma política pela **utilidade esperada**. Uma política ótima é aquela que gera a maior utilidade esperada. 

