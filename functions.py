FILEPATH = r"files\todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file:
        todos = file.readlines()
        return todos


def write_todos(todos, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos)


def empty(filepath=FILEPATH):
    with open(filepath, "w") as file:
        pass


def show():
    to_dos = get_todos()
    display = ""
    for i, item in enumerate(to_dos):
        display = display + f"{i+1}) {item}"
    return display.rstrip("\n")
