# конкатенация символа новой строки со строковыми значениями
def main():
    print("Enter three name of your friends")
    name1 = input("Enter your first name: ")
    name2 = input("Enter your second name: ")
    name3 = input("Enter your third name: ")

    my_file = open('files/friends.txt', "w")

    my_file.write(name1 + "\n")
    my_file.write(name2 + "\n")
    my_file.write(f'{name3}\n') # можно и так

    my_file.close()
    print("Your friends have been written successfully")

if __name__ == "__main__":
    main()