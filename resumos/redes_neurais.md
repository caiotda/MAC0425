# Redes Neurais

### Introdução redes neurais

![](/home/caio/Imagens/NeuralNetwork.png)

As redes neurais surgiram como uma ideia de modelar computacionalmente o funcionamento de um neurônio. Você tem inputs de outros neurônios (nesse caso são os dados), e alguns desses impulsos nervosos são mais estimulantes aos neurônios, outros menos (aqui, usamos os pesos nos dados para regular o quão importante ele é pro neuronio). No corpo do neurônio, ele lida com toda a infirmação que ele recebe de todos outros neurônios (no caso da rede neural, é uma conta entre o valor e os pesos com um certo viés). Depois de tudo isso, ele cospe um impulso nervoso pro próximo neurônio (no nosso caso, computamos uma função dos valores de entrada para o proximo neuronio). Para classificar se o neurônio passa a informação adiante ou não (e quanto dessa informação é passada) modelamos cada neurônio como uma unidade de regressão logística.

Toda a idéia das redes neurais é se perguntar "Por que rodar apenas uma unidade de regressão logística (neurônio), e não várias unidades(rede neural)?"

Exceto que nessa rede a gente não quer, de antemão, decidir o que cada neurônio quer prever, e sim **deixar a rede neural descobrir o que é útil de ser previsto em cada neurônio**. 

Mas como isso é feito? Bem, a rede neural em si possui um objetivo: Na ponta da rede neural vamos ter um classificador linear que pode dar resultados positivos ou negativos, e o que vamos fazer é dizer pra rede neural ir ajustando os parâmetros no meio da rede (chamamos esse trecho da rede neural de **hidden layer** ou camada oculta) para que o erro seja mínimo e o resultado máximo. 

### Anatomia de um neurônio

Cada neurônio recebe um dado (pode ser um dado de entrada, ou o dado computado por outro neurônio) e retorna esse dado computado. Normalmente o neurônio apenas retorna valores entre 0 e 1, porque queremos usar o grau de ativação de um neurônio como uma probabilidade. Para tanto, envolvemos o valor de saída do neurônio por uma função normalizadora (como a função logística, função RElu, função tangente hiperbólica). Cada neurônio faz uma operação nos seus dados, relacionando a entrada com seu peso correspondente e o viés.

Da mesma forma que um neurônio humano, um perceptron (neurônio de uma rede neural) recebe um impulso, transforma ele em outra coisa, e encaminha esse impulso para outro neurônio ou uma terminação nervosa. Aqui que entra a utilidade de pesos e vieses na nossa rede neural: o que cada perceptron faz é olhar para seu peso e viés e **decide se deve valorizar ou não aquela entrada**. Neurônios com alto viés e peso alto vão valorizar muito sua entrada, e por consequência, vão ter uma saída com valor elevado. Neurônios com viés baixo e peso baixo não vão valorizar a sua entrada e por consequência vão ter valores de saídas baixos. O neurônio relaciona os pesos, entradas e vieses de uma maneira simples: Dado que os pesos são armazenados num vetor $W$, as entradas num vetor $x$ e os vieses num vetor $b$, temos que a ativação do i-ésimo neuronio de uma camada é: 
$$
z_i = w_i*x_i + b_i
$$


Todo valor de saída de um neurônio é alimentado para uma função que mapeia a sua saída para valores entre 0 e 1.  Isso é feito porque queremos que a saída de cada neurônio  - também chamada de **ativação do neurôno** -na ponta da rede neural seja um número de pode facilmente ser interpretado como uma probabilidade, e porque assim evitamos valores de saída muito grandes de um neurônio qualquer que podem enviesar a rede neural por completo.

### Visão geral da estrutura de uma rede neural

Uma rede neural é organizada em **camadas**. Normalmente, toda rede neural tem pelo menos 3 camadas:

1. Camada de entrada: Aqui que colocamos nossos dados de **entrada**
2. Camada oculta: Aqui que acontece a magia das redes neurais: Os valores de entrada interagem com os pesos e vieses e se **transformam** em algo diferente. Podemos ter mais do que 1 camada oculta.
3. Camada de saída: Depois dos dados serem processados na camada oculta, eles são dispostos na camada de saída. Aqui fazemos a **avaliação** dos valores de saída: eles já estão bons o suficiente? Estão próximos do que esperamos? Se não estiverem, realizamos um processo chamado de **backpropagation** para atualizar os pesos e vieses e assim obter valores melhores.

O processo de ir da camada de entrada até a camada de saída é chamado de **forward pass**.

### Otimização de parâmetros

Se analisarmos as transformações que cada neurônio faz, fica claro que a rede neural tem 2 parâmetros: Pesos e vieses. Quando criamos uma rede neural, normalmente inicializamos esses valores de maneira aleatória, e ao longo do tempo **treinamos** nossa rede neural para escolher valores ótimos de parâmetros para obtermos um valor de saída desejado (isto é, um valor tal que uma função de erro usada tenha resultado mínimo). Essa otimização é feita utilizando o algoritmo de **Stochastich Gradient descent (SGD)**. Essencialmente, o que fazemso é, dado parâmetros armazenados num vetor $\theta$ e uma função de erro $J(\theta)$, podemos fazera  aatualização como 
$$
\theta_j = \theta_{j-1} - \alpha\nabla_\theta J(\theta)
$$
Como o gradiente aponta a direção na qual a função cresce mais rapidamente, o que estamos fazendo aqui é atualizar os parâmetros $\theta$ para minimizarmos a função de erro, caminhando na direção de maior **decrescimento**. 

### Notação matricial para uma camada (modelo matemático)

Para cada camada, vamos ter

1. Um vetor de entradas($\vec{x}$) 
2. Um vetor de saídas ($\vec{a}$)
3. Um vetor de conectores, que determinam quanto cada conector é valorizado pela rede neural (seria o peso) - ($\vec{w}$)
4. Um viés ($\vec{b}$)
5. Um valor de saída do neurônio (z)
6. O valor de ativação do neurônio (a)

Assim, podemos relacionar essas variáveis por:
$$
z = W^Tx + b \\
a = f(z)
$$
Onde $f$ é uma função de ativação - também chamada de não linearidade. Um exemplo de função de ativação é a sigmoide:
$$
f(z) = \frac{1}{1+ e^{-z}}
$$


A função f é aplicada a cada elemento de z. Mas por que a aplicação da função de não-linearidade é importante?

### Importância da função f

Sem uma função não linear, cada camada da rede neural simplesmente faria uma transformação linear com os dados da camada anterior. Dessa forma, nem sequer precisariamos de uma série de camadas, poderíamos ter só uma camada de rede neural que faz todas essas operações em uma única transformação linear. 

Quando adicionamos um elemento de não linearidade, conseguimos aproximar funções mais complexas de classificação.

### Computação com feed forward

Para fazer toda essa computação, vamos usar uma rede neural. Como entrada, temos o nosso vetor de palavras. Ele é passado por uma camada oculta, e o input da camapda oculta é descrito por:
$$
z = WX + b
$$
Esse valor sai da camada oculta aplicando uma função de ativação:
$$
a = f(z)
$$
E por fim, obtemos um valor estimado "score", que é determinado por:
$$
s = U^Ta
$$
Onde s é um número real e U é uma matriz (acho que essa matriz é computada pela rede neural?)

E basicamente, para avaliar como nossa rede aprende, vamos analisar **derivada parcial do score pelo viés** (podemos também analisar a variação do erro. Podemos reescrever s como:
$$
s = u^Th
\\
\therefore
\\
s = u^Tf(z), \>\> z = Wx + b
$$
Então para descobrir a derivada de s em relação a b, basta aplicar a regra da cadeia:
$$
\frac{\part s}{\part b} = 
\frac{\part s}{\part h}
\frac{\part h}{\part z}
\frac{\part z}{\part b}
$$


### Algumas derivações comuns:

$$
\frac{\part}{\part u}u^Th = h^T
\\
\frac{\part}{\part z}f(z) = diag(f'(z))
\\
\frac{\part}{\part b} (Wx + b) = I
$$

### Voltando para nossa derivada:

$$
\frac{\part}{\part b}u^Th = h^T
\\
e
\\
\frac{\part}{\part z} f(z) = diag(f'(z))
\\
e
\\
\frac{\part}{\part b} Wx + b = I
\\
\therefore
\\
\frac{\part s}{\part b} = 
\frac{\part s}{\part h}
\frac{\part h}{\part z}
\frac{\part z}{\part b} = h^T f'(z) = (f(z))^Tf'(z)
$$

Lembrando que $h = f(z)$

### Re-utilizando computações

Agora vamos supor que queremos avaliar o score baseado nos pesos. De novo, vamos usar uma regra da cadeia:
$$
\frac{\part s}{\part W} = 
\frac{\part s}{\part h}
\frac{\part h}{\part z}
\frac{\part z}{\part W}
$$
Ja conhecemos o valor dos dois primeiros termos. Faz sentido, inclusive, esses dois primeiros termos sempre aparecerem: eles relacionam a saída com a função de discretização da camada oculta, e a saida da camada oculta com sua entrada. Assim, é comum denotar os dois primeiros termos como **sinal de erro local**:
$$
\delta =\frac{\part s}{\part h}
\frac{\part h}{\part z} = h^T f'(z)
$$

### Calculando a derivada de s em relação a W

Como o W é um vetor de tamanho $N.M$ e s é uma função com 1 saída, o jacobiano teria formato 1 x Nm. Mas isso é meio ruim, por causa do algoritmo de atualização via gradient descend: 
$$
\theta^{novo} = \theta^{velho} - \alpha\nabla_\theta J(\theta)
$$
Seria muito bom se o gradiente tivesse a mesma dimensão que o vetor de parâmetros. Para tanto, a derivada de s em relação em w deve ter a mesma dimensão que W. Assim, seria bom termos um jacobiano nesse formato: 
$$
\frac{\part s}{\part W} = \begin{bmatrix}
\frac{\part s}{\part W_{11}} & \dots & \frac{\part s}{\part W_{1M}} \\
\vdots & \ddots &  \vdots
\\
\frac{\part s}{\part W_{n1}} & \dots & \frac{\part s}{\part W_{nm}}
\end{bmatrix}
$$
Voltando ao cálculo:
$$
\frac{\part s}{\part W} = \delta\frac{\part z}{\part W} =  \delta\frac{\part}{\part W} Wx + b = \delta^T\times x^T
$$
Como W é uma matriz, devemos fazer essa derivação com cuidado. Vamos considerar a derivada em relação a um único peso $W_{ij}$. Note que, por construção, $W_{ij}$ só contribui pra $z_i$, já que $W_{ij}$ é o peso da aresta que coneccta xj com zi. logo:
$$
\frac{\part z_i}{\part W_{ij}} = \frac{\part}{\part W_{ij}} w_i.\vec{x} + b_i
\\
=\frac{\part}{\part W_{ij}} \sum_{k=1}^{d}w_{ik}x_k = x_j
$$
Esse argumento se aplica para todo elemento de W. Assim, a derivada de um único elemento:
$$
\frac{\part s}{\part W_{ij}} = \delta_ix_j
$$
Uma forma de generalizar isso para matrizes é fazer:
$$
\frac{\part s}{\part W} = \delta^T \times x^T
$$
Ou seja, fazer o produto vetorial. Como $\delta^T$ é [N x 1] e $\x^T$ é [1 x n] vamos obter uma matriz [N x M] onde para cada elemento vale aquela equação ali em cima.

### Backpropagation

Nós passamos por cima de alguns tópicos aqui que quase são backpropagation! Qual o funcionamento basico das redes neurais? Vamos por passos:

1. Forward pass: Passamos os dados dos inputs até o cálculo da recompensa, fazendo todas aquelas transformações lineares entre camadas
2. Backwards pass: Com o resultado que temos, vamos fazer um gradient update com os pesos da rede neural vizando minimizar a função de erro.

Como queremos fazer a atualização dos parâmetros por gradient descent, precisamos encontrar as derivadas dos parâmetros! Como cada camada da rede depende exclusivamente da anterior (e, por consequência dos parâmetros - pesos e vieses por ex - da camada anterior) a taxa de variação de algum parâmetro no fim da rede neural em relação a outro parâmetro pode ser parametrizado pelas derivadas em cada par de camadas anteriores. Em outras palavras:

```
---(input) --- w1 ---- (act()) ----- w2 --- (act())----w3-----(act())
						hidden1				hidden2				output
```

Cada neurônio é uma função do neurônio anterior. Podemos definir isso matematicamente:
$$
output = act(w3 * hidden 2)
\\
hidden2 = act(w2*hidden1)
\\
hidden1 = act(w1 * input)
\\
\therefore 
\\
output  = act(w3 * act(w2*act(w1 * input)))
$$
Assim, se queremos calcular o erro de uma aproximação na saída da rede neural em relação a um parâmetro qualquer, podemos ir "propagando" essa diferenciação para trás. Nesse exemplo, vamos avaliar o erro (loss(E)) em relação a um peso $w_{i,j}$. Esse erro depende da saída do nó $o_j$ (nó que providencia o resultado), qie por sua vez depende da saida da rede j (camada oculta da rede), e esta depende do peso $w_{i, j}$ - que conecta a camada oculta com os inputs.
$$
\frac{\part E}{\part w_{i, j}} = \frac{\part E}{\part o_j}\frac{\part o_j}{\part net_j}\frac{\part net_j}{\part w_{i, j}}
$$
Tem uma maneira um pouco mais fácil de organizar as idéias com as derivações. Suponha que um neurônio possua inputs W e x e com eles produza uma saída  $z = Wx + b$ que passa pela função de ativação $a = f(z)$. Suponha também que o neurônio atual é seguido por outro, com saída s. Vamos seprar tres derivadas para cada neurônio:

1. Gradiente local: Simplesmente a derivada da saída do neurônio em relação a cada entrada
   $$
   \frac{\part z}{\part W} = x 
   \\
   \frac{\part z}{\part x} = W
   $$
   
2. Derivada upstream: É o que relaciona o neurônio atual com o próximo.
   $$
   \frac{\part s}{\part z}
   $$
   
3. Derivada downstream: Propaga o conhecimento do próximo neurônio com as camadas anteriores do gradiente local. **É simplesmente o produto do gradiente local pela derivada upstream**

![](/home/caio/Área de trabalho/Screenshot_20200626_085859.png)

Esse aqui é um exemplo da aula de redes neurais, onde temos como entradas x = 1, y = 2 e z = 0

Primeiro, o que fazemos é computador os valores de entrada e de saída de cada nó (etapa de forward pass), que estão em preto em cada aresta. Agora, para fazer o backpropagation, precisamos descobrir o gradiente local de cada nó

Dentro de cada nó, conseguimos computador o gradiente local. No caso do nó ''+'', a função de saída é simplesmente x + y, então o gradiente local dele é :
$$
[\frac{\part a}{\part x} = 1, \frac{\part a}{\part y} = 1, ]
$$
Se fizermos o mesmo para o nó max (função b), veremos 
$$
[\frac{\part b}{\part y} = 1 ( se \ y > z), \frac{\part b}{\part z} = 1, (se\ z > y)]
$$
E o mesmo pra função f de multiplicação:
$$
[\frac{\part f}{\part a} = b = 2, \frac{\part f}{\part b} = a = 3]
$$
Agora vamos descobrir a derivada upstream. Ela é simplesmente a saída do próximo nó derivado pela saída do nó atual (em outras palavras, uma das componentes do gradiente local!). Com isso, só fazer o produto do upstream gradient pelo local gradient pra descobrir o backwards gradient. 

Isso tudo é uma forma de sistematizar como ocorrem as derivações do backwards propagation, porque no fundo ela é essencialmente uma regra da cadeia: você quer derivar a saída da rede por uma das entradas, então voce aplica uma sequência de derivações pela regra da cadeia para obter esse resultado.

Então backpropagation é uma regra da cadeia glorificada =p

### Ideia geral da computação de backprop

Agora que já vimos a inutição matemática por trás do backpropagation, vamos analisar - em termos gerais - como vai funcionar a computação dos valores.

1. Forward propagation: Visite os nós em ordem topológica. Passe input pelos neurônios, gerando a saída formatada pela função de ativação, e eventualmente obtenha o valor de saída da rede neural

   * Obs.: ordem topológica: computar valores dado seus predecessores. Pensando naquela imagem típida da rede neural, queremos computar da esquerda para a direita

2. Back propagation:

   * Inicialize o gradiente da saída da rede neural como 1 (derivada de z por z sempre dá 1)

   * Visite os nós em ordem topológica reversa

     * Então, para um nó X, temos um conjunto de nós $\{y_1, y_2 , \dots, y_n\}$ que são sucessores de x, temos:
       $$
       \frac{\part z}{\part x} = \sum_{i=1}^{n} \frac{\part z}{\part y_i}\frac{\part y_i}{\part x}
       $$

     * Se feito corretamente, a complexidade no pior caso do forward pass e do backward propagation é a mesma

Em frameworks modernos de DL como PyTorch e Tensorflow, basta computar, na mão, o valor de retorno de cada nó  - forward pass -(por exemplo, definir uma função) e definir o backward pass, então teria que definir como é o gradiente local. O framework faz todo o resto. Um exemplo: 

```python
class ComputationalGraph(object):
    #...
    def forward(inputs):
        #1... passe os inputs para os input gates
        #2.... faça o forward pass
        for gate in self.graph_nodes_topologically_sorted():
            gate.forward()
        return loss # Valor de retorno da rede
    def backward():
        for gate in reversed(self.graph_nodes_topologically_sorted()):
            gate.backward()
        return inputs_gradients
```



Onde cada "Gate" é um nó. A gente usa esse nome porque ele recebe n inputs e permite apenas uma saída, dando essa idéia de controle, como um portão. Vamos dar um exemplo de metodos forward e backward para um Gate que simplesmente usa uma função de multiplicação de dois inputs:

```python
class MultiplyGate(object):
    def forward(x, y):
        z = x*y
        self.x = x
        self.y = y
        return z
   	def backward(dz): #Derivada da função LOSS por z
        dx = dz * self.y # [dl/dz * dz/dx]
        dy = dz * self.x # [dl/dz * dz/dy]
        return [dx, dy]
```

### Algumas dicas sobre modelar redes neurais

* É bom fazer uma regularização da função de erro ([L2 Regularization](https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c)) sobre todos parâmetros do modelo. Isso evita overfitting
  
* Quando o modelo se adapta bem até demais aos dados de treino, de forma que ele não consegue generalizar para novos dados do mundo
  
* Valorize vetores e matrizes sobre for loops

* Sobre funções de não linearidade:

  * A sigmoide não é muito utilizada hoje em dia, somente quando você necessariamente quer um valor entre 0 e 1 na sua rede neural.

  * As funções tanh (tangente hiperbólica) são bem usadas. A fórmula é:
    $$
    f(x) = tanh(x) = \frac{e^x - e^{-x}}{e^{-x} + e^x}
    $$

  * O problema dessas duas funções é usar exponenciais, o que é meio lento

  * Uma alternativa é uma tanh um pouco "quadrada". Ela é basicamente assiom:
    $$
    hardTanh(x) = -1 \ se \ x \ <  -1 
    \\ = x, \ se -1 \leq x \leq 1
    \\ = 1 \ se \ x > 1
    $$

  * Ela funciona bem! Note que o gradiente dessa função é 0 ou 1, dependendo da região do gráfico.

  * **ReLU**: Essa é a função mais usada hoje em dia (Rectified linear unit):

    
    $$
    Rect(z) =  max(z, 0)
    $$

    * São bem rápidas, performam bem, e treinam a rede muito bem.
    * É o padrão pra redes feed forward

  * Existe a alternativa da **leaky RElu** que introduz uma leve inclinação quando z é negativo.

* Inicialização de parâmetros: Inicialize os pesos como valores aleatórios! Seguindo uma distribuição uniforme, claro. 

  * Em pytorch ou tensor flow, existe uma inicialização chamada **xavier inicialization** que funciona bem para inicializar os pesos aleatoriamente com valores razoáveis (considera o peso entre camadas: se toda a inicialização for aleatória, pode er que tenhamos niveis com pesos cada vez maiores e isso pode ser ruim. Essa inicialização sempre considera a camada anterior e a próxima camada para inicializar os pesos )

* Otimizações:

  * Normalmende, SGD (gradient descent) funciona muito bem. O problema é que você precisa ir ajustando a taxa de aprendizado.
    * Podemos usar uma taxa constante
    * Mas podemos obter resultados melhores se permitpermitirmos o learning rate ir se reduzindo conforme treinamos o modelo.
      * Existem fórmulas pra essa tualização, ou algumsa regras (tipo, a cada vez que iterarmos 3 vezes por todos os dados - chamamos 1 passada por todos os dados de "epoch" - reduzimos a taxa de aprendizado em um fator de 10)
  * Existem outras alternativas, não vou listar aqui
    * Adagrad
    * RMSProp
    * Adam
    * SparseAdam
    * Varios outros, aqui vou focando mais no SGD mesmo