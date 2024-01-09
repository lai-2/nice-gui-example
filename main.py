from pages import home, sign_in, sign_up
import layout

from nicegui import app, ui


@ui.page('/')
def index_page() -> None:
    with layout.navbar('Homepage'):
        home.content()


@ui.page('/sign-in')
def sign_in_page() -> None:
    with layout.navbar('Sign-in'):
        sign_in.content()


@ui.page('/sign-up')
def sign_up_page() -> None:
    with layout.navbar('Sign-in'):
        sign_up.content()

ui.run(title='NiceGUI Example', port=8888)
