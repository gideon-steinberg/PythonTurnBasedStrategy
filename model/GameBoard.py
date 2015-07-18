from model.sprite.Sprite import Sprite
from helper.Constants import Constants
from model.sprite.CreatureSprite import CreatureSprite
from model.sprite.PlayerSprite import PlayerSprite

class GameBoard:
    
    def print_board(self):
        ''' Print the board 
            Print out the type of each item
        '''
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                print self.__board[i][j].get_type() + ",",
            print ""
            
    def get_sprite(self, x, y):
        return self.__board[x][y]
    
    def get_width(self):
        return len(self.__board)
    
    def get_height(self):
        return len(self.__board[0]) 

    def __init__(self, width = Constants.DEFAULT_BOARD_WIDTH(),
                 height = Constants.DEFAULT_BOARD_HEIGHT()):
        self.__board = []
        
        # populate the __board
        # _ is an "i don't care variable"
        for _ in range(width):
            array = []
            for _ in range(height):
                array.append(Sprite())
            self.__board.append(array)
            
        # insert a player sprite
        self.__board[2][3] = PlayerSprite()
        
        # insert a creature sprite
        self.__board[0][1] = CreatureSprite()
        