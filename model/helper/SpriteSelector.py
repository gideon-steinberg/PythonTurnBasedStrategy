from model.state.GameState import GameState
from model.sprite.PlayerSprite import PlayerSprite
from model.helper.SpriteSwapper import SpriteSwapper
from model.sprite.CreatureSprite import CreatureSprite
class SpriteSelector:
    
    @staticmethod
    def select_player_sprite(x, y):
        turntracker = GameState.get_turntracker()
        sprite = GameState.get_board().get_sprite(x, y)
        
        # if it is not the players turn don't do anything
        if not turntracker.is_player_turn():
            return
        
        if isinstance(sprite, PlayerSprite):
            SpriteSelector.__update_player_selection(x, y)
        elif SpriteSelector.__player_is_selected(sprite):
            SpriteSelector.__handle_player_is_selected(x, y)
        else:
            SpriteSelector.__reset_selection()
        
    @staticmethod
    def select_monster_sprite(x, y):
        board = GameState.get_board()
        turntracker = GameState.get_turntracker()
        selected_x = board.get_selected_x()
        selected_y = board.get_selected_y()
        
        # if it is not the momsters turn don't do anything
        if turntracker.is_player_turn():
            return
        
        if selected_x >= 0 and selected_y >= 0:
            SpriteSelector.__move_sprite(x, y)
        else:
            # capture this selection
            board.set_selected_x(x)
            board.set_selected_y(y)
    
    @staticmethod
    def __update_player_selection(x, y):
        board = GameState.get_board()
        turntracker = GameState.get_turntracker()
        selected_x = board.get_selected_x()
        selected_y = board.get_selected_y()
        player = board.get_sprite(x, y)
        
        if (player in turntracker.get_players_to_move() or
           player in turntracker.get_players_to_attack()):
            # already selected
            if selected_x == x and selected_y == y:
                SpriteSelector.__reset_selection()
            else:
                # capture this selection
                board.set_selected_x(x)
                board.set_selected_y(y)
    
    @staticmethod
    def __handle_player_is_selected(x, y):
        board = GameState.get_board()
        turntracker = GameState.get_turntracker()
        selected_x = board.get_selected_x()
        selected_y = board.get_selected_y()
        player = board.get_sprite(selected_x, selected_y)
        
        if player in turntracker.get_players_to_move():
            SpriteSelector.__move_sprite(x, y)
        elif player in turntracker.get_players_to_attack():
            SpriteSelector.__attack_sprite(x, y)
            
    @staticmethod
    def __move_sprite(x, y):
        board = GameState.get_board()
        turntracker = GameState.get_turntracker()
        selected_x = board.get_selected_x()
        selected_y = board.get_selected_y()
        player = board.get_sprite(selected_x, selected_y)
        
        if isinstance(player, CreatureSprite):
            player.move(selected_x, selected_y,
                        x, y, board, SpriteSwapper(turntracker))
        SpriteSelector.__reset_selection()
        
    @staticmethod
    def __attack_sprite(x, y):
        board = GameState.get_board()
        turntracker = GameState.get_turntracker()
        selected_x = board.get_selected_x()
        selected_y = board.get_selected_y()
        first_sprite = board.get_sprite(selected_x, selected_y)
        second_sprite = board.get_sprite(x, y)
        
        if isinstance(first_sprite, CreatureSprite) and isinstance(second_sprite, CreatureSprite):
            first_sprite.attack(second_sprite, turntracker)
            
        SpriteSelector.__reset_selection()
        
    @staticmethod
    def __player_is_selected(sprite):
        board = GameState.get_board()
        x = board.get_selected_x()
        y = board.get_selected_y()
        
        return isinstance(board.get_sprite(x, y), PlayerSprite) or x < 0 or y < 0
    
    @staticmethod
    def __reset_selection():
        GameState.get_board().reset_selected_item()