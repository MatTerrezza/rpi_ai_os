"""Каскадные окна и глобальный объект приложения."""
from __future__ import annotations

import urwid


class CascadingBoxes(urwid.WidgetPlaceholder):
    """Каскад окон: каждое новое накладывается поверх предыдущего."""

    MAX_LEVELS = 4

    def __init__(self, initial_box: urwid.Widget) -> None:
        super().__init__(urwid.SolidFill("/"))
        self.box_level = 0
        self._pending_subprocess: list[str] | None = None
        self._exit_requested = False
        self.open_box(initial_box)

    def open_box(self, box: urwid.Widget) -> None:
        self.original_widget = urwid.Overlay(
            urwid.LineBox(box),
            self.original_widget,
            align=urwid.CENTER,
            width=(urwid.RELATIVE, 70),
            valign=urwid.MIDDLE,
            height=(urwid.RELATIVE, 80),
            min_width=24,
            min_height=8,
            left=self.box_level * 3,
            right=(self.MAX_LEVELS - self.box_level - 1) * 3,
            top=self.box_level * 2,
            bottom=(self.MAX_LEVELS - self.box_level - 1) * 2,
        )
        self.box_level += 1

    def close_box(self) -> None:
        if self.box_level > 1:
            self.original_widget = self.original_widget[0]
            self.box_level -= 1

    def keypress(self, size, key):
        if key == "esc" and self.box_level > 1:
            self.close_box()
            return None
        return super().keypress(size, key)

    def exit_to_subprocess(self, cmd: list[str]) -> None:
        """Выйти из MainLoop, запустить cmd, вернуться в меню."""
        self._pending_subprocess = cmd
        raise urwid.ExitMainLoop()

    def request_exit(self) -> None:
        """Выйти из приложения насовсем."""
        self._exit_requested = True
        raise urwid.ExitMainLoop()


# Глобальный объект приложения. Заполняется в menu.py до старта MainLoop.
app: CascadingBoxes = None       # type: ignore
