from model.sprite.Sprite import Sprite
from helper.MovementHelper import MovementHelper

class CreatureSprite(Sprite):
    def is_blank(self):
        return False
    
    def get_type(self):
        return 'creature'
    
    def get_hp(self):
        return self.__hp
    
    def __init__(self):
        self.__hp = 5
        
    def get_default_colour(self):
        return 'orange'
    
    def get_movement_range(self):
        return 5
    
    def move(self, current_x, current_y, x, y, board, sprite_swapper):
        possible_movements = MovementHelper.get_possible_movement_spaces(self.get_movement_range(), current_x, current_y)
        # if we can move there and there is a blank sprite
        if [x,y] in possible_movements and board.get_sprite(x, y).is_blank():
            sprite_swapper.swap_sprites(x, y, current_x, current_y, board)