from model.GameBoard import GameBoard
from model.TurnTracker import TurnTracker

class GameState:
    __board = None
    __turntracker = None
    
    @staticmethod
    def get_board():
        ''' Get the Singleton GameBoard object '''
        if GameState.__board is None:
            GameState.__board = GameBoard()
            GameState.__board.set_turntracker(GameState.get_turntracker())
        return GameState.__board
    
    @staticmethod
    def reset_board():
        ''' reset the GameBoard '''
        GameState.__board = None
        
    @staticmethod
    def get_turntracker():
        ''' Get the Singleton TurnTracker object '''
        if GameState.__turntracker is None:
            GameState.__turntracker = TurnTracker()
            GameState.__turntracker.set_board(GameState.get_board())
            GameState.__turntracker.refresh_players_and_monsters()
        return GameState.__turntracker
    
    @staticmethod
    def reset_turntracker():
        ''' reset the TurnTracker '''
        GameState.__turntracker = None