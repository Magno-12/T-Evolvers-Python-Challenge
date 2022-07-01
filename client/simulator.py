from sqlite3 import Timestamp
import PySimpleGUI as sg
import random
import requests
import time
import calendar
import string
import asyncio


layout = [[sg.Text("Hello from PySimpleGUI")], [
    sg.Button("START")]]

isRunning = False

# Create the window
window = sg.Window("Demo", layout)
id_device = ''.join(random.choice(string.ascii_lowercase)
                    for i in range(10))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button

    if event == "START":
        isRunning = True
    elif event == sg.WIN_CLOSED:
        isRunning = False
        break
    else:
        isRunning = False

    while isRunning == True:

        metric = str(random.randint(10, 100)) + " kmg"
        timestamp = int(time.time())

        payload = {
            "metrics": metric,
            "device_id": id_device,
            "timestamp": timestamp,
        }
        print(payload)
        response = requests.post('http://127.0.0.1:5000/api/metric',
                                 data=payload)
        print(response)

window.close()
