from modules import functions as fn
import FreeSimpleGUI as sg

label = sg.Text("Type In A To-Do")
input_box = sg.InputText(tooltip="Enter To-Do",key="todo")
add_button = sg.Button("Add")

Window = sg.Window("My To-do App",layout=[[label, add_button],[input_box]],
                   font=('Comic Sans MS',20))
while True:
    event, values = Window.read()

    match event:
        case "Add":
            todos = fn.get_todos()
            todos.append(values["todo"] + "\n")
            fn.set_todos(todos)

        case sg.WIN_CLOSED:
            break


Window.close()