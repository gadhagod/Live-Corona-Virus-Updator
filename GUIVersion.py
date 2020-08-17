import PySimpleGUI as sg
import backend as bk

sg.theme('Dark')
font_size = 25
font = False

cases, deaths, recoveries = bk.data_return()
layout = [
    [sg.Text('Global Cases: ' + cases, font=('Helvetica', font_size))],
    [sg.Text('Global Deaths: ' + deaths, font=('Helvetica', font_size))],
    [sg.Text('Global Recoveries: ' + recoveries, font=('Helvetica', font_size))],
    [sg.Button('Font Size', button_color=('white', 'black')), sg.Button('Update', button_color=('white', 'black')),
     sg.Button('Close', button_color=('white', 'black'))]
]

window = sg.Window('Live Coronavirus Display', layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    elif event == 'Font Size':
        layout_fontSize = [
            [sg.Slider((1, 100), key='_OUTPUT_', size=(50, 20), orientation='h', default_value=font_size)],
            [sg.Button('OK', button_color=('white', 'black'))]
        ]
        window_font = sg.Window('Font Size', layout_fontSize)
        font = True
        while True:
            event, value = window_font.read()
            if event == 'OK':
                font_size = int(value['_OUTPUT_'])
                window_font.close()
                break

    elif event == 'Update':
        cases, deaths, recoveries = bk.data_return()
        layout = [
            [sg.Text('Global Cases: ' + cases, font=('Helvetica', font_size))],
            [sg.Text('Global Deaths: ' + deaths, font=('Helvetica', font_size))],
            [sg.Text('Global Recoveries: ' + recoveries, font=('Helvetica', font_size))],
            [sg.Button('Font Size', button_color=('white', 'black')), sg.Button('Update', button_color=('white', 'black')),
             sg.Button('Close', button_color=('white', 'black'))]
        ]
        window.close()
        window = sg.Window('Live Coronavirus Display', layout)


window.close()
