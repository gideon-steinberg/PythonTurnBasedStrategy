from controller.timers.BaseTimer import BaseTimer

class RefreshTimer(BaseTimer):
    def do_action(self):
        self.__canvas.refresh()
        
    def __init__(self, frame_root, interval, canvas):
        self.__canvas = canvas
        BaseTimer.__init__(self, frame_root, interval)