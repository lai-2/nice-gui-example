from nicegui import ui

def on_click():
    print('button clicked')

ui.button('click me~', on_click=lambda: ui.notify('button click'))
ui.run()