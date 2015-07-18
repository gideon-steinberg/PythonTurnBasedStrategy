from model.GameState import GameState
from helper.Constants import Constants
class SelectPrinter:
    @staticmethod
    def print_selected(canvas):
        ''' print out the selected_item to the given canvas '''
        x =  GameState.get_board().get_selected_x()
        y =  GameState.get_board().get_selected_y()
                
        # print this selection
        canvas.create_rectangle(x * Constants.DEFAULT_SPRITE_WIDTH()       + 15,
                                y * Constants.DEFAULT_SPRITE_HEIGHT()      + 15,
                               (x + 1) * Constants.DEFAULT_SPRITE_WIDTH()  - 15,
                               (y + 1) * Constants.DEFAULT_SPRITE_HEIGHT() - 15,
                                fill='green')