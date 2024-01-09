from contextlib import contextmanager

from menu import menu

from nicegui import ui


@contextmanager
def navbar(navtitle: str):
    ui.colors(
        primary="#6E93D6", secondary="#53B689", accent="#111B1E", positive="#53B689"
    )

    # navbar
    with ui.header().classes("justify-between text-white"):
        ui.label("NiceGUI Example").classes("font-bold")
        ui.label(navtitle)
        with ui.row():
            menu()

    # main page content
    with ui.column().classes("absolute-center items-center"):
        yield
