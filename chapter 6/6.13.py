# добавление, вывод, поиск, редактирование

import os # нужен для функции remove и rename

from numpy.random import choice


def menu():
    print('Если вы хотите записать данные в файл, то нажмите - 1')
    print('Если вы хотите прочитать данные из файла, то нажмите - 2')
    print('Если вы хотите найти запись из файла, то нажмите - 3')
    print('Если вы хотите отредактировать запись из файла, то нажмите - 4')
    print('Если вы хотите удалить запись из файла, то нажмите - 5')
    print('Если вы хотите выйти из меню, то введите любой символ\n')


    try:
        choice = int(input())

        if choice == 1:
            write_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            search_file()
        elif choice == 4:
            edit_file()
        elif choice == 5:
            delete_file()
    except:
        pass


def write_file():
    another = 'y'
    coffee = r'files/coffee.txt'

    coffee_file = open(coffee, 'a')

    while another == 'y':
        print('Enter data of coffee')
        descr = input('Enter description of coffee: ')
        qty = float(input('Enter quantity of coffee: '))

        coffee_file.write(descr + '\n')
        coffee_file.write(f'{qty}\n')

        another = input("Maybe add a coffee? (y - yes): ")

    coffee_file.close()
    print('File written successfully.')

def read_file():
    coffee = r'files/coffee.txt'
    coffee_file = open(coffee, 'r')

    descr = coffee_file.readline()

    while descr != '':
        qty = float(coffee_file.readline())

        descr = descr.rstrip('\n')

        print(descr)
        print(qty)

        descr = coffee_file.readline()

    coffee_file.close()

def search_file():
    found = False
    coffee = r'files/coffee.txt'

    search = input('Enter the search description of coffee: ')

    coffee_file = open(coffee, 'r')

    descr = coffee_file.readline()

    while descr != '':
        qty = float(coffee_file.readline())

        descr = descr.rstrip('\n')

        if descr == search:
            print(descr)
            print(qty)
            found = True

        descr = coffee_file.readline()

    coffee_file.close()

    if not found:
        print('Description not found.')

def edit_file():
    found = False

    search = input('Enter the search description of coffee: ')
    new_qty = float(input('Enter new quantity of coffee: '))

    coffee = r'files/coffee.txt'
    coffee_file = open(coffee, 'r')

    temp_name_file = r'files/temp.txt'
    temp_file = open(temp_name_file, 'w') # создаем для записи временный файл

    descr = coffee_file.readline()

    while descr != '':
        qty = float(coffee_file.readline())
        descr = descr.rstrip('\n')

        if descr == search:
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n') # если нашли искомое описание кофе, то пишем новый вес во временный файл

            found = True
        else:
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')

        descr = coffee_file.readline()

    coffee_file.close()
    temp_file.close()

    os.remove(coffee) # удаляем исходный файл
    os.rename(temp_name_file, coffee) # переименовываем старый файл как исходный

    if found:
        print('File updated successfully.')
    else:
        print('File not updated.')

def delete_file(): # похоже на редактирование файла
    found = False

    search = input('Enter the search description of coffee for deletion: ')

    coffee = r'files/coffee.txt'
    coffee_file = open(coffee, 'r')

    temp_name_file = r'files/temp.txt'
    temp_file = open(temp_name_file, 'w') # создаем для записи временный файл

    descr = coffee_file.readline()

    while descr != '':
        qty = float(coffee_file.readline())
        descr = descr.rstrip('\n')

        if descr != search:
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n') # если нашли искомое описание кофе, то пишем новый вес во временный файл
        else:
            found = True

        descr = coffee_file.readline()

    coffee_file.close()
    temp_file.close()

    os.remove(coffee) # удаляем исходный файл
    os.rename(temp_name_file, coffee) # переименовываем старый файл как исходный

    if found:
        print('File updated successfully.')
    else:
        print('File not updated.')

if __name__ == '__main__':
    menu()