class Todo:
    def __init__(self, task, percent):
        self.percent = percent
        self.task = task
        self.items = []

    def input_todo(self, task, percent):
        self.items.append({"Задача": task, "Процент выполнения": percent})


    def dis(self):
        return self.items


obj = Todo("Задача", "Проценты")
while True:
    task = input("Добавьте задачу в список: ")
    percent = int(input("Процент выполнения задачи: "))
    obj.input_todo(task, percent)
    print("Список: ", obj.dis())