from nicegui import ui

ui.input(
    label="Enter oyur text",
    placeholder="start typing herer",
    on_change=lambda e: result.set_text(f"you typed: {e.value}"),
    validation={'Input too long': lambda value: len(value) > 5}
)

result = ui.label()

ui.run()
