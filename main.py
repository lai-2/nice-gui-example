from left_sidebar import LeftSidebar

from nicegui import ui

[ui.label(f'Line {i}') for i in range(100)]
with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
    ui.label('HEADER')
    ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')

# custom left sidebar
with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
    ui.label('LEFT DRAWER')
    left_sidebar = LeftSidebar('test left sidebar', on_change=lambda e: ui.notify(f'The value changed to {e.args}.'))

with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
    ui.label('RIGHT DRAWER')
with ui.footer().style('background-color: #3874c8'):
    ui.label('FOOTER')

ui.run()
