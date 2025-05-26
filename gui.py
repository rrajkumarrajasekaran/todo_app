from modules import functions as fn
import FreeSimpleGUI as sg

# Left Side Column
label = sg.Text("Type In A To-Do")
input_box = sg.InputText(tooltip="Enter To-Do",key="todo")
list_box = sg.Listbox(values=fn.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
output_text = sg.Text(key="output")
left_column =sg.Column([[label],[input_box],[list_box],[output_text]])


# Right Side Column
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
right_column =sg.Column([[add_button],[edit_button],[complete_button],[exit_button]])

# Construct the layout
layout = [[left_column, right_column]]


Window = sg.Window("My To-do App",layout=layout,
                   font=('Comic Sans MS',20))
while True:
    event, values = Window.read()

    match event:
        case "Add":
            todos = fn.get_todos()
            todos.append(values["todo"] + "\n")
            fn.set_todos(todos)
            Window["todos"].update(values=todos)

        case "Edit":
            todos = fn.get_todos()
            old = values['todos'][0]
            index = todos.index(old)
            todos[index] = values["todo"] + "\n"
            fn.set_todos(todos)
            Window["todos"].update(values=todos)

        case "todos":
            Window["todo"].update(value=values['todos'][0])

        case "Complete":
            todos = fn.get_todos()
            to_complete = values['todos'][0]
            index = todos.index(to_complete)
            completed = todos.pop(index).strip("\n")
            Window["output"].update(value=f"`{completed}` is marked completed")
            fn.set_todos(todos)
            Window["todos"].update(values=todos)
            Window["todo"].update(value="")

        case sg.WIN_CLOSED | "Exit":
            break

Window.close()