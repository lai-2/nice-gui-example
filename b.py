from nicegui import ui
# ui.add_head_html('<style>.q-drawer--left { width: 50% !important }</style>')

with ui.label('test 123').classes(replace="width: 225px !important;"):
    with (
        ui.left_drawer(top_corner=False, bottom_corner=True, bordered=True)
        # .style(
        #     replace="height: calc(100% + 20px) !important;  background-color: #f3f3f3; border-right: 1px solid #ccc; width: 225px !important;"
        # )
        # .props("width:225")
    ):
        with ui.column():
            with ui.column():
                ui.link("Link 1 ", "/").classes(replace="text-lg")
            with ui.column():
                ui.link("Link 2", "/").classes(replace="text-lg")

ui.run()
