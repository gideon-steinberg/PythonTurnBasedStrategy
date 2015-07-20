from controller.timers.BaseTimer import BaseTimer
from model.state.GameState import GameState
from helper.MovementHelper import MovementHelper
from random import randint
from helper.OnScreenHelper import OnScreenHelper
from model.helper.SpriteSelector import SpriteSelector
       
class MonsterTimer(BaseTimer):
    def do_action(self):
        if not GameState.get_turntracker().is_player_turn():
            if len(GameState.get_turntracker().get_monsters_to_move()) == 0:
                GameState.get_turntracker().refresh_players_and_monsters()
            elif self.__selection == None:
                monster = GameState.get_turntracker().get_monsters_to_move()[0]
                movement_range = monster.get_movement_range()
                monster_info = GameState.get_turntracker().get_monster_info(monster)
                x = monster_info[0]
                y = monster_info[1]
                possible_movements = MovementHelper.get_possible_movement_spaces(movement_range, x, y)
                
                new_x = -1
                new_y = -1
                while not OnScreenHelper.is_on_screen(new_x, new_y):
                    random = randint(0, len(possible_movements) - 1)
                    self.__selection = possible_movements[random]
                    new_x = self.__selection[0]
                    new_y = self.__selection[1]
                self.__monster_info = monster_info
                SpriteSelector.select_monster_sprite(x, y)
            else:
                x = self.__selection[0]
                y = self.__selection[1]
                
                GameState.get_board().reset_selected_item()
                SpriteSelector.select_monster_sprite(self.__monster_info[0], self.__monster_info[1])
                SpriteSelector.select_monster_sprite(x, y)
                
                self.__selection = None
                self.__monster_info = None
                if len(GameState.get_turntracker().get_monsters_to_move()) == 0:
                    GameState.get_turntracker().refresh_players_and_monsters()
            
    def __init__(self, frame_root, interval):
        self.__selection = None
        self.__monster_info = None
        BaseTimer.__init__(self, frame_root, interval)