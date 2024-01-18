from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    line = Line(Point(50,50), Point(400,400))
    win.draw_line(line, "black")
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

