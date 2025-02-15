# Вложенные циклы

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)


rows = int(input('Enter number of rows: ')) # строки
cols = int(input('Enter number of columns: '))  # колонки

for row in range(rows):
    for col in range(cols):
        print('*', end='')
    print()

for row in range(rows):
    for x in range(row+1):
        print('*', end='')
    print()

for row in range(rows):
    for x in range(row):
        print(' ', end='')
    print('#')