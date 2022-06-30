import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("START")], [sg.Button("STOP")]]


# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "START":
        pass

    if event == "STOP":
        pass

    if event == sg.WIN_CLOSED:
        break

window.close()