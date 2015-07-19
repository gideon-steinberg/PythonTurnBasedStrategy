from model.sprite.PlayerSprite import PlayerSprite
from model.sprite.MonsterSprite import MonsterSprite

class SpriteSwapper:
    def swap_sprites(self, x1, y1, x2, y2, board):
        
        first_sprite = board.get_sprite(x1 , y1)
        second_sprite = board.get_sprite(x2 , y2)
        
        board.set_sprite(x1, y1, second_sprite)
        board.set_sprite(x2, y2, first_sprite)
        
        # get the turntracker to track this action
        if isinstance(second_sprite, PlayerSprite):
            self.__turntracker.track_player_move(second_sprite, x1, y1)
            
        # get the turntracker to track this action
        if isinstance(second_sprite, MonsterSprite):
            self.__turntracker.track_monster_move(second_sprite, x1, y1)
            
    def __init__(self, turnracker):
        self.__turntracker = turnracker