from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)

    x1 = 40
    y1 = 30
    cell_size_x = x1
    cell_size_y = y1
    num_rows = int((600-(2*y1))/cell_size_y)
    num_cols = int((800-(2*x1))/cell_size_x)
    
    maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()


main()


