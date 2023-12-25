def get_todos():
    with open('todolist.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_1, filename='todolist.txt'):
    with open(filename, 'w') as file:
        file.writelines(todos_1)


if __name__ == "__todolist3.1__":
    print("hello")
    print(get_todos())