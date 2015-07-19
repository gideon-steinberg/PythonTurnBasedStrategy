from Tkinter import Frame
from Tkinter import Tk
from Tkinter import Canvas
from helper.Constants import Constants
from controller.timers.RefreshTimer import RefreshTimer
from controller.eventhandlers.ArrowHandler import ArrowHandler
from controller.eventhandlers.KeyMovementHandler import KeyMovementHandler
from controller.eventhandlers.MouseClickHandler import MouseClickHandler
from view.printers.SelectPrinter import SelectPrinter
from view.printers.BoardPrinter import BoardPrinter
from controller.timers.MonsterTimer import MonsterTimer

class CanvasFrame(Frame):
    
    def __initialize_canvas(self):
        self.__canvas = Canvas(self.master,
                            width=Constants.DEFAULT_FRAME_WIDTH(),
                            height=Constants.DEFAULT_FRAME_HEIGHT())
        self.__canvas.pack()
        self.pack()
        
    def __setup_timer(self):
        RefreshTimer(self.master, 100, self)
        MonsterTimer(self.master, 1000)
        
    def __setup_handlers(self):
        ArrowHandler(self.master)
        KeyMovementHandler(self.master)
        MouseClickHandler(self.master)
        
    def refresh(self):
        self.__canvas.delete('all')
        BoardPrinter.print_board(self.__canvas)
        SelectPrinter.print_selected(self.__canvas)
        
    def __init__(self):
        Frame.__init__(self, Tk())
        self.pack()
        
        self.__initialize_canvas()
        self.__setup_timer()
        self.__setup_handlers()