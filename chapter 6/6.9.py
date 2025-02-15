"""
Применение цикла for для чтения строк
"""

def main():
    sales_name = r'files/sales.txt'
    sales_file = open(sales_name, 'r')

    for line in sales_file:
        amount = float(line)
        print(amount)

    sales_file.close()
    print('Done')

if __name__ == '__main__':
    main()