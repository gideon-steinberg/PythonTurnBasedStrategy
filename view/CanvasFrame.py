from Tkinter import Frame
from Tkinter import Tk
from Tkinter import Canvas
from Utils.Constants import Constants

class CanvasFrame(Frame):
    
    def initializeCanvas(self):
        self.canvas = Canvas(self.master,
                            width=Constants.DEFAULT_FRAME_WIDTH(),
                            height=Constants.DEFAULT_FRAME_HEIGHT())
        self.canvas.pack()
        self.pack()
        
    def setup_timer(self):
        self.x = 10
        self.y = 10
        self.rectangleX = 50
        self.rectangleY = 70
        self.timer_tick()
        
    def timer_tick(self):
        self.canvas.delete('all')
        self.canvas.create_line(self.x, self.y, 50, 50)
        self.canvas.create_rectangle(self.rectangleX, self.rectangleY, self.rectangleX + 150, 75, fill="blue")
        self.x = self.x + 1
        self.y = self.y + 2
        self.rectangleX = self.rectangleX + 1
        self.master.after(1000, self.timer_tick)
        
    def __init__(self):
        Frame.__init__(self, Tk())
        self.pack()
        self.initializeCanvas()
        self.setup_timer()