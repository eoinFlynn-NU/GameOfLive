
import typing



class Cell():
    def __init__(self, width_posn: int, length_posn: int) -> None:
        self.alive = False
        self.alive_next_turn = False
        self.width = width_posn
        self.length = length_posn
    
    def set_alive(self, is_alive: bool):
        self.alive = is_alive

    def is_alive(self):
        return self.alive

    def set_alive_next_turn(self, is_alive: bool):
        self.alive_next_turn = is_alive
    
    def is_alive_next_turn(self):
        return self.alive_next_turn
    

class Board():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.cells = self.__create_dead_board(self.width, self.height)
        self.alive_cells = []
    
    def __str__(self):
        board = ""
        for w in range(self.width):
            for h in range(self.height):
                if self.cells[w][h].is_alive():
                    board += "☺"
                else:
                    board += "■"
            board += "\n"
        return board


    def __create_dead_board(self,width: int, height: int):
        dead_board = []
        for w in range(width):
            dead_row = []
            for h in range(height):
                dead_row.append(Cell(w,h))
            dead_board.append(dead_row)

        return dead_board
    
    def revive_cells(self, list_of_posns):
        for posn in list_of_posns:
            self.cells[posn[0]][posn[1]].set_alive(True)
            self.cells[posn[0]][posn[1]].set_alive_next_turn(True)
            self.alive_cells.append(posn)
    

    def __get_relavent_cell_posns(self):
        relavent_cell_posns = set()
        for posn in self.alive_cells:
            for relative_w in range(-1,2):
                for relative_h in range(-1,2):
                    neighbor_w = posn[0] + relative_w
                    neighbor_h = posn[1] + relative_h
                    if (neighbor_w >= 0 and neighbor_w < self.width) and (neighbor_h >= 0 and neighbor_h < self.height):
                        relavent_cell_posns.add((neighbor_w, neighbor_h))
        return relavent_cell_posns

    def __find_alive_neighbors(self, posn):
        alive_neighbors = 0
        for relative_w in range(-1,2):
            for relative_h in range(-1,2):
                neighbor_w = posn[0] + relative_w
                neighbor_h = posn[1] + relative_h
                if neighbor_w == posn[0] and neighbor_h == posn[1]:
                    continue
                if (neighbor_w >= 0 and neighbor_w < self.width) and (neighbor_h >= 0 and neighbor_h < self.height):
                    if self.cells[neighbor_w][neighbor_h].is_alive():
                        alive_neighbors += 1
        return alive_neighbors
    

    def set_cells_state_next_turn(self, relavent_cell_posns):
        alive_next_turn = []
        for posn in relavent_cell_posns:
            alive_neighbors = self.__find_alive_neighbors(posn)
            currently_alive = self.cells[posn[0]][posn[1]].is_alive()
            if currently_alive and alive_neighbors < 2:
                self.cells[posn[0]][posn[1]].set_alive_next_turn(False)
                #print("Died: {}".format(posn) )
            elif currently_alive and alive_neighbors >= 2 and alive_neighbors <= 3:
                self.cells[posn[0]][posn[1]].set_alive_next_turn(True)
                alive_next_turn.append(posn)
            elif currently_alive and alive_neighbors > 3:
                self.cells[posn[0]][posn[1]].set_alive_next_turn(False)
                #print("Died: {}".format(posn) )
            elif not currently_alive and alive_neighbors == 3:
                self.cells[posn[0]][posn[1]].set_alive_next_turn(True)
                alive_next_turn.append(posn)
                #print("Born: {}".format(posn) )
        
        return alive_next_turn

    def update_cell_state(self, relavent_cell_posns):
        for posn in relavent_cell_posns:
            if self.cells[posn[0]][posn[1]].is_alive_next_turn():
                self.cells[posn[0]][posn[1]].set_alive(True)
            else:
                self.cells[posn[0]][posn[1]].set_alive(False)

    def start_sim(self):
        loops = 0
        while loops < 25:
            print("loop {}".format(loops))
            print(self)
            relavent_cell_posns = self.__get_relavent_cell_posns()
            posns_alive_next_turn = self.set_cells_state_next_turn(relavent_cell_posns)
            self.update_cell_state(relavent_cell_posns)
            self.alive_cells = posns_alive_next_turn
            loops += 1







#new_board = Board(20,20)
