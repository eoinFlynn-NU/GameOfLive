from board import Board

class Controller():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)

    
    def start_sim(self):
        self.board.start_sim()
    

    def set_alive_cells(self):
        alive_cells = [(9,9),(10,10),(11,10),(12,9),(11,8),(10,8),(9,10)]
        self.board.revive_cells(alive_cells)
    
    
controller = Controller(20,20)
controller.set_alive_cells()
controller.start_sim()