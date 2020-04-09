"""
  AO PREENCHER ESSE CABECALHO COM O MEU NOME E O MEU NUMERO USP,
  DECLARO QUE SOU A UNICA PESSOA AUTORA E RESPONSAVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCICIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUCOES
  DESSE EP E, PORTANTO, NAO CONSTITUEM ATO DE DESONESTIDADE ACADEMICA,
  FALTA DE ETICA OU PLAGIO.
  DECLARO TAMBEM QUE SOU A PESSOA RESPONSAVEL POR TODAS AS COPIAS
  DESSE PROGRAMA E QUE NAO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUICAO. ESTOU CIENTE QUE OS CASOS DE PLAGIO E
  DESONESTIDADE ACADEMICA SERAO TRATADOS SEGUNDO OS CRITERIOS
  DIVULGADOS NA PAGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NAO SERAO CORRIGIDOS E,
  AINDA ASSIM, PODERAO SER PUNIDOS POR DESONESTIDADE ACADEMICA.

  Nome : Caio Túlio de Deus Andrade 
  NUSP : 9797232

  Referencias: Com excecao das rotinas fornecidas no enunciado
  e em sala de aula, caso voce tenha utilizado alguma referencia,
  liste-as abaixo para que o seu programa nao seja considerado
  plagio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em:
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""

import util
import math
from time import sleep

############################################################
# Part 1: Segmentation problem under a unigram model

class SegmentationProblem(util.Problem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def isState(self, state):
        """ Metodo que implementa verificacao de estado """
        return len(state) >= len(self.query)

    def initialState(self):
        """ Metodo que implementa retorno da posicao inicial """
        print('O estado inicial é: {}'.format(self.query))
        return self.query

    def _get_words_cost(self, state):
        words = state.split(' ')
        cost = 0
        for word in words:
            cost += self.unigramCost(word)
        return cost

    def _split(self, word, index, separator):
        return word[:index] + separator + word[index:]

    def actions(self, state): #problema: ele ta considerando espaços em branco como validos e ta inserindo espaço neles
        """ Metodo que implementa retorno da lista de acoes validas
        para um determinado estado
        """
        valid_actions = []
        min_sentence_cost = self._get_words_cost(state)

        for i in range(0, len(state) + 1):
            test_word = self._split(state, i, ' ')
            possible_sentence_cost = self._get_words_cost(test_word)
            if(possible_sentence_cost < min_sentence_cost):
                min_sentence_cost = possible_sentence_cost
                valid_actions.append(str(i))
        return valid_actions

    def nextState(self, state, action):
        action = int(action)
        """ Metodo que implementa funcao de transicao """
        return self._split(state, action, ' ')
    def isGoalState(self, state):
        """ Metodo que implementa teste de meta """
        possible_actions = self.actions(state) #Talvez seja custoso.
        return len(possible_actions) == 0

    def stepCost(self, state, action):
        action = int(action)
        """ Metodo que implementa funcao custo """
        next_state = self.nextState(state, action)
        current_cost = self.unigramCost(state)
        next_cost = self.unigramCost(next_state)
        return abs(next_cost - current_cost)


def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''
    problem = SegmentationProblem(query, unigramCost)
    goal_node = util.uniformCostSearch(problem)
    valid, solution = util.getSolution(goal_node, problem)
    print('Query:{}, Solução:{} valida?{} goal_node:{}'.format(query, solution, valid, goal_node.state))
    return goal_node.state
     
    # BEGIN_YOUR_CODE 
    # Voce pode usar a função getSolution para recuperar a sua solução a partir do no meta
    # valid,solution  = util.getSolution(goalNode,problem)


    # END_YOUR_CODE
############################################################
# Part 2: Vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.Problem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def isState(self, state):
        """ Metodo  que implementa verificacao de estado """
        raise NotImplementedError

    def initialState(self):
        """ Metodo  que implementa retorno da posicao inicial """
        raise NotImplementedError

    def actions(self, state):
        """ Metodo  que implementa retorno da lista de acoes validas
        para um determinado estado
        """
        raise NotImplementedError

    def nextState(self, state, action):
        """ Metodo que implementa funcao de transicao """
        raise NotImplementedError

    def isGoalState(self, state):
        """ Metodo que implementa teste de meta """
        raise NotImplementedError

    def stepCost(self, state, action):
        """ Metodo que implementa funcao custo """
        raise NotImplementedError



def insertVowels(queryWords, bigramCost, possibleFills):
    # BEGIN_YOUR_CODE 
    # Voce pode usar a função getSolution para recuperar a sua solução a partir do no meta
    # valid,solution  = util.getSolution(goalNode,problem)
    raise NotImplementedError
    # END_YOUR_CODE

############################################################


def getRealCosts(corpus='corpus.txt'):

    """ Retorna as funcoes de custo unigrama, bigrama e possiveis fills obtidas a partir do corpus."""
    
    _realUnigramCost, _realBigramCost, _possibleFills = None, None, None
    if _realUnigramCost is None:
        print('Training language cost functions [corpus: '+ corpus+']... ')
        
        _realUnigramCost, _realBigramCost = util.makeLanguageModels(corpus)
        _possibleFills = util.makeInverseRemovalDictionary(corpus, 'aeiou')

        print('Done!')

    return _realUnigramCost, _realBigramCost, _possibleFills

def main():
    """ Voce pode/deve editar o main() para testar melhor sua implementacao.

    A titulo de exemplo, incluimos apenas algumas chamadas simples para
    lhe dar uma ideia de como instanciar e chamar suas funcoes.
    Descomente as linhas que julgar conveniente ou crie seus proprios testes.
    """
    unigramCost, bigramCost, possibleFills  =  getRealCosts()
    
    resulSegment = segmentWords('believeinyourselfhavefaithinyourabilities', unigramCost)
    print(resulSegment)
    

    resultInsert = insertVowels('smtms ltr bcms nvr'.split(), bigramCost, possibleFills)
    print(resultInsert)

if __name__ == '__main__':
    main()
