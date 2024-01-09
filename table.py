from nicegui import ui

columns = [
    {
        "name": "name",
        "label": "Name",
        "field": "name",
        "required": True,
    },
    {
        'name': 'age',
        'label': 'Age',
        'field': 'age',
        'sortable': True,
    },
]

row = [
    {'name': 'Daniel', 'age': 32},
    {'name': 'Quoc', 'age': 31},
    {'name': 'Lai', 'age': 18},
]

ui.table(columns=columns, rows=row, row_key='name')
ui.run()