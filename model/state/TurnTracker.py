from model.sprite.PlayerSprite import PlayerSprite
from model.sprite.MonsterSprite import MonsterSprite
class TurnTracker:
    
    def set_board(self, board):
        self.__board = board
    
    def refresh_players_and_monsters(self):
        
        self.__players  = []
        self.__monsters = []
        self.__players_to_act = []
        self.__monsters_to_act = []
        self.__monster_info = {}
        width = self.__board.get_width()
        height = self.__board.get_height()
        
        for i in range(width):
            for j in range(height):
                sprite = self.__board.get_sprite(i,j)
                if isinstance(sprite, PlayerSprite):
                    self.__players.append(sprite)
                    self.__players_to_act.append(sprite)
                elif isinstance(sprite, MonsterSprite):
                    self.__monsters.append(sprite)
                    self.__monsters_to_act.append(sprite)
                    self.__monster_info[sprite] = [i, j]
                    
    def get_players_to_act(self):
        return self.__players_to_act
    
    def get_monsters_to_act(self):
        return self.__monsters_to_act
    
    def get_monster_info(self, monster):
        return self.__monster_info[monster]
    
    def track_player_turn(self, player):
        self.__players_to_act.remove(player)
        
    def track_monster_turn(self, monster):
        self.__monsters_to_act.remove(monster)