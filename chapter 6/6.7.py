# использование цикла при чтении файлов
def main():
    num_days = int(input("Enter the number of days: "))

    sales_file = open("files/sales.txt", "w")

    for count in range(1, num_days+1):
        sales = float(input("Enter the sales of a day: "))
        sales_file.write(str(sales) + "\n")

    sales_file.close()
    print("Sales file is written successfully!")

if __name__ == "__main__":
    main()