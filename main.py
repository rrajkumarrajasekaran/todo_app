from modules import functions as func
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todos = func.get_todos()

        # remove "add " from the user_action and assign to to_do. Append todos to a to do
        todo = user_action[4:]
        todos.append(todo + "\n")

        # print the message that to_do has been added
        print(f"The #toDo `{todo}` has been added")

        func.set_todos(todos)

    elif user_action.startswith("show"):
        todos = func.get_todos()

        # Remove the \n that is in the list to print in a better formatting
        show_todos = [item.strip("\n") for item in todos]

        # Print the todos with index number
        for index, show_todo in enumerate(show_todos):
            print(index +1, "-", show_todo)

    elif user_action.startswith("edit"):
        try:
            todos = func.get_todos()

            # remove "edit " from the user_action and that shall be your number eg: edit 2
            number = int(user_action[4:])
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            func.set_todos(todos)

        except ValueError:
            print("Enter a relevant item number.")
            continue

        except IndexError:
            print("Entered Value is Out of Range.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = func.get_todos()

            # remove "complete " from the user_action and that shall be your number eg: complete 2
            number = int(user_action[8:])
            number = number - 1
            completed_todo = todos.pop(number)
            print(f"`{completed_todo.strip("\n")}` is now marked completed.")

            func.set_todos(todos)

        except ValueError:
            print("Enter a relevant item number.")
            continue

        except IndexError:
            print("Entered Value is Out of Range.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Unknown Command")