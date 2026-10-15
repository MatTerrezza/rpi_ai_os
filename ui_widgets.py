"""Базовые виджеты: кнопка, меню, кнопка-подменю."""
from __future__ import annotations

import urwid


def make_button(caption, on_press) -> urwid.AttrMap:
    """Кнопка с инверсией при фокусе."""
    button = urwid.Button(caption, on_press=on_press)
    return urwid.AttrMap(button, None, focus_map="reversed")


def make_menu(title: str, items: list) -> urwid.ListBox:
    """Заголовок + линия + список пунктов."""
    body = [urwid.Text(title), urwid.Divider(), *items]
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def make_submenu_button(caption: str, items: list) -> urwid.AttrMap:
    """Кнопка, открывающая подменю поверх текущего окна."""
    import ui_app

    submenu = make_menu(caption, items)

    def open_submenu(_button):
        ui_app.app.open_box(submenu)

    return make_button([caption, " …"], open_submenu)
