from nicegui import ui, app

app.add_static_files('/examples', 'examples')
ui.label('Static demo').classes('text-h5')

ui.link('redirect.py', '/redirect.py')
ui.run()