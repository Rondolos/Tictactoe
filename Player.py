
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
import time
import copy

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

class Computer_smart_tictactoe(player):
    #initializes a smart computer player
    def __init__(self, player, order, color):
        super().__init__(player, order, color)
        if self.order == 0:
            self.letter = 'X'
        else:
            self.letter = 'O'
    
    def get_move(self,game):
        if len(game.available_moves()) == len(game.board):
            choice = random.choice(game.available_moves())
        else:
            choice = self.minmax_init(game)
        return choice
        
        
    def minmax_init(self,game):
        #print('minmax is initiated')
        state = copy.deepcopy(game)
        Remaining_moves = copy.deepcopy(state.available_moves()) 
        #print('available moves at minmax iniation : ')
        #print(Remaining_moves)
        
        #This creates a list where the scores of each move are placed
        self.scores_you = [0 for _ in range(len(Remaining_moves))]
        self.scores_opponent = [0 for _ in range(len(Remaining_moves))]
        
        #This for loop, loops through each possible move in Remaining moves, and memorizes the index of the move
        test = 0
        for loc, move in enumerate(Remaining_moves):
            test += 1
            #print('iteration ' +str(test))
            letter = self.letter
            #print(move)
            state.change_game_board(move,letter)
            #state.draw_board_command_line()
            self.minmax(state,move,letter,loc) 
            state.board[move] = ' '
        
        print(self.scores_you)
        print(self.scores_opponent)
        

        winning_score = [x - self.scores_opponent[i] for i,x in enumerate(self.scores_you)]
        print(winning_score)
        
        if max(winning_score) < 0:
            print('imhere')
            return Remaining_moves[self.scores_opponent.index(min(self.scores_opponent))] 
        else:
            return Remaining_moves[winning_score.index(max(winning_score))] 
        
        
        
    def minmax(self,state,move,letter,loc):
        #change the board with the new input
        #print(letter)  
        #Check if the move is a winning move or a draw
        
        state.condition_checker_tictactoe(letter,move)
        Remaining_moves = state.available_moves()
        
        
        if state.Game_won == 1:
            #print(letter +' won')
            if self.letter == letter:
                if self.scores_you[loc] < 1 + 1*state.board.count(' '):
                    self.scores_you[loc] = 1 + 1*state.board.count(' ')
                    #print(self.scores_you)
                    
            else:
                if self.scores_opponent[loc] < (1 + 1*state.board.count(' ')):
                    self.scores_opponent[loc] = (1 + 1*state.board.count(' '))
                    #print(self.scores_opponent)
            #print(self.scores)
            state.board[move] = ' '
        
        if state.Game_draw == 1:
            #print('its a draw')
            state.board[move] = ' '

        
        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'
        
        #print(self.scores)
        if state.Game_won == 0 and state.Game_draw == 0:
            for x in Remaining_moves:
                #print(Remaining_moves)
            
                state.change_game_board(x,letter)
                #state.draw_board_command_line()
                #print('next recursion')
                self.minmax(state,x,letter,loc)
            
                if state.Game_won == 0 and state.Game_draw == 0:
                    #print('This gets passed')
                    state.board[x] = ' '
                    
                #print('step back after recursion')
                #state.draw_board_command_line()
                
            
           
            
        state.Game_won = 0 #This resets the Game_won to 0
        state.Game_draw = 0 #This resets the draw
            
            
            #time.sleep(2)
        

            
                
#if __name__ == "__main__":
    #a = Human_player_tictactoe('Thijn', 0 ,'red')
    #available_player.param_objects.append(a)
    #a.get_action()
    #test = a.get_move(tictactoe)
    #b = Computer_random_tictactoe('Yaniv',1,'Blue')
    #available_player.param_objects.append(b)



