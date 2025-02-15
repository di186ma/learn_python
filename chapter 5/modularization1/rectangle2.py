# выполняется как автономная программа, но также с помощью __name__ определяется режим работы:
# как модуль или отдельная программа
def area(width, length):
    return width * length

def perimeter(width, length):
    return 2 * (width + length)

def main():
    width = 10
    length = 12
    print(area(width, length))
    print(perimeter(width, length))

# если вызывается из другой программы, то __name__ равен названию модуля 'rectangle2',
# если это главная программа, то __name__ равен '__main__'
if __name__ == 'rectangle2':
    print("Я", __name__, "вызвался из другой программы")
if __name__ == '__main__':
    print("Я", __name__, "полноценная самостоятельная программа")
    main()