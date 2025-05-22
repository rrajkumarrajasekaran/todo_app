def get_todos(filepath="todos.txt"):
    """Open the todos file and read the list of to_dos."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local

def set_todos(todos_arg, filepath="todos.txt"):
    """Open the todos file and write the list of to_dos."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
