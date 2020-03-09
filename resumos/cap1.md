# Introdução

### O que é IA?

* IA = Inteligência Artificial

* Como definir uma inteligência artificial?

* Temos várias definições para o campo da IA, podemos faze-las definidos em 4 aspectos, alinhados num plano cartesiano

  * Eixo y: Pensamento
    * Preocupado com processos de pensamento e raciocínio.
  * Eixo x: Ação
    * Relaciona como a inteligência age perante o mundo

* O plano fica mais ou menos assim. Dentro de cada célula, uma definição pertinente

  | Pensando de forma humana<br /> "O esforço de fazer computadores pensarem... máquinas com mentes, no sentido total e literal" (Haugeland, 1985) | Pensando de forma racional <br /> " O estudo das faculdades mentais através do uso de modelos computacionais " (Charniak, 1985) |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | **Agindo de forma humana**<br />**"O ato de criar maquinas que performam funções que requeririam inteligência se realizadas por humanos" (Kurzweil, 1990)** | **Agindo de forma racional**<br />**"É o estudo da criação de agentes inteligentes" (Poole, 1998)** |

* Note que, assim, podemos definir a IA numa abordagem mais antropocêntrica (isto é, focado no ser humano), ou num comportamento ideal, vamos chamar isso de **racionalidade**. Assim, podemos definir o pensamento de forma ideal, ou baseado na humanidade. Da mesma forma, podemos definir a ação de uma IA de forma ideal, ou de forma humana.

### Agindo de forma humana: A abordagem do teste de Turing

* O teste de turing foi proposto por Alan Turing em 1950 e seu objetivo é **analisar se uma máquina pode se passar por um humano sem ser detectada por outro humano**. Se isso acontece, afirmamos que a máquina passou no teste de turing
* Se uma máquina passa no teste de turing, ela age de forma humana
* Como funciona o teste?
  * Um humano (avaliador) senta numa cabine e conversa com duas entidades (avaliados): uma delas é uma pessoa, uma delas é uma máquina. O avaliador não sabe qual dos avaliados é uma maquina e qual é um humano. O avaliador, então, conversa com os avaliados: faz perguntas e recebe respostas.
  * Para uma máquina ser aprovada no teste, ela deve implementar com maestria as seguintes areas da IA
    * Representação de conhecimento: armazena as perguntas do entrevistador e suas proprias respostas de forma satisfatória. 
    * Processamento de linguagem natural: processa a fala do entrevistador, transforma em conhecimento, e consegue transformar o proprrio conhecimento em fala. **Seria equivalente a nossa habilidade de falar**
    * Raciocínio automatizado: Toma as informações armazenadas e tira novas conclusões
    * Aprendizado em máquina: se adapta a novas circunstancias
* Também existe o **teste completo de turing** no qual avalia-se também habilidades cognitivas-motoras. Neste caso, a máquina deve possuir **visão computacional** e **robótica**

### Pensando de forma humana: A abordagem da modelagem cognitiva

* Para definirmos de um computador está pensando de forma humana, antes precisamos definir **como** um ser humano pensa. Como podemos definir como um ser humano pensa? São os pensamentos que passam pela sua cabeça ao longo de um raciocínio (introspecção) ? São os resultados obtidos por um experimento psicológico, avaliando como um ser humano reage a estímulos do mundo físico?
* A partir do momento que sabemos como um ser humano pensa (seja por introspecção ou por experimentação), fica claro como devemos construir o raciocínio de uma IA
* O projeto do General Problem Solver (GPS, 1961) se preocupava em construir uma máquina que poderia resolver problemas gerais, além disso, também se preocupava em fazer máquinas que resolvessem problemas baseado na forma que humanos raciocinam um problema
* O campo das **Ciências cognitivas** visa combinar modelos computacionais da IA com técnicas experimentais d apsicologia para construir teorias precisas e testáveis da mente humana.

### Pensando racionalmente: a abordagem das "Leis do pensamento"

* Aristóteles foi um dos primeiros a tentar codificar o "pensamento correto", isto é, um pensamento irrefutavel: dadas certas premissas e fatos do mundo, só há uma conclusão
  * ex.: "Todos homens são mortais. Sócrates é um homem. Portanto, sócrates é mortal." Temos dois fatos e deles só há uma conclusão possível: sócrates é mortal. Isso é o que chamamos de **silogismo aristotélico**
* As idéias de Aristóteles são a base para o campo da **lógica**, a ferramenta por trás das definições de IA sobre pensamento racional.
* Os "lógicos" criaram uma notação quase que matemática para definir conhecimento, e deste poder extrair conclusões irrefutáveis. A tradição lógica visa construir sistemas inteligentes baseado nessas notações
* Temos alguns problemas com essa abordagem
  * É muito difícil definir conhecimento incerto do mundo real e definir em termos formais. Para colocarmos em termos lógicos, as bases devem ser irrefutáveis (se não, não podemos tirar conclusões irrefutaveis. Pense em casos que não temos certeza se todo homem é mortal. Como concluir disso que sócrates é um mortal também?).
  * A cada conhecimento novo que adicionamos a nossas regras, a complexidade da regra pode aumentar exponencialmente. Assim, regras complexas podem ser difíceis de computar.

### Agindo racionalmente: a abordagem dos agentes racionais

* Um "agente" é qualquer entidade que pode agir(sim, é uma defnição circular)
* Computadores são agentes, de fato. Dado um programa, o computador consegue - de forma autonoma e eficiente - executar essa ação
* Um agente racional visa **executar uma ação e obter o melhor resultado**, ou, quando se há incerteza, o melhor resultado possível.
* Para tanto, deve-se saber qual o melhor resultado, e nisso vai muito do pensamento racional: o programa deve, baseado em alguns fatos do seu problema, saber definir qual o melhor resultado e com isso traçar uma ação
* Mas as vezes não se há uma melhor ação (aquele problema do carro autonomo: voce esta dirigindo e na sua frente tem um grupo de pedestres: se voce desviar deles, o carro bate numa arvore e o motorista morre. Se o carro ir em frente, ele atropela o grupo de pedestres mas o motorista vive). Mas mesmo assim *algo* deve ser feito
* Mas nem todo agente racional precisa definir o melhor comportamento baseado em racionalidade. Isso pode ser definido por **instinto** (nós não raciocinamos se faz sentido tirar a mão de uma superfície quente, como uma frigideira, nós só tiramos e não perdemos tempo).
* Essa abordagem é superior as anteriores por algumas razões
  * É mais geral do que a abordagem lógica: inferencia correta é apenas **uma** forma de obter resultados corretos (note o exemplo do institnto acima).
  * É mais cientificamente amigavel do que as anteriores: se definirmos nossa abordagem em algo tão aberto como o pensamento ou a ação humana, não iriamos muito longe. Tendo uma definição de racionalidade e focando na ação, e não no pensamento, pode-se construir mais rápido. 

**TODO: ler os subcapitulos de bases filosoficas da IA e historia**

