# двумерные списки
import random

students = [['Joe', 'Kim'], ['Sam', 'Seu'], ['Kelly', 'Kris']] # вложенный список, 3 строки, 2 столбца
print(students)
print(students[0])
print(students[1])
print(students[2])
print(students[2][1]) # пример доступа к вложенному списку

values = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for row in values: # идем по очереди о вложенным спискам
    for item in row:
        print(item)


# присваивание элементам вложенных списков случайные числа
ROWS = 3
COLS = 4
values = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for r in range(ROWS):
    for c in range(COLS):
        values[r][c] = random.randint(1, 100)

print(values)

# чтение двумерного списка, но без констант
index = 0
for r in values:
    for c in values[index]:
        print(c)
    index += 1
