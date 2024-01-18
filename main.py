from graphics import Window, Point, Line, Cell

def main():
    win = Window(850, 600)

    cells = [
    Cell(50, 50, 100, 100, win),
    Cell(100, 50, 150, 100, win, True, True, True, False),
    Cell(150, 50, 200, 100, win, True, False, True, True),
    Cell(200, 50, 250, 100, win, True, True, False, True),
    Cell(250, 50, 300, 100, win, True, True, True, False),
    Cell(300, 50, 350, 100, win, False, False, True, True),
    Cell(350, 50, 400, 100, win, False, True, False, True),
    Cell(400, 50, 450, 100, win, False, True, True, False),
    Cell(450, 50, 500, 100, win, True, False, False, True),
    Cell(500, 50, 550, 100, win, True, False, True, False),
    Cell(550, 50, 600, 100, win, True, True, False, False),
    Cell(600, 50, 650, 100, win, False, False, False, True),
    Cell(650, 50, 700, 100, win, False, False, True, False),
    Cell(700, 50, 750, 100, win, False, True, False, False),
    Cell(750, 50, 800, 100, win, True, False, False, False)
    ]
    for cell in cells:
        win.draw_cell(cell, fill_color="Black")

    win.wait_for_close()

main()


'''
Personal Attempt at drawing grid - not pat of actual code


 width = 800
    length = 600
    win = Window(800, 600)
    
    dist = 50
    points = []
    lines = []
    
    for i in range(dist, width, dist):
        for j in range(dist, length, dist):
            point = Point(i, j)
            points.append(point)
    
    
    for p1 in points:
        for p2 in points:
            if (p1.x == p2.x and p1.y == p2.y + dist) or (p1.x == p2.x + dist and p1.y == p2.y):
                line = Line(p1, p2)
                lines.append(line)

    for line in lines:
        win.draw_line(line, "black")
'''

