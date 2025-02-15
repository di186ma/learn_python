# методы обработки списков и полезные встроенные функции

def menu():
    print("Если хочешь разобраться со вставкой в конец списка - 1")
    print("Если хочешь разобраться с поиском индекса по значению в списке - 2")
    print("Если хочешь разобраться со вставкой значения по индексу в список - 3")
    print("Если хочешь разобраться с сортировкой по возрастанию в списке - 4")
    print("Если хочешь разобраться с удалением элемента по значению в списке - 5")
    print("Если хочешь разобраться с инвертированием списка - 6")
    print("Если хочешь разобраться с удалением элемента по индексу в списке - 7")
    print("Если хочешь разобраться с поиском минимального и максимального значения в списке - 8")
    print("Если хочешь хочешь выйти из меню - иное")

    try:
        choice = int(input())
        if choice == 1:
            append_list()
        elif choice == 2:
            index_list()
        elif choice == 3:
            insert_list()
        elif choice == 4:
            sort_list()
        elif choice == 5:
            remove_list()
        elif choice == 6:
            reverse_list()
        elif choice == 7:
            del_list()
        elif choice == 8:
            min_and_max_list()
    except:
        pass

def append_list():
    name_list = [] # создание пустого списка

    again = 'y'

    while again == 'y':
        name = input('Enter a name: ')
        name_list.append(name) # добавляет в конец списка новое имя
        print('Would you like to add another name?')
        again = input('y - yes, another - no: ')
        print()
    for name in name_list:
        print(name)

def index_list():
    food = ['pizza', 'burger', 'chips']

    print(food)

    item = input('Enter an item, that you search: ')

    try:
        item_index = food.index(item) # возвращает индекс с искомым значением первый попавшегося элемента
        new_item = input('Enter new name of the item: ')
        food[item_index] = new_item # присваивает новое значение искомому элементу
        print(food)
    except:
        print('Item not found')

def insert_list():
    names = ['James', 'John', 'Joey', 'Smith']
    print(names)

    names.insert(1, 'Kyle') # добавляет (не заменяет) в данный индекс новое значение
    print(names)

def sort_list():
    names = ['James', 'John', 'Joey', 'Smith']
    numbers = [7, 5, 0, 3, 6, 3, 6]

    print(numbers)
    print(names)

    numbers.sort() # перестраивает элементы от самого малого до самого большого
    names.sort() # перестраивает элементы от самого малого до самого большого

    print(numbers)
    print(names)

def remove_list():
    food = ['pizza', 'burger', 'chips']
    print(food)
    item = input('Enter an item, that you search: ')
    try:
        food.remove(item) # удаляет первый элемент с данным значением из списка (не путать с del)
        print(food)
    except:
        print('Item not found')

def reverse_list():
    food = ['pizza', 'burger', 'chips']
    print(food)
    food.reverse() # просто инвертирует элементы (делает обратный порядок)
    print(food)

def del_list():
    food = ['pizza', 'burger', 'chips']
    print(food)
    del food[0] # удаляет элемент по индексу (не путать с remove), запомнить что это обычная инструкция
    print(food)

def min_and_max_list():
    food = [5, 4, 3, 2, 50, 40, 30]
    print('min:', min(food))
    print('max:', max(food))


if __name__ == '__main__':
    menu()
