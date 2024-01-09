from nicegui import ui

with ui.tabs() as tabs:
    ui.tab('Home', icon='home')
    ui.tab('About', icon='about')

with ui.tab_panels(tabs, value='Home'):
    with ui.tab_panel('Home'):
        ui.label('This is the first tab')
    
    with ui.tab_panel('About'):
        ui.label('This is the second tab')

ui.run()