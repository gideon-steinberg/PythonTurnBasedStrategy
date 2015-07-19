from model.sprite.Sprite import Sprite
from helper.Constants import Constants
from model.sprite.PlayerSprite import PlayerSprite
from model.sprite.MonsterSprite import MonsterSprite

class GameBoard:
             
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
    
    def set_selected_x(self, x):
        self.__selected_x = x
    
    def set_selected_y(self, y):
        self.__selected_y = y
    
    def set_turntracker(self, turntracker):
        self.__turntracker = turntracker
    
    def set_sprite(self, x, y, sprite):
        self.__board[x][y] = sprite
            
    def reset_selected_item(self):
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
        
        # insert some creature sprites
        self.__board[0][1] = MonsterSprite()
        self.__board[2][4] = MonsterSprite()
        
        self.reset_selected_item()