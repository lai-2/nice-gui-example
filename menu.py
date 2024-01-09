from nicegui import ui


def menu() -> None:
    ui.link('Home', '/').classes(replace='text-white')
    ui.link('Sign in', '/sign-in').classes(replace='text-white')
    ui.link('Sign up', '/sign-up').classes(replace='text-white')
