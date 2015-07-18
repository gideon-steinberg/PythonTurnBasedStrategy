from model.GameBoard import GameBoard

class GameState:
    __board = None
    
    @staticmethod
    def get_board():
        ''' Get the Singleton GameBoard object '''
        if GameState.__board is None:
            GameState.__board = GameBoard()
        return GameState.__board
    
    @staticmethod
    def reset_board():
        ''' reset the GameBoard '''
        GameState.__board = None