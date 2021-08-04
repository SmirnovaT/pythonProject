class Todo:
    def __init__(self):
        self.list = []

    def input_todo(self, task):
        return self.list.append({"задача": task})

    def remove(self, b):
        self.list.remove(b)

    def dis(self):
        return self.list

obj = Todo()
task = input("Добавьте задачу в список: ")
obj.input_todo(task)
print("Список: ", obj.dis())



     #def add_list(self):
#        return self.list.append({"task": task})
 #      print(self.list)

#apple = Todo("зеленое")
#apple.add_list()
#comment



