from model.sprite.CreatureSprite import CreatureSprite

class PlayerSprite(CreatureSprite):
    def get_type(self):
        return 'player'
    
    def get_default_colour(self):
        return 'blue'
    
    def track_attack(self, turntracker):
        turntracker.track_player_attack(self)
        
    def can_attack(self, other_creature):
        return not isinstance(other_creature, PlayerSprite)