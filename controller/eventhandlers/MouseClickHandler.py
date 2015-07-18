from controller.eventhandlers.BaseHandler import BaseHandler
from helper.Constants import Constants
from model.GameState import GameState
class MouseClickHandler(BaseHandler):
    def handle_event(self, event):
        x_index = event.x / Constants.DEFAULT_SPRITE_WIDTH()
        y_index = event.y / Constants.DEFAULT_SPRITE_HEIGHT()
        GameState.get_board().select_item(x_index, y_index)
            
    def events_to_bind(self):
        return ['<Button-1>']