# передача нескольких параметров по позиции

def main():
    show_sum(12, 45)
    my_name = 'dima'
    my_lastname = 'tsuguy'
    reverse_name(my_name, my_lastname)

def reverse_name(name, lastname):
    print(lastname, name)


def show_sum(num1, num2):
    result = num1 + num2
    print(result)

main()


