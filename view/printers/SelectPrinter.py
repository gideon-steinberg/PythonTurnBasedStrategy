from model.state.GameState import GameState
from helper.Constants import Constants
from helper.MovementHelper import MovementHelper
from helper.OnScreenHelper import OnScreenHelper
class SelectPrinter:
    @staticmethod
    def print_selected(canvas):
        ''' print out the selected_item to the given canvas '''
        x =  GameState.get_board().get_selected_x()
        y =  GameState.get_board().get_selected_y()
        
        # if on screen
        if OnScreenHelper.is_on_screen(x, y):
            # print this selection
            SelectPrinter.__print_small_box(canvas, x, y, 'green')
            
            
            sprite = GameState.get_board().get_sprite(x,y)
            movement_range = sprite.get_movement_range()
            blank_check = True
            if (sprite in GameState.get_turntracker().get_players_to_attack() or 
                sprite in GameState.get_turntracker().get_monsters_to_attack()):
                movement_range = sprite.get_attack_range()
                blank_check = False
                    
            possible_movements = MovementHelper.get_possible_movement_spaces(movement_range, x, y)
            
            # print possible options to move!
            for movement in possible_movements:
                if (movement[0] >= 0 and movement[1] >= 0 and 
                    movement[0] < Constants.DEFAULT_BOARD_WIDTH() and movement[1] < Constants.DEFAULT_BOARD_HEIGHT()):
                    target = GameState.get_board().get_sprite(movement[0], movement[1])
                    if target.is_blank() == blank_check and sprite.can_attack(target):
                        SelectPrinter.__print_small_box(canvas, movement[0], movement[1], 'red')
            
    @staticmethod
    def __print_small_box(canvas, x, y, colour):
        canvas.create_rectangle(x * Constants.DEFAULT_SPRITE_WIDTH()       + 15,
                                y * Constants.DEFAULT_SPRITE_HEIGHT()      + 15,
                               (x + 1) * Constants.DEFAULT_SPRITE_WIDTH()  - 15,
                               (y + 1) * Constants.DEFAULT_SPRITE_HEIGHT() - 15,
                                fill=colour)
        