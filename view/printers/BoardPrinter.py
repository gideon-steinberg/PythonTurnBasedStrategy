from model.GameState import GameState
from helper.Constants import Constants
class BoardPrinter:
    @staticmethod
    def print_board(canvas):
        ''' print out the board to the given canvas '''
        
        # get the game board
        game_board = GameState.get_board()
        
        # print out everything
        for i in range(game_board.get_width()):
            for j in range(game_board.get_height()):
                colour =  game_board.get_sprite(i,j).get_default_colour()
                
                # print this sprite
                canvas.create_rectangle(i * Constants.DEFAULT_SPRITE_WIDTH(),
                                        j * Constants.DEFAULT_SPRITE_HEIGHT(),
                                        (i + 1) * Constants.DEFAULT_SPRITE_WIDTH(),
                                        (j + 1) * Constants.DEFAULT_SPRITE_HEIGHT(),
                                        fill=colour)