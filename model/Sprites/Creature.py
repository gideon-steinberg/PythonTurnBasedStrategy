class Creature:
    def is_blank(self):
        return False
    
    def get_type(self):
        return 'creature'
    
    def get_hp(self):
        return self.hp
    
    def __init__(self):
        self.hp = 5