from model.sprites.Sprite import Sprite
from utils.Constants import Constants
from model.sprites.CreatureSprite import CreatureSprite
from model.sprites.PlayerSprite import PlayerSprite

class GameBoard:
    
    def print_board(self):
        ''' Print the board 
            Print out the type of each item
        '''
        for i in range(0, len(self.__board)):
            for j in range(0, len(self.__board[i])):
                print self.__board[i][j].get_type() + ",",
            print ""
            
    def get_sprite(self, x, y):
        return self.__board[x][y]

    def __init__(self, width = Constants.DEFAULT_BOARD_WIDTH(),
                 height = Constants.DEFAULT_BOARD_HEIGHT()):
        self.__board = []
        
        # populate the __board
        # _ is an "i don't care variable"
        for _ in range(0,width):
            array = []
            for _ in range(0,height):
                array.append(Sprite())
            self.__board.append(array)
            
        # insert a player sprite
        self.__board[2][3] = PlayerSprite()
        
        # insert a creature sprite
        self.__board[0][1] = CreatureSprite()
        