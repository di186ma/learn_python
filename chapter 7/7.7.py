# передача списка в функцию и возвращение из функции

def main():
    numbers = [2, 4, 6, 8, 10]
    sum, new_numbers = get_totals(numbers)
    print(sum, new_numbers)

def get_totals(numbers):
    total = 0
    for num in numbers:
        total += num
    return total, numbers

if __name__ == '__main__':
    main()