# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 06:43:29 2021

@author: thijn
"""

#There needs to be set of actions that can be taken by a player
#actions by ai are different than actions for human players
#the goal is that I make the class such that I can use it for tictactoe and chess or checkers, 
#but also extend it so that more than two players can be added for scaleability (denk ganzenborden of catan oid)

import random
import game_engine

class player():
    
    def __init__(self, player, order, color):
        self.player = player                  #new instance of player
        self.order = order                    #Defines when player will play, can be used to change the order in which people play (Think Uno for example) This might be better in the game player profile
        self.color = color                    #This will define the color of the player, which can be different for chess and tictactoe (in some cases determines where you start)        
        self.get_action = False
        
    def get_action(self):
        self.get_action = True
        
    def end_action(self):
        self.get_action = False
        
        
        
class Computer_random_tictactoe(player):
    def __init__(self, player, order, color):
        super().__init__(player, order, color)
        if self.order == 0:
            self.letter = 'X'
        else:
            self.letter = 'O'
        
    def get_move(self,game):
        choice = random.choice(game.available_moves())
        return choice
    
    
class Human_player_tictactoe(player):
    def __init__(self, player, order, color):
        #This calls the methods from player
        super().__init__(player, order, color)
        #this assigns the letter based on order
        if self.order == 0:
            self.letter = 'X'
        else:
            self.letter = 'O'

        
    def get_move(self,game):
        Legal_choice = False
        while Legal_choice == False:
            choice = int(input('Choose an option : ')) #This should be extended for checkers or chess
            if any(x == choice for x in game.available_moves()):
                Legal_choice = True
            else:
                print('the option was not available, choose from '+ str(game_engine.tictactoe.available_moves(game)))
        return choice

#if __name__ == "__main__":
    #a = Human_player_tictactoe('Thijn', 0 ,'red')
    #available_player.param_objects.append(a)
    #a.get_action()
    #test = a.get_move(tictactoe)
    #b = Computer_random_tictactoe('Yaniv',1,'Blue')
    #available_player.param_objects.append(b)


