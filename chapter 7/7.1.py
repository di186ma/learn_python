import random # для извлечения случайного элемента из списка

even_numbers = [2, 4, 6, 8, 10] # пример списка
names = ['Molly', 'Stiven', 'Will', 'Alisia', 'Adriana'] # тоже список
info = ['Alisia', 27, 1550.87] # и это тоже список
print(even_numbers)

numbers = list(range(5)) # преобразование в список итерируемого объекта
print(numbers)

numbers2 = list(range(1, 10, 2))
print(numbers2)

numbers3 = [0] * 5 # оператор повторения (повторяет список 5 раз и объединяет их в список)
print(numbers3)

numbers4 = [1, 2, 3] * 3
print(numbers4)

numbers5 = [1, 2, 3, 4] # обход списка в цикле for
for number in numbers5:
    print(number)

numbers6 = [1, 2, 3, 4] # обход списка в цикле for
for number in numbers6:
    number = 99 # не влияет на значения элементов списка, т.к. это просто их копия
print(numbers6)

my_list = [10, 20, 30, 40]
print(my_list[0], my_list[1], my_list[2], my_list[3]) # печать элементов списка по индексам
print(type(my_list))
index = 0
while index < 4:
    print(my_list[index]) # также печатает элементы по индексу
    index += 1
# -1 это последний элемент, -2 предпоследний элемент и т.д.
print(my_list[-1], my_list[-2], my_list[-3], my_list[-4]) # печать элементов списка по отрицательным индексам

# print(my_list[5]) # вызовется исключения из-за недопустимого индекса
size = len(my_list) # возвращение длины списка
print(size)

index = 0
while index < len(my_list): # применение функции len в цикле
    print(my_list[index])
    index += 1

for index in range(len(names)): # применение размера списка для обхода по нему
    print(names[index])

numbers7 = [1, 2, 3, 4, 5]
print(numbers7)
numbers7[0] = 99
# numbers7[5] = 99 # недопустимый индекс, будет вызвано исключение
print(numbers7) # доказательство изменения списка

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
list3 = list1 + list2 # пример конкатенации
print(list3)

all_list = even_numbers + names + info # конкатенировать можно любые списка, даже с разными типами и размеров
print(all_list)

all_list += list3 # можно даже использовать формулы сокращения
print(all_list)

# all_list += 8 # будет вызвано исключение, т.к. списки можно конкатенировать только со списками
print(all_list)

winner = random.choice(all_list) # случайный выбор элемента
print(winner)

winners = random.choices(all_list, k=3) # случайный выбор трех элементов
print(winners)

winners = random.sample(all_list, k=3) # случайный выбор трех элементов без повторений, если они есть
print(winners)