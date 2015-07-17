from Tkinter import Tk
from MainFrame import MainFrame

root = Tk()
app = MainFrame(master=root)
app.mainloop()
root.destroy()