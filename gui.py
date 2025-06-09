from modules import functions as fn
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

sg.theme("Black")

# Left Side Column
clock = sg.Text("",key="clock")
label = sg.Text("Type In A To-Do")
input_box = sg.InputText(tooltip="Enter To-Do",key="todo")
list_box = sg.Listbox(values=fn.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
output_text = sg.Text(key="output")
left_column =sg.Column([[clock],[label],[input_box],[list_box],[output_text]])


# Right Side Column
add_button = sg.Button(size=10,image_source="add.png",key="Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
right_column =sg.Column([[add_button],[edit_button],[complete_button],[exit_button]])

# Construct the layout
layout = [[left_column, right_column]]


Window = sg.Window("My To-do App",layout=layout,
                   font=('Comic Sans MS',20))
while True:
    event, values = Window.read(timeout=100)
    Window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = fn.get_todos()
            todos.append(values["todo"] + "\n")
            fn.set_todos(todos)
            Window["todos"].update(values=todos)

        case "Edit":
            try:
                todos = fn.get_todos()
                old = values['todos'][0]
                index = todos.index(old)
                todos[index] = values["todo"] + "\n"
                fn.set_todos(todos)
                Window["todos"].update(values=todos)

            except IndexError:
                sg.popup("Select an appropriate to-do to edit!")
                continue

        case "todos":
            try:
                Window["todo"].update(value=values['todos'][0])
            except IndexError:
                continue

        case "Complete":
            try:
                todos = fn.get_todos()
                to_complete = values['todos'][0]
                index = todos.index(to_complete)
                completed = todos.pop(index).strip("\n")
                Window["output"].update(value=f"`{completed}` is marked completed")
                fn.set_todos(todos)
                Window["todos"].update(values=todos)
                Window["todo"].update(value="")

            except IndexError:
                sg.popup("Select an appropriate to-do to Complete!")
                continue

        case sg.WIN_CLOSED | "Exit":
            break

Window.close()