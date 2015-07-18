from model.sprites.Sprite import Sprite

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