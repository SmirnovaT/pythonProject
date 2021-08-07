class Todo:
    def __init__(self):
        self.items = []

    def input_todo(self, task, percent):
        self.task = task
        self.percent = percent
        sum = f"{task}: {percent}"
        return self.items.append(sum)

    def remove(self, delete):
        self.delete = delete
        for el in self.items:
            if delete in el:
                self.items.remove(el)
            else:
                print("Данной задачи в списке нет")

    def dis(self):
        return self.items


obj = Todo()

while True:
    user = input("Введите команду: ").lower()
    if user == "показать":
        print("Список: ", obj.dis())
    elif user == "добавить":
        task = input("Добавьте задачу в список: ").lower()
        while True:
            try:
                percent = int(input("Введите процент выполнения задачи: "))
                break
            except ValueError:
                print("Пожалуйста, введите процент выполнения в цифрах")
        obj.input_todo(task, percent)
        print("Список: ", obj.dis())
    elif user == "удалить":
        delete = input("Что удалить из списка: ").lower()
        obj.remove(delete)
        print("Список: ", obj.dis())
    elif user == "стоп":
        break
    else:
        print("Заданной команды нет, повторите ввод")


