# запись и чтение записей в файле
# есть закомментированная строка в конце

def write_file():
    num_emps = int(input("Enter number of employees: "))

    employees = r'files/employees.txt'

    emp_file = open(employees, 'w')

    for count in range(1, num_emps + 1):
        print('Enter data of employee', count)
        name = input('Enter employee name: ')
        id_num = input('Enter employee id: ')
        dept = input('Enter employee department: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

    emp_file.close()
    print('File created')

def read_file():
    employees = r'files/employees.txt'
    emp_file = open(employees, 'r')

    name = emp_file.readline()

    while name != '':
        id_num = emp_file.readline()
        dept = emp_file.readline()

        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        print(name)
        print(id_num)
        print(dept)

        name = emp_file.readline()

    emp_file.close()

if __name__ == '__main__':
    # write_file()
    read_file()