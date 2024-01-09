from nicegui import ui

with ui.dialog() as dialog, ui.card():
    ui.label('Welcome')
    ui.button('Close', on_click=dialog.close)

ui.button('Open', on_click=dialog.open)

ui.run()