#!/usr/bin/env python3
"""
RPi AI OS — TUI на urwid с каскадными окнами.

Установка:  pip install urwid
Запуск:     python menu.py

Управление:
    ↑ / ↓   — перемещение
    Enter   — выбрать
    Esc     — назад
    Ctrl+C  — выход
"""
from __future__ import annotations

import subprocess

import urwid

import ui_app
from ui_app import CascadingBoxes
from ui_palette import PALETTE
from ui_widgets import make_menu


def _bootstrap_app() -> CascadingBoxes:
    """Собирает app после импорта всех модулей."""
    from menus_main import build_main_menu
    root_menu = make_menu("RPi AI OS", build_main_menu())
    return CascadingBoxes(root_menu)


def main() -> None:
    ui_app.app = _bootstrap_app()

    while not ui_app.app._exit_requested:
        try:
            urwid.MainLoop(ui_app.app, palette=PALETTE).run()
        except KeyboardInterrupt:
            return

        cmd = ui_app.app._pending_subprocess
        ui_app.app._pending_subprocess = None
        if cmd:
            try:
                subprocess.run(cmd, start_new_session=True)
            except FileNotFoundError:
                from ui_dialogs import show_message
                show_message("Ошибка", f"{cmd[0]} не установлен.")
            except KeyboardInterrupt:
                pass


if __name__ == "__main__":
    main()
