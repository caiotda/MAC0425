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

### Utilidades ao longo do tempo

Primeiramente, vamos definir a utilidade (também chamado de varlo V) de um histórico no ambiente com n estados como 
$$
U_h([s_0, s_1, \dots,s_n])
$$


Devemos responder algumas questões antes de definir nosso modelo de utilidade:

1. **O horizonte é finito?** Isto é, nosso "jogo" tem fim? Se isso for verdadeiro, nada mais importa depois de um estado N final. Portanto: 
   $$
   U_h([s_0, s_1, \dots,s_n + k]) = U_h([s_0, s_1, \dots,s_n])
   $$
   Se o horizonte é finito, dizemos que nossa política é não estacionária: se nosso N for pequeno, podemos ter uma política e se N for grande, podemos ter outra política (ou seja, o plano de ação para um mesmo estado, dependendo do N, pode mudar)

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
      Onde gama é o fator de desconto, um número entre 0 e 1. Note que a potencia no gamma faz o agente valorizar mais recompensas próximas do que distantes. Vamos usar essa abordagem.

Note que temos um problema: se um ambiente não tiver estado final ou se o agente não atinge o estado final, então os históricos dos ambientes seriam infinitamente longos e, consequentemente, as utilidades seriam infinitas. Para esse problema, temos 3 soluções:

1. Se usarmos recompensas com desconto, a soma da sequencia é finita: 

$$
U_h([s_0, s_1, \dots,s_n]) = \sum_{t=0}^{\infty}\gamma^tR(S_t) \leq \sum_{t=0}^{\infty}\gamma^tR_{max} = \frac{R_{max}}{1-\gamma}
$$

Sendo R max a recompensa maxima possivel

2. Se for garantido que o ambiente possui um estado final e o agente chega nele eventualmente, obviamente não vai ser infinito. Políticas que garantem que o agente chegue ao estado final são chamadas de **adequadas**. Com esse tipo de política, podemos tranquilamente usarmos gamma = 1, porque o valor da soma com certeza será finito.
3. Podemos medir a **recompensa média por passo de tempo**. Assim, mesmo que tenhamos uma sequência infinita, ainda teriamos recompensas medias finitas

Com todas essas observações, vamos adotar recompensas descontadas como abordagem por evitar melhor o problema de historicos infinitos.

### Políticas ótimas e a utilidade dos estados.

Queremos comparar políticas usando a utilidade esperada obtida ao executar essas políticas. Para tanto, vamos assumir que o agente está num estado inicial s e defir uma variável aleatório St para ser o estado do agente num instante t executando uma política pi. A utilidade esperada para executar pi começando em s é dada por:
$$
U^{\pi}(s) = E[\sum_{t=0}^{\infty}\gamma^tR(S_t)]
$$
Queremos uma política ótima pi estrela definida como:
$$
\pi^*_s = argmax_\pi U^\pi(s)
$$
Ou seja, é a política que maximiza a utilidade. Um fato interessante é que a política ótima independe do seu estado inicial. Asim, podemos dizer que a utilidade de um estado é 
$$
U^{\pi^*}(s)
$$
Ou seja, é a utilidade partindo de s seguindo a política ótima. Vamos simplesmente escrever isso como U(s). Note a diferença entre R(s) e U(s): R(s) é a recompensa de simplesmente estar em s. U(s) é a recompensa que teremos partindo de s e seguindo a política ótima.



A função de utilidade U(s) permite ao agente selecionar ações usando o principio de **maximização de utilidade esperada**, isto é, escolher a ação que maximiza a utilidade esperada do estado subsequente:
$$
\pi^*(s) = argmax_{a \in A(s)} \sum_{s'}P(s'|s,a)U(s')
$$
Onde 
$$
P(s'|s,a)
$$
É a função de transição.

## Iteração de valores

## A equação de Bellman para utilidades



Segue das definições anteriores um relacionamento interessante entre estado atual e proximos estados: **a utilidade de um estado é a recomensa de estar nele, mas a utilidade descontada de estar no proximo estado, assumindo que o agente toma a ação ótima**. Então a utilidade no estado s é :
$$
U(s) = R(s) + \gamma max_{a \in A(s)} \sum_{s'}P(s'|s, a)U(s')
$$

### O algoritmo de iteração de valores

Num MDP, se existem n estados, então existem n equações de Bellman, 1 por estado. E cada equação de bellman, possui n variáveis (que são as utilidades de cada estado s' no somatório). Assim, poderíamos usar um sistema linear pra achar uma solução para nosso ambiente, mas as equações não são lineares devido ao uso do operador "max".

Para achar soluções para a equação de bellman, vamos tomar uma solução *iterativa*. Vamos começar com valores arbitrários para as utilidades, calcular o lado direito da equação, e colocar no lado esquerdo, e vamos repetir. Seja Ui(s) a utilidade de s no instante i, a **atualização de bellman** é descrita por:
$$
U_{i+1}(s) \leftarrow R(s) + \gamma max_{a \in A(s)} \sum_{s'}P(s'|s, a)U_i(s')
$$


Repetiremos essa atualização até que o erro absoluto entre U(s) e U'(s) for menor que um epsilon. O algoritmo é descrito pelo pseudocódigo:

```
funcao ITERAÇÃO-VALORS(mdp, epsilon): funçao-utilidade
inicialize U' e U como 0.
{
	repita{
		U <- U'; delta <- 0
		for each state s in S do {
			U'[s] <- R(s) + gamma*
				max(
					soma(P(s'|s,a)*U[s'], s' in (s, a) )
				,a in A(s))
			if |U'[s] - U[s]| > delta {
				delta <- |U'[s] - U[s]|
			}
		}
	} até que delta < epsilon * (1 - gamma)/gamma
retorne U
}
```

Note como fazemos a atualização por camadas de instante de tempo: cada estado no instante t do meu mundo é atualizado de maneira concorrente, utilizando os estados vizinhos no instante t-1. Assim, não existe uma "seção crítica" na qual usamos um estado, digamos (1,1) para atualizar o estado (1,2), mas logo em seguida vamos atualizar o estado (1,2) e corremos o risco de usar o valor atualizado armazenado em (1,1). Mas isso não ocorre porque as atualizações são sempre feitas baseadas num instante passado de tempo.

Um bom exercício é simular o algoritmo de iteração de valor. Teste com o seguinte grid world:



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

Agora repita para o instante t = 2. Note como a utilidade vai se propagando dos valores inicialmente conhecidos para valores que não conheciamos inicialmente e chutamos um valor (no caso, chutamos 0). A gente repete isso até que a diferença entre iterações seja muito pequena.