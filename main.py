import time

from functions import get_todos, write_todos, show, empty
''' To Do
add edit function
Change menu numbers
abstract to functions
use 'with open() as file'
error handling
'''

def main():
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print("It is", now)
    while True:
        newmenu = "add, show, edit, complete, empty, or exit: "
        menu = input(newmenu)
        menu = menu.strip()
        if menu.startswith(("add", "Add", "ADD")):
            if len(menu) == 3:
                task = input("Enter task to add to list: ") + "\n"
            else:
                task = menu[4:] + "\n"

            todos = get_todos()
            todos.append(task)
            write_todos(todos)

        elif menu.startswith(("show", "Show", "SHOW")):
            print(show())
        elif menu.startswith(("edit", "Edit", "EDIT")):
            if len(menu) == 4:
                to_edit = input("Enter task number to edit: ")
            else:
                to_edit = menu[5:]
            try:
                to_edit = int(to_edit) - 1
            except ValueError:
                print("Must enter a task number. Returning to Main Menu.")
                continue

            new_task = input("Enter new task: ") + "\n"
            todos = get_todos()
            try:
                todos[to_edit] = new_task
            except IndexError:
                print("That task doesn't exist! Exiting to Main Menu")
                continue

            write_todos(todos)
        elif menu.startswith(("complete", "Complete", "COMPLETE")):
            if len(menu) == 8:
                print(show())
                remove = input("Which task number to complete? ")
            else:
                remove = menu[9:]

            try:
                remove = int(remove) - 1
            except ValueError:
                print("Must enter a task number. Returning to Main Menu.")
                continue

            to_dos = get_todos()
            try:
                removed = to_dos.pop(remove)
            except IndexError:
                print("That task doesn't exist! Exiting to Main Menu")
                continue

            write_todos(to_dos)
            print(removed.rstrip("\n"), "Completed")
        elif menu.startswith(("empty", "Empty", "EMPTY")):
            empty()
            print("List erased!")
        elif menu.startswith(("exit", "Exit", "EXIT")):
            break






if __name__ == "__main__":
    main()