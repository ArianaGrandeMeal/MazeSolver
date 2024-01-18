from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root=Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color = "black"):
        line.draw(self.__canvas, fill_color )

    def draw_cell(self, cell, fill_color = "Black"):
        cell.draw(cell.top_left, cell.bottom_right, self.__canvas, fill_color)

    def close(self):
        self.__running = False

    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)
        
class Cell:
    def __init__(self, _x1, _y1, _x2, _y2, _win, left=True, right=True, top=True, bottom=True):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self._x1 = _x1
        self._y1 = _y1
        self._x2 = _x2
        self._y2 = _y2
        self._win = _win
        
        self.top_left = Point(self._x1, self._y1)
        self.bottom_right = Point(self._x2, self._y2)


    def draw(self, top_left, bottom_right, canvas, fill_color="black"):
        self.tl = top_left
        self.bl = Point(top_left.x, bottom_right.y)
        self.br = bottom_right
        self.tr = Point(bottom_right.x, top_left.y)

        lines = []
        if self.left:
            line = Line(self.tl, self.bl)
            lines.append(line)
        if self.right:
            line = Line(self.tr, self.br)
            lines.append(line)
        if self.top:
            line = Line(self.tl, self.tr)
            lines.append(line)
        if self.bottom:
            line = Line(self.bl, self.br)
            lines.append(line)
        
        for line in lines:
            line.draw(canvas, fill_color)



        



    '''
    self.top_left = top_left
    self.bottm_right = bottom_right
    '''    
