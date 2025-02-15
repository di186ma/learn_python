import turtle

turtle.showturtle()

turtle.speed(1)

for x in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.clearscreen()

for x in range(8):
    turtle.forward(100)
    turtle.left(45)

turtle.clearscreen()

NUM_CIRCLES = 20
STARTING_RADIUS = 20
OFFSET = 10
ANGLE = 18

radius = STARTING_RADIUS

turtle.speed(10)

for count in range(NUM_CIRCLES):
    turtle.circle(radius)

    x = turtle.xcor()
    y = turtle.ycor() - OFFSET

    radius += OFFSET

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.clearscreen()
radius = STARTING_RADIUS

for x in range(NUM_CIRCLES):
    turtle.circle(radius)
    turtle.left(ANGLE)

turtle.done()