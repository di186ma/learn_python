# проверка на простые числа
def is_prime(number):
    flag = True
    if number >= 0 and number < 2:
        pass
    elif number < 0:
        flag = False

    for i in range(2, number):
        if number % i == 0:
            flag = False

    return flag

def main():
    for i in range(1, 101):
        if is_prime(i):
            print(i, "is a prime number")
        else:
            print(i, "is not a prime number")

if __name__ == '__main__':
    main()
