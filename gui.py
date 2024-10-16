#from main import new_todo

import functions
import FreeSimpleGUI as sg
import time
import functions

sg.theme("Black")
clock = sg.Text('', key = "clock")
labe = sg.Text("type a to do")
input_box = sg.InputText(tooltip="enter todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),key='todos',enable_events=True, size=[45,10])
edit_button= sg.Button("Edit")
complete_button= sg.Button("Complete")
exit_but=sg.Button("Exit")
window  = sg.Window('My to-do-app',
                    layout=[[labe,[clock]], [input_box,add_button],[list_box,edit_button,complete_button,exit_but]],
                    font=('Helvetica',20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case sg.WIN_CLOSED:
            break
        case "Edit":
            try:
                todo = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todos'].update(values=todo)
            except IndexError:
                sg.popup("please select somthing first",font=('Helvetica',20))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todo'].update(value=todos)
                window['todo'].update(values=todo)
            except IndexError:
                sg.popup("please select somthing first",font=('Helvetica',20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'exit':
            break
window.close()