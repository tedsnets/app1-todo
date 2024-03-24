import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo_input")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todolist",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todolist"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo_input"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todolist"].update(values=functions.get_todos())
        case "Edit":
            todo_to_edit = values["todolist"][0]
            new_todo = values["todo_input"] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todolist"].update(values=functions.get_todos())
        case "todolist":
            window["todo_input"].update(value=values["todolist"][0])
        case sg.WIN_CLOSED:
            break


window.close()
