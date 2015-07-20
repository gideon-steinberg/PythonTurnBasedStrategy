from model.sprite.PlayerSprite import PlayerSprite

class PlayerArcherSprite(PlayerSprite):
    def get_type(self):
        return 'archer'
    
    def get_default_colour(self):
        return 'green'
    
    def get_movement_range(self):
        return 6
    
    def get_attack_range(self):
        return 4