from modules import functions as fn
import FreeSimpleGUI as sg

label = sg.Text("Type In A To-Do")
input_box = sg.InputText(tooltip="Enter To-Do",key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fn.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

Window = sg.Window("My To-do App",layout=[[label, add_button],[input_box],[list_box,edit_button]],
                   font=('Comic Sans MS',20))
while True:
    event, values = Window.read()

    match event:
        case "Add":
            todos = fn.get_todos()
            todos.append(values["todo"] + "\n")
            fn.set_todos(todos)

        case "Edit":
            todos = fn.get_todos()
            old = values['todos'][0]
            index = todos.index(old)
            todos[index] = values["todo"] + "\n"
            fn.set_todos(todos)
            Window["todos"].update(values=todos)

        case "todos":
            Window["todo"].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

Window.close()