import streamlit as st
import functions
import os

if not os.path.exists(r"files\todos.txt"):
    os.makedirs("files")
    with open(r"files\todos.txt", "w") as file:
        pass

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        print(index, todo, todos[index])
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()

st.text_input(label="Input box for new task to add",
              label_visibility="collapsed",
              placeholder="Enter a Task to add.",
              on_change=add_todo, key="new_todo",)

# st.session_state
