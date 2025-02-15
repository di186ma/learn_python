# проверка на четность
import random

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    odd = 0
    even = 0
    for i in range(100):
        number = random.randint(1, 100)
        if is_even(number):
            even += 1
        else:
            odd += 1
        print(number)
    print("odd: ", odd)
    print("even: ", even)

if __name__ == '__main__':
    main()