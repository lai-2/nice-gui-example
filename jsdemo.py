from nicegui import ui

async def alert():
    await ui.run_javascript(
        "alert('helloe')",
        # respond=False
    )

ui.button('fire and forget', on_click=alert)

ui.run()