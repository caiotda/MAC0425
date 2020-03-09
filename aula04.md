# Aula 04

***

## Busca heurística (informada)

* Nem toda heurística garante o melhor caminho. Apenas garante uma solução
* Busca cega: 
  * Despreza conhecimento sobre solução do problema
* Busca informada
  * Usa conhecimento (intuição) sobre solução do problema

### Função heurística

* Estima custo de uma solução parcial (nó) a uma meta
* Dependente de dominio
* Propriedades: h(n) >= 0, h(meta) = 0
  * h sendo a função heurística.

* Ex do pacman: 

  * A cada nó, verifico qual nó adjacente apresenta uma distância menor  em relação ao objetivo.

  ### Busca de melhor escolha (Escolha gulosa)

  * Inicie arvore com estado inicial
  * Repita
    * Selecione o nó com menor heurística (h(n))
    * Expanda n
    * Se algum filho de n for estado meta, retorne solução correspondente

  * Melhor cenario: leva a caminho menos custoso à meta
  * Pior cenário: expande arvore completa (BP)
  * Não é completa
    * Pode entrar em ciclos

  ## Algoritmo A*

  * Combina busca de custo uniforme e busca da melhor escolha
    * Prioriza o passado
    * 