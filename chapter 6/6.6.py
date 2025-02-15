"""
чтение строковых значений из файла и преобразование их в численные
"""

# чтение из файла
def main():
    file_dir = r'files/numbers.txt' # сохраняем в переменную путь к файлу
    input_file = open(file_dir, 'r') # открываем файл для чтения

    input_file = open(file_dir, 'r')  # открываем файл для чтения

    num1 = int(input_file.readline())
    num2 = int(input_file.readline())
    num3 = int(input_file.readline())

    input_file.close()  # обязательно закрываем файл

    total = num1 + num2 + num3
    print(total)

if __name__ == '__main__':
    main()