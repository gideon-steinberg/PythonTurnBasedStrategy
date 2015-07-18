from Tkinter import Frame
from Tkinter import Button
from view.frames import CanvasFrame

class MainFrame(Frame):
    def say_hi(self):
        print "hi there, everyone!"
        self.canvasFrame = CanvasFrame()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.createWidgets()