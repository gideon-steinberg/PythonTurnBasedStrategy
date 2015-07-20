from model.sprite.PlayerSprite import PlayerSprite
from model.sprite.MonsterSprite import MonsterSprite
import math
class TurnTracker:
    
    def set_board(self, board):
        self.__board = board
    
    def refresh_players_and_monsters(self):
        
        self.__players  = []
        self.__monsters = []
        self.__players_to_move = []
        self.__monsters_to_move = []
        self.__players_to_attack = []
        self.__monsters_to_attack = []
        self.__monster_info = {}
        self.__player_info = {}
        width = self.__board.get_width()
        height = self.__board.get_height()
        
        for i in range(width):
            for j in range(height):
                sprite = self.__board.get_sprite(i,j)
                if isinstance(sprite, PlayerSprite):
                    self.__players.append(sprite)
                    self.__players_to_move.append(sprite)
                    self.__player_info[sprite] = [i, j]
                elif isinstance(sprite, MonsterSprite):
                    self.__monsters.append(sprite)
                    self.__monsters_to_move.append(sprite)
                    self.__monster_info[sprite] = [i, j]
                    
    def get_players_to_move(self):
        return self.__players_to_move
    
    def get_monsters_to_move(self):
        return self.__monsters_to_move
    
    def get_players_to_attack(self):
        return self.__players_to_attack
    
    def get_monsters_to_attack(self):
        return self.__monsters_to_attack
    
    def get_monster_info(self, monster):
        return self.__monster_info[monster]
    
    def get_player_info(self, player):
        return self.__player_info[player]
    
    def track_player_move(self, player, x, y):
        self.__players_to_move.remove(player)
        self.__player_info[player] =  [x, y]
        
        # find monsters that are 1 square away
        for monster in self.__monster_info.keys():
            monster_info = self.__monster_info[monster]
            if math.fabs(monster_info[0] - x) + math.fabs(monster_info[1] - y) <= player.get_attack_range():
                self.__players_to_attack.append(player)
                break
        
    def track_monster_move(self, monster, x, y):
        self.__monsters_to_move.remove(monster)
        self.__monster_info[monster] = [x, y]
        
        # find players that are 1 square away
        for player in self.__player_info.keys():
            player_info = self.__player_info[player]
            if math.fabs(x - player_info[0]) + math.fabs(y - player_info[1]) <= monster.get_attack_range():
                self.__monsters_to_attack.append(monster)
                break
    
    def track_player_attack(self, player):
        self.__players_to_attack.remove(player)
        
    def track_monster_attack(self, monster):
        self.__monsters_to_attack.remove(monster)
            
    def is_player_turn(self):
        return ((len(self.__players_to_move) > 0 or
                len(self.__players_to_attack) > 0) and
                len(self.__monsters_to_attack) == 0)