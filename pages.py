from nicegui import ui

@ui.page('/home')
def home():
    ui.label('welcome to home page')


@ui.page('/about')
def about():
    ui.label('About!!')


@ui.page('/parameter/{demo}/{count}')
def param(demo: str, count:int):
    ui.label(f'{demo=}, {count=}')

ui.link('Visit home!', home)
ui.link('About', about)

ui.run()