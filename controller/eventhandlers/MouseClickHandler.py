from controller.eventhandlers.BaseHandler import BaseHandler
from helper.Constants import Constants
from model.helper.SpriteSelector import SpriteSelector
class MouseClickHandler(BaseHandler):
    def handle_event(self, event):
        x = event.x / Constants.DEFAULT_SPRITE_WIDTH()
        y = event.y / Constants.DEFAULT_SPRITE_HEIGHT()
        SpriteSelector.select_player_sprite(x, y)
            
    def events_to_bind(self):
        return ['<Button-1>']