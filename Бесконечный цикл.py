todo = ["apple", 14, "bread"]


def show_todo():
    print(todo)


def add_todo():
    input_todo = input("Дополните список: ")
    todo.append(input_todo)
    print(todo)


def remove_todo():
    input_remove = input("Что нужно удалить из списка? ")
    if input_remove in todo:
        todo.remove(input_remove)
        print(todo)
    else:
        print("Объект не найден")


def main():
    while True:
        user = input("Введите команду: ").lower()
        if user == "показать":
            show_todo()
        elif user == "добавить":
            add_todo()
        elif user == "удалить":
            remove_todo()
        elif user == "стоп":
            break
        else:
            print("Заданной команды нет, повторите ввод")


main()