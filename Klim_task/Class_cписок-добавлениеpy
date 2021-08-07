# Только добавление задачи
class Todo:
    def __init__(self):
        self.list = []


    def input_todo(self, task, percent):
        self.list.append({'Задача': task, 'Процент выполнения': percent})


    def dis(self):
        return self.list


obj = Todo()
while True:
    task = input("Добавьте задачу в список: ")
    while True:
        try:
            percent = int(input("Введите процент выполнения задачи: "))
            break
        except ValueError:
            print("Пожалуйста, введите процент выполнения в цифрах")
    obj.input_todo(task, percent)
    print("Список: ", obj.dis())




