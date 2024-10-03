#from main import new_todo

import functions
import FreeSimpleGUI as sg



labe = sg.Text("type a to do")
input_box = sg.InputText(tooltip="enter todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),key='todos',enable_events=True, size=[45,10])
edit_button= sg.Button("Edit")


window  = sg.Window('My to-do-app',
                    layout=[[labe], [input_box,add_button],[list_box,edit_button]],
                    font=('Helvetica',20))
while True:
    event, values = window.read()
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
            todo = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
window.close()