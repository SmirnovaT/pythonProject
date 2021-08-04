class Todo:
    def __init__(self):
        self.list = []

    def input_todo(self, task, percent):
        self.task = task
        self.percent = percent
        sum = f"{task}: {percent}"
        return self.list.append(sum)

    def remove(self, b):
        self.list.remove(b)


    def dis(self):
        return self.list


obj = Todo()

while True:
    user = input("Введите команду: ").lower()
    if user == "показать":
        print("Список: ", obj.dis())
    elif user == "добавить":
        task = input("Добавьте задачу в список: ")
        percent = int(input("Процент выполнения задачи: "))
        obj.input_todo(task, percent)
        print("Список: ", obj.dis())
    elif user == "удалить":
        list = input("Что удалить из списка: ")
        obj.remove(list)
        print("Список: ", obj.dis())
    elif user == "стоп":
        break
    else:
        print("Заданной команды нет, повторите ввод")