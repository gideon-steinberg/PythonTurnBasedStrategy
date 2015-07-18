from controller.timers.BaseTimer import BaseTimer
from model.GameState import GameState
from helper.MovementHelper import MovementHelper
from random import randint
from helper.OnScreenHelper import OnScreenHelper
       
class MonsterTimer(BaseTimer):
    def do_action(self):
        players = GameState.get_turntracker().get_players_to_act()
        monsters = GameState.get_turntracker().get_monsters_to_act()
        if len(players) == 0:
            if self.__selection == None:
                monster = monsters[0]
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
                GameState.get_board().select_sprite(x, y, True)
            else:
                x = self.__selection[0]
                y = self.__selection[1]
                
                GameState.get_board().reset_selected_item()
                GameState.get_board().select_sprite(self.__monster_info[0], self.__monster_info[1], True)
                GameState.get_board().select_sprite(x, y, True)
                
                self.__selection = None
                self.__monster_info = None
                if len(GameState.get_turntracker().get_monsters_to_act()) == 0:
                    GameState.get_turntracker().refresh_players_and_monsters()
            
    def __init__(self, frame_root, interval):
        BaseTimer.__init__(self, frame_root, interval)
        self.__selection = None
        self.__monster_info = None