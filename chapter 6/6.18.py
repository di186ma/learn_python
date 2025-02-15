# сохранение исключения, else и finally

def main():
    try:
        hours = int(input("Enter hours: "))
        pay_rate = float(input("Enter pay rate: "))
        gross_pay = hours * pay_rate
        print(f"Gross pay is {gross_pay}")
    except ValueError as e: # сохранение исключения ValueError в переменную e
        print(f"Error: {e}")
    except Exception as err: # определение исключения как объект типа Exception
        print(f"Error: {err}")
    else: # исполняется если исключений не было
        print("Thank you for your pay!")
    finally: # исполняется в любом случае, было исключение или нет
        print("Thank you for your pay!")

if __name__ == "__main__":
    main()