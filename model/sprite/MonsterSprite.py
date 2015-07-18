from model.sprite.CreatureSprite import CreatureSprite
from helper.MovementHelper import MovementHelper

class MonsterSprite(CreatureSprite):
    def get_type(self):
        return 'monster'
    
    def get_default_colour(self):
        return 'pink'
    
    def move(self, current_x, current_y, x, y, board):
        possible_movements = MovementHelper.get_possible_movement_spaces(self.get_movement_range(), current_x, current_y)
        # if we can move there and there is a blank sprite
        if [x,y] in possible_movements and board.get_sprite(x, y).is_blank():
            board.swap_sprites(x, y, current_x, current_y)