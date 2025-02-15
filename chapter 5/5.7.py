import random # библиотека для генерирования случайных значений

def main():
    for count in range(5):
        # генерирование случайного целого числа в диапазоне от 0 до 100 (оба значения включены в диапазон)
        number = random.randint(1, 100)
        print('через переменную:', number)

    for count in range(5):
        # генерирование случайного целого числа в диапазоне от 0 до 100 (оба значения включены в диапазон)
        print('напрямую через print:', random.randint(1, 100))

    for count in range(5):
        # генерирование случайного целого числа в диапазоне от 0 до 100 (оба значения включены в диапазон)
        print(f"через f-строки: {random.randint(1, 100): ^10d}")

    for count in range(5):
        # пример использования случайного числа в математическом выражении
        number = random.randint(1, 100) * 11
        print('через переменную:', number)

    # пример случайного числа с инструкцией if
    if random.randint(1, 2) == 1:
        print("Случайно выпала 1")
    else:
        print("Случайно выпала 2")

    print('случайное число из диапазона 0-99 с помощью функции randrange:', random.randrange(100))
    print('случайное число из диапазона 5-9 с помощью функции randrange:', random.randrange(5, 10))
    print('случайное число из диапазона 5-99 с помощью функции randrange и шагом 2:',
          random.randrange(5, 100, 2))

    print('случайное число с плавающей точкой из диапазона 0-1 с помощью функции random:', random.random())
    print('случайное число с плавающей точкой из диапазона 1-10 с помощью функции uniform:',
          random.uniform(1.0, 10.0))

    print("Псевдослучайные числа с помощью задания начального значения для вычисления случайных значений")
    random.seed(10)
    print(random.randrange(100))
    print(random.randrange(100))
    print(random.randrange(100))
    print(random.randrange(100))


main()