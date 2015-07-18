class BaseTimer:
    def __init__(self, frame_root, interval):
        self.__frame_root = frame_root
        self.__interval = interval
        self.__timer_tick()
        
    def do_action(self):
        ''' method implemented in children '''
        pass
    
    def __timer_tick(self):
        self.do_action()
        self.__frame_root.after(self.__interval, self.__timer_tick)
