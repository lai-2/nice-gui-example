from nicegui import ui

slider = ui.slider(min = 0, max=10, value=5)

ui.label().bind_text_from(slider, 'value')


ui.run()