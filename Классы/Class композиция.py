# Наследование
#class BookShelf:
#    def __init__(self, quantity):
#        self.quantity = quantity

#    def __str__(self):
#        return f"BookShelf with {self.quantity} books."

#shelf = BookShelf(300)

#class Book(BookShelf):
#    def __init__(self, name, quantity):
#        super().__init__(quantity)
#        self.name = name

 #   def __str__(self):
 #       return f"Book {self.name}"

#book = Book("Hary Potter", 120)
#print(book)




#  Композиция

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Hary Potter")
book2 = Book("Python")
shelf = BookShelf(book, book2)

print(shelf)







class WinDoor:
    def __init__(self, x, y):
        self.square = x * y

class Room:
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []

    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))

    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square


r1 = Room(6, 3, 2.7)
print(r1.square)  # выведет 48.6
r1.addWD(1, 1)
r1.addWD(1, 1)
r1.addWD(1, 2)
print(r1.workSurface())  # выведет 44.6