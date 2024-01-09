from nicegui import ui

with ui.image('https://www.w3schools.com/images/img_spaces_up_generic_120.png') as image:
    ui.label('some advertising').classes('absolute-button text-subtitle')

ui.run()