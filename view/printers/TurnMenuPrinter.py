from helper.Constants import Constants
from model.state.GameState import GameState
class TurnMenuPrinter:
    @staticmethod
    def print_turn_menu(canvas):
        turntracker = GameState.get_turntracker()
        players_to_move = turntracker.get_players_to_move()
        monsters_to_move = turntracker.get_monsters_to_move()
        players_to_attack = turntracker.get_players_to_attack()
        monsters_to_attack = turntracker.get_monsters_to_attack()
        
        separator_x = Constants.DEFAULT_SPRITE_WIDTH() + Constants.DEFAULT_FRAME_WIDTH() + 5
        # separator line between players and monsters
        canvas.create_line(separator_x, 0, separator_x, Constants.DEFAULT_FRAME_HEIGHT())

        # labels
        canvas.create_text(Constants.DEFAULT_FRAME_WIDTH() + 25, 15, text="Players")
        canvas.create_text(separator_x + 30, 15, text="Monsters")
        
        players = []
        monsters = []
        for player in players_to_move:
            if player not in players:
                players.append(player)
                
        for player in players_to_attack:
            if player not in players:
                players.append(player)
                
        for monster in monsters_to_move:
            if monster not in monsters:
                monsters.append(monster)
                
        for monster in monsters_to_attack:
            if monster not in monsters:
                monsters.append(monster)
        
        position_down = 0
        x_starting = Constants.DEFAULT_FRAME_WIDTH()
        for player in players:
            TurnMenuPrinter.__print_small_box(canvas, x_starting, 
                                              position_down * 60 + 20,
                                              player.get_default_colour())
            
            player_info = turntracker.get_player_info(player)
            
            canvas.create_text(x_starting + 25, position_down * 60 + 65,
                               text="(" + str(player_info[0]) + "," + str(player_info[1]) + ")")
            
            position_down = position_down + 1
            
        position_down = 0
        x_starting = Constants.DEFAULT_FRAME_WIDTH() + 50
        for monster in monsters:
            TurnMenuPrinter.__print_small_box(canvas, x_starting, 
                                              position_down * 60 + 20,
                                              monster.get_default_colour())
            
            monster_info = turntracker.get_monster_info(monster)
            
            canvas.create_text(x_starting + 25, position_down * 60 + 65,
                               text="(" + str(monster_info[0]) + "," + str(monster_info[1]) + ")")
            
            position_down = position_down + 1
            
    @staticmethod
    def __print_small_box(canvas, x, y, colour):
        canvas.create_rectangle(x + 15,
                                y + 15,
                                x + 35,
                                y + 35,
                                fill=colour)