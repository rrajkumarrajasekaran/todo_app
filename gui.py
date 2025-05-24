from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type In A To-Do")
input_box = sg.InputText(tooltip="Enter To-Do")
add_button = sg.Button("Add")

Window = sg.Window("My To-do App",layout=[[label, add_button],[input_box]])
Window.read()
Window.close()