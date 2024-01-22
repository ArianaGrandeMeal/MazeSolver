import time, random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        
    
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        for i in range(self._num_cols): 
            for j in range(self._num_rows):
                self._draw_cell(i, j)
  
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = (i * self._cell_size_x) + self._x1
        y1 = (j * self._cell_size_y) + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        _current = self._cells[i][j]
        _current.visited = True
        l = i-1
        r = i+1
        u = j-1
        d = j+1

        while True:
            
            _to_visit = []
            # determine which cell to visit
            # check left cell 
            if i > 0 and self._cells[l][j].visited == False:
                _to_visit.append((l, j))
            # check above cell
            if j > 0 and self._cells[i][u].visited == False:
                _to_visit.append((i, u))
            # check right cell
            if i < self._num_cols - 1 and self._cells[r][j].visited == False:
                _to_visit.append((r, j))
            # check lower cell
            if j < self._num_rows -1 and self._cells[i][d].visited == False:
                _to_visit.append((i, d))
            
            # draw cell if no options, otherwise choose an adjacent cell
            if not _to_visit:
                self._draw_cell(i, j)
                return
            
            _direction = random.randrange(len(_to_visit))
            _to_index = _to_visit[_direction]
            
            # knock down walls between current and chosen cell
            # chosen cell is right, remove right of current and left of chosen
            if _to_index[0] == r:
                _current.has_right_wall = False
                self._cells[r][j].has_left_wall = False
            # chosen cell is left, remove left of current and right of chosen
            if _to_index[0] == l:
                _current.has_left_wall = False
                self._cells[l][j].has_right_wall = False
            # chosen cell is below, remove bottom of current and top of chosen
            if _to_index[1] == d:
                _current.has_bottom_wall = False
                self._cells[i][d].has_top_wall = False
            # chosen cell is above, remove top of current and bottom of chosen
            if _to_index[1] == u:
                _current.has_top_wall = False
                self._cells[i][u].has_bottom_wall = False
           
            # recursively visit next cell
            self._break_walls_r(_to_index[0], _to_index[1])
            
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

            