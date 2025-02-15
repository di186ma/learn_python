# Функции с возвратом значения

def main():
    first_age = int(input("Enter first age: "))
    second_age = int(input("Enter second age: "))

    total1 = sum1(first_age, second_age)
    total2 = sum2(first_age, second_age)
    print(total1, total2)

    print(get_dollar()) # пример с возвратом f-строки

    number = 53

    if is_even(number): # пример с возвратом битового значения
        print("Even")
    else:
        print("Odd")

    first_name, last_name = get_name()
    print(first_name, last_name)# пример с возвратом нескольких значений

    number1 = 10
    number2 = 0
    quotient = divide(number1, number2) # пример с возвратом None (значение, которое указывает на отсутствие значения)

    if quotient is None: # Для сравнения с None лучше использовать оператор is или is not, вместо == или !=
        print("No quotient")
    else:
        print(quotient)

def sum1(sum1, sum2): # базовый шаблон для функций с возвращающим значением
    result = sum1 + sum2
    return result

def sum2(sum1, sum2): # пример с возвратом выражения
    return sum1 + sum2

def get_dollar(): # пример с возвратом f-строки
    dollar = 56
    return  f'${dollar:,.2f}'

def is_even(num): # пример с возвратом битового значения
    if num % 2 == 0:
        status = True
    else:
        status = False
    return status

def get_name(): # пример с возвратом нескольких значений
    first = 'Dima'
    last = 'Tsuguy'
    return first, last

def divide(num1, num2): # пример с возвратом None (значение, которое указывает на отсутствие значения)
    if num2 == 0:
        return None
    else:
        return num1 / num2

main()
