import time
from graphics import Window, Point, Line
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = int(num_rows)
        self.num_cols = int(num_cols)
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    
    def _create_cells(self):
        self._cells = []
        for column in range(1, self.num_cols):
            self._col = []
            for row in range(1, self.num_rows):
                cell = Cell(self._win)
                self._col.append(cell)
            self._cells.append(self._col)

        i=1
        for column in range(len(self._cells)): 
            j=1
            for cell in range(len(self._cells[column])):
                self._draw_cell(i, j)
                j += 1
            i += 1
  
    
    def _draw_cell(self, i, j):
        self.x1pos = (i * self.cell_size_x) + self.x1
        self.y1pos = (j * self.cell_size_y) + self.y1
        self.x2pos = self.x1pos + self.cell_size_x
        self.y2pos = self.y1pos + self.cell_size_y

        cell = self._cells[i-1][j-1]
        cell.draw(self.x1pos, self.y1pos, self.x2pos, self.y2pos)

        self._animate()
        

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

