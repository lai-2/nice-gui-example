from nicegui import ui

ui.textarea(
    label='type something haha',
    placeholder='start typing',
    on_change= lambda e: result.set_text(e.value),
)

result = ui.label()
ui.run()