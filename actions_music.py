from __future__ import annotations

import subprocess

import ui_app
from ui_dialogs import show_message
from utils_shell import run_cmd


def music_play_action(_button=None) -> None:
    """Запускает cmus в foreground. Меню вернётся после выхода из cmus."""
    ui_app.app.exit_to_subprocess(["cmus"])


def music_status_action(_button=None) -> None:
    """Проверяет, запущен ли cmus-remote (то есть играет ли что-то)."""
    output = run_cmd(["cmus-remote", "-Q"])
    if "status" in output.lower():
        show_message("Music - status", output)
    else:
        show_message("Music", "cmus not playing.")
