# MazeSolver
Program to automate designing and solving of mazes.  Program uses tkinter.




##################################################################### 
#  THIS PORTION OF README CONTAINS CODE THAT I HAVE WRITTEN         #
#  INDEPENDENTLY OF THE PROVIDED SOLUTION CODE, AND WHICH DIFFERS   #
#  FROM THE SOLUTION CODE, BUT THAT I WISH TO RETAIN FOR REFERENCE  #
#  THROUGHOUT THE PROJECT.                                          #
#####################################################################

# cell_draw() method from Cell class:

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