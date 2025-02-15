# включение в список

list1 = [1, 2, 3, 4, 5]
list2 = []

for item in list1:
    list2.append(item) # в таком случае изменение одного списка не влияет на второй


"""
[item for item in list1]
|____||________________|
   |          |____________
выражение результата      |
                выражение итерации
"""
list3 = [item for item in list1] # на каждой итерации элементу целевой переменной присваивается значение элемента
print(list1)
print(list2)
print(list3)

list4 = [item**2 for item in list1] # возводит в новый список квадраты чисел из старого списка
print(list4)

# хранение в новом списке длин строк в элементах из старого списка (сохранение длин строк)
cities = ['New York', 'London', 'Paris']
len_list = []
for city in cities:
    len_list.append(len(city))

# вариант получше
cities = ['New York', 'London', 'Paris']
len_list = [len(stroke) for stroke in cities]



list5 = [1, 12, 2, 20, 3, 15, 4]
list6 = []
for item in list5:
    if item < 10:
        list6.append(item) # добавляем в новый список только элементы < 10

# вариант получше
list5 = [1, 12, 2, 20, 3, 15, 4]
list6 = [item for item in list5 if item < 10]

# записываем только короткие слова
last_names = ['Jackson', 'Johnson', 'Smith']
short_names = [name for name in last_names if len(name) < 6]