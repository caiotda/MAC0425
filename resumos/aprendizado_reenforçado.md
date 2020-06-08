# Aprendizado por reforço

## Introdução

Nesse capítulo vamos estudar aprendizado não supervisionado, ou seja, no qual os dados não estão etiquetados com valores esperados (como numa regressão linear ou logística por exemplo).

Ex.: Aprender a jogar xadrez. Um agente supervisionado precisaria saber a consequência de cada ação pra começar a aprender.

Sem supervisão, dependenmos de recompensar **ou reforço** ao agente por tomar decisões favoráveis. Recompensas foram apresentadas quando estudamos MDPs, nos quais usamos recompensas para definir políticas ótimas. Em contraste ao capítulo 17 (de MDPs) onde conhecíamos o mundo e a função de transição, aqui não assumimos informação alguma do mundo, só definimos recompensas positivas (ganhar um jogo, por ex) ou negativa.

Para simplificar um pouco, vamos assumir um ambiente totalmente observável, no entanto, nosso agente não sabe como ele funciona (ou seja, não tem informação da função de transição).



Vamos utilizar três tipos de agentes nesse capítulo:

* **Agentes baseados em utilidade**: Ele aprende uma função de utilidade baseado nos seus estados e usa isso para selecionar ações que maxmizam a saída da função de utilidade. Esses agentes precisam ter informações do ambiente para saber se suas ações serão legais ou simplesmente como vão impactar a função de utilidade.

* **Agente Q-Learning** : o agente aprende uma função **ação-utilidade**, ou função-q, dando a utilidade esperada de tomar uma açao num estado. O agente q pode avaliar a utilidade das suas solhar sem saber suas consequências, então não precisa de um modelo elaborado de ambiente. Por não saberem a consequência de suas ações, esses agentes podem ter um aprendizado limitado.

* **Agente de reflexo**: o agente aprende uma política que mapeia diretamente estados para ações.

## Aprendizado passivo por reforço



Vamos começar tratando de um agente que  usa uma representação baseado em estados de um ambiente totalmente observável. Nesse caso, a política do agente é fixa: num estado S, o agente sempre executa a ação $\pi$(s). Dessa forma, ele espera testar a utilidade dessa política. O agente conhece a função de recompensa.



Vamos supor que estamos no mesmo grid world que tratamos no capítulo de MDPS: 

| $\to$      | $\to$        | $\to$        | +1           |
| ---------- | ------------ | ------------ | ------------ |
| $\uparrow$ | x            | $\uparrow$   | -1           |
| $\uparrow$ | $\leftarrow$ | $\leftarrow$ | $\leftarrow$ |

Nosso agente recebe uma política e tenta obter a função de utilidade $U^\pi(s)$. O que vamos fazer aqui é rodar vários **experimentos**, por exemplo, colocar o agente num ponto inicial (estado (1,1)) e deixar ele andar até chegar em algum estado terminal. A única coisa que ele tem conhecimento, além da política a ser testada,  é uma recompensa que ele recebe ou perde a cada estado. Para estimarmos a utilidade em (1,1) podemos fazer o seguinte caminho:
$$
(1,1)_{-.04} \to (1,2)_{-.04} \to (1,3)_{-.04} \to (1,2)_{-.04} \to \\(1,3)_{-.04} \to (2,3)_{-.04} \to (3,3)_{-.04} \to (4,3)_{+1}
$$
Assim, conseguimos estimar a utilidade de (1,1) como a soma desses descontos e obter 0.72. Em outras palavras, a utilidade num estado s seguindo a política $\pi$ pode ser estimada como: 
$$
U^\pi(s) = E\lceil\sum_{t=0}^\infty\gamma^tR(S_t)\rceil
$$
Onde $\gamma$  é o fator de desconto e $S_t$ é uma variável aleatória.

### Estimação direta de utilidade

A idéia aqui é entender a utilidade de um estado como a recompensa esperada total **daquele estado em diante** (**reward to-go**) e cada experimento providencia uma *amostra* dessa quantidade para cada estado visitado no experimento. Por exemplo, no nosso exempo anterior, a gente teria uma estimação de 0.72 pro estado (1,1), uma estimação de 0.76 e 0.84 pra (1.2) e assim em diante. Portanto, ao fim de um experimento, o algoritmo calcula a recompensa **to-go** e atualiza a utilidade estimada para aquele estado, e faz isso mantendo uma tabela com a média de utilidade pra cada estado.

No limite de infinitas iterações desse algoritmo, teríamos um resultado parecido com aquela equação ali em cima.



A força dessa idéia é que um único experimento providencia dados para todos estados intermediários entre o estado inicial e o estado final. O problema dessa técnica é na sua modelagem: nos supomos que a utilidade de um estado é dada pela sua recompensa mais a utilidade dos proximos estados, ou seja, **ela supões independência entre estados**.

 Por exemplo, digamos que estamos fazendo outro experimento, e chegamos no estado (3,2) que não foi previamente visitado. Depois, chegamos ao estado (3,3) que por experimentos anteriores sabemos que tem uma utilidade alta. Se nosso modelo suposse estados dependentes, poderiamos usar a equação de bellman para descobrir que (3,2) tem uma utilidade alta (dado que ela veio de 3,3). Mas nesse caso, só iríamos descobrir a utilidade de (3,2) ao fim do experimento. 



Em outras palavras, a estimação direta de utilidade faz a busca de utilidades num espaço de busca muito maior do que poderia ser (se contemplassemos dependência entre estados), o que faz com que o valor da utilidade de um estado venha a convergir muito lentamente.



### Programação adaptativa dinamica (ADP)

Um agente ADP usa métodos de programação dinâmica para aprender um modelo de transição que conecta e resolve os MDPs dos estados. O que isso significa é o agente plugar o modelo de transição que foi aprendido ( $P(s'|s, \pi(s))$ ) e as recompensas observados $R(s)$ na equação de bellman para calcular a utilidade dos estados.



Nesse modelo de aprendizado, temos um mundo totalmente observável, um par estado-ação e a saída é um estado resultando. Podemos representar o modelo de transição simplesmente como uma tabela de probabilididades. Vamos registrar quão frequentemente cada resultado de ação acontece e estimar $P(s'|s,a)$ da frequência que s' ocorre partindo de s e executando "a". Por exemplo, no nosso exemplo de grid world podemos verificar quantas vezes executamos a ação "Direita" partindo de (1,3) e verificarmos quantas vezes acabamos em (2,3), dessa forma poderiamos estimar $P((2,3)|(1,3), "Direita")$.



O ADP converge tão rápido quanto sua habildade de aprender o modelo de transição. Note que nosso aprendizado é feito exclusivamente nas ações do agente, então é preciso cuidado ao escolhermos uma política baseada no modelo de transição aprendido, porque o modelo de transição pode estar errado! 

* Por exemplo, um agente que dirige um taxi pode não ter conhecimento sobre semáforos, e aprender com isso e eventualmente valorizar ações que atravessam semáforos vermelhos.
* Assim, é interessante escolher uma política que, apesar de não ser ótima, é abrangente o bastante para cobrir modelos que são razoáveis o bastante para pdoerem ser verdadeiros.

O livro explcia MUITO mal essa parte, ver melhor outra fonte

### Aprendizado de diferença temporal

