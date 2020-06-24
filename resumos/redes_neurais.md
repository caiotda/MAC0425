# Redes Neurais

* Essas notas de aula foram baseadas nas aulas do Cristopher manning para o curso de NLP  - CS224

### Revisão de regressão logística

Digamos que recebemos um dataset consistindo de amostras:
$$
\{x_i, y_i\}^N_{i=1}
$$
Os xi são chamados de **inputs** (vetor de dimensão d), enquanto que os yi são chamados de **rótulos**. Por exemplo, xi pode ser um conjunto de palavras e yi podem ser o sentimento de um texto (positivo, negativo, etc). Então o que queremos fazer aqui é classificar novos xi em categorias determinadas previamente pelos yi (lembrando que os valores de y são valores discretos, não determinísticos). Uma forma de fazer essa classificação é usando um **classificador softmax**:
$$
p(y|x) = \frac{exp(W_y.x)}{\sum_{c=1}^Cexp(W_c.x)}
$$
Onde w é a matriz de pesos e C é a quantidade de classes de classificação (redundante, mas enfim). Vamos analisar essa expressão com um pouco mais de calma:
$$
W_y.x = \sum_{i=1}^dW_{yi}xi = f_y
$$
Ou seja, o que isso signficia é: fixe a y-ésima linha da matriz W e faça um produto escalar com o vetor x. O mesmo vale para o denominador da fração.

Então depois de descobrir $exp(f_y)$, a gente simplesmente normaliza esse valor pra transformar ele numa probabilidade, dividindo ele por todos os $f_c$:
$$
p(y|x) = \frac{exp(f_y)}{\sum_{c=1}^C exp(f_c)}
$$
Ou seja, essa função pega um bando de números e transforma em uma probabilidade! Isso é parecido com regressão logística, mas aqui usamos um vetor de pesos para **cada rótulo**, em regressão linear se usa menos.



Para cada exemplo de treino, nosso objetivo é maximizar a probabilidade da classe correta y.

Ou, podemos minimizar o log negativo da probabilidade:
$$
-log \ p(y|x) = -log(\frac{exp(f_y)}{\sum_{c=1}^{C}exp(f_c)})
$$
Mas isso é pouco usado. Um método mais usado é usar **entropia cruzada** (ou cross entropy loss)

### Cross entropy loss

Assumimos que existe uma probabilidade P verdadeira, e digamos que montamos uma distribuição de probabilidade Q seguindo nosso modelo. Queremos estimar quão boa é nossa aproximação, e para fazer isso calculamos:
$$
H(p, q) = -\sum_{c=1}^Cp(c)\ log\ q(c)
$$
Esse H é nossa medida de entropia cruzada. Note que como estamos buscando classificar os nossos dados em alguma classe C, esse vetor p tem a forma:

```
p = [0,0,0,1,0,0,0,0]
```

O que isso quer dizer é que nossos dados são da classe 3 (p[3] = 1)

Então o que essa formula faz nesse caso é basicamente resultar em  $-log \ q(c)$ porque todos outros valores de p[c] são 0. Mas isso nem sempre é verdade! As vezes podemos ter probabilidades fracionarias em varios valores de p. 

### De volta a classificação

Assim, a classificação num dataset $\{x_i, y_i\}^N_{i=1}$pode ser feita usando a função $J(\theta)$, que é o log da função verossimilhança:
$$
J(\theta) = \frac{1}{N}\sum_{i=1}^{N} - log \ p(x_i|y_i;\theta)
$$
Substituindo a expressão de probabilidade que descrevemos ali em cima:
$$
J(\theta) = \frac{1}{N}\sum_{i=1}^{N} - log (\frac{exp(f_{y_i})}{\sum_{c=1}^Cexp(f_c)})
$$
Daqui pra frente, ao invés de escrever $f_y = w_y.x$ vamos escrever em notação completa de matriz: $f = Wx$.

### Otimização tradicional em ML

Em ml, geralmente os parâmetros são um vetor de pesos de d dimensões, consistindo apenas das colunas de W:
$$
\theta = \begin{bmatrix}
W_{.1}
\\
\vdots
\\
W_{.d}
\end{bmatrix}
$$
Onde cada item do vetor $\theta$ é uma coluna de W. Como cada coluna de W tem dimensão C, o vetor de parametros tem dimensão Cd.



Vamos atualizar nosso modelo usando Descendente gradiente. Atualizar nosso modelo basicamente significa mover a linha que corta o gráfico para atualizar como classificamos os pontos no plano. Só lembrando, o gradiente pode ser definido como:
$$
\nabla_\theta J(\theta) =\begin{bmatrix}
\nabla W_{.1}
\\
\vdots
\\
\nabla W_{.d}
\end{bmatrix}
$$

## Classificadores em redes neurais

O problema de regressões usando classificadores softmax é que essas classificações não são muito poderosas, pelo simples fato da classificação ser linear: só conseguimos traçar uma reta no espaço, mas e se eu quiser fazer uma classificação mais complexa?

Redes neurais conseguem traçar limites não lineares no espaço (nonlinear decision boundaries, não sei se a tradução foi boa). Assim, conseguimos fazer classificações mais poderosas. 

### Classificações com word vectors

* Fazendo NLP com deep learning, conseguimos fazer duas atualizações ao mesmo tempo:
  1. Atualizar os pesos do gradiente (parametros convencionais)
  2. Atualizar o vetor de representação de cada palavra no nosso corpus