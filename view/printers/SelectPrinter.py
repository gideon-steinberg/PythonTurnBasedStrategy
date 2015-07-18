from model.GameState import GameState
from helper.Constants import Constants
from helper.MovementHelper import MovementHelper
from model.sprite.Sprite import Sprite
class SelectPrinter:
    @staticmethod
    def print_selected(canvas):
        ''' print out the selected_item to the given canvas '''
        x =  GameState.get_board().get_selected_x()
        y =  GameState.get_board().get_selected_y()
        
        if (x > 0 and y > 0 and x < Constants.DEFAULT_BOARD_WIDTH() and y < Constants.DEFAULT_BOARD_HEIGHT()):
            # print this selection
            SelectPrinter.__print_small_box(canvas, x, y, 'green')
            
            # print possible options to move!
            
            movement_range = GameState.get_board().get_sprite(x,y).get_movement_range()
            possible_movements = MovementHelper.get_possible_movement_spaces(movement_range, x, y)
            print possible_movements
            
            for movement in possible_movements:
                if GameState.get_board().get_sprite(movement[0], movement[1]).is_blank():
                    SelectPrinter.__print_small_box(canvas, movement[0], movement[1], 'red')
            
    @staticmethod        
    def __print_small_box(canvas, x, y, colour):
        canvas.create_rectangle(x * Constants.DEFAULT_SPRITE_WIDTH()       + 15,
                                y * Constants.DEFAULT_SPRITE_HEIGHT()      + 15,
                               (x + 1) * Constants.DEFAULT_SPRITE_WIDTH()  - 15,
                               (y + 1) * Constants.DEFAULT_SPRITE_HEIGHT() - 15,
                                fill=colour)
        