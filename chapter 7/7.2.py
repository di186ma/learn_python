# пример присвоения элементам списка вводимых пользователем значений
NUM_DAYS = 5

def main():
    sales = [0] * NUM_DAYS

    print("Sales of day")

    for index in range(len(sales)):
        sales[index] = float(input(f"Enter the sales of day {index + 1}: "))

    print("Sales per day")
    for value in sales:
        print(f"{value:.2f}")

if __name__ == "__main__":
    main()