from nicegui import ui

@ui.page('/')
def page():
    with ui.left_drawer(fixed=True):
        ui.label('left drawer')
    with ui.header():
        ui.label('header haaha')
    with ui.right_drawer():
        ui.label('right drawer')
    with ui.footer():
        ui.label('footer drawer')

ui.run()