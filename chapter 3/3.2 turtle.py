import turtle
import math

turtle.showturtle()

if turtle.xcor() >= 0 or turtle.ycor() >= 0:
    turtle.goto(320,0)

if turtle.heading() <= 0 or turtle.heading() > 60:
    turtle.setheading(180)

if not(turtle.isdown()):
    turtle.pendown()

if turtle.isvisible():
    turtle.hideturtle()

if turtle.pencolor() == "black":
    turtle.pencolor('red')

if turtle.fillcolor() == "black":
    turtle.fillcolor('red')

if turtle.bgcolor() == 'black':
    turtle.bgcolor('blue')

if turtle.pensize() < 5:
    turtle.pensize(5)

if turtle.speed() > 0:
    turtle.speed(1)

turtle.clearscreen()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
TARGET_LEFT_X = 100
TARGET_LEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LEFT_X, TARGET_LEFT_Y)
ANGLE_TARGET = turtle.heading()
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

angle = turtle.numinput("Требуются пользовательские данные", "Введите угол выстрела снаряда от 0 до 90", minval=0, maxval=90)
force = turtle.numinput("Требуются пользовательские данные", "Введите пусковую силу от 0 до 10", minval=0, maxval=10)

distance = force * FORCE_FACTOR

turtle.setheading(angle)

turtle.pendown()
turtle.forward(distance)
TARGET_DISTANCE = math.sqrt(((TARGET_LEFT_X - turtle.xcor()) ** 2 ) + ((TARGET_LEFT_Y - turtle.ycor()) ** 2))

if (turtle.xcor() >= TARGET_LEFT_X and
    turtle.xcor() <= (TARGET_LEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LEFT_Y and
    turtle.ycor() <= (TARGET_LEFT_Y + TARGET_WIDTH)):
    turtle.write("Цель поражена!")
else:
    if turtle.heading() > ANGLE_TARGET:
        turtle.write("Попробуйте угол поменьше\n", font= ("Arial", 16, "bold"))
    elif turtle.heading() > ANGLE_TARGET:
        turtle.write("Попробуйте угол побольше\n", font= ("Arial", 16, "bold"))
    if (turtle.xcor() > TARGET_LEFT_X and turtle.ycor() > TARGET_LEFT_Y) and TARGET_DISTANCE > 0:
        turtle.write("Попробуйте уменьшить пусковую силу", font= ("Arial", 16, "bold"))
    elif (turtle.xcor() < TARGET_LEFT_X and turtle.ycor() < TARGET_LEFT_Y) and TARGET_DISTANCE > 0:
        turtle.write("Попробуйте увеличить пусковую силу", font= ("Arial", 16, "bold"))



turtle.done()