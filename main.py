from nicegui import ui
from left_sidebar import LeftSidebar
from counter import Counter

# @ui.page('/page_layout')
# def page_layout():

ui.label("CONTENT")
[ui.label(f"Line {i}") for i in range(100)]
with ui.header(elevated=True).style("background-color: #3874c8").classes(
    "items-center justify-between"
):
    ui.label("HEADER")
    ui.button(on_click=lambda: right_drawer.toggle(), icon="menu").props(
        "flat color=white"
    )
# with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
#     ui.label('LEFT DRAWER')
with (
    ui.left_drawer(top_corner=True, bottom_corner=True)
    .style("background-color: #d7e3f4")
    .props("width=500")
):
    # ui.label('LEFT DRAWER')
    # counter = LeftSidebar('Some title')
    counter = Counter("some title init in main.py", on_change=lambda e: ui.notify(f'The value changed to {e.args}.'))

    # with ui.card():
    # counter = LeftSidebar('Some title')
    # ui.label('lai test 111')

with ui.right_drawer(fixed=False).style("background-color: #ebf1fa").props(
    "bordered"
) as right_drawer:
    ui.label("RIGHT DRAWER")
with ui.footer().style("background-color: #3874c8"):
    ui.label("FOOTER")

# ui.link('show page with fancy layout', page_layout)

ui.run(title="Lai test example")
