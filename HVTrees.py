from graphics import *

factor = 1 # global variable factor
# alreadyKnown = {}
# if order not in alreadyKnown:

win = GraphWin("HV-Tree", 400, 400)

def drawLine(x, y, order, length):

    if order == 0:
        return
    else:

        if order % 2 == 1:
            x1 = x - length
            x2 = x + length
            line = Line(Point(x1, y), Point(x2, y))

            drawLine(x1, y, order - 1, length * factor)
            drawLine(x2, y, order - 1, length * factor)
        else:
            y1 = y - length
            y2 = y + length
            line = Line(Point(x, y1), Point(x, y2))

            drawLine(x, y1, order - 1, length * factor)
            drawLine(x, y2, order - 1, length * factor)

        line.draw(win)









# reading args
for arg in sys.argv[1:]:
    print(arg)

if len(sys.argv) == 3:
    factor = float(sys.argv[2])
    order = int(sys.argv[1])

    drawLine(200, 200, order, 100)

    win.getMouse()  # Pause to view result




    win.close()

import turtle

\




