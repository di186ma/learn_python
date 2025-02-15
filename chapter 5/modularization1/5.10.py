import circle # модуль должен быть в той же папке
import rectangle # модуль должен быть в той же папке
import rectangle2 # модуль должен быть в той же папке
# import math эта библиотека не будет использоваться в модуле circle, там нужен собственный import

def main():
    radius = 5
    print("Circle area:", circle.area(radius))
    print("circle circumference:", circle.circumference(radius))

    width = 5
    length = 4
    print("Rectangle area:", rectangle.area(width, length))
    print("Rectangle perimeter:", rectangle.perimeter(width, length))

    print("Rectangle area:", rectangle2.area(width, length))
    print("Rectangle perimeter:", rectangle2.perimeter(width, length))


main()