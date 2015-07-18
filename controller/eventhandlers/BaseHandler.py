class BaseHandler:
    def __init__(self, frame_root):
        self.__frame_root = frame_root
        self.setup_handler()
        
    def handle_event(self, event):
        ''' method implemented in children '''
        pass
    
    def setup_handler(self):
        for event in self.events_to_bind():
            self.__frame_root.bind(event, self.handle_event)
        
    def events_to_bind(self):
        return []
    