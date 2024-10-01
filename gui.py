from cProfile import label

import functions
import FreeSimpleGUI as sg

labe = sg.Text("type a to do")
input_box = sg.InputText(tooltip="enter todo")
add_button = sg.Button

window  = sg.Window('My to-do-app',layout=[[labe, input_box]])
window.read()
window.close()