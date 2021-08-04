#from typing import list

#def list_avg(sequence: list) -> float:
#    return sum(sequence) / len(sequence)

#list_avg(123)




#class Book:
#   def __init__(self, name: str, page_count: int):
#        self.name = name
#        self.page_count = page_count




#from typing import list

#class Book:
#    pass

#class BookShelf:
#    def __init__(self, books: list[Book]):
#        self.books = books

#    def __str__(self) -> str:
#        return f'Bookshelf with {len(self.books)} books.'



class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f'<Book {self.name}, {self.book_type}, weight {self.weight}g>'

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return Book(name, Book.TYPES[1], page_weight)

book = Book.hardcover('Harry Potter', 1500)
light = Book.paperback("Python 101", 600)
print(book)
print(light)