"""
Применение функций и модуляризации в черепашке!!!
"""

import turtle
import my_graphics

X1 = 0
Y1 = 100
X2 = -100
Y2 = -100
X3 = 100
Y3 = -100
RADIUS = 50

def main():
    turtle.showturtle()
    turtle.hideturtle()

    my_graphics.square(X2, Y2, (X3 -X2), 'gray')

    my_graphics.circle(X1, Y1, RADIUS, 'blue')
    my_graphics.circle(X1, Y1, RADIUS, 'red')
    my_graphics.circle(X1, Y1, RADIUS, 'green')

    my_graphics.line(X1, Y1, X2, Y2, 'black')
    my_graphics.line(X1, Y1, X3, Y3, 'black')
    my_graphics.line(X2, Y2, X3, Y3, 'black')

    turtle.done()

if __name__ == '__main__':
    main()