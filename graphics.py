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

    def close(self):
        self.__running = False



class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, Canvas, fill_color):
        canvas = Canvas
        self.fill_color = fill_color

        canvas.create_line(x1, y1, x2, y2, )
        canvas.pack()


win = Window(800, 600)
win.wait_for_close()
