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
    
    def get_selected_x(self):
        return self.__selected_x
    
    def get_selected_y(self):
        return self.__selected_y
    
    def select_item(self, x ,y):
        if isinstance(self.__board[x][y], PlayerSprite):
            # already selected
            if self.__selected_x == x and self.__selected_y == y:
                self.__reset_selected_item()
            else:
                self.__selected_x = x
                self.__selected_y = y
        else:
            self.__reset_selected_item()
    
    def __reset_selected_item(self):
        self.__selected_x = -1
        self.__selected_y = -1

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
            
        # insert some player sprite
        self.__board[2][3] = PlayerSprite()
        self.__board[2][6] = PlayerSprite()
        
        # insert a creature sprite
        self.__board[0][1] = CreatureSprite()
        
        self.__reset_selected_item()