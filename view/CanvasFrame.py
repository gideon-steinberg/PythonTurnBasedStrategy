from Tkinter import Frame
from Tkinter import Tk
from Tkinter import Canvas
from utils.Constants import Constants
from controller.timers.PrintTimer import PrintTimer
from controller.timers.RefreshTimer import RefreshTimer

class CanvasFrame(Frame):
    
    def initializeCanvas(self):
        self.__canvas = Canvas(self.master,
                            width=Constants.DEFAULT_FRAME_WIDTH(),
                            height=Constants.DEFAULT_FRAME_HEIGHT())
        self.__canvas.pack()
        self.pack()
        
    def __setup_timer(self):
        self.x = 10
        self.y = 10
        self.rectangleX = 50
        self.rectangleY = 70
        refresh_timer = RefreshTimer(self.master, 100, self)
        refresh_timer.setup_timer()
        
    def refresh(self):
        self.__canvas.delete('all')
        self.__canvas.create_line(self.x, self.y, 50, 50)
        self.__canvas.create_rectangle(self.rectangleX, self.rectangleY, self.rectangleX + 150, 75, fill="blue")
        self.x = self.x + 1
        self.y = self.y + 2
        self.rectangleX = self.rectangleX + 1
        
    def __init__(self):
        Frame.__init__(self, Tk())
        self.pack()
        self.initializeCanvas()
        self.__setup_timer()
        print_timer = PrintTimer(self.master, 50)
        print_timer.setup_timer() 