"""Действия Bluetooth."""
from __future__ import annotations

from ui_dialogs import show_message
from utils_shell import run_cmd


def bt_list_action(_button=None) -> None:
    output = run_cmd(["bluetoothctl", "devices"])
    show_message("Bluetooth устройства", output)


def bt_connections_action(_button=None) -> None:
    output = run_cmd(["bluetoothctl", "paired-devices"])
    show_message("Bluetooth подключения", output)


def bt_on_action(_button=None) -> None:
    run_cmd(["sudo", "systemctl", "start", "bluetooth"], capture=False)
    show_message("Bluetooth", "Служба bluetooth запущена.")


def bt_off_action(_button=None) -> None:
    run_cmd(["sudo", "systemctl", "stop", "bluetooth"], capture=False)
    show_message("Bluetooth", "Служба bluetooth остановлена.")
