from helper.Constants import Constants
class OnScreenHelper:
    @staticmethod
    def is_on_screen(x, y):
        return x >= 0 and y >= 0 and x < Constants.DEFAULT_BOARD_WIDTH() and y < Constants.DEFAULT_BOARD_HEIGHT()