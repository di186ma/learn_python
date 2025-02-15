import turtle

factorail = int(input("Enter the factorial no.: "))
sum = 1
if factorail != 1:
    for i in range(1, factorail + 1):
        sum *= i
print(sum)

turtle.showturtle()

n = 5
while True:
    turtle.forward(n)
    turtle.left(90)
    n += 5

turtle.done()