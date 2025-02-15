# передача нескольких параметров по именованным аргументам (позиции неважны)
def main():
    show_interest(rate = 0.01, periods = 10, principal = 10000.0)

def show_interest(principal, rate, periods):
    interest = principal*rate*periods
    print(f"The interest is: {interest:,.2f}")

main()