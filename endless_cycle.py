# создать функцию запуска с бесконечным циклом
# список доступных команд: показать, добавить, удалить, стоп
# Добавить open на чтение при старте
# Сделать функцию записи и добавить ее в добавление и удаление
# Переделать под словарь
# Сделать на классах
# Гитхаб и свои проеты заливать, гит баш.

file = open("todo.txt", 'r')

todo = ["apple", "bread"]

if file is not None:
    todo = file.read().split("|")
    file.close()

def file_write():
    f = open('todo.txt', 'w')
    todo_string = "|".join(todo) # "apple|bread|new_item"
    f.write(todo_string)
    f.close()

def show_todo():
    print(todo)


def add_todo():
    input_todo = input("Дополните список: ") # new_item
    todo.append(input_todo) # ["apple", "bread", "new_item"]
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
        user = input('Введите команду: ').lower()
        if user == "показать":
            show_todo()
        elif user == "добавить":
            add_todo()
            file_write()
        elif user == "удалить":
            remove_todo()
            file_write()
        elif user == "стоп":
            break
        else:
            print("Заданной команды нет")

main()
