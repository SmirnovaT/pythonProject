class Todo:
    def __init__(self):
        self.list = {}

    def input_todo(self, task, percent):
        self.task = task
        self.percent = percent
        dic_todo = {task: percent}
        return self.list.update(dic_todo)

    def remove(self, b):
        self.list.remove(b)

    def dis(self):
        return self.list

obj = Todo()
while True:
    task = input("Добавьте задачу в список: ")
    percent = int(input("Процент выполнения на текущий момент: "))
    obj.input_todo(task, percent)
    print("Список: ", obj.dis())
