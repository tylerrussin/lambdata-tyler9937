'''
classes to represent games.
'''
from random import random

class Game:
    '''
    General representation of an abstract game.
    '''

    fun_level = 5
    def __init__(self, rounds = 2, player1 = 'tom', player2 = 'steve'):
        self.rounds = rounds
        self.current_round = 0
        self.player1 = player1
        self.player2 = player2

    def print_players(self):
        '''
        Print game players
        '''
        print('{} is playing {}'.format(self.player1, self.player2))

    def add_round(self):
        '''
        Increment rounds by 1
        '''
        self.rounds += 1

    def winner(self):
        '''
        pick a winner
        '''
        return self.player1 if random() > 0.5 else self.player2
class Tic(Game):
    '''
    Tictactoe subclass of games
    '''

    def __init__(self, rounds = 3, player1 = 'Mike', player2 = 'Emma'):
        pass
