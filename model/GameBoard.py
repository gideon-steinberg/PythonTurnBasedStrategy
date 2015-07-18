from model.Sprites.Sprite import Sprite
from Utils.Constants import Constants
from model.Sprites.CreatureSprite import CreatureSprite
from model.Sprites.PlayerSprite import PlayerSprite

class GameBoard:
    
    def print_board(self):
        ''' Print the board 
            Print out the type of each item
        '''
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                print self.board[i][j].get_type() + ",",
            print ""

    def __init__(self, width = Constants.DEFAULT_BOARD_WIDTH(),
                 height = Constants.DEFAULT_BOARD_HEIGHT()):
        self.board = []
        
        # populate the board
        # _ is an "i don't care variable"
        for _ in range(0,width):
            array = []
            for _ in range(0,height):
                array.append(Sprite())
            self.board.append(array)
            
        # insert a player sprite
        self.board[2][3] = PlayerSprite()
        
        # insert a creature sprite
        self.board[0][1] = CreatureSprite()
        