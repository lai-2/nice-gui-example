from left_sidebar import LeftSidebar

from nicegui import ui


# onchange event for left sidebar
def on_change_left_sidebar(event):
    if isinstance(event, str):
        label.set_text(f'Your name is "{event}"' if event != "" else "")
    else:
        # when event sent from resizing action, it format is ['resive', new width]
        left_drawer.props(f'width={event[1]}')

with ui.header(elevated=True).style("background-color: #3874c8").classes(
    "items-center justify-between"
):
    ui.label("HEADER")
    ui.button(on_click=lambda: right_drawer.toggle(), icon="menu").props(
        "flat color=white"
    )

# custom left sidebar
with ui.left_drawer(top_corner=True, bottom_corner=True).style(
    "background-color: #d7e3f4"
) as left_drawer:
    ui.label("LEFT DRAWER")
    left_sidebar = LeftSidebar(
        "test left sidebar",
        on_change=lambda e: on_change_left_sidebar(e.args)
    )
    ui.button('Reset', on_click=left_sidebar.reset).props('small outline')


with ui.right_drawer(fixed=False).style("background-color: #ebf1fa").props(
    "bordered"
) as right_drawer:
    ui.label("RIGHT DRAWER")
with ui.footer().style("background-color: #3874c8"):
    ui.label("FOOTER")

label = ui.label()
[ui.label(f"Line {i}") for i in range(100)]
ui.run()
