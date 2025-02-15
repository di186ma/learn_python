# чтение данных из файла в цикле

def main():
    sales_name = r'files/sales.txt'
    sales_file = open(sales_name, 'r')

    line = sales_file.readline()
    while line != '':
        amount = float(line)
        print(amount)
        line = sales_file.readline()

    sales_file.close()
    print('Done')

if __name__ == '__main__':
    main()