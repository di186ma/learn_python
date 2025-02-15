import turtle

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



turtle.done()