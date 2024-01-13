from typing import Callable, Optional

from nicegui.element import Element


class LeftSidebar(Element, component='left-sidebar.js'):

    def __init__(self, title: str) -> None:
        super().__init__()
        self._props['title'] = title
        # self.on('change', on_change)

    def reset(self) -> None:
        pass
        # self.run_method('reset')