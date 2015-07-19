from model.sprite.Sprite import Sprite
from helper.Constants import Constants
from model.sprite.PlayerSprite import PlayerSprite
from model.sprite.MonsterSprite import MonsterSprite
from model.sprite.CreatureSprite import CreatureSprite

class GameBoard:
    
    def print_board(self):
        ''' Print the board 
            Print out the type of each item
        '''
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                print self.__board[i][j].get_type() + ",",
            print ""
            
    def get_sprite(self, x, y):
        return self.__board[x][y]
    
    def get_width(self):
        return len(self.__board)
    
    def get_height(self):
        return len(self.__board[0])
    
    def get_selected_x(self):
        return self.__selected_x
    
    def get_selected_y(self):
        return self.__selected_y
    
    def set_turntracker(self, turntracker):
        self.__turntracker = turntracker
    
    def swap_sprites(self, x1, y1, x2, y2):
        temp = self.__board[x1][y1]
        self.__board[x1][y1] = self.__board[x2][y2]
        self.__board[x2][y2] = temp
        
        # get the turntracker to track this action
        if isinstance(self.__board[x1][y1], PlayerSprite):
            self.__turntracker.track_player_turn(self.__board[x1][y1])
            
        # get the turntracker to track this action
        if isinstance(self.__board[x2][y2], PlayerSprite):
            self.__turntracker.track_player_turn(self.__board[x2][y2])
            
                    # get the turntracker to track this action
        if isinstance(self.__board[x1][y1], MonsterSprite):
            self.__turntracker.track_monster_turn(self.__board[x1][y1])
            
        # get the turntracker to track this action
        if isinstance(self.__board[x2][y2], MonsterSprite):
            self.__turntracker.track_monster_turn()(self.__board[x2][y2])
    
    def select_sprite(self, x ,y, monster_action=False):
        # player turn
        if len(self.__turntracker.get_players_to_act()) > 0:
            # if a player is selected
            if isinstance(self.__board[x][y], PlayerSprite):
                # if there are no players to act ignore it
                if self.__board[x][y] in self.__turntracker.get_players_to_act():
                    # already selected
                    if self.__selected_x == x and self.__selected_y == y:
                        self.reset_selected_item()
                    else:
                        # capture this selection
                        self.__selected_x = x
                        self.__selected_y = y
            # if there is a captured player selection
            elif self.__is_captured_player_selection():
                # move the player
                player = self.__board[self.__selected_x][self.__selected_y]
                if isinstance(player, PlayerSprite):
                    player.move(self.__selected_x, self.__selected_y, x, y, self)
                self.reset_selected_item()
            else:
                self.reset_selected_item()
        # creature action   
        elif monster_action and len(self.__turntracker.get_players_to_act()) == 0:
            if self.__selected_x >= 0 and self.__selected_y >= 0:
                #move the creature
                creature = self.__board[self.__selected_x][self.__selected_y]
                if isinstance(creature, CreatureSprite):
                    creature.move(self.__selected_x, self.__selected_y, x, y, self)
                self.reset_selected_item()
            else:
                # capture this selection
                self.__selected_x = x
                self.__selected_y = y
    
    def __is_captured_player_selection(self):
        result = True
        if not isinstance(self.__board[self.__selected_x][self.__selected_y], PlayerSprite):
            result = False
        if self.__selected_x < 0 or self.__selected_y < 0:
            result = False
        return result
    
    def reset_selected_item(self):
        self.__selected_x = -1
        self.__selected_y = -1

    def __init__(self, width = Constants.DEFAULT_BOARD_WIDTH(),
                 height = Constants.DEFAULT_BOARD_HEIGHT()):
        self.__board = []
        
        # populate the __board
        # _ is an "i don't care variable"
        for _ in range(width):
            array = []
            for _ in range(height):
                array.append(Sprite())
            self.__board.append(array)
            
        # insert some player sprite
        self.__board[2][3] = PlayerSprite()
        self.__board[2][6] = PlayerSprite()
        
        # insert some creature sprites
        self.__board[0][1] = MonsterSprite()
        self.__board[2][4] = MonsterSprite()
        
        self.reset_selected_item()