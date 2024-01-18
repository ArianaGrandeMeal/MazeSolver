from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        center1 = Point(((self._x1 + self._x2)/2), ((self._y1 + self._y2)/2))
        center2 = Point(((to_cell._x1 + to_cell._x2)/2), ((to_cell._y1 + to_cell._y2)/2))
        line = Line(center1, center2)
        
        if to_cell.visited == True:
            undo = True
        
        fill_color = "red"
        if undo == True:
            fill_color = "gray"
        

        if ((center1.x < center2.x and center1.y == center2.y) 
            and self.has_left_wall == False and to_cell.has_right_wall == False):
            self._win.draw_line(line, fill_color)
            to_cell.visited = True
        elif ((center1.x == center2.x and center1.y < center2.y)
            and self.has_bottom_wall == False and to_cell.has_top_wall == False):
            self._win.draw_line(line, fill_color)
            to_cell.visited = True
        elif ((center1.x > center2.x and center1.y == center2.y)
            and self.has_right_wall == False and to_cell.has_left_wall == False):
            self._win.draw_line(line, fill_color)
            to_cell.visited = True
        elif ((center1.x == center2.x and center1.y > center2.y) 
            and self.has_top_wall == False and to_cell.has_bottom_wall == False):
            self._win.draw_line(line, fill_color)
            to_cell.visited = True
        
    
        
        # need to write logic to set undo flag.
        