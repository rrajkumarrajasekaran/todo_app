import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo + "\n")
    functions.set_todos(todos)


st.title("myTodo List")
st.subheader("Reminder List to get things done")
st.write("This app is to boost your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="to_do",placeholder="Enter a todo",label_visibility="hidden", on_change=add_todo, key='new_todo')