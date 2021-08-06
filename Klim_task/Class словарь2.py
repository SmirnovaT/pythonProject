class Todo:
    def __init__(self):
        self.list = {}

    def input_todo(self, task, percent):
        self.task = task
        self.percent = percent
        dic_todo = {task: percent}
        return self.list.update(dic_todo)

    def remove(self, delete):
        self.list.pop(delete)

    def dis(self):
        return self.list

obj = Todo()

while True:
    user = input('Введите команду: ').lower()
    if user == "показать":
        print("Список: ", obj.dis())
    elif user == "добавить":
        task = input("Добавьте задачу в список: ").lower()

        while True:
            try:
                percent = int(input("Процент выполнения на текущий момент: "))
                break
            except ValueError:
                print("Пожалуйста, введите процент выполнения задачи в цифрах")
        obj.input_todo(task, percent)
        print("Список: ", obj.dis())

    elif user == "удалить":
        while True:
            try:
                delete = input("Какую задачу удалить? ").lower()
                obj.remove(delete)
            except KeyError:
                print("Данной задачи в списке нет")
            print("Список: ", obj.dis())
    elif user == "стоп":
        break
    else:
        print("Заданной команды нет")




