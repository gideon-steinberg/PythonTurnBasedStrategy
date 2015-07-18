from model.sprites.CreatureSprite import CreatureSprite

class PlayerSprite(CreatureSprite):
    def get_type(self):
        return 'player'
    
    def get_default_colour(self):
        return 'blue'