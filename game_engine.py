# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 07:06:50 2021

@author: thijn
"""
#The goal is to make an engine that can create a new game board, based on input of the specific game

# Every game has a number of actions that are not unique to the gameboard
import Player
import sys
import time

class game:
    def __init__(self):
        self.Game_won = 0
        self.Game_draw = 0
        
    def Set_game_board(self,lenx,leny):
        #Sets up the board
        self.board = [' ' for _ in range(lenx*leny)]
        self.numberboard = [[str(i+1) for i in range(j*lenx,(j+1)*lenx)] for j in range(leny)]
        self.lenx = lenx
        self.leny = leny
        
    def change_game_board(self,location,letter):
        #This expects to receive a list of tuples, (zero,zero), which will be read as follows
        # if (1,#), then that location in the list will change, # denotes what will be placed in the list
        # for tictactoe the tuple is not needed, but if I want to create checkers I need something like this
        #print(letter)
        #print(location)
        self.board[location] = letter
    
    def draw_board_command_line(self):
    #Draws the command line board based on inputs from game
    #drawing method depends on if I want to use tkinter or use command line
    #Writing my own method for drawing could be interesting but is very time-consuming
        for row in [self.board[i*self.lenx:(i+1)*self.lenx] for i in range(self.leny)]:
            print('| ' + ' | '.join(row) +' |')                             #Ik wist niet dat dit kon, sick
            
    def draw_board_command_line_numbers(self):
        #draws the numbers of the board
        for row in self.numberboard:
            print('| ' + ' | '.join(row) +' |')                           
    
    def draw_board_tkinter(self,shape_board):
        #draws tkinter board
        pass
    

    def Check_conditions(self,player):
        #Checks win condition
        #if player won, game resets 
        if self.Game_won == 1:
            print('Congrats : ' + player + ' won!')
            self.Set_game_board(self.lenx, self.leny)
            sys.exit()
        if self.Game_draw == 1:
            print('It\'s a draw!')
            self.Set_game_board(self.lenx, self.leny)    
            sys.exit()
  
class tictactoe(game):
    #Sets the game board with width and length of 3
    #creates an empty list of players
    def __init__(self):
        
        self.Game_won = 0
        self.Game_draw = 0
        self.width = 3
        self.length = 3
        self.Set_game_board(self.width,self.length)
        self.players = []
        
    def available_moves(self):
         return [i for i, spot in enumerate(self.board) if spot == ' '] #this can be used to check if the move is legal, or to only allow these moves to be chosen

    def condition_checker_tictactoe(self,letter,location):
        #this checks for a winning move
        #first check rows
        #print('Rows')
        row_index = location//self.lenx
        row = self.board[row_index*self.lenx:(row_index+1)*self.lenx]
        if all([x == letter for x in row]):
            self.Game_won = 1
            
        #now check columns
        #print('Columns')
        column_index = location % self.lenx #deze moet ik even uitzoeken
        column = [self.board[column_index+i*self.lenx] for i in range(self.lenx)]
        #print(column)
        if all([x == letter for x in column]):
            self.Game_won = 1
        
        #now check diagonals
        #print('Diagonals')
        
        diagonal1 = [self.board[i] for i in [0,4,8]]
        if all(x == letter for x in diagonal1):
            #print('diagonal1 won')
            self.Game_won = 1
        diagonal2 = [self.board[i] for i in [2,4,6]]
        if all(x == letter for x in diagonal2):  
            #print('diagonal2 won')
            self.Game_won = 1
            
        #this checks for a draw
        if any(x == ' ' for x in self.board):
            self.Game_draw = 0
        else: 
            self.Game_draw = 1
        
        
def tictactoe_play(game):
    #This checks if there are two players, if not, it asks to add the players to the game
    while len(game.players) < 2:
        
        if input('Do you want to add a computer player : ') == 'Yes':
            #a = Player.Computer_random_tictactoe(input('Name computer player : '),input(' 0 = X, 1 = O : '),input('color : '))
            a = Player.Human_player_tictactoe('Thijn',0,'red')
        else:
            #a = Player.Human_player_tictactoe(input('Name human player : '),input(' 0 = X, 1 = O : '),input('color : '))
            a = Player.Computer_smart_tictactoe('Yaniv',1,'blue')
            
        if a.order == 0:
            a.letter = 'X'
        else:
            a.letter = 'O'

        game.players.append(a)
    
    while game.Game_won == 0 and game.Game_draw == 0:
        for x in game.players:
            print('Its ' + x.player + '\'s turn')
            
            location = x.get_move(game)
            print(location)
            game.change_game_board(location,x.letter)
            print(game.available_moves())
            game.draw_board_command_line()
            
            #This checks the conditions at the end of the players turn
            game.condition_checker_tictactoe(x.letter,location)
            game.Check_conditions(x.player)
            time.sleep(2)
            
        game.Game_won = 0
        game.Game_draw = 0    
            

def tictactoe_debug(game):
    #This checks if there are two players, if not, it asks to add the players to the game

    a = Player.Computer_smart_tictactoe('Thijn',0,'red')
    b = Player.Computer_smart_tictactoe('Yaniv',1,'blue')


    game.players.append(b)
    game.players.append(a)
    
    game.board = ['O','X',' ',' ','X',' ',' ',' ',' ']
    
    game.draw_board_command_line()
    
    while game.Game_won == 0:
        for x in game.players:
            print('Its ' + x.player + '\'s turn')
            
            location = x.get_move(game)
            print(location)
            game.change_game_board(location,x.letter)
            print(game.available_moves())
            game.draw_board_command_line()
            
            #This checks the conditions at the end of the players turn
            game.condition_checker_tictactoe(x.letter,location)
            game.Check_conditions(x.player)
            time.sleep(2)
        
        game.Game_won = 0
        game.Game_draw = 0                
    
if __name__ == "__main__":
    a = tictactoe()
    tictactoe_play(a)
    