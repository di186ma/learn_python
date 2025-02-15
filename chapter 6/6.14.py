# try/except
# как только выполнение переходит в except, в try он не возвращается

def main():
    try:
        hours = int(input("Enter hours: "))
        pay_rate = float(input("Enter pay rate: "))
        gross_pay = hours * pay_rate
        print(f'Your gross pay: {gross_pay}')
    except ValueError:
        print('Please enter a valid number.')

if __name__ == '__main__':
    main()