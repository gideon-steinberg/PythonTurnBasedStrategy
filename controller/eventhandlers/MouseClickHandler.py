from controller.eventhandlers.BaseHandler import BaseHandler
from helper.Constants import Constants
class MouseClickHandler(BaseHandler):
    def handle_event(self, event):
        x_index = event.x / Constants.DEFAULT_SPRITE_WIDTH()
        y_index = event.y / Constants.DEFAULT_SPRITE_HEIGHT()
        print x_index,
        print y_index
            
    def events_to_bind(self):
        return ['<Button-1>']