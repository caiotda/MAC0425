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

import math
import random
from collections import defaultdict
import util


# **********************************************************
# **            PART 01 Modeling BlackJack                **
# **********************************************************

DETERMINISTIC = 1
TERMINAL_STATE = None
class BlackjackMDP(util.MDP):
    """
    The BlackjackMDP class is a subclass of MDP that models the BlackJack game as a MDP
    """
    def __init__(self, valores_cartas, multiplicidade, limiar, custo_espiada):
        """
        valores_cartas: list of integers (face values for each card included in the deck)
        multiplicidade: single integer representing the number of cards with each face value
        limiar: maximum number of points (i.e. sum of card values in hand) before going bust
        custo_espiada: how much it costs to peek at the next card
        """
        self.valores_cartas = valores_cartas
        self.multiplicidade = multiplicidade
        self.limiar = limiar
        self.custo_espiada = custo_espiada

    def startState(self):
        """
         Return the start state.
         Each state is a tuple with 3 elements:
           -- The first element of the tuple is the sum of the cards in the player's hand.
           -- If the player's last action was to peek, the second element is the index
              (not the face value) of the next card that will be drawn; otherwise, the
              second element is None.
           -- The third element is a tuple giving counts for each of the cards remaining
              in the deck, or None if the deck is empty or the game is over (e.g. when
              the user quits or goes bust).
        """
        return (0, None, (self.multiplicidade,) * len(self.valores_cartas))

    def actions(self, state):
        """
        Return set of actions possible from |state|.
        You do not must to modify this function.
        """
        return ['Pegar', 'Espiar', 'Sair']

    def set_state_as_terminal(self, state):
        """
            Set a state as terminal. A state is terminal if state[2] is None.
        """
        if type(state) is tuple:
            state = list(state)
        state[2] = None
        return tuple(state)

    def is_end_state(self, state):
        """
            Checks if the given state is an end state
        """
        return state[2] == None

    def is_double_peeking(self, state, action):
        """
            Verifies if the player is trying to peek a card two times in a row,
            an illegal move.
        """
        return state[1] != None and action == 'Espiar'

    def user_won(self, total_of_cards):
        """
        Checks if the player has won. This happens if he has drawn all cards in the deck
        and hasn't busted.
        """
        return total_of_cards == 0

    def user_busted(self, hand):
        """
        Checks if the players hand is larger that the limit. If that happens,
        we say that the user has busted.
        """
        return hand > self.limiar
    def set_state(self, state, hand, peek, deck):
        """
        Method that sets a state with the given parameters: the players new hand, if he will peek a
        card or not and the ammount of each card available in the deck.
        """
        if type(state) is tuple:
            state = list(state)
        state[0] = hand
        state[1] = peek
        if type(deck) is list:
            deck = tuple(deck)
        state[2] = deck
        state = tuple(state)
        return state

    def succAndProbReward(self, state, action):
        """
        Given a |state| and |action|, return a list of (new_state, prob, reward) tuples
        corresponding to the states reachable from |state| when taking |action|.
        A few reminders:
         * Indicate a terminal state (after quitting, busting, or running out of cards)
           by setting the deck to None.
         * If |state| is an end state, you should return an empty list [].
         * When the probability is 0 for a transition to a particular new state,
           don't include that state in the list returned by succAndProbReward.
        """
        # BEGIN_YOUR_CODE
        if self.is_end_state(state) or self.is_double_peeking(state, action):
            return []

        next_state = list(state[:])
        hand, peek_card, deck = state

        total_of_cards = 0
        for ammount in deck:
            # Gets the ammount of each card in the deck
            total_of_cards += ammount
        if action == 'Sair':
            next_state = self.set_state(next_state, hand, None, None)
            return [(next_state, DETERMINISTIC, hand)]

        if action == 'Espiar':
            next_states = []
            for i in range(len(self.valores_cartas)):
                if deck[i] != 0:
                    # we'll check only cards that are on the deck
                    peek = i
                    next_state = self.set_state(next_state, hand, peek, deck)
                    probability = deck[i]/total_of_cards
                    next_states.append(( next_state, probability, -self.custo_espiada))
            return next_states
        if action == 'Pegar':
            next_states = []
            next_deck = list(deck[:])
            reward = 0
            if peek_card != None:
                # Picks the peeked card
                next_deck[peek_card] -= 1
                total_of_cards -= 1

                hand += self.valores_cartas[peek_card]


                if self.user_busted(hand) or self.user_won(total_of_cards):
                    # Either if the player won or busted, we need to set the
                    # state as terminal (and to make sure we set the next state
                    # with and empty deck, we do that as well)
                    next_state = self.set_state_as_terminal(next_state)
                    next_deck = None
                    if self.user_won(total_of_cards):
                        # Only if the player has won that we give him a reward
                        reward = hand
                next_state = self.set_state(next_state, hand, None, next_deck)
                next_states = [(next_state, DETERMINISTIC, reward)]
            else:
                for i in range(len(self.valores_cartas)):
                    # Constroi cada next_state possivel
                    # Invariante: A cada iteração, temos que resetar a mão, recompensa e total de cartas
                    new_total_of_cards = total_of_cards
                    hand = state[0]
                    next_deck = list(deck[:])

                    if deck[i] > 0: 
                        # Carta está disponível
                        next_deck[i] = deck[i] - 1
                        probability = deck[i]/total_of_cards
                        new_total_of_cards -= 1

                        hand += self.valores_cartas[i]

                        if self.user_busted(hand):
                            next_deck = None
                        if self.user_won(new_total_of_cards):
                            ## Jogador venceu, não existem mais cartas
                            next_state = self.set_state_as_terminal(next_state)
                            next_deck = None
                            reward = hand
                        next_state = self.set_state(next_state, hand, None, next_deck)

                        next_states.append((next_state, probability, reward))
    
                
            return next_states

        # END_YOUR_CODE

    def discount(self):
        """
        Return the descount  that is 1
        """
        return 1
# **********************************************************
# **                    PART 02 Value Iteration           **
# **********************************************************

class ValueIteration(util.MDPAlgorithm):
    """ Asynchronous Value iteration algorithm """
    def __init__(self):
        self.pi = {}
        self.V = {}

    def solve(self, mdp, epsilon=0.001):
        """
        Solve the MDP using value iteration.  Your solve() method must set
        - self.V to the dictionary mapping states to optimal values
        - self.pi to the dictionary mapping states to an optimal action
        Note: epsilon is the error tolerance: you should stop value iteration when
        all of the values change by less than epsilon.
        The ValueIteration class is a subclass of util.MDPAlgorithm (see util.py).
        """
        mdp.computeStates()
        def computeQ(mdp, V, state, action):
            # Return Q(state, action) based on V(state).
            return sum(prob * (reward + mdp.discount() * V[new_state]) \
                            for new_state, prob, reward in mdp.succAndProbReward(state, action))

        def computeOptimalPolicy(mdp, V):
            # Return the optimal policy given the values V.
            pi = {}
            for state in mdp.states:
                pi[state] = max((computeQ(mdp, V, state, action), action) for action in mdp.actions(state))[1]
            return pi
        V = defaultdict(float)  # state -> value of state
        # Implement the main loop of Asynchronous Value Iteration Here:
        # BEGIN_YOUR_CODE

        new_v = defaultdict()
        for state in mdp.states:
            V[state] = 0.
            new_v[state] = 0.
        
        while True:
            # Rode enquanto não converge
            for state in mdp.states:
                if mdp.is_end_state(state):
                    V[state] = 0.
                else:
                    V[state] = max(computeQ(mdp, V, state, action) for action in mdp.actions(state))
            if max(abs(new_v[state] - V[state]) for state in mdp.states) < 1e-10:
                break
            new_v = V
        # END_YOUR_CODE

        # Extract the optimal policy now
        pi = computeOptimalPolicy(mdp, V)
        self.pi = pi
        self.V = V

# First MDP
MDP1 = BlackjackMDP(valores_cartas=[1, 5], multiplicidade=2, limiar=10, custo_espiada=1)

# Second MDP
MDP2 = BlackjackMDP(valores_cartas=[1, 5], multiplicidade=2, limiar=15, custo_espiada=1)

def geraMDPxereta():
    """
    Return an instance of BlackjackMDP where peeking is the
    optimal action for at least 10% of the states.
    """
    # BEGIN_YOUR_CODE
    return BlackjackMDP(valores_cartas=[4, 7, 14], multiplicidade=2, limiar=20, custo_espiada=1)
    # END_YOUR_CODE


# **********************************************************
# **                    PART 03 Q-Learning                **
# **********************************************************

class QLearningAlgorithm(util.RLAlgorithm):
    """
    Performs Q-learning.  Read util.RLAlgorithm for more information.
    actions: a function that takes a state and returns a list of actions.
    discount: a number between 0 and 1, which determines the discount factor
    featureExtractor: a function that takes a state and action and returns a
    list of (feature name, feature value) pairs.
    explorationProb: the epsilon value indicating how frequently the policy
    returns a random action
    """
    def __init__(self, actions, discount, featureExtractor, explorationProb=0.2):
        self.actions = actions
        self.discount = discount
        self.featureExtractor = featureExtractor
        self.explorationProb = explorationProb
        self.weights = defaultdict(float)
        self.numIters = 0

    def getQ(self, state, action):
        """
         Return the Q function associated with the weights and features
        """
        score = 0
        for f, v in self.featureExtractor(state, action): # Isso não é iteravel pelo visto
            score += self.weights[f] * v
        return score

    def getAction(self, state):
        """
        Produce an action given a state, using the epsilon-greedy algorithm: with probability
        |explorationProb|, take a random action.
        """
        self.numIters += 1
        if random.random() < self.explorationProb:
            return random.choice(self.actions(state))
        return max((self.getQ(state, action), action) for action in self.actions(state))[1]

    def getStepSize(self):
        """
        Return the step size to update the weights.
        """
        return 1.0 / math.sqrt(self.numIters)

    def getV(self, state):
        """
        Finds the action that maximizes Q in a given state and returns the
        corresponding value.
        """
        V = -math.inf
        for action in self.actions(state):
            Q = self.getQ(state, action)
            if Q > V:
                V = Q
        return V

    def incorporateFeedback(self, state, action, reward, new_state):
        """
         We will call this function with (s, a, r, s'), which you should use to update |weights|.
         You should update the weights using self.getStepSize(); use
         self.getQ() to compute the current estimate of the parameters.

         HINT: Remember to check if s is a terminal state and s' None.
        """
        # BEGIN_YOUR_CODE
        if state == None:
            # Se estamos no estado final, não atualizaremos os pesos
            return
        if new_state == None:
            V = 0
        else:
            V = self.getV(new_state)
        for f, _ in self.featureExtractor(state, action):
            for _ in range(self.numIters):
                # Para cada feature, atualize o valor do peso self.numIters vezes
                if self.weights.get(f) is None:
                    self.weights[f] = self.getStepSize() * (reward + self.discount * V) - self.getQ(state, action)
                else:
                    self.weights[f] += self.getStepSize() * (reward + self.discount * V) - self.getQ(state, action)
            
        # END_YOUR_CODE

def identityFeatureExtractor(state, action):
    """
    Return a single-element list containing a binary (indicator) feature
    for the existence of the (state, action) pair.  Provides no generalization.
    """
    featureKey = (state, action)
    featureValue = 1
    return [(featureKey, featureValue)]

# Large test case
largeMDP = BlackjackMDP(valores_cartas=[1, 3, 5, 8, 10], multiplicidade=3, limiar=40, custo_espiada=1)

# **********************************************************
# **        PART 03-01 Features for Q-Learning             **
# **********************************************************

def get_ammout_of_cards(deck):
    total = 0
    if deck is None:
        return 0
    for card in deck:
        total += card
    return total

def get_card_presence_indicator(deck): 
    result = []
    for card in deck:
        if card > 0:
            result.append(1)
        else:
            result.append(0)
    return tuple(result)
        

def blackjackFeatureExtractor(state, action):
    """
    You should return a list of (feature key, feature value) pairs.
    (See identityFeatureExtractor() above for a simple example.)
    """
    # BEGIN_YOUR_CODE
    total, peek, deck = state
    features = []
    if deck != None: 
        # Exemplo 1: Feature para o total de cartas na mão do jogar 
        value = 1
        key = (total, action)
        features.append((key, value))
        # Exemplo 2: Indicador de presença/ausencia de cada carta no baralho

        key = (get_card_presence_indicator(deck), action)
        value = 1
        features.append((key, value))

        # Exemplo 3: Indicar quantidade disponível de cada carta para ação
        for i in range(len(deck)):
            features.append(( (i, deck[i], action), 1))
    return features
    # END_YOUR_CODE

