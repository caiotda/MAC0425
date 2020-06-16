# Aprendizado por reforço

## Introdução

Nesse capítulo vamos estudar aprendizado não supervisionado, ou seja, no qual os dados não estão etiquetados com valores esperados (como numa regressão linear ou logística por exemplo).

Ex.: Aprender a jogar xadrez. Um agente supervisionado precisaria saber a consequência de cada ação pra começar a aprender.

Sem supervisão, dependemos de recompensas **ou reforço** ao agente por tomar decisões favoráveis. Recompensas foram apresentadas quando estudamos MDPs, nos quais usamos recompensas para definir políticas ótimas. Em contraste ao capítulo 17 (de MDPs) onde conhecíamos o mundo e a função de transição, aqui não assumimos informação alguma do mundo, só definimos recompensas positivas (ganhar um jogo, por ex) ou negativa.

Para simplificar um pouco, vamos assumir um ambiente totalmente observável, no entanto, nosso agente não sabe como ele funciona (ou seja, não tem informação da função de transição).



Vamos utilizar três tipos de agentes nesse capítulo:

* **Agentes baseados em utilidade**: Aprende uma função de utilidade. Usa isso para escolher ações que maximizam o valor (Função V) do estado. Precisa ter um modelo do ambiente para tomar decisões, já que ele precisa conhecer os estados que seguem das ações escolhidas.

* **Agente Q-Learning** : o agente aprende uma função **ação-utilidade**, ou função-q, dando a utilidade esperada de tomar uma açao num estado. Como a função Q avalia a utilidade de performar a ação A no estado S sem precisar saber a utilidade em S' (estamos supondo aqui o modelo de transição T(S, A, S'), esse agente não precisa ter um modelo de ambiente, já que ele não precisa conhecer de antemão a consequência das suas ações. Isso pode limitar a capacidade de aprendizado desse agente.

* **Agente de reflexo**: o agente aprende uma política que mapeia diretamente estados para ações.

## Aprendizado passivo por reforço



Vamos começar tratando de um agente que  usa uma representação baseado em estados de um ambiente totalmente observável. Nesse caso, a política do agente é fixa: num estado S, o agente sempre executa a ação $\pi$(s). O objetivo do agente simplesmente é descobrir quão boa essa política é, ou seja, obter a função $V^{\pi}(s)$.

Vamos supor que estamos no mesmo grid world que tratamos no capítulo de MDPS: 

| $\to$      | $\to$        | $\to$        | +1           |
| ---------- | ------------ | ------------ | ------------ |
| $\uparrow$ | x            | $\uparrow$   | -1           |
| $\uparrow$ | $\leftarrow$ | $\leftarrow$ | $\leftarrow$ |

A diferença daqui com o exemplo de MDPs é que nosso agente não conhece a função de transição. ele também não conhece a função de recompensa, no máximo ele **percebe** a recompensa por estar num dado estado, mas não tem conhecimento das recompensas de antemão.

 O que vamos fazer aqui é rodar vários **experimentos**, por exemplo, colocar o agente num ponto inicial (estado (1,1)) e deixar ele andar até chegar em algum estado terminal. A única coisa que ele tem conhecimento, além da política a ser testada,  é uma recompensa que ele recebe ou perde a cada estado. Para estimarmos a utilidade em (1,1) podemos fazer o seguinte caminho:
$$
(1,1)_{-.04} \to (1,2)_{-.04} \to (1,3)_{-.04} \to (1,2)_{-.04} \to \\(1,3)_{-.04} \to (2,3)_{-.04} \to (3,3)_{-.04} \to (4,3)_{+1}
$$
Assim, conseguimos estimar a utilidade de (1,1) como a soma desses descontos e obter 0.72. Em outras palavras, a utilidade num estado s seguindo a política $\pi$ pode ser estimada como: 
$$
V^{\pi}(s) = U^\pi(s) = E\lceil\sum_{t=0}^\infty\gamma^tR(S_t)\rceil
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

Para lidar com esses problemas, temos dois métodos:

* Aprendizado reenforçado bayesiano:  Assumimos uma probabilidade a priori $P(h)$ para cada hipótese de qual é o modelo verdadeiro. A probabilidade posteriori $P(h|\vec{e})$ é dada observando as evidencias  do nosso mundo. Depois de observarmos as evidências sobre cada hipótese, ou seja, o agente terminar de aprender sobre o mundo, podemos estimar a política ótima como aquela que dá a maior utilidade. 

  * Então, usamos $P(h|e)$ como um multiplicador para a utilidade esperada seguindo a hipótese h e politica $\pi$:

  $$
  \pi^* = argmax_{\pi}\sum_hP(h|\vec{e})V_h^{\pi}
  $$

* Teoria de controle robusto.

### Aprendizado de diferença temporal

Podemos utilizar as transições observadas para ajustar as utilidades dos estados observados. Por exemplo, digamos que estejamos rodando vários experimentos no nosso grid world para descobrir a utilidade esperada para uma política $\pi$. Digamos que numa iteração, estamos analisando a transição entre os estados (1,3) e (2,3). Nessa iteração, descobrimos que $V^{\pi}((1,3)) = 0.84$ e $V^{\pi}((2,3)) = 0.92$. Então se essa transição ocorrese da mesma forma sempre, poderiamos dizer que 
$$
V^{\pi}((1,3)) = -0.04 + V^{\pi}((2,3))
$$
Então $V^{\pi}((1,3))$ seria 0.88, ou seja, nossa estimativa de 0.84 estaria um pouquinho errada e deveria ser atualizada. Essa é a ideia central de aprendizado de diferença temporal: Analisamos a diferença entre dois estados: S e S', onde S' é o estado sucessor de S; E vamos atualizando As utilidades baseadas nessa diferença. Ou seja:
$$
V^{\pi}(s) \leftarrow V^{\pi}(s) + \alpha(R(s) + \gamma (V^{\pi}(s') - V^{\pi}(s))
$$
Onde $\alpha$ é a taxa de aprendizado.

## Aprendizado ativo por reforço

Em contrapartida com um agente passivo - que seguia exclusivamente as ações determinadas por uma política -, um agente ativo deve decidir que ações tomar.

 Vamos começar considerando o agende ADP visto anteriormente e modifica-lo para seu aprendizado ser ativo. O nosso agente deve aprender um modelo completo de transição, para todas ações, ao invés de aprender uma política fixa. O ADP funciona bem nesse caso (lembrando que ele mantém uma tabela com a probabilidade de transição entre estados e vai atualizando-a).

O nosso agente também deve, dentre todas ações que pode vir a tomar, escolher aquela que maximiza a sua utilidade. A equação de bellman serve para ilustrar esse problema e o algoritmo de iteração de valores serve para resolve-lo.

Mas se temos todas essas ferramentas, poderíamos simplesmente rodar iteração de políticas e descobrir a política ótima. Dessa forma poderia simplesmente reproduzir as ações da política, certo? Errado. 

Experimentos mostram que agentes que usam uma política ótima para aprenderem não consegue aprender as utilidades ótimas correspondentes. Isso acontece porque a política ótima foi criada baseada no mundo real, no qual temos acessos a funções de transição e de recompensa. Nesse caso, o agente não conhece nenhum dos dois então o resultado não é o esperado.



### Exploração

O agente, ao seguir cegamente a política ideal, busca recompensas por meio de suas ações. No entanto, ao faze-lo, ele não percebe que as ações possuem outro benefício alem de prover recompensas: elas também nos dão maior conhecimento do mundo (por exemplo, no caso de ADPs, toda probabilidade de transição é catalogada e adquirimos conhecimento de mundo). Se o agente explorar mais o mundo, ele terá mais certeza de suas ações e poderá receber recompensas maiores (ou mais certeiras).



Assim, o agente deve fazer uma escolha entre **recompensas em curto prazo** e **explorações**, que maximizam as recompensas de **longo prazo**. O agente pode explorar eternamente, mas isso de nada serve se ele não aproveitar esse conhecimento e adquirir recompensas, da mesma forma que não adianta ele sair cambaleando pelo mundo sem ter conhecimento algum e esperar ter alta chance de obter recompensas.

Na estatística, existe o **problema do caça níqueis** que é razoavelmente similar: quantos jogos deve jogar no caça níquel antes de me sentir confortavel em desistir do jogo? Quanto eu devo explorar o mundo antes de me sentir confortável de começar a colher recompensas?

Uma abordagem que vamos usar é olhar para ações que já tomamos, e ações que ainda não tomamos. E vamos dar pesos para as ações que não foram utilizadas frequentemente, enquanto que tentamos evitar ações que acreditamos serem de baixa utilidade. 

O que isso quer dizer é que vamos designar alta utilidade para pares (s,a) que não foram previamente explorados. Então inicialmente o agente se encontrará imerso num mundo cheio de recompensas altas (obviamente, no início nenhum par estado-ação foi utilizado) e aos poucos ele vai atualizando essa estimativa.

Vamos utilizar $V^+(s)$ para representar a utilidade otimista esperada para s, e $N(s, a)$ o número de vezes que a ação $a$ foi utilizada no estado $s$. Vamos reescrever a atualização de bellman como:
$$
V^+(s) \leftarrow max_a(f(\ Q(s,a), N(s, a)\ )
$$
Ou
$$
V^+(s) \leftarrow R(s) + \gamma max_a f( \sum_{s'}P(s'|s, a)V^+(s), N(s, a))
$$
Onde $P(s'|s, a) = T(s, a, s')$ que é o modelo de transição.

$f(v, n)$ é a **função de exploração**. Essa função determina o quanto **ganância** (preferência por altos valores de V) é trocada em relação a **curiosidade** (preferencia por ações que ainda não foram tentadas, ou seja, um n baixo). A função F(v, n) deve ser crescente se aumentarmos v e decrescente conforme aumentamos N. Existem várias funções que cabem nessas restrições, mais uma siples é:
$$
f(u,n) = \begin{cases} 
R^+ &  se  \ n < N_e 
\\
u & do \ contrario
\end{cases}
$$
Onde $R^+$ é estimativa otimista da melhor recompensa obtível de qualquer estado e $N_e$ é um parâmetro fixo. O que isso faz basicamente é fazer o agente explorar todos pares ação-estado pelo menos $N_e$ vezes antes de começar a explorar as utilidades.

O uso de $U^+$ ao invés de U implica que o agente valoriza explorar regiões novas (o benefício da exploração é propagado pra trás vindo as regiões novas).

Assim, construimos um agente ADP com aprendizado ativo.

### Aprendendo uma função ação-utilidade

Nosso bojetivo agora é construir um agente ativo usando diferença temporal. A primeira diferença com o caso anterior é a ausência de uma política. Se aprendermos uma função V, precisaremos ainda descobrir qual ação é mapeada dessa função.

 Devido a ausência de um modelo, o agente precisaria testar o ambiente, transicionando para estados adjacentes para decidir qual a melhor ação (**one step look ahead**). 

Quanto a regra de atualização do valor, é a mesma do agente de diferença de tempo (TD).

Mas esse método não é tão bom por dois motivos:

1. É custoso ficar dando passos em falso pra entender o ambiente
2. A regra de atualização, apesar de converger tão bem quanto um ADP, considera movimentos em falso como verdadeiros para a atualização.

Com isso, surge o método alternativo do **Q-LEARNING**, no qual o agente aprende uma função ação-utilidade ao invés de aprender utilidades. A função Q(s, a) é definida por
$$
U(s) = max_aQ(s, a)
$$
Para aprender o valor de Q(s, a) e selecionar ações, um modelo q-learning **não precisa ter conhecimento da função de transição**, da mesma forma que um agente TD. Por isso, o q-learning é um método chamado de **livre de modelo**.

Para aprender o valor de Q(s, a), vamos usar a regra de atualização de um agente TD:
$$
Q(s, a) \leftarrow Q(s, a) + \alpha(R(s) + \gamma max_{a'}Q(s', a') - Q(s, a))
$$
Para verificar a corretude do valor de Q(s, a) calculada, podemos usa a equação
$$
Q(s, a) = R(s) + \gamma \sum_{s'}P(s'|s, a) max_{a'}Q(s', a')
$$
Se soubermos um modelo (o que nem sempre é o caso) poderíamos usar essa equação diretamente para calcular Q(s, a)

Uma implementação possível de um agente q_learning usa ações aleatórias para atualizar o valor de Q. Segue abaixo como seria a implementação aproximadamente

``` python
def q_learning_agent(s, a, Q, percept, alpha):
    """
    Recebe um estado, ação e recompensa
    anteriores, uma 
    tabela Q, um percept (que fornece
    o estado atual e as ações possiveis) e 
    devolve a ação ótima
    """
    if isTerminal(s):
        Q[s][None] = r
    if s is not None:
        max = -inf
        for action in actions:
            diff = Q[percept.s][action] - Q[s][a] 
            if diff > max:
                max = diff
                opt_a = action
        Q[s][a] += alpha*diff
    return opt_a
```

Também existe outra implementação que valoriza ações frequentemente utilizadas (e por isso, multiplica o diff pela frequencia desse par ação - estado), nessa implementação, usamos a função de exploração previamente usada no agente ADP.

