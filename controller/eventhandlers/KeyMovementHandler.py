from controller.eventhandlers.BaseHandler import BaseHandler
class KeyMovementHandler(BaseHandler):
    def handle_event(self, event):
        if event.char == 'w':
            print 'up'
        if event.char == 's':
            print 'down'
        if event.char == 'a':
            print 'left'
        if event.char == 'd':
            print 'right'
            
    def events_to_bind(self):
        return ['a', 'w', 's', 'd']