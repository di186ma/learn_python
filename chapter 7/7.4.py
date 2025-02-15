# поиск значения в списке выполняется при помощи оператора in
from re import search


def main():
    prod_nums = ['V475', 'F987', 'Q143', 'R688']

    search = input('Enter a product name to search for: ')

    if search in prod_nums: # если поисковое значение содержится в списке, то вернется True, иначе False,
        # можно использовать и not in
        print('The product name you entered is valid.')
    else:
        print('The product name you entered is not valid.')

if __name__ == '__main__':
    main()