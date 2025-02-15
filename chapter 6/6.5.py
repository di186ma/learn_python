"""
преобразование числовых значений в строковые перед записью в файл
"""

# запись в файл
def main():
    file_dir = r'files/numbers.txt' # сохраняем в переменную путь к файлу
    output_file = open(file_dir, 'w') # открываем файл для записи

    num1 = input('enter a number: ')
    num2 = input('enter another number: ')
    num3 = input('enter another number: ')

    output_file.write(str(num1) + '\n')
    output_file.write(str(num2) + '\n')
    output_file.write(str(num3) + '\n')

    output_file.close() # обязательно закрываем файл
    print('done')

if __name__ == '__main__':
    main()