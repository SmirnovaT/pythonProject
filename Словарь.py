shopping_list = {"apple": 1, "bread": 2}

def show_shopping_list():
    print(shopping_list)

def add_shopping_list(**kwargs):
    input_todo_product = input("Введите продукт: ").lower()
    while True:
        try:
            input_todo_quantity = int(input("Введите необходимое количество:"))
            break
        except ValueError:
            print("Пожалуйста, введите количество в цифрах")

    dic_product_quantity = {input_todo_product: input_todo_quantity}
    shopping_list.update(dic_product_quantity)
    print(shopping_list)


def remove_shopping_list(**kwargs):
    delete_input = input("Какой продукт удалить? ").lower()
    delete_todo = shopping_list.pop(delete_input)
    print(shopping_list)


def main():
    while True:
        user = input('Введите команду: ').lower()
        if user == "показать":
            show_shopping_list()
        elif user == "добавить":
            add_shopping_list(**shopping_list)
        elif user == "удалить":
            remove_shopping_list(**shopping_list)
        elif user == "стоп":
            break
        else:
            print("Заданной команды нет")

main()
