# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y: %H:%M:%S")
print(f"It is : {now}")
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} - {item.capitalize()}")

    elif user_action.startswith('edit'):
        try:
            number = user_action[5:]
            number = int(number)

            todos = functions.get_todos()

            new_todo = input("Enter a new task: ") + '\n'
            todos[number - 1] = new_todo

            functions.write_todos(todos)
        except (ValueError, TypeError, IndexError):
            print("Enter 'edit' and then the number of the task to be edited ")
            continue

    elif user_action.startswith('complete'):
        try:
            number = user_action[9:]
            number = int(number)

            todos = functions.get_todos()

            todos.remove(todos[number - 1])

            functions.write_todos(todos)
        except (IndexError, TypeError, ValueError):
            print("You entered an unknown command.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("You entered an unknown choice.")

print("Bye!")
