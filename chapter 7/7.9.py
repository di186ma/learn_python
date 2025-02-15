# работа со списками и файлами

def menu():
    print("Если хотите записать в файл весь список целиком, то введите - 1")
    print("Если хотите записать в файл список строк последовательно по элементам, то введите - 2")
    print("Если хотите записать строковое содержимое файла в список, то введите - 3")
    print("Если хотите записать в файл список чисел последовательно по элементам, то введите - 4")
    print("Если хотите записать числовое содержимое файла в список, то введите - 5")

    try:
        choice = int(input())
        if choice == 1:
            writelines()
        elif choice == 2:
            write_list()
        elif choice == 3:
            read_list()
        elif choice == 4:
            write_numbers_list()
        elif choice == 5:
            read_numbers_list()
    except:
        pass

def writelines():
    cities = ['New York', 'London', 'Paris']
    file_name = r'files/file_list.txt'
    outfile = open(file_name, 'w')
    outfile.writelines(cities) # записывает содержимое списка в файл, но без разделителей и перевода строки
    outfile.close()

def write_list():
    cities = ['New York', 'London', 'Paris']
    file_name = r'files/file_list.txt'
    outfile = open(file_name, 'w')

    for city in cities:
        outfile.write(city + '\n') # запись каждого элемента списка последовательно с переносом строки
    outfile.close()

def read_list():
    file_name = r'files/file_list.txt'
    infile = open(file_name, 'r')
    cities = infile.readlines() # присвоение всего файла в список,
    # каждой строка вместе с символом перевода строки присваивается по элементам
    infile.close()

    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1

    print(cities)

def write_numbers_list():
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    file_name = r'files/file_list.txt'
    outfile = open(file_name, 'w')
    for number in numbers_list:
        outfile.write(str(number) + '\n') # для записи чисел в файл их сначала надо перевести в строку
        # и добавить символ перевода строки
    outfile.close()

def read_numbers_list():
    file_name = r'files/file_list.txt'
    infile = open(file_name, 'r')

    numbers_list = infile.readlines()
    infile.close()

    index = 0
    while index < len(numbers_list):
        numbers_list[index] = int(numbers_list[index]) # для сохранения чисел из файла в список
        # необходимо сконвертировать элементы списка в тип int
        index += 1
    print(numbers_list)

if __name__ == '__main__':
    menu()