from nicegui import ui

toggle = ui.toggle([ 'A', 'B', 'C' ], value='D')
another_toggle = ui.toggle({1: 'A', 2: 'B'}).bind_value(toggle)

ui.run()