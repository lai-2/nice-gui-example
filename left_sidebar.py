from typing import Callable, Optional

from nicegui.element import Element


class LeftSidebar(Element, component="left_sidebar.js"):
    def __init__(self, title: str, *, on_change: Optional[Callable] = None) -> None:
        super().__init__()
        self._props["title"] = title
        self.on("change", on_change)
