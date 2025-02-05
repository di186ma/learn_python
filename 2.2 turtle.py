import turtle # загрузка модуля turtle в память

# import math
# x = math.sqrt(25)
# импортирование библиотеки math

'''
import math as mt
x = mt.sqrt(25)
импортирование библиотеки math с псевдонимом mt

from math import *
x = sqrt(25)
импортирование библиотеки math с подстановочным символом (может привести к конфликту имен)

from math import sin, cos, pi
импортирование определенных функций из библиотеки

from math import sqrt as square
импортирование определенной функции из библиотеки с псевдонимом

from math import sqrt as square, tan as tangens
импортирование определенных функций из библиотеки  с псевдонимом
'''


turtle.showturtle() # отображение черепашки в окне
turtle.pensize(3) # размер пера
turtle.pencolor("red") # цвет пера
turtle.bgcolor("black") # цвет фона
turtle.setup(800, 600) # размер окна
turtle.goto(100,100) # переход к координатам (начало координат в центре)
turtle.hideturtle() # скрываем черепаху
turtle.showturtle() # показываем черепаху

turtle.speed(10) # скорость черепахи (0 - мгновенно, 1 - 10 от медленно до быстро)
turtle.forward(100) # идем вперед
turtle.left(40) # поворот налево в определленом угле
turtle.dot() # рисуем точку
turtle.penup() # поднимаем перо (перестаем рисовать)
turtle.forward(100)
turtle.right(60) # поворот направо в определленом угле
turtle.pendown() # опускаем перо (продолжаем рисовать)
turtle.dot()
turtle.forward(100)
turtle.setheading(180) # задаем угол

print(turtle.heading()) # пишем текущий угол
print(turtle.pos()) # пишем текущую позицию
print(turtle.xcor()) # печать координаты X
print(turtle.ycor()) # печать координаты Y
print(turtle.speed()) # печать скорости

turtle.circle(100) # рисуем круг радиусом 100 пикселей

# turtle.reset()
# все стриается, задается черный цвет пера, черепаха возвращается в центр координат, цвет фона не изменяется

# turtle.clear()
# просто все стриается

turtle.clearscreen()
# все стирается, задается черный цвет пера, черепаха возвращается в центр координат, цвет фона задается белый


turtle.write("Hello, World!") # пишем в окне черепашки
turtle.clearscreen()
# все стирается, задается черный цвет пера, черепаха возвращается в центр координат, цвет фона задается белый

turtle.fillcolor("red")
turtle.begin_fill() # начало заливки
turtle.circle(100)
turtle.end_fill() # конец заливки

# все стирается, задается черный цвет пера, черепаха возвращается в центр координат, цвет фона задается белый

turtle.fillcolor("red")
turtle.begin_fill() # начало заливки
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill() # конец заливки
# если фигура не замкнута, то заливается только какаято часть
turtle.clearscreen()

radius = turtle.numinput("Требуются данные", "Введите радиус", default=70, minval=50, maxval=100)
# возвращает число с плавающей точкой, пишет заголовок и запрос
# default указывает на значение по умолчанию, minvalue и maxvalue на минимальное и максимальное значения
turtle.circle(radius)
turtle.clearscreen()

name = turtle.textinput("Требуется текст", "Введите текст")
# возвращает строковый литерал
turtle.write(name)


turtle.done() # Оставить окно открытым