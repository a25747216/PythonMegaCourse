import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo")
add_botton = PySimpleGUI.Button("Add")

window = PySimpleGUI.Window("My To-Do App", layout=[[label], [input_box, add_botton]])
window.read()
window.close()