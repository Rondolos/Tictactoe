# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 07:06:50 2021

@author: thijn
"""
#The goal is to make an engine that can create a new game board, based on input of the specific game

# Every game has a number of actions that are not unique to the gameboard
import Player



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
        
    def change_game_board(self):
        #This expects to receive a list of tuples, (zero,zero), which will be read as follows
        # if (1,#), then that location in the list will change, # denotes what will be placed in the list
        # for tictactoe the tuple is not needed, but if I want to create checkers I need something like this
        for x in range(enumerate(self.board)):
            var = self.changes[x]
            if var[0] == 1:
                self.board[x] = var[1]
    
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
            print('Congrats' + player + 'won')
            self.Set_game_board(self.lenx, self.leny)
        if self.Game_draw == 1:
            print('It\'s a draw')
            self.Set_game_board(self.lenx, self.leny)    
    
  
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

    def condition_checker_tictactoe(self):
        if any(x == ' ' for x in self.board):
            self.Game_draw = 1
        
        self.Check_conditions()
        
        
    def tictactoe_play(self):
        #This checks if there are two players, if not, it asks to add the players to the game
        while len(self.players) < 2:
            
            if input('Do you want to add a computer player : ') == 'Yes':
                #a = Player.Computer_random_tictactoe(input('Name computer player : '),input('color : '),input('letter [X or O] : '))
                a = Player.Computer_random_tictactoe('Thijn','red','X')
            else:
                #a = Player.Human_player_tictactoe(input('Name human player : '),input('color : '),input('letter [X or O] : '))
                a = Player.Human_player_tictactoe('Yaniv','blue','O')
                
            self.players.append(a)
        
        while self.Game_won == 0 and self.Game_draw == 0:
            for x in self.players:
                print('Its ' + x.player + '\'s turn')
                
                self.change_game_board(x.get_move())
                
                self.draw_board_command_line()
                
                #This checks the conditions at the end of the players turn
                self.condition_checker_tictactoe(x.player)
                
        self.Game_won = 0
        self.Game_draw = 0    
            

            
    
if __name__ == "__main__":
    a = tictactoe()
    a.tictactoe_play()
    