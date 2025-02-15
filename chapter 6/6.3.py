# чтение из файла
def main():
    file_dir = r'files/test.txt' # сохраняем в переменную путь к файлу
    input_file = open(file_dir, 'r') # открываем файл для чтения

    file_contents = input_file.read()  # записываем все содержимое файла в переменную

    input_file.close() # обязательно закрываем файл
    print(file_contents)

    input_file = open(file_dir, 'r')  # открываем файл для чтения

    # записываем первую строку файла в переменную вместе с символом '\n' если он есть
    first_stroke = input_file.readline()
    # записываем вторую строку файла в переменную вместе с символом '\n' если он есть
    second_stroke = input_file.readline()

    first_stroke = first_stroke.rstrip('\n') # удаление символа перевода строки в конце строки
    second_stroke = second_stroke.rstrip('\n') # удаление символа перевода строки в конце строки

    input_file.close()  # обязательно закрываем файл
    print("first line:", first_stroke)
    print("second line:", second_stroke)

if __name__ == '__main__':
    main()