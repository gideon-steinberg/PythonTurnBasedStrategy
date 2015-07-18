from controller.eventhandlers.BaseHandler import BaseHandler
class ArrowHandler(BaseHandler):
    def handle_event(self, event):
        if event.keycode == 38:
            print 'up'
        if event.keycode == 40:
            print 'down'
        if event.keycode == 37:
            print 'left'
        if event.keycode == 39:
            print 'right'
            
    def events_to_bind(self):
        return ['<Up>', '<Down>', '<Right>', '<Left>']