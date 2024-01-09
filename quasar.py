from nicegui import ui

ui.radio(['x', 'y', 'z'], value='x').props('inline color=green')
ui.button().props('icon=touch_app outline round').classes('shadow')

ui.label('Stylish!').style('color: #6e93d6; font-size: 200%')
ui.run()