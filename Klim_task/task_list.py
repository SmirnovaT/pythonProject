# Сделать список задач из элементов справочников
# Например {"name": "Выучить питон", "percent": 40}

#1. Словарь
task_list = {"name": "Выучить питон", "percent": 30}

# Первый вариант вывода
def show_list():
    print(f"{task_list['name'], task_list['percent']}")

show_list()

# Второй вариант вывода
for task in task_list:
    print(f'{task_list[task]}')

# Третий вариант вывода
for name, percent in task_list.items():
    print(f'{name}: {percent}')

# 2. Список словарей
task_list = [
    {"name": "Выучить питон", "percent": 30},
    {"sport": "Стоять в планке", "minutes": 4}
]
# Первый вариант вывода
print(task_list[0]["name"], task_list[0]["percent"])
print(task_list[1]['sport'], task_list[1]['minutes'])

# Второй вариант вывода
for task in task_list:
    print(task.items())



# Сделать функцию добавления в список
todo = []
def append_todo():
    user = input("Добавьте новую задачу в список: ")
    todo.append(user)

append_todo()
print(todo)



# сделать удаление элемента из списка
todo = [14, 'apple', 'juice', 54]
def delete_todo():
    todo.remove(14)

delete_todo()
print(todo)




# создать функцию запуска с бесконечным циклом
# список доступных команд: показать, добавить, удалить, стоп
todo = ["python", "train", "run"]

def cycle():
    while True:
        user = input("Добавьте задачу: ").lower()
        if user == "показать":
            print(todo)
        if user == "добавить":
            todo.append("cherry")
            print(todo)
        if user == "удалить":
            todo.remove("train")
            print(todo)
        if user == "стоп":
            break

cycle()