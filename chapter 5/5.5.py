# передача нескольких параметров по позиции и именованным аргументам
# здесь в начале должны указываться позиционные аргументы, а потом именованные аргументы
def main():
    show_interest(10000.0, periods = 10, rate = 0.01)

def show_interest(principal, rate, periods):
    interest = principal*rate*periods
    print(f"The interest is: {interest:,.2f}")

main()