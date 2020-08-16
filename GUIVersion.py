import PySimpleGUI as sg
import backend as bk

sg.theme('SystemDefault1')
font_size = 25

cases, deaths, recoveries = bk.data_return()
layout = [
    [sg.Text('Global Cases: ' + cases, font=('Helvetica', font_size))],
    [sg.Text('Global Deaths: ' + deaths, font=('Helvetica', font_size))],
    [sg.Text('Global Recoveries: ' + recoveries, font=('Helvetica', font_size))],
    [sg.Button('Menu', button_color=('white', 'black')), sg.Button('Update', button_color=('white', 'black')),
     sg.Button('Close', button_color=('white', 'black'))]
]

window = sg.Window('Live Coronavirus Display', layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    elif event == 'Menu':
        layout_menu = [
            [sg.Button('Font Size', button_color=('white', 'black'))],
            [sg.Button('Close', button_color=('white', 'black'))]
        ]
        window_menu = sg.Window('Menu', layout_menu, margins=(30, 12.5))
        while True:
            event, value = window_menu.read()
            if event == sg.WIN_CLOSED or event == 'Close':
                window_menu.close()
                break
            elif event == 'Font Size':
                layout_fontSize = [
                    [sg.Input()],
                    [sg.Button('OK', button_color=('white', 'black')), sg.Button('Close', button_color=('white', 'color'))]
                ]
                window_fontSize = sg.Window('Font Size', layout_fontSize)
                while True:
                    event, value = window_fontSize.read()
                    if event == 'Close' or event == sg.WIN_CLOSED:
                        window_fontSize.close()
                        break
                    elif event == 'OK':
                        try:
                            font_size = int(value[0])
                            window_fontSize.close()
                            break
                        except ValueError:
                            sg.Popup('You can only enter numbers, not words. Please try again.')

    elif event == 'Update':
        cases, deaths, recoveries = bk.data_return()
        layout = [
            [sg.Text('Global Cases: ' + cases, font=('Helvetica', font_size))],
            [sg.Text('Global Deaths: ' + deaths, font=('Helvetica', font_size))],
            [sg.Text('Global Recoveries: ' + recoveries, font=('Helvetica', font_size))],
            [sg.Button('Menu', button_color=('white', 'black')), sg.Button('Update', button_color=('white', 'black')),
             sg.Button('Close', button_color=('white', 'black'))]
        ]
        window.close()
        window = sg.Window('Live Coronavirus Display', layout)


window.close()
