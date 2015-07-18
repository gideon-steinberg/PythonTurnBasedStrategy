from model.GameState import GameState
from model.sprite.PlayerSprite import PlayerSprite
from model.sprite.MonsterSprite import MonsterSprite
class TurnTracker:
    def refresh_players_and_monsters(self):
        board = GameState.get_board()
        
        self.__players  = []
        self.__monsters = []
        self.__players_to_act = []
        width = board.get_width()
        height = board.get_height()
        
        for i in range(width):
            for j in range(height):
                sprite = board.get_sprite(i,j)
                if isinstance(sprite, PlayerSprite):
                    self.__players.append(sprite)
                    self.__players_to_act.append(sprite)
                elif isinstance(sprite, MonsterSprite):
                    self.__monsters.append(sprite)
                    
    def get_players_to_act(self):
        return self.__players_to_act
    
    def get_monsters(self):
        return self.__monsters
    
    def __init__(self):
        self.refresh_players_and_monsters()