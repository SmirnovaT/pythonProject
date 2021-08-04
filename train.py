



def file_add():
    input_remove = input("Что нужно удалить из списка? ")
    f = open('todo.txt', 'w')
    f.write(input_remove)

file_add()
