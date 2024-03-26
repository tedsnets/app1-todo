import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my todo app.")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Input box for new task to add",
              label_visibility="collapsed",
              placeholder="Enter a Task to add.",
              on_change=add_todo, key="new_todo")
