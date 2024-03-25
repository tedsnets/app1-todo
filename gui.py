import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    os.makedirs("files")
    with open(r"files\todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo_input")
add_button = sg.Button(size=16, image_size=(40, 40), image_source=r"add.png", mouseover_colors="LightGreen",
                       tooltip="Click to Add Item To List", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todolist",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit", size=8)
complete_button = sg.Button(key="Complete", image_filename=r"complete.png", image_size=(50, 50),
                            mouseover_colors="red", tooltip="Click to Remove Item from List")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, complete_button, edit_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=500)
    if event == sg.WIN_CLOSED:
        break
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values["todolist"])
    match event:
        case "Add":
            if values["todo_input"] == "":
                continue
            todos = functions.get_todos()
            new_todo = values["todo_input"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todolist"].update(values=functions.get_todos())
            window["todo_input"].update(value="")
        case "Edit":
            try:
                todo_to_edit = values["todolist"][0]
                new_todo = values["todo_input"] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todolist"].update(values=functions.get_todos())
            except IndexError:
                sg.popup("Please select an item to Edit", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todolist"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todolist"].update(values=functions.get_todos())
                window["todo_input"].update(value="")
            except IndexError:
                sg.popup("Please select an item to Complete", font=("Helvetica", 20))
        case "Exit":
            break
        case "todolist":
            window["todo_input"].update(value=values["todolist"][0])
        case sg.WIN_CLOSED:
            break


window.close()
