from model.sprite.CreatureSprite import CreatureSprite

class MonsterSprite(CreatureSprite):
    def get_type(self):
        return 'monster'
    
    def get_default_colour(self):
        return 'pink'
    
    def track_attack(self, turntracker):
        turntracker.track_monster_attack(self)
        
    def can_attack(self, other_creature):
        return not isinstance(other_creature, MonsterSprite)