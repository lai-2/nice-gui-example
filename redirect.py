from nicegui import ui

@ui.page('/redirect')
def redirect():
    ui.label('this is redirect to google')
    ui.button('go', on_click=lambda: ui.open('https://google.com'))

ui.button('redirect', on_click=lambda: ui.open(redirect))
ui.run()