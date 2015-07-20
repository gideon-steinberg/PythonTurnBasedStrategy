from model.sprite.Sprite import Sprite
from helper.MovementHelper import MovementHelper

class CreatureSprite(Sprite):
    def is_blank(self):
        return False
    
    def get_type(self):
        return 'creature'
    
    def __get_hp(self):
        return self.__hp
    
    def __init__(self):
        self.__hp = 5
        self.__current_hp = 5
        
    def get_default_colour(self):
        return 'orange'
    
    def get_movement_range(self):
        return 5
    
    def get_attack_range(self):
        return 1
    
    def __get_current_hp(self):
        return self.__current_hp
    
    def get_attack(self):
        return 2
    
    def get_hp_string(self):
        return str(self.__current_hp) + "/" + str(self.__hp)
    
    def decrease_hp(self, damage):
        self.__current_hp = self.__current_hp - damage
    
    def move(self, current_x, current_y, x, y, board, sprite_swapper):
        possible_movements = MovementHelper.get_possible_movement_spaces(self.get_movement_range(), current_x, current_y)
        # if we can move there and there is a blank sprite
        if [x,y] in possible_movements and board.get_sprite(x, y).is_blank():
            sprite_swapper.swap_sprites(x, y, current_x, current_y, board)
    
    def track_attack(self, turntracker):
        ''' defined in MonsterSprite and PlayerSprite '''
        pass
            
    def attack(self, other_creature, turntracker):
        damage = self.get_attack()
        other_creature.decrease_hp(damage)
        self.track_attack(turntracker)
        