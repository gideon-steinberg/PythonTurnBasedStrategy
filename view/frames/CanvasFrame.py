from Tkinter import Frame
from Tkinter import Tk
from Tkinter import Canvas
from utils.Constants import Constants
from controller.timers.PrintTimer import PrintTimer
from controller.timers.RefreshTimer import RefreshTimer
from view.printers.BoardPrinter import BoardPrinter

class CanvasFrame(Frame):
    
    def __initialize_canvas(self):
        self.__canvas = Canvas(self.master,
                            width=Constants.DEFAULT_FRAME_WIDTH(),
                            height=Constants.DEFAULT_FRAME_HEIGHT())
        self.__canvas.pack()
        self.pack()
        
    def __setup_timer(self):
        refresh_timer = RefreshTimer(self.master, 100, self)
        refresh_timer.setup_timer()
        
    def refresh(self):
        self.__canvas.delete('all')
        BoardPrinter.print_board(self.__canvas)
        
    def __init__(self):
        Frame.__init__(self, Tk())
        self.pack()
        
        self.__initialize_canvas()
        self.__setup_timer()
        
        print_timer = PrintTimer(self.master, 50)
        print_timer.setup_timer() 