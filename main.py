from tkinter import Tk, BOTH, Canvas

class Window:
    
    def __init__(self, width, height):
        self.root=Tk()
        self.root.title("Window")

        canvas = Canvas(self.root)
        canvas.pack()

        running = False

        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()

    def close(self):
        self.running = False

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y






win = Window(800, 600)
win.wait_for_close()

