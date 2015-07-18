from model.Sprites.Creature import Creature
from model.Sprites.BlankSprite import BlankSprite

class GameBoard:
    
    def print_board(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                print self.board[i][j].get_type() + ",",
            print ""

    
    def __init__(self, width = 3, height = 4):
        self.board = [[BlankSprite()] * width] * height
        