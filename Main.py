from Tkinter import Tk
from view.MainFrame import MainFrame

root = Tk()
app = MainFrame(master=root)
app.mainloop()
root.destry()