class ClassList():
    def __init__(self):
        self.list = []

    def __str__(self):
        return self.list

    def append(self, ob):
        self.list.append(ob)

a = input("Введите данные: ").split(', ')
car = Car(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
array = ClassList()
array.append(car)
array.append(car_copy)

print(array.__str__())