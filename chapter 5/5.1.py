"""
pass - позволяет написать пустой блок, чтобы потом к нему вернуться
if 6 < 7:
    pass

while 6 < 7:
    pass
"""

# Пример работы функции
def hey():
    print("Hey")
    input("Press enter to continue...")
    message()
    print("Bye")

def message():
    print("Hello World")

def important():
    pass  # позволяет написать пустую функцию, чтобы потом к ней вернуться

hey()


# Локальные переменные и их видимость
# Если переменная инициализирована внутри функции, то она локальна и может использоваться только внутри функции
# Если переменная инициализирована за пределами всех функций, то она называется глобальной
# и может использоваться в любой функции
# поизучайте переменную birds
def main():
    texas()
    california()
    paris()

def texas():
    birds = 5000
    print("Birds in Texas: ",  birds)
    paris()

def california():
    birds = 8000
    print("Birds in California: ", birds)

def paris():
    print("Birds in Paris: ", birds)

birds = 3000
main()