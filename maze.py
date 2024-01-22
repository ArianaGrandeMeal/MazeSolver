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
        if seed:
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
        time.sleep(0.05)

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
            
            to_visit = []
            # determine which cell to visit
            # check left cell 
            if i > 0 and self._cells[l][j].visited == False:
                to_visit.append((l, j))
            # check above cell
            if j > 0 and self._cells[i][u].visited == False:
                to_visit.append((i, u))
            # check right cell
            if i < self._num_cols - 1 and self._cells[r][j].visited == False:
                to_visit.append((r, j))
            # check lower cell
            if j < self._num_rows -1 and self._cells[i][d].visited == False:
                to_visit.append((i, d))
            
            # draw cell if no options, otherwise choose an adjacent cell
            if not to_visit:
                self._draw_cell(i, j)
                return
            
            # assign cell to visit
            direction = random.randrange(len(to_visit))
            to_index = to_visit[direction]
            
            # knock down walls between current and chosen cell
            # chosen cell is right, remove right of current and left of chosen
            if to_index[0] == r:
                _current.has_right_wall = False
                self._cells[r][j].has_left_wall = False
            # chosen cell is left, remove left of current and right of chosen
            if to_index[0] == l:
                _current.has_left_wall = False
                self._cells[l][j].has_right_wall = False
            # chosen cell is below, remove bottom of current and top of chosen
            if to_index[1] == d:
                _current.has_bottom_wall = False
                self._cells[i][d].has_top_wall = False
            # chosen cell is above, remove top of current and bottom of chosen
            if to_index[1] == u:
                _current.has_top_wall = False
                self._cells[i][u].has_bottom_wall = False
           
            # recursively visit next cell
            self._break_walls_r(to_index[0], to_index[1])
            
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    # helper for _solve_r() method to improve readability while iteratively checking 
    # adjacent cells-x,y represent i,j indexes for each-for open path.  
    # if cell is valid, move is drwan and _solve_r() is called recursively on successive
    # cells, otherwise, an undo move is drawn
    def _try_cell(self, current, x, y):
        current.draw_move(self._cells[x][y])
        if self._solve_r(x,y):
            return True
        current.draw_move(self._cells[x][y], True)
        return False
    
    def _solve_r(self, i, j):
        self._animate()
        
        # set and visit current cell
        current = self._cells[i][j]
        current.visited = True
        
        # if end cell is reached, maze is solved
        if self._cells[-1][-1].visited:
            return True
        
        l = i-1
        r = i+1
        u = j-1
        d = j+1
        directions = [[l, j, 'left'], [i, u, 'top'], [r, j, 'right'], [i, d, 'bottom']]
        # Make sure we are within grid and path is open, then _try_cell() recrusively attempts
        # to check and draw path through successive cells in same direction
        for x, y, dir in directions:
            if 0 <= x < self._num_cols and 0 <= y < self._num_rows:
                if dir == 'left' and not current.has_left_wall and not self._cells[x][y].visited:
                    if self._try_cell(current, x, y):
                        return True
                if dir == 'top' and not current.has_top_wall and not self._cells[x][y].visited:
                    if self._try_cell(current, x, y):
                        return True
                if dir == 'right' and not current.has_right_wall and not self._cells[x][y].visited:
                    if self._try_cell(current, x, y):
                        return True
                if dir == 'bottom' and not current.has_bottom_wall and not self._cells[x][y].visited:
                    if self._try_cell(current, x, y):
                        return True
        
        # signifies a wall or dead end in attempted direction, returns false 
        return False
                
    # creates moves for solution using depth-first search.  
    def solve(self):
        return self._solve_r(0,0)
    