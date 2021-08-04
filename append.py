# сделать функцию добавления в список

todo = []
def append_todo():
    user = input("Добавьте новую задачу в список")
    todo.append(user)

append_todo()
print(todo)