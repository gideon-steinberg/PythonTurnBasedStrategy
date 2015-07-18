from model.Sprites.Creature import Creature

class Player(Creature):
    def get_type(self):
        return 'player'