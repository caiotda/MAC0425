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

  * Ex.: o que é melhor? Chegar no aeroporto com antecedência de 5 dias e chance de perder seu voo de 0.1% ou chegar 4 horas antes com chande de perder o voo de 5%? A teoria utilitarista serve como contrapeso à probabilidade

* Assim, vamos associar uma recompensa R(s) a cada estado s. Pode ser positiva ou negativa

  * Essa recompensa é aditiva: a utilidade de um caminho é a soma das recompensas recebidas

* Um problema sequencial para um mundo totalmente observável e estocástico com um modelo de transição markoviano e recompensas aditivas é um **Processo de decisão Markoviano** (Markov decision process) também conhecido como MDP.

  * Um MDP consiste de um conjunto de estados, ações ( ACTIONS(s) ), um modelo de transição P(s'|s, a) e uma função de recompensa R(s)

* Nesse caso, uma solução não pode mais ser uma sequência de ações, dado o não determinismo do nosso mundo. Para tanto, diremos que uma solução é uma **política** pi. A política deve fornecer uma ação ao agente, para qualquer estado. Denotaremos a ação recomendada no estado s pela política pi como: 
  $$
  \pi(s)
  $$

* Medimos a qualidade de uma política pela **utilidade esperada**. Uma política ótima é aquela que gera a maior utilidade esperada.

### Utilidades ao longo do tempo

Primeiramente, vamos definir a utilidade (também chamado de valor V) de um histórico no ambiente com n estados como 
$$
U_h([s_0, s_1, \dots,s_n])
$$


Devemos responder algumas questões antes de definir nosso modelo de utilidade:

1. **O horizonte é finito?** Isto é, nosso "jogo" tem fim? Se isso for verdadeiro, nada mais importa depois de um estado N final. Portanto: 
   $$
   U_h([s_0, s_1, \dots,s_n, \dots ,s_{n + k}]) = U_h([s_0, s_1, \dots,s_n])
   $$
   Se o horizonte é finito, dizemos que nossa política é não estacionária: se nosso N for pequeno, podemos ter uma política e se N for grande podemos ter outra política (ou seja, o plano de ação para um mesmo estado, dependendo do N, pode mudar)

   Se o horizonte for infinito, dizemos que nossa política é estacionária: independente do n, independente do tempo, a ação para um estado qualquer será sempre o mesmo, a ação ótima depende apenas do estado atual. Note que esse segundo caso é bem mais simples

2. **Como calcular a utilidade da sequência de estados?** Existem duas maneiras basicamente

   1. Recompensas aditivas: a utilidade da sequencia de estados é:
      $$
      U_h([s_0, s_1, \dots,s_n]) = R(s_0) + R(s_1) + R(s_2) + \dots
      $$

   2. Recompensas com desconto:
      $$
      U_h([s_0, s_1, \dots,s_n]) = R(s_0) + \gamma R(s_1) + \gamma ^2R(s_2) + \dots
      $$
      Onde gama é o fator de desconto, **um número entre 0 e 1**. Note que a potencia no gamma faz o agente valorizar mais recompensas próximas do que distantes.

Note que temos um problema: se um ambiente não tiver estado final ou se o agente não atinge o estado final, então os históricos dos ambientes seriam infinitamente longos e, consequentemente, as utilidades seriam infinitas. Para esse problema, temos 3 soluções:

1. Se usarmos recompensas com desconto, a soma da sequencia é finita: 

$$
U_h([s_0, s_1, \dots,s_n]) = \sum_{t=0}^{\infty}\gamma^tR(S_t) \leq \sum_{t=0}^{\infty}\gamma^tR_{max} = \frac{R_{max}}{1-\gamma}
$$

Sendo R max a recompensa maxima possivel

2. Se for garantido que o ambiente possui um estado final e o agente chega nele eventualmente, obviamente não vai ser infinito. Políticas que garantem que o agente chegue ao estado final são chamadas de **adequadas**. Com esse tipo de política, podemos tranquilamente usarmos gamma = 1, porque o valor da soma com certeza será finito.
3. Podemos medir a **recompensa média por passo de tempo**. Assim, mesmo que tenhamos uma sequência infinita, ainda teriamos recompensas medias finitas

Com todas essas observações, **vamos adotar recompensas descontadas** na nossa modelagem por evitar melhor o problema de historicos infinitos.

### Definições e utilidade dos estados.

Queremos comparar políticas usando a utilidade esperada obtida ao executar essas políticas. Para tanto, vamos assumir que o agente está num estado inicial s e defir uma variável aleatório $S_t$ para ser o estado do agente num instante t executando uma política $\pi$. A utilidade esperada para executar $\pi$ começando em s é dada por:
$$
V_\pi(s) = U^{\pi}(s) = E[\sum_{t=0}^{\infty}\gamma^tR(S_t)]
$$
Onde V é o valor do caminho (é simplesmente a utilidade esperada). 

O que V faz é contabilizar a utilidade **esperada** partindo de s, isso considera todos estados futuros possíveis. Quando estamos em s, podemos tomar diversas ações, quem vai determinar essa escolha é a política.Como ações são não determinísticas, quando tomamos uma ação chegamos a um estado intermediário, chamado de **chance node**.



Estado S -> ação tomada definida pela política $\pi$ -> chance state (s,a) -> Probabilidade de 1 - x % -> Estado sucessor s'
																							|

​																							|

​																							----- Probabilidade de x% -> Outro estado sucessor s'

 O estado normal determina quais ações podem ser escolhidas, quando escolhemos uma ação, chegamos a um chance node - representado por (s,a), o estado s' que sucede s é não determinístico. Por isso é útil definirmos uma função, a função " Q" :
$$
Q(s,a)
$$
É o valor esperado partindo de s **e tomando uma ação a**. Isso vai ser útil pra facilitar umas contas mais para frente. 

Agora falta relacionar esses termos. Vamos definir V(s) como:
$$
V_\pi(s)  = 0 \ se \ s \ é \ estado\ final 
\\
V_\pi(s) = Q_\pi(s,a) \ do \ contrario
$$
Ok, e Q(s,a)? Pela definição, Q é uma função que avalia a utilidade de s se ele tomar a ação a, ou seja, Vamos definir como:
$$
Q\pi(s, a) = \sum_{s'} T(s, a, s') * (R(s') + \gamma V_ \pi(s'))
$$
Em outras palavras, a utilidade dos possíveis estados sucessores ponderada pela probabilidade de transição.



### Avaliação de políticas

Se temos uma política $\pi$ e queremos avaliar qual será o valor em cada estado, podemos rodar o algoritmo de avaliação de politicas:

```python
def policy_evaluation(pi, mdp, t_max):
    v = {}
    for state in mdp.states():
        v[state] = 0
    for time in range(len(t_max)):
        for state in mdp.states():
            v[state] = q(state, action) #pega essa ação de alguma forma
    return v
```



### Valores ótimos



Mas e se quisermos escolher o vlaor ótimo para um estado? é muito simples na verdade:
$$
V_{opt}(s)  = 0 \ se \ s \ é \ estado\ final 
\\
V_{opt}(s) = max_{a \in actions}Q(s,a) \ do \ contrario
$$
Ou seja, o valor ótimo dá a melhor ação possivel pro Q(S,a)

Queremos uma política ótima pi estrela definida como:

### Política ótima

E a política ótima segue trivialmente dai:
$$
\pi^*_s = argmax_{a \in actions} Q_{opt}(s,a)
$$
Ou seja, é a politica que tem argumentos tal que a ação escolhida pra função Q é sempre maximo. 
## Iteração de valores

## A equação de Bellman para utilidades



Segue das definições anteriores um relacionamento interessante entre estado atual e proximos estados: **a utilidade de um estado é a recomensa de estar nele, mais a utilidade descontada de estar no proximo estado, assumindo que o agente toma a ação ótima**. Então a utilidade no estado s é :
$$
U(s) = R(s) + \gamma max_{a \in A(s)} \sum_{s'}P(s'|s, a)U(s')
$$

Essa equação é chamada de **equação de Bellman**.

### O algoritmo de iteração de valores

Num MDP, se existem n estados, então existem n equações de Bellman, 1 por estado. E cada equação de bellman, possui n variáveis (que são as utilidades de cada estado s' no somatório). Assim, poderíamos usar um sistema linear pra achar uma solução para nosso ambiente, mas as equações não são lineares devido ao uso do operador "max".

Para achar soluções para a equação de bellman, vamos tomar uma solução *iterativa*. Vamos começar com valores arbitrários para as utilidades, calcular o lado direito da equação, e colocar no lado esquerdo, e vamos repetir. Seja Ui(s) a utilidade de s no instante i, a **atualização de bellman** é descrita por:
$$
U_{i+1}(s) \leftarrow R(s) + \gamma max_{a \in A(s)} \sum_{s'}P(s'|s, a)U_i(s')
$$



Repetiremos essa atualização até que o erro absoluto entre U(s) e U'(s) for menor que um epsilon. A atualização de Bellman é utilizada no **algortimo de iteração de valores**, descrito a seguir:

```
funcao ITERAÇÃO-VALORS(mdp, epsilon): funçao-utilidade
inicialize U' e U como 0.
{
	repita{
		U <- vetor_de_zeros(); delta <- 0
		for each state s in S do {
			U' <- R(s) + gamma*
				max( soma(P(s'|s,a)*U[s'], s' in (s, a) ) ,a in A(s))
			if |U' - U[s]| > delta {
				delta <- |U' - U[s]|
			}
		}
	} até que delta < epsilon * (1 - gamma)/gamma
retorne U
}
```

Note como fazemos a atualização por camadas de instante de tempo: cada estado no instante t do meu mundo é atualizado de maneira concorrente, utilizando os estados vizinhos no instante t-1. Assim, não existe uma "seção crítica" na qual usamos um estado, digamos (1,1) para atualizar o estado (1,2), mas logo em seguida vamos atualizar o estado (1,2) e corremos o risco de usar o valor atualizado armazenado em (1,1). Mas isso não ocorre porque as atualizações são sempre feitas baseadas num instante passado de tempo.

Esse é o método **assíncrono** de atualização de velor, no qual olhamos para um estado de cada vez. Existe um outro método síncrono no qual atualizamos a utilidade olhando para todos os estados ao mesmo tempo. O método assíncrono converge mais rápido e ocupa menos memória (note que aqui só armazenamos um vetor de utilidades e uma variável auxiliar u' para armazenar o u[s] antes da atualização. No método síncrono, precisariamos de um vetor para armazenar a utilidade atual e a próxima utilidade).

Um bom exercício é simular o algoritmo de iteração de valor. Teste com o seguinte grid world:



Um outro método de implementação inicializa a recomepnsa dos estados iniciais como 0 e usa a função Q(s, a) pra facilitar a conta:

```python
def valueIteration(mdp):
    V = {}
    for state in mdp.states():
        V[state] = 0
    def Q(s,a):
        return sum(prob * (reward + mdp.discount()*V[new_state])) \
    		for newState, prob, reward in mdp.sucessor(state, action)
        
    while True:
        new_v = {}
        for state in mdp.states():
            if mdp.isEdState(state):
                new_v[state] = 0
            else:
                new_v[state] = max(Q(state, action) for action in mdp.actions(state))
```





| 0    | 0    | 0    | +1   |
| ---- | ---- | ---- | ---- |
| 0    | x    | 0    | -1   |
| 0    | 0    | 0    | 0    |

Aqui inicializamos todos estados com recompensa 0, exceto um objetivo marcado como +1 e um poço marcado como -1. Tomando gamma = 0.9, e uma função de transição tal que mover-se para frente tem uma probabilidade de 0,8 e uma chacne de 0,1 para cair para direita e 0,1 de cair para a esquerda, atualize sua crença de mundo: 



| 0    | 0    | ?    | +1   |
| ---- | ---- | ---- | ---- |
| 0    | x    | 0    | -1   |
| 0    | 0    | 0    | 0    |

Vamos atualizar a utilidade do estado U1(0,2) (isto é, a utilidade de (0,2) no instante 1):
$$
U_1(0,2) = R((0,2)) + \gamma *max(\sum_{s'}P(s'|(0,2),a) * U_0((0,2)))
\\
\therefore
\\
U_1(0,2) =0 + \gamma *max(0.8 * 1 + 0 * 0,1 + 0*0.1 (direita),
\\ 0.8 * 0 + 0.1*1 \ (baixo), 
\\0.8 * 0 + 0.1 * 0 \ (esquerda)
)
\\
\therefore
\\
U_1(0,2) = 0.9*0.8 = 0.72
$$

| 0    | 0    | 0.72 | +1   |
| ---- | ---- | ---- | ---- |
| 0    | x    | 0    | -1   |
| 0    | 0    | 0    | 0    |

##### Agora repita para o instante t = 2. Note como a utilidade vai se propagando dos valores inicialmente conhecidos para valores que não conheciamos inicialmente e chutamos um valor (no caso, chutamos 0). A gente repete isso até que a diferença entre iterações seja muito pequena.