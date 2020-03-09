# Capítulo 2 - agentes inteligentes

* No caítulo anterior, definimos que a melhor abordagem para definir IA é em cima da **ação racional**. Isso denota a necessidade de definirmos um agente inteligente
* Para tanto, vamos entender os conceitos de *agentes, ambientes e a relação entre eles*.
* **Agente**: é qualquer coisa que pode perceber seu ambiente por meio de *sensores* e interagir com ele por meio de *atuadores*
  * Ex: o ser humano possui os cinco sentidos como sensores e seus braços, pernas, voz como atuadores
  * Um agente de software possui arquivos, entradas de texto ou imagem como inputs e possui texto, imagens, videos ou sons como atuadores.
* **percept**: Algo que o agente percebe do ambiente num dado instante. Podemos ter uma sequência de percepts armazenados no agente
* **O agente toma ações baseado na sua sequência de percepts**. Ele não toma ações baseado em coisas que ele ainda não percebeu
* Função agente: definição matematica do que o agente faz. Toma percepções e gera ações.

$$
A(percepts) \implies Ações
$$

* Existe uma diferença entre **listar toda ação possível dado um cenário(tabulação)** e **definir uma função agente**. Na tabulação, simplesmente definimos o que pode acontecer dado o ambiente. Ao definirmos uma funçõa agente, nos preocupamos em **como** prencher essa tabela, ou seja, como agir de forma **inteligente e eficiente** dado um ambiente. Essa eficiencia separa agentes espertos de agentes burros.

## Bom comportamento: o conceito de racionalidade

* Um agente racional é aquele que faz a **coisa certa**, isto é, preenche corretamente a ação correspondente pra cada estado do programa. Pensa naquela tabela que mencionei la em cima. A gente pode listar todos os estados possíveis do programa. Se meu agente sempre acerta qual ação deve fazer, ele é racional.
  * Ex: Digamos que nosso programa é o pacman. Temos algumas ações possiveis:
    * Viu um fantasma
    * Viu um docinho
    * Bateu numa parede
  * Nós, que somos agentes inteligentes, sabemos que se virmos um fantasma temos que fugir. Se virmos um docinho, temos que comer. Se batermos numa parede, devemos mudar de direção. Se nosso programa conseguir interpretar esses estados corretamente e agir de forma satisfatória, ele é um agente inteligente.
    * Note que aqui não deifnimos a noção de racionalidade baseado no humano, e sim em regras do jogo. Sim, houve uma comparação com o ser humano mas apenas no sentido de comparar dois agentes inteligentes, não de criar um padrão de inteligência.
* Claro que nesse caso a ação certa é bem definida dadas as regras do jogo do pacman. Mas e se não soubermos a regra do jogo? **O que é fazer a coisa certa?**
  * Podemos analisar o que é a coisa certa avaliando as **consequências** de uma ação, de forma que a consequencia seja a melhor possivel
    * No caso do pacman, a coisa certa é comer o maximo de doces e maximizar o tempo vivo.

* As consequências dessas ações são baseadas nos estados do **ambiente** após ações do agente. Se medissemos a performance de um agente baseados do estado do proprio agente, poderíamos sempre nos iludir e pensar que fizemos boas ações, por isso que o que julga o agente deve ser externo a ele.
* ASsim, vale que uma boa avaliação de performance se baseia em **como queremos que o ambiente esteja numa situação de sucesso**  (no pacman, queremos que o ambiente tenha menos docinhos e muitos pontos marcados pelo pacman) e não de acordo com uma performance ideal do agente.

### Racionalidade

Definição de agente racional: 

" *Para cada sequencia de percepções possivel, um agente racional deve selecionar uma ação pela qual espera-se maximizar seu medidor de performance, dada a sequencia de percepções e qualquer conhecimento pré-determinado que o agente tem*"

* Ou seja, o agente tem que tomar a melhor ação possivel a cada passo, dado tudo que ele ja percebeu ou ja sabia.
  * No caso do pacman, uma ação que aumenta a quantidade de pontos é uma ação racional. A geografia do tabuleiro já é conhecida de ante-mão, assim como a distinção entre docinhos e fantasmas.

### Onisciência, aprendizado e autonomia

* Se você parar pra pensar, o nosso agente racional parece ser bom demais pra ser verdade: como assim ele *sempre* escolhe a melhor ação? Isso não seria uma onisciência? Como ele escolhe a melhor ação?
* Mas na verdade existe uma diferneça. Um agente onisciente **sabe o resultado de qualquer ação**. O agente racional **segue uma heuristica** que deve retornar a melhor ação para um estado do ambiente.
  * Distinção: digamos que eu esteja atravessando a Rua Lineu prestes e veja um amigo meu na ECA. Olho ao redor da rua, não vejo carros, então eu tento atravessar a rua para dar um oi. Exceto que, no momento que estou atravessando a rua, um raio cai na minha cabeça e eu morro. Tomei a decisão racional ao atravessar a rua? Sim. Dado minha sequencia de percepções (Não tinha carro nenhum vindo na minha direção) e meus conhecimentos pré-determinados (carros andam na rua, carros podem te atropelar e morrer, não posso atravessar uma rua se tem um veículo vindo em minha direção), fui perfeitamente racional. Um agente onisciente, por outro lado, saberia que um raio cairia exatamente naquele local exatamente no horario que eu estaria atravessando a rua. Note que o agente onisciente é racional, mas um agente racional nem sempre é onisciente.
* Racionalidade maximiza a performance esperada, ela nem sempre providencia a maior performance **possível**.
* Também é esperado que nosso agentes inteligentes **aprendam** com o ambiente. No nosso caso, sabemos que devemos tomar cuidado com carros ao atravessar a rua. Em tese, os carros apresentam uma via de circulação bem estabelecida, mas com o tempo aprendemos que alguns motoristas não respeitam essas regras e podem pegar a rua na contra mão. Nós, agentes inteligentes, aprendemos com isso e sempre olhamos para os dois lados da rua antes de atravessar, mesmo que seja de mão única.
  * Se o agente só depende do seu conhecimento pré estabelecido e não aprende nada, dizemos que ele não possui **autonomia**. Um agente inteligente deve ser autonomo.

## A natureza dos ambientes

* Agora que definimos o conceito de racionalidade, precisamos especificar como é o ambiente no qual o agente inteligente irá agir.

  ### Especificando o ambiente da tarefa

  * Para especificar o ambiente da tarefa olhamos quatro coisas : Perfomance, Ambiente, Atuadores e Sensores (PAAS, ou PEAS em inglês)
  * Vamos usar um exemplo de um carro autonomo pra exemplificar cada parte
  * Performance: é o medidor de performance do nosso agente inteligente. No caso do carro autonomo, podemos pensar em alguns pontos
    * Rota segura
    * Rota rapida
    * Viagem confortavel
    * Minimizar gastos com combustivel
      * Note que alguns pontos conflitam, por isso precisamos de alguns trade offs mesmo
  * Ambiente: definimos com o que nosso agente irá interagir no ambiente.
    * No nosso exemplo, o carro vai interagir com pedestres, outros carros, passageiros e sinalizações de transito
    * Quanto mais restrito o ambiente de tarefa, mais fácil é de interagir com ele, entretanto, o agente torna-se menos adaptavel (podemos te rum carro autonomo que só dirige em ruas extremamente bem sinalizadas e com poucos carros. Isso seria mais facil de programar, mas esse carro claramente não consguiria pegar uma estrada no interior do Brasil, por exemplo).
  * Atuadores: Ações que nosso agente pode exercer
    * frear
    * acelerar
    * virar o volante
    * puxar freio de mão
    * Algum meio de comunicação para interagir com o passageiro (receber instruções e retornar resultados)
  * Sensores: Recebem percepções do ambiente
    * Sensor infravermelho
    * profundidade
    * GPS
    * Acelerômetro