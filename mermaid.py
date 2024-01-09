from nicegui import ui

ui.mermaid('''
graph
           a --> b;
           a --> c;
           b-->     d;
           d-->     e;
           c-->     e;
           ''')

ui.run()