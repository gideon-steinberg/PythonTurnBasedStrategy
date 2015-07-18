from controller.timers.BaseTimer import BaseTimer

class PrintTimer(BaseTimer):
    def do_action(self):
        print self.__counter
        self.__counter = self.__counter + 1
        
    def __init__(self, frame_root, interval):
        self.__counter = 0
        BaseTimer.__init__(self, frame_root, interval)