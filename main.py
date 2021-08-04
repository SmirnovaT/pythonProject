# Сделать список задач из элементов справочников
# Например {"name": "Выучить питон", "percent": 40}

# 1. Список из словарей
task_list = [
    {"name": "Выучить питон", "percent": 30},
    {"sport": "Стоять в планке", "minutes": 4}
]
# Первый вариант вывода
print(task_list[0]["name"] , task_list[0]["percent"])
print(task_list[1]['sport'], task_list[1]['minutes'])

#Второй вариант вывода
for task in task_list:
    print(task.items())

#2. Словарь
task_list = {"name": "Выучить питон", "percent": 30}

# Первый вариант вывода
for task in task_list:
    print(f'{task_list[task]}')

#Второй Вариант вывода
for name, percent in task_list.items():
    print(f'{name}: {percent}')

