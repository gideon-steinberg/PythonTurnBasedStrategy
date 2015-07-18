from model.GameState import GameState
from view.frames.CanvasFrame import CanvasFrame

gb = GameState.get_board()
gb.print_board();

app = CanvasFrame()
app.mainloop()