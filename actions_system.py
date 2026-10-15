"""Системные действия: reboot, poweroff, exit."""
from __future__ import annotations

import ui_app
from ui_dialogs import ask_yes_no
from utils_shell import run_cmd


def reboot_action(_button=None) -> None:
    ask_yes_no(
        "Перезагрузка",
        "Перезагрузить систему?",
        on_yes=lambda: run_cmd(["sudo", "reboot"], capture=False),
    )


def poweroff_action(_button=None) -> None:
    ask_yes_no(
        "Выключение",
        "Выключить систему?",
        on_yes=lambda: run_cmd(["sudo", "poweroff"], capture=False),
    )


def exit_action(_button=None) -> None:
    ui_app.app.request_exit()
